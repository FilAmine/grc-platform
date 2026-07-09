import { zodResolver } from '@hookform/resolvers/zod';
import AddIcon from '@mui/icons-material/Add';
import ArchiveIcon from '@mui/icons-material/Archive';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
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
  TextField,
  Typography,
} from '@mui/material';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { Link as RouterLink, useParams } from 'react-router-dom';
import { z } from 'zod';
import {
  archiveDocument,
  createVersion,
  decideApproval,
  getApprovals,
  getDocument,
  getVersions,
  submitForApproval,
} from '../api/documents';
import type { DocumentStatus, DocumentVersion, VersionStatus } from '../api/types';

const statusColor: Record<DocumentStatus, 'default' | 'info' | 'success' | 'warning'> = {
  draft: 'default',
  in_review: 'info',
  published: 'success',
  archived: 'warning',
};

const versionStatusColor: Record<VersionStatus, 'default' | 'info' | 'success' | 'error'> = {
  draft: 'default',
  pending_approval: 'info',
  approved: 'success',
  rejected: 'error',
};

const versionSchema = z.object({
  file_reference: z.string().min(1, 'Provide a file reference or URL'),
  change_summary: z.string().min(1, 'Describe what changed'),
});
type VersionFormValues = z.infer<typeof versionSchema>;

const approvalSchema = z.object({
  comment: z.string().min(1, 'A comment is required'),
  signature_reference: z.string().optional(),
});
type ApprovalFormValues = z.infer<typeof approvalSchema>;

function VersionCard({ version, documentId }: { version: DocumentVersion; documentId: string }) {
  const queryClient = useQueryClient();
  const [approvalDialog, setApprovalDialog] = useState<'approve' | 'reject' | null>(null);
  const approvals = useQuery({
    queryKey: ['documents', 'versions', version.id, 'approvals'],
    queryFn: () => getApprovals(version.id),
  });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<ApprovalFormValues>({ resolver: zodResolver(approvalSchema) });

  const invalidate = async () => {
    await queryClient.invalidateQueries({ queryKey: ['documents', documentId, 'versions'] });
    await queryClient.invalidateQueries({ queryKey: ['documents', documentId] });
    await queryClient.invalidateQueries({ queryKey: ['documents', 'versions', version.id, 'approvals'] });
  };

  const submitMutation = useMutation({
    mutationFn: () => submitForApproval(version.id),
    onSuccess: invalidate,
  });

  const decisionMutation = useMutation({
    mutationFn: (values: ApprovalFormValues) =>
      decideApproval(version.id, {
        approve: approvalDialog === 'approve',
        comment: values.comment,
        signature_reference: values.signature_reference || null,
      }),
    onSuccess: async () => {
      await invalidate();
      setApprovalDialog(null);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => decisionMutation.mutate(values));

  return (
    <Accordion elevation={0} sx={{ border: '1px solid', borderColor: 'divider', '&:before': { display: 'none' } }}>
      <AccordionSummary expandIcon={<ExpandMoreIcon />}>
        <Stack direction="row" alignItems="center" spacing={1.5} sx={{ width: '100%', pr: 2 }}>
          <Typography fontWeight={600}>v{version.version_number}</Typography>
          <Typography variant="body2" color="text.secondary" sx={{ flexGrow: 1 }}>
            {version.change_summary}
          </Typography>
          <Chip size="small" label={version.status.replace('_', ' ')} color={versionStatusColor[version.status]} />
        </Stack>
      </AccordionSummary>
      <AccordionDetails>
        <Stack spacing={2}>
          <Typography variant="body2" color="text.secondary">
            File: {version.file_reference}
          </Typography>

          <Stack direction="row" spacing={1}>
            {version.status === 'draft' && (
              <Button size="small" variant="outlined" disabled={submitMutation.isPending} onClick={() => submitMutation.mutate()}>
                Submit for approval
              </Button>
            )}
            {version.status === 'pending_approval' && (
              <>
                <Button size="small" variant="contained" color="success" onClick={() => setApprovalDialog('approve')}>
                  Approve
                </Button>
                <Button size="small" variant="outlined" color="error" onClick={() => setApprovalDialog('reject')}>
                  Reject
                </Button>
              </>
            )}
          </Stack>

          {Boolean(approvals.data?.length) && (
            <Stack spacing={1}>
              <Typography variant="subtitle2">Approval history</Typography>
              {approvals.data!.map((approval) => (
                <Box key={approval.id}>
                  <Stack direction="row" spacing={1} alignItems="center">
                    <Chip size="small" label={approval.decision} color={versionStatusColor[approval.decision]} />
                    {approval.signature_reference && (
                      <Typography variant="caption" color="text.secondary">
                        signed: {approval.signature_reference}
                      </Typography>
                    )}
                  </Stack>
                  {approval.comment && (
                    <Typography variant="body2" color="text.secondary">
                      "{approval.comment}"
                    </Typography>
                  )}
                </Box>
              ))}
            </Stack>
          )}
        </Stack>
      </AccordionDetails>

      <Dialog open={approvalDialog !== null} onClose={() => setApprovalDialog(null)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>{approvalDialog === 'approve' ? 'Approve version' : 'Reject version'}</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Comment"
                multiline
                minRows={2}
                error={Boolean(errors.comment)}
                helperText={errors.comment?.message}
                {...register('comment')}
              />
              {approvalDialog === 'approve' && (
                <TextField
                  label="Signature reference (optional)"
                  placeholder="e.g. docusign:envelope-id"
                  {...register('signature_reference')}
                />
              )}
            </Stack>
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setApprovalDialog(null)}>Cancel</Button>
            <Button type="submit" variant="contained" disabled={isSubmitting}>
              {approvalDialog === 'approve' ? 'Approve' : 'Reject'}
            </Button>
          </DialogActions>
        </Box>
      </Dialog>
    </Accordion>
  );
}

export function DocumentDetailPage() {
  const { documentId } = useParams<{ documentId: string }>();
  const queryClient = useQueryClient();
  const [versionDialogOpen, setVersionDialogOpen] = useState(false);

  const documentQuery = useQuery({
    queryKey: ['documents', documentId],
    queryFn: () => getDocument(documentId!),
    enabled: Boolean(documentId),
  });
  const versions = useQuery({
    queryKey: ['documents', documentId, 'versions'],
    queryFn: () => getVersions(documentId!),
    enabled: Boolean(documentId),
  });

  const versionForm = useForm<VersionFormValues>({ resolver: zodResolver(versionSchema) });
  const createVersionMutation = useMutation({
    mutationFn: (values: VersionFormValues) => createVersion(documentId!, values),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['documents', documentId, 'versions'] });
      setVersionDialogOpen(false);
      versionForm.reset();
    },
  });

  const archiveMutation = useMutation({
    mutationFn: () => archiveDocument(documentId!),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['documents', documentId] });
      await queryClient.invalidateQueries({ queryKey: ['documents'] });
    },
  });

  if (!documentId) return null;

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Button startIcon={<ArrowBackIcon />} component={RouterLink} to="/documents" sx={{ mb: 2 }}>
        Back to documents
      </Button>

      {documentQuery.isError && <Alert severity="error">Could not load this document.</Alert>}

      {documentQuery.data && (
        <Stack spacing={3}>
          <Stack direction="row" alignItems="flex-start" justifyContent="space-between">
            <Box>
              <Stack direction="row" alignItems="center" spacing={1.5}>
                <Typography variant="h4">{documentQuery.data.title}</Typography>
                <Chip
                  label={documentQuery.data.status.replace('_', ' ')}
                  color={statusColor[documentQuery.data.status]}
                />
                <Chip size="small" variant="outlined" label={documentQuery.data.document_type} />
              </Stack>
              <Typography variant="body2" color="text.secondary" sx={{ mt: 0.5 }}>
                Owner: {documentQuery.data.owner}
                {documentQuery.data.published_version_id ? ' · has a published version' : ''}
              </Typography>
            </Box>
            {documentQuery.data.status !== 'archived' && (
              <Button
                startIcon={<ArchiveIcon />}
                variant="outlined"
                color="warning"
                disabled={archiveMutation.isPending}
                onClick={() => archiveMutation.mutate()}
              >
                Archive
              </Button>
            )}
          </Stack>

          <Stack direction="row" alignItems="center" justifyContent="space-between">
            <Typography variant="h6">Versions</Typography>
            <Button size="small" startIcon={<AddIcon />} onClick={() => setVersionDialogOpen(true)}>
              New version
            </Button>
          </Stack>
          <Stack spacing={1.5}>
            {(versions.data ?? []).map((version) => (
              <VersionCard key={version.id} version={version} documentId={documentId} />
            ))}
            {!versions.data?.length && (
              <Typography variant="body2" color="text.secondary">
                No versions yet.
              </Typography>
            )}
          </Stack>
        </Stack>
      )}

      <Dialog open={versionDialogOpen} onClose={() => setVersionDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={versionForm.handleSubmit((v) => createVersionMutation.mutate(v))} noValidate>
          <DialogTitle>New version</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="File reference"
                placeholder="s3://bucket/policy-v2.pdf or a URL"
                error={Boolean(versionForm.formState.errors.file_reference)}
                helperText={versionForm.formState.errors.file_reference?.message}
                {...versionForm.register('file_reference')}
              />
              <TextField
                label="Change summary"
                multiline
                minRows={2}
                error={Boolean(versionForm.formState.errors.change_summary)}
                helperText={versionForm.formState.errors.change_summary?.message}
                {...versionForm.register('change_summary')}
              />
            </Stack>
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setVersionDialogOpen(false)}>Cancel</Button>
            <Button type="submit" variant="contained" disabled={versionForm.formState.isSubmitting}>
              Create
            </Button>
          </DialogActions>
        </Box>
      </Dialog>
    </Container>
  );
}
