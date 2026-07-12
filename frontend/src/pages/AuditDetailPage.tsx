import { zodResolver } from '@hookform/resolvers/zod';
import {
  Add as AddIcon,
  ArrowBack as ArrowBackIcon,
  ExpandMore as ExpandMoreIcon,
} from '@mui/icons-material';
import {
  Accordion,
  AccordionDetails,
  AccordionSummary,
  Alert,
  Box,
  Button,
  Checkbox,
  Chip,
  Container,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Divider,
  Grid,
  IconButton,
  MenuItem,
  Paper,
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
  createChecklistItem,
  createCorrectiveAction,
  createFinding,
  getAudit,
  getAuditReport,
  getChecklistItems,
  getCorrectiveActions,
  getFindings,
  updateAuditStatus,
  updateChecklistItemStatus,
  updateCorrectiveActionStatus,
  updateFindingStatus,
} from '../api/audits';
import type {
  AuditStatus,
  ChecklistItemStatus,
  CorrectiveActionStatus,
  Finding,
  FindingSeverity,
  FindingStatus,
} from '../api/types';

const statusColor: Record<AuditStatus, 'default' | 'info' | 'success' | 'warning'> = {
  planned: 'default',
  in_progress: 'info',
  completed: 'success',
  closed: 'warning',
};

const severityColor: Record<FindingSeverity, 'default' | 'warning' | 'error'> = {
  minor: 'default',
  major: 'warning',
  critical: 'error',
};

// Mirrors backend/app/modules/audits/service.py::AUDIT_STATUS_MACHINE
const NEXT_STATUSES: Record<AuditStatus, { label: string; status: AuditStatus }[]> = {
  planned: [{ label: 'Start audit', status: 'in_progress' }],
  in_progress: [{ label: 'Mark completed', status: 'completed' }],
  completed: [
    { label: 'Close audit', status: 'closed' },
    { label: 'Reopen', status: 'in_progress' },
  ],
  closed: [],
};

const findingSchema = z.object({
  title: z.string().min(2, 'At least 2 characters'),
  description: z.string().min(1, 'Required'),
  severity: z.enum(['minor', 'major', 'critical']),
});
type FindingFormValues = z.infer<typeof findingSchema>;

const checklistSchema = z.object({ description: z.string().min(2, 'At least 2 characters') });
type ChecklistFormValues = z.infer<typeof checklistSchema>;

const correctiveActionSchema = z.object({
  description: z.string().min(2, 'At least 2 characters'),
  owner: z.string().min(2, 'At least 2 characters'),
  due_date: z.string().optional(),
});
type CorrectiveActionFormValues = z.infer<typeof correctiveActionSchema>;

function FindingCard({ finding, auditId }: { finding: Finding; auditId: string }) {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const actions = useQuery({
    queryKey: ['findings', finding.id, 'corrective-actions'],
    queryFn: () => getCorrectiveActions(finding.id),
  });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<CorrectiveActionFormValues>({ resolver: zodResolver(correctiveActionSchema) });

  const statusMutation = useMutation({
    mutationFn: (status: FindingStatus) => updateFindingStatus(finding.id, status),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['audits', auditId, 'findings'] });
      await queryClient.invalidateQueries({ queryKey: ['audits', auditId, 'report'] });
    },
  });

  const createActionMutation = useMutation({
    mutationFn: (values: CorrectiveActionFormValues) =>
      createCorrectiveAction(finding.id, { ...values, due_date: values.due_date || null }),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['findings', finding.id, 'corrective-actions'] });
      await queryClient.invalidateQueries({ queryKey: ['audits', auditId, 'report'] });
      setDialogOpen(false);
      reset();
    },
  });

  const toggleActionMutation = useMutation({
    mutationFn: ({ actionId, status }: { actionId: string; status: CorrectiveActionStatus }) =>
      updateCorrectiveActionStatus(actionId, status),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['findings', finding.id, 'corrective-actions'] });
      await queryClient.invalidateQueries({ queryKey: ['audits', auditId, 'report'] });
    },
  });

  const onSubmit = handleSubmit((values) => createActionMutation.mutate(values));

  return (
    <Accordion elevation={0} sx={{ border: '1px solid', borderColor: 'divider', '&:before': { display: 'none' } }}>
      <AccordionSummary expandIcon={<ExpandMoreIcon />}>
        <Stack direction="row" alignItems="center" spacing={1.5} sx={{ width: '100%', pr: 2 }}>
          <Chip size="small" label={finding.severity} color={severityColor[finding.severity]} />
          <Typography fontWeight={600} sx={{ flexGrow: 1 }}>
            {finding.title}
          </Typography>
          <Chip size="small" variant="outlined" label={finding.status.replace('_', ' ')} />
        </Stack>
      </AccordionSummary>
      <AccordionDetails>
        <Stack spacing={2}>
          <Typography variant="body2" color="text.secondary">
            {finding.description}
          </Typography>
          <Stack direction="row" spacing={1}>
            {(['open', 'in_remediation', 'closed'] as FindingStatus[])
              .filter((s) => s !== finding.status)
              .map((s) => (
                <Button
                  key={s}
                  size="small"
                  variant="outlined"
                  disabled={statusMutation.isPending}
                  onClick={() => statusMutation.mutate(s)}
                >
                  Mark {s.replace('_', ' ')}
                </Button>
              ))}
          </Stack>

          <Divider />

          <Stack direction="row" alignItems="center" justifyContent="space-between">
            <Typography variant="subtitle2">Corrective actions</Typography>
            <Button size="small" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
              Add
            </Button>
          </Stack>
          <Stack spacing={1}>
            {(actions.data ?? []).map((action) => (
              <Stack key={action.id} direction="row" alignItems="center" spacing={1.5}>
                <Checkbox
                  size="small"
                  checked={action.status === 'done'}
                  onChange={(_, checked) =>
                    toggleActionMutation.mutate({ actionId: action.id, status: checked ? 'done' : 'open' })
                  }
                />
                <Box sx={{ flexGrow: 1 }}>
                  <Typography
                    variant="body2"
                    sx={{ textDecoration: action.status === 'done' ? 'line-through' : 'none' }}
                  >
                    {action.description}
                  </Typography>
                  <Typography variant="caption" color="text.secondary">
                    {action.owner}
                    {action.due_date ? ` · due ${action.due_date}` : ''}
                  </Typography>
                </Box>
                <Chip size="small" label={action.status.replace('_', ' ')} />
              </Stack>
            ))}
            {!actions.data?.length && (
              <Typography variant="body2" color="text.secondary">
                No corrective actions yet.
              </Typography>
            )}
          </Stack>
        </Stack>
      </AccordionDetails>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New corrective action</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Description"
                multiline
                minRows={2}
                error={Boolean(errors.description)}
                helperText={errors.description?.message}
                {...register('description')}
              />
              <TextField
                label="Owner"
                error={Boolean(errors.owner)}
                helperText={errors.owner?.message}
                {...register('owner')}
              />
              <TextField
                label="Due date"
                type="date"
                InputLabelProps={{ shrink: true }}
                {...register('due_date')}
              />
            </Stack>
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setDialogOpen(false)}>Cancel</Button>
            <Button type="submit" variant="contained" disabled={isSubmitting}>
              Add
            </Button>
          </DialogActions>
        </Box>
      </Dialog>
    </Accordion>
  );
}

export function AuditDetailPage() {
  const { auditId } = useParams<{ auditId: string }>();
  const queryClient = useQueryClient();
  const [findingDialogOpen, setFindingDialogOpen] = useState(false);
  const [checklistDialogOpen, setChecklistDialogOpen] = useState(false);

  const audit = useQuery({ queryKey: ['audits', auditId], queryFn: () => getAudit(auditId!), enabled: Boolean(auditId) });
  const report = useQuery({
    queryKey: ['audits', auditId, 'report'],
    queryFn: () => getAuditReport(auditId!),
    enabled: Boolean(auditId),
  });
  const checklistItems = useQuery({
    queryKey: ['audits', auditId, 'checklist-items'],
    queryFn: () => getChecklistItems(auditId!),
    enabled: Boolean(auditId),
  });
  const findings = useQuery({
    queryKey: ['audits', auditId, 'findings'],
    queryFn: () => getFindings(auditId!),
    enabled: Boolean(auditId),
  });

  const statusMutation = useMutation({
    mutationFn: (status: AuditStatus) => updateAuditStatus(auditId!, status),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['audits', auditId] });
      await queryClient.invalidateQueries({ queryKey: ['audits'] });
    },
  });

  const findingForm = useForm<FindingFormValues>({
    resolver: zodResolver(findingSchema),
    defaultValues: { severity: 'minor' },
  });
  const createFindingMutation = useMutation({
    mutationFn: (values: FindingFormValues) => createFinding(auditId!, values),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['audits', auditId, 'findings'] });
      await queryClient.invalidateQueries({ queryKey: ['audits', auditId, 'report'] });
      setFindingDialogOpen(false);
      findingForm.reset();
    },
  });

  const checklistForm = useForm<ChecklistFormValues>({ resolver: zodResolver(checklistSchema) });
  const createChecklistMutation = useMutation({
    mutationFn: (values: ChecklistFormValues) => createChecklistItem(auditId!, values.description),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['audits', auditId, 'checklist-items'] });
      await queryClient.invalidateQueries({ queryKey: ['audits', auditId, 'report'] });
      setChecklistDialogOpen(false);
      checklistForm.reset();
    },
  });

  const toggleChecklistMutation = useMutation({
    mutationFn: ({ itemId, status }: { itemId: string; status: ChecklistItemStatus }) =>
      updateChecklistItemStatus(itemId, status, ''),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['audits', auditId, 'checklist-items'] });
      await queryClient.invalidateQueries({ queryKey: ['audits', auditId, 'report'] });
    },
  });

  if (!auditId) return null;

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Button startIcon={<ArrowBackIcon />} component={RouterLink} to="/audits" sx={{ mb: 2 }}>
        Back to audits
      </Button>

      {audit.isError && <Alert severity="error">Could not load this audit.</Alert>}

      {audit.data && (
        <Stack spacing={3}>
          <Stack direction="row" alignItems="flex-start" justifyContent="space-between">
            <Box>
              <Stack direction="row" alignItems="center" spacing={1.5}>
                <Typography variant="h4">{audit.data.title}</Typography>
                <Chip label={audit.data.status.replace('_', ' ')} color={statusColor[audit.data.status]} />
              </Stack>
              <Typography color="text.secondary" sx={{ mt: 0.5 }}>
                {audit.data.scope}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                Lead auditor: {audit.data.lead_auditor}
                {audit.data.period_start ? ` · ${audit.data.period_start} → ${audit.data.period_end ?? '—'}` : ''}
              </Typography>
            </Box>
            <Stack direction="row" spacing={1}>
              {NEXT_STATUSES[audit.data.status].map((transition) => (
                <Button
                  key={transition.status}
                  variant="outlined"
                  disabled={statusMutation.isPending}
                  onClick={() => statusMutation.mutate(transition.status)}
                >
                  {transition.label}
                </Button>
              ))}
            </Stack>
          </Stack>

          {report.data && (
            <Grid container spacing={2}>
              <Grid item xs={6} sm={3}>
                <Paper elevation={0} sx={{ p: 2, border: '1px solid', borderColor: 'divider' }}>
                  <Typography variant="body2" color="text.secondary">
                    Checklist
                  </Typography>
                  <Typography variant="h6" fontWeight={800}>
                    {report.data.checklist_done}/{report.data.checklist_total}
                  </Typography>
                </Paper>
              </Grid>
              <Grid item xs={6} sm={3}>
                <Paper elevation={0} sx={{ p: 2, border: '1px solid', borderColor: 'divider' }}>
                  <Typography variant="body2" color="text.secondary">
                    Open findings
                  </Typography>
                  <Typography variant="h6" fontWeight={800}>
                    {report.data.open_findings}
                  </Typography>
                </Paper>
              </Grid>
              <Grid item xs={6} sm={3}>
                <Paper elevation={0} sx={{ p: 2, border: '1px solid', borderColor: 'divider' }}>
                  <Typography variant="body2" color="text.secondary">
                    Corrective actions
                  </Typography>
                  <Typography variant="h6" fontWeight={800}>
                    {report.data.corrective_actions_done}/{report.data.corrective_actions_total}
                  </Typography>
                </Paper>
              </Grid>
              <Grid item xs={6} sm={3}>
                <Paper elevation={0} sx={{ p: 2, border: '1px solid', borderColor: 'divider' }}>
                  <Typography variant="body2" color="text.secondary" gutterBottom>
                    Findings by severity
                  </Typography>
                  <Stack direction="row" spacing={0.5} flexWrap="wrap">
                    {Object.entries(report.data.findings_by_severity).map(([severity, count]) => (
                      <Chip key={severity} size="small" label={`${severity}: ${count}`} />
                    ))}
                    {!Object.keys(report.data.findings_by_severity).length && (
                      <Typography variant="body2" color="text.secondary">
                        None
                      </Typography>
                    )}
                  </Stack>
                </Paper>
              </Grid>
            </Grid>
          )}

          <Grid container spacing={3}>
            <Grid item xs={12} lg={5}>
              <Paper elevation={0} sx={{ p: 3, border: '1px solid', borderColor: 'divider' }}>
                <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 2 }}>
                  <Typography variant="h6">Checklist</Typography>
                  <IconButton size="small" onClick={() => setChecklistDialogOpen(true)}>
                    <AddIcon fontSize="small" />
                  </IconButton>
                </Stack>
                <Stack spacing={1}>
                  {(checklistItems.data ?? []).map((item) => (
                    <Stack key={item.id} direction="row" alignItems="center" spacing={1.5}>
                      <Checkbox
                        size="small"
                        checked={item.status === 'done'}
                        onChange={(_, checked) =>
                          toggleChecklistMutation.mutate({ itemId: item.id, status: checked ? 'done' : 'pending' })
                        }
                      />
                      <Typography
                        variant="body2"
                        sx={{ textDecoration: item.status === 'done' ? 'line-through' : 'none' }}
                      >
                        {item.description}
                      </Typography>
                    </Stack>
                  ))}
                  {!checklistItems.data?.length && (
                    <Typography variant="body2" color="text.secondary">
                      No checklist items yet.
                    </Typography>
                  )}
                </Stack>
              </Paper>
            </Grid>

            <Grid item xs={12} lg={7}>
              <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 2 }}>
                <Typography variant="h6">Findings</Typography>
                <Button size="small" startIcon={<AddIcon />} onClick={() => setFindingDialogOpen(true)}>
                  New finding
                </Button>
              </Stack>
              <Stack spacing={1.5}>
                {(findings.data ?? []).map((finding) => (
                  <FindingCard key={finding.id} finding={finding} auditId={auditId} />
                ))}
                {!findings.data?.length && (
                  <Typography variant="body2" color="text.secondary">
                    No findings recorded yet.
                  </Typography>
                )}
              </Stack>
            </Grid>
          </Grid>
        </Stack>
      )}

      <Dialog open={checklistDialogOpen} onClose={() => setChecklistDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={checklistForm.handleSubmit((v) => createChecklistMutation.mutate(v))} noValidate>
          <DialogTitle>New checklist item</DialogTitle>
          <DialogContent>
            <TextField
              autoFocus
              fullWidth
              label="Description"
              sx={{ mt: 1 }}
              error={Boolean(checklistForm.formState.errors.description)}
              helperText={checklistForm.formState.errors.description?.message}
              {...checklistForm.register('description')}
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setChecklistDialogOpen(false)}>Cancel</Button>
            <Button type="submit" variant="contained" disabled={checklistForm.formState.isSubmitting}>
              Add
            </Button>
          </DialogActions>
        </Box>
      </Dialog>

      <Dialog open={findingDialogOpen} onClose={() => setFindingDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={findingForm.handleSubmit((v) => createFindingMutation.mutate(v))} noValidate>
          <DialogTitle>New finding</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Title"
                error={Boolean(findingForm.formState.errors.title)}
                helperText={findingForm.formState.errors.title?.message}
                {...findingForm.register('title')}
              />
              <TextField
                label="Description"
                multiline
                minRows={2}
                error={Boolean(findingForm.formState.errors.description)}
                helperText={findingForm.formState.errors.description?.message}
                {...findingForm.register('description')}
              />
              <TextField label="Severity" select defaultValue="minor" {...findingForm.register('severity')}>
                {(['minor', 'major', 'critical'] as FindingSeverity[]).map((s) => (
                  <MenuItem key={s} value={s}>
                    {s}
                  </MenuItem>
                ))}
              </TextField>
            </Stack>
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setFindingDialogOpen(false)}>Cancel</Button>
            <Button type="submit" variant="contained" disabled={findingForm.formState.isSubmitting}>
              Add
            </Button>
          </DialogActions>
        </Box>
      </Dialog>
    </Container>
  );
}
