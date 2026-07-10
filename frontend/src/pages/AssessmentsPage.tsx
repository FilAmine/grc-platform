import { zodResolver } from '@hookform/resolvers/zod';
import AddIcon from '@mui/icons-material/Add';
import {
  Box,
  Button,
  Chip,
  Container,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  MenuItem,
  Paper,
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
import { useMemo, useState } from 'react';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';
import { z } from 'zod';
import { createAssessment, getAssessments, getFrameworkCatalog, getFrameworkVersions } from '../api/compliance';
import type { AssessmentStatus } from '../api/types';

const schema = z.object({
  framework_id: z.string().min(1, 'Select a framework'),
  framework_version_id: z.string().min(1, 'Select a version'),
  name: z.string().min(2, 'At least 2 characters'),
  period_start: z.string().optional(),
  period_end: z.string().optional(),
});

type FormValues = z.infer<typeof schema>;

const statusColor: Record<AssessmentStatus, 'default' | 'info' | 'success' | 'warning'> = {
  draft: 'default',
  in_progress: 'info',
  completed: 'success',
  archived: 'warning',
};

export function AssessmentsPage() {
  const queryClient = useQueryClient();
  const navigate = useNavigate();
  const [dialogOpen, setDialogOpen] = useState(false);

  const assessments = useQuery({ queryKey: ['assessments'], queryFn: getAssessments });
  const catalog = useQuery({ queryKey: ['compliance-catalog'], queryFn: getFrameworkCatalog });

  const versionLabel = useMemo(() => {
    const map = new Map<string, string>();
    if (catalog.data) {
      for (const framework of catalog.data.frameworks) {
        for (const version of catalog.data.versionsByFramework[framework.id] ?? []) {
          map.set(version.id, `${framework.name} — v${version.version}`);
        }
      }
    }
    return (versionId: string) => map.get(versionId) ?? versionId;
  }, [catalog.data]);

  const {
    register,
    handleSubmit,
    watch,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema) });

  const selectedFrameworkId = watch('framework_id');
  const versions = useQuery({
    queryKey: ['framework-versions', selectedFrameworkId],
    queryFn: () => getFrameworkVersions(selectedFrameworkId),
    enabled: Boolean(selectedFrameworkId),
  });

  const createMutation = useMutation({
    mutationFn: (values: FormValues) =>
      createAssessment({
        framework_version_id: values.framework_version_id,
        name: values.name,
        period_start: values.period_start || null,
        period_end: values.period_end || null,
      }),
    onSuccess: async (assessment) => {
      await queryClient.invalidateQueries({ queryKey: ['assessments'] });
      setDialogOpen(false);
      reset();
      navigate(`/assessments/${assessment.id}`);
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Assessments</Typography>
          <Typography color="text.secondary">Run compliance assessments against a framework version.</Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New assessment
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Framework version</TableCell>
              <TableCell>Period</TableCell>
              <TableCell>Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(assessments.data ?? []).map((assessment) => (
              <TableRow
                key={assessment.id}
                hover
                onClick={() => navigate(`/assessments/${assessment.id}`)}
                sx={{ cursor: 'pointer' }}
              >
                <TableCell>
                  <Typography fontWeight={600} color="text.primary">
                    {assessment.name}
                  </Typography>
                </TableCell>
                <TableCell>{versionLabel(assessment.framework_version_id)}</TableCell>
                <TableCell>
                  {assessment.period_start ?? '—'} → {assessment.period_end ?? '—'}
                </TableCell>
                <TableCell>
                  <Chip size="small" label={assessment.status.replace('_', ' ')} color={statusColor[assessment.status]} />
                </TableCell>
              </TableRow>
            ))}
            {!assessments.data?.length && (
              <TableRow>
                <TableCell colSpan={4}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No assessments yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New assessment</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Framework"
                select
                defaultValue=""
                error={Boolean(errors.framework_id)}
                helperText={errors.framework_id?.message}
                {...register('framework_id')}
              >
                {(catalog.data?.frameworks ?? []).map((framework) => (
                  <MenuItem key={framework.id} value={framework.id}>
                    {framework.name}
                  </MenuItem>
                ))}
              </TextField>
              <TextField
                label="Version"
                select
                defaultValue=""
                disabled={!selectedFrameworkId}
                error={Boolean(errors.framework_version_id)}
                helperText={errors.framework_version_id?.message}
                {...register('framework_version_id')}
              >
                {(versions.data ?? []).map((version) => (
                  <MenuItem key={version.id} value={version.id}>
                    {version.version}
                  </MenuItem>
                ))}
              </TextField>
              <TextField
                label="Name"
                error={Boolean(errors.name)}
                helperText={errors.name?.message}
                {...register('name')}
              />
              <Stack direction="row" spacing={2}>
                <TextField
                  label="Period start"
                  type="date"
                  InputLabelProps={{ shrink: true }}
                  fullWidth
                  {...register('period_start')}
                />
                <TextField
                  label="Period end"
                  type="date"
                  InputLabelProps={{ shrink: true }}
                  fullWidth
                  {...register('period_end')}
                />
              </Stack>
            </Stack>
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setDialogOpen(false)}>Cancel</Button>
            <Button type="submit" variant="contained" disabled={isSubmitting}>
              Create
            </Button>
          </DialogActions>
        </Box>
      </Dialog>
    </Container>
  );
}
