import { zodResolver } from '@hookform/resolvers/zod';
import { Add as AddIcon } from '@mui/icons-material';
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
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';
import { z } from 'zod';
import { createDocument, getDocuments } from '../api/documents';
import type { DocumentStatus, DocumentType } from '../api/types';

const DOCUMENT_TYPES: DocumentType[] = ['policy', 'procedure', 'standard', 'guideline', 'template'];

const schema = z.object({
  title: z.string().min(2, 'At least 2 characters'),
  document_type: z.enum(['policy', 'procedure', 'standard', 'guideline', 'template']),
  owner: z.string().min(2, 'At least 2 characters'),
  file_reference: z.string().min(1, 'Provide a file reference or URL'),
});

type FormValues = z.infer<typeof schema>;

const statusColor: Record<DocumentStatus, 'default' | 'info' | 'success' | 'warning'> = {
  draft: 'default',
  in_review: 'info',
  published: 'success',
  archived: 'warning',
};

export function DocumentsPage() {
  const queryClient = useQueryClient();
  const navigate = useNavigate();
  const [dialogOpen, setDialogOpen] = useState(false);
  const documents = useQuery({ queryKey: ['documents'], queryFn: getDocuments });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema), defaultValues: { document_type: 'policy' } });

  const createMutation = useMutation({
    mutationFn: createDocument,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['documents'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Documents</Typography>
          <Typography color="text.secondary">Policies, procedures, standards, guidelines, and templates.</Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New document
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Title</TableCell>
              <TableCell>Type</TableCell>
              <TableCell>Owner</TableCell>
              <TableCell>Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(documents.data ?? []).map((doc) => (
              <TableRow key={doc.id} hover onClick={() => navigate(`/documents/${doc.id}`)} sx={{ cursor: 'pointer' }}>
                <TableCell>
                  <Typography fontWeight={600} color="text.primary">
                    {doc.title}
                  </Typography>
                </TableCell>
                <TableCell>
                  <Chip size="small" label={doc.document_type} />
                </TableCell>
                <TableCell>{doc.owner}</TableCell>
                <TableCell>
                  <Chip size="small" label={doc.status.replace('_', ' ')} color={statusColor[doc.status]} />
                </TableCell>
              </TableRow>
            ))}
            {!documents.data?.length && (
              <TableRow>
                <TableCell colSpan={4}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No documents yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New document</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Title"
                error={Boolean(errors.title)}
                helperText={errors.title?.message}
                {...register('title')}
              />
              <TextField label="Type" select defaultValue="policy" {...register('document_type')}>
                {DOCUMENT_TYPES.map((type) => (
                  <MenuItem key={type} value={type}>
                    {type}
                  </MenuItem>
                ))}
              </TextField>
              <TextField
                label="Owner"
                error={Boolean(errors.owner)}
                helperText={errors.owner?.message}
                {...register('owner')}
              />
              <TextField
                label="File reference"
                placeholder="s3://bucket/policy.pdf or a URL"
                error={Boolean(errors.file_reference)}
                helperText={errors.file_reference?.message}
                {...register('file_reference')}
              />
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
