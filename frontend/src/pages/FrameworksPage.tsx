import { zodResolver } from '@hookform/resolvers/zod';
import { Add as AddIcon, ExpandMore as ExpandMoreIcon, UploadFile as UploadFileIcon } from '@mui/icons-material';
import {
  Accordion,
  AccordionDetails,
  AccordionSummary,
  Alert,
  Box,
  Button,
  Chip,
  Container,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Stack,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  TextField,
  Typography,
} from '@mui/material';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import Papa from 'papaparse';
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import {
  bulkImportRequirements,
  createFramework,
  createFrameworkVersion,
  getFrameworks,
  getFrameworkVersions,
} from '../api/compliance';
import type { Framework, FrameworkVersion, RequirementImportRow } from '../api/types';

const frameworkSchema = z.object({
  code: z.string().min(2, 'At least 2 characters'),
  name: z.string().min(2, 'At least 2 characters'),
  description: z.string().optional(),
});
type FrameworkFormValues = z.infer<typeof frameworkSchema>;

const versionSchema = z.object({
  version: z.string().min(1, 'Required'),
  published_at: z.string().optional(),
});
type VersionFormValues = z.infer<typeof versionSchema>;

function ImportRequirementsDialog({ version, onClose }: { version: FrameworkVersion; onClose: () => void }) {
  const queryClient = useQueryClient();
  const [rows, setRows] = useState<RequirementImportRow[]>([]);
  const [parseError, setParseError] = useState<string | null>(null);
  const [fileName, setFileName] = useState<string | null>(null);

  const importMutation = useMutation({
    mutationFn: (items: RequirementImportRow[]) => bulkImportRequirements(version.id, items),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['requirements', version.id] });
      onClose();
    },
  });

  const handleFile = (file: File) => {
    setFileName(file.name);
    setParseError(null);
    Papa.parse<Record<string, string>>(file, {
      header: true,
      skipEmptyLines: true,
      complete: (results) => {
        const columns = results.meta.fields ?? [];
        if (!columns.includes('code') || !columns.includes('title')) {
          setParseError('CSV must have "code" and "title" columns (an optional "description" column too).');
          setRows([]);
          return;
        }
        const parsed = results.data
          .filter((row) => row.code?.trim() && row.title?.trim())
          .map((row) => ({
            code: row.code.trim(),
            title: row.title.trim(),
            description: row.description?.trim() ?? '',
          }));
        setRows(parsed);
      },
      error: (error: Error) => {
        setParseError(error.message);
        setRows([]);
      },
    });
  };

  return (
    <Dialog open onClose={onClose} fullWidth maxWidth="sm">
      <DialogTitle>Import requirements — v{version.version}</DialogTitle>
      <DialogContent>
        <Stack spacing={2} sx={{ mt: 1 }}>
          <Alert severity="info">
            Only import requirement text from a standard your organization already holds a license for. This
            platform never ships licensed standards text itself.
          </Alert>
          <Button variant="outlined" component="label">
            Choose CSV file
            <input
              type="file"
              accept=".csv,text/csv"
              hidden
              onChange={(event) => {
                const file = event.target.files?.[0];
                if (file) handleFile(file);
              }}
            />
          </Button>
          {fileName && <Typography variant="body2">{fileName}</Typography>}
          {parseError && <Alert severity="error">{parseError}</Alert>}
          {rows.length > 0 && (
            <>
              <Typography variant="body2" color="text.secondary">
                {rows.length} requirement{rows.length === 1 ? '' : 's'} parsed and ready to import.
              </Typography>
              <Table size="small">
                <TableHead>
                  <TableRow>
                    <TableCell>Code</TableCell>
                    <TableCell>Title</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {rows.slice(0, 5).map((row) => (
                    <TableRow key={row.code}>
                      <TableCell>{row.code}</TableCell>
                      <TableCell>{row.title}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
              {rows.length > 5 && (
                <Typography variant="caption" color="text.secondary">
                  …and {rows.length - 5} more
                </Typography>
              )}
            </>
          )}
          {importMutation.isError && (
            <Alert severity="error">Import failed. Check the file and try again.</Alert>
          )}
        </Stack>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button
          variant="contained"
          disabled={!rows.length || importMutation.isPending}
          onClick={() => importMutation.mutate(rows)}
        >
          Import {rows.length || ''} requirement{rows.length === 1 ? '' : 's'}
        </Button>
      </DialogActions>
    </Dialog>
  );
}

function FrameworkVersions({ framework }: { framework: Framework }) {
  const queryClient = useQueryClient();
  const [versionDialogOpen, setVersionDialogOpen] = useState(false);
  const [importVersion, setImportVersion] = useState<FrameworkVersion | null>(null);

  const versions = useQuery({
    queryKey: ['framework-versions', framework.id],
    queryFn: () => getFrameworkVersions(framework.id),
  });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<VersionFormValues>({ resolver: zodResolver(versionSchema) });

  const createVersionMutation = useMutation({
    mutationFn: (values: VersionFormValues) =>
      createFrameworkVersion(framework.id, { version: values.version, published_at: values.published_at || null }),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['framework-versions', framework.id] });
      setVersionDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => createVersionMutation.mutate(values));

  return (
    <Stack spacing={2}>
      <Stack direction="row" justifyContent="flex-end">
        <Button size="small" startIcon={<AddIcon />} onClick={() => setVersionDialogOpen(true)}>
          New version
        </Button>
      </Stack>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Version</TableCell>
            <TableCell>Published</TableCell>
            <TableCell align="right">Actions</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {(versions.data ?? []).map((version) => (
            <TableRow key={version.id}>
              <TableCell>{version.version}</TableCell>
              <TableCell>{version.published_at ?? '—'}</TableCell>
              <TableCell align="right">
                <Button size="small" startIcon={<UploadFileIcon />} onClick={() => setImportVersion(version)}>
                  Import CSV
                </Button>
              </TableCell>
            </TableRow>
          ))}
          {!versions.data?.length && (
            <TableRow>
              <TableCell colSpan={3}>
                <Typography color="text.secondary" variant="body2">
                  No versions yet.
                </Typography>
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>

      <Dialog open={versionDialogOpen} onClose={() => setVersionDialogOpen(false)} fullWidth maxWidth="xs">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New version of {framework.name}</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Version"
                error={Boolean(errors.version)}
                helperText={errors.version?.message}
                {...register('version')}
              />
              <TextField
                label="Published date"
                type="date"
                InputLabelProps={{ shrink: true }}
                {...register('published_at')}
              />
            </Stack>
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setVersionDialogOpen(false)}>Cancel</Button>
            <Button type="submit" variant="contained" disabled={isSubmitting}>
              Create
            </Button>
          </DialogActions>
        </Box>
      </Dialog>

      {importVersion && <ImportRequirementsDialog version={importVersion} onClose={() => setImportVersion(null)} />}
    </Stack>
  );
}

export function FrameworksPage() {
  const queryClient = useQueryClient();
  const [frameworkDialogOpen, setFrameworkDialogOpen] = useState(false);

  const frameworks = useQuery({ queryKey: ['frameworks'], queryFn: getFrameworks });
  const systemFrameworks = (frameworks.data ?? []).filter((f) => f.is_system);
  const customFrameworks = (frameworks.data ?? []).filter((f) => !f.is_system);

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FrameworkFormValues>({ resolver: zodResolver(frameworkSchema) });

  const createFrameworkMutation = useMutation({
    mutationFn: (values: FrameworkFormValues) => createFramework(values),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['frameworks'] });
      setFrameworkDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => createFrameworkMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Frameworks</Typography>
          <Typography color="text.secondary">
            Manage custom frameworks and import requirement text from standards your organization holds a license
            for.
          </Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setFrameworkDialogOpen(true)}>
          New framework
        </Button>
      </Stack>

      <Typography variant="h6" sx={{ mb: 1 }}>
        Your custom frameworks
      </Typography>
      <Stack spacing={1} sx={{ mb: 4 }}>
        {customFrameworks.map((framework) => (
          <Accordion key={framework.id} disableGutters>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Stack direction="row" spacing={1} alignItems="center">
                <Typography fontWeight={600}>{framework.name}</Typography>
                <Chip size="small" label={framework.code} />
              </Stack>
            </AccordionSummary>
            <AccordionDetails>
              <FrameworkVersions framework={framework} />
            </AccordionDetails>
          </Accordion>
        ))}
        {!customFrameworks.length && (
          <Typography color="text.secondary">
            No custom frameworks yet. Create one, then import its requirement text via CSV.
          </Typography>
        )}
      </Stack>

      <Typography variant="h6" sx={{ mb: 1 }}>
        System catalog (read-only)
      </Typography>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Name</TableCell>
            <TableCell>Code</TableCell>
            <TableCell>Description</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {systemFrameworks.map((framework) => (
            <TableRow key={framework.id}>
              <TableCell>{framework.name}</TableCell>
              <TableCell>{framework.code}</TableCell>
              <TableCell>{framework.description}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>

      <Dialog open={frameworkDialogOpen} onClose={() => setFrameworkDialogOpen(false)} fullWidth maxWidth="xs">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New custom framework</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Code"
                error={Boolean(errors.code)}
                helperText={errors.code?.message}
                {...register('code')}
              />
              <TextField
                label="Name"
                error={Boolean(errors.name)}
                helperText={errors.name?.message}
                {...register('name')}
              />
              <TextField label="Description" multiline rows={2} {...register('description')} />
            </Stack>
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setFrameworkDialogOpen(false)}>Cancel</Button>
            <Button type="submit" variant="contained" disabled={isSubmitting}>
              Create
            </Button>
          </DialogActions>
        </Box>
      </Dialog>
    </Container>
  );
}
