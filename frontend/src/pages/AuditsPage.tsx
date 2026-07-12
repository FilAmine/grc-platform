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
import { createAudit, getAudits } from '../api/audits';
import type { AuditStatus } from '../api/types';

const schema = z.object({
  title: z.string().min(2, 'At least 2 characters'),
  scope: z.string().min(1, 'Describe the audit scope'),
  lead_auditor: z.string().min(2, 'At least 2 characters'),
  period_start: z.string().optional(),
  period_end: z.string().optional(),
});

type FormValues = z.infer<typeof schema>;

const statusColor: Record<AuditStatus, 'default' | 'info' | 'success' | 'warning'> = {
  planned: 'default',
  in_progress: 'info',
  completed: 'success',
  closed: 'warning',
};

export function AuditsPage() {
  const queryClient = useQueryClient();
  const navigate = useNavigate();
  const [dialogOpen, setDialogOpen] = useState(false);
  const audits = useQuery({ queryKey: ['audits'], queryFn: getAudits });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema) });

  const createMutation = useMutation({
    mutationFn: (values: FormValues) =>
      createAudit({
        title: values.title,
        scope: values.scope,
        lead_auditor: values.lead_auditor,
        period_start: values.period_start || null,
        period_end: values.period_end || null,
      }),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['audits'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Audits</Typography>
          <Typography color="text.secondary">Plan, run, and report on internal and external audits.</Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New audit
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Title</TableCell>
              <TableCell>Lead auditor</TableCell>
              <TableCell>Period</TableCell>
              <TableCell>Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(audits.data ?? []).map((audit) => (
              <TableRow
                key={audit.id}
                hover
                onClick={() => navigate(`/audits/${audit.id}`)}
                sx={{ cursor: 'pointer' }}
              >
                <TableCell>
                  <Typography fontWeight={600} color="text.primary">
                    {audit.title}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    {audit.scope}
                  </Typography>
                </TableCell>
                <TableCell>{audit.lead_auditor}</TableCell>
                <TableCell>
                  {audit.period_start ?? '—'} → {audit.period_end ?? '—'}
                </TableCell>
                <TableCell>
                  <Chip size="small" label={audit.status.replace('_', ' ')} color={statusColor[audit.status]} />
                </TableCell>
              </TableRow>
            ))}
            {!audits.data?.length && (
              <TableRow>
                <TableCell colSpan={4}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No audits planned yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New audit</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Title"
                error={Boolean(errors.title)}
                helperText={errors.title?.message}
                {...register('title')}
              />
              <TextField
                label="Scope"
                multiline
                minRows={2}
                error={Boolean(errors.scope)}
                helperText={errors.scope?.message}
                {...register('scope')}
              />
              <TextField
                label="Lead auditor"
                error={Boolean(errors.lead_auditor)}
                helperText={errors.lead_auditor?.message}
                {...register('lead_auditor')}
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
