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
  Chip,
  Container,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Grid,
  MenuItem,
  Paper,
  Stack,
  TextField,
  Typography,
} from '@mui/material';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { useEffect, useState } from 'react';
import { useForm } from 'react-hook-form';
import { Link as RouterLink, useParams } from 'react-router-dom';
import { z } from 'zod';
import {
  computeScore,
  createEvidence,
  getAssessment,
  getAssessmentResults,
  getEvidenceForResult,
  getRequirements,
  getScore,
  updateAssessmentStatus,
  upsertAssessmentResult,
} from '../api/compliance';
import type { AssessmentResult, AssessmentStatus, Requirement, RequirementResultStatus } from '../api/types';

const statusColor: Record<AssessmentStatus, 'default' | 'info' | 'success' | 'warning'> = {
  draft: 'default',
  in_progress: 'info',
  completed: 'success',
  archived: 'warning',
};

const resultStatusColor: Record<RequirementResultStatus, 'default' | 'success' | 'warning' | 'error' | 'info'> = {
  not_assessed: 'default',
  compliant: 'success',
  partially_compliant: 'warning',
  non_compliant: 'error',
  not_applicable: 'info',
};

const RESULT_STATUSES: RequirementResultStatus[] = [
  'not_assessed',
  'compliant',
  'partially_compliant',
  'non_compliant',
  'not_applicable',
];

// Mirrors backend/app/modules/compliance/service.py's Assessment status machine.
const NEXT_STATUSES: Record<AssessmentStatus, { label: string; status: AssessmentStatus }[]> = {
  draft: [{ label: 'Start assessment', status: 'in_progress' }],
  in_progress: [{ label: 'Mark completed', status: 'completed' }],
  completed: [
    { label: 'Archive', status: 'archived' },
    { label: 'Reopen', status: 'in_progress' },
  ],
  archived: [],
};

const evidenceSchema = z.object({
  title: z.string().min(2, 'At least 2 characters'),
  description: z.string().optional(),
  file_reference: z.string().min(1, 'Provide a file reference or URL'),
});
type EvidenceFormValues = z.infer<typeof evidenceSchema>;

function RequirementRow({ requirement, result, assessmentId }: { requirement: Requirement; result: AssessmentResult; assessmentId: string }) {
  const queryClient = useQueryClient();
  const [notes, setNotes] = useState(result.notes);
  const [dialogOpen, setDialogOpen] = useState(false);

  useEffect(() => setNotes(result.notes), [result.notes]);

  const evidence = useQuery({
    queryKey: ['assessment-results', result.id, 'evidence'],
    queryFn: () => getEvidenceForResult(result.id),
  });

  const statusMutation = useMutation({
    mutationFn: (status: RequirementResultStatus) =>
      upsertAssessmentResult(assessmentId, requirement.id, { status, notes }),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['assessments', assessmentId, 'results'] });
    },
  });

  const notesMutation = useMutation({
    mutationFn: () => upsertAssessmentResult(assessmentId, requirement.id, { status: result.status, notes }),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['assessments', assessmentId, 'results'] });
    },
  });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<EvidenceFormValues>({ resolver: zodResolver(evidenceSchema) });

  const createEvidenceMutation = useMutation({
    mutationFn: (values: EvidenceFormValues) =>
      createEvidence({ ...values, assessment_result_id: result.id }),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['assessment-results', result.id, 'evidence'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => createEvidenceMutation.mutate(values));

  return (
    <Accordion elevation={0} sx={{ border: '1px solid', borderColor: 'divider', '&:before': { display: 'none' } }}>
      <AccordionSummary expandIcon={<ExpandMoreIcon />}>
        <Stack direction="row" alignItems="center" spacing={1.5} sx={{ width: '100%', pr: 2 }}>
          <Chip size="small" label={requirement.code} variant="outlined" />
          <Typography fontWeight={600} sx={{ flexGrow: 1 }}>
            {requirement.title}
          </Typography>
          <Chip size="small" label={result.status.replace('_', ' ')} color={resultStatusColor[result.status]} />
        </Stack>
      </AccordionSummary>
      <AccordionDetails>
        <Stack spacing={2}>
          {requirement.description && (
            <Typography variant="body2" color="text.secondary">
              {requirement.description}
            </Typography>
          )}

          <TextField
            label="Status"
            select
            size="small"
            value={result.status}
            disabled={statusMutation.isPending}
            onChange={(event) => statusMutation.mutate(event.target.value as RequirementResultStatus)}
            sx={{ maxWidth: 260 }}
          >
            {RESULT_STATUSES.map((s) => (
              <MenuItem key={s} value={s}>
                {s.replace('_', ' ')}
              </MenuItem>
            ))}
          </TextField>

          <TextField
            label="Notes"
            multiline
            minRows={2}
            size="small"
            value={notes}
            onChange={(event) => setNotes(event.target.value)}
            onBlur={() => {
              if (notes !== result.notes) notesMutation.mutate();
            }}
          />

          <Stack direction="row" alignItems="center" justifyContent="space-between">
            <Typography variant="subtitle2">Evidence</Typography>
            <Button size="small" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
              Add
            </Button>
          </Stack>
          <Stack spacing={1}>
            {(evidence.data ?? []).map((item) => (
              <Box key={item.id}>
                <Typography variant="body2" fontWeight={600}>
                  {item.title}
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  {item.file_reference}
                </Typography>
              </Box>
            ))}
            {!evidence.data?.length && (
              <Typography variant="body2" color="text.secondary">
                No evidence attached yet.
              </Typography>
            )}
          </Stack>
        </Stack>
      </AccordionDetails>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>Add evidence</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Title"
                error={Boolean(errors.title)}
                helperText={errors.title?.message}
                {...register('title')}
              />
              <TextField label="Description (optional)" multiline minRows={2} {...register('description')} />
              <TextField
                label="File reference"
                placeholder="s3://bucket/evidence.pdf or a URL"
                error={Boolean(errors.file_reference)}
                helperText={errors.file_reference?.message}
                {...register('file_reference')}
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

export function AssessmentDetailPage() {
  const { assessmentId } = useParams<{ assessmentId: string }>();
  const queryClient = useQueryClient();

  const assessment = useQuery({
    queryKey: ['assessments', assessmentId],
    queryFn: () => getAssessment(assessmentId!),
    enabled: Boolean(assessmentId),
  });
  const requirements = useQuery({
    queryKey: ['framework-versions', assessment.data?.framework_version_id, 'requirements'],
    queryFn: () => getRequirements(assessment.data!.framework_version_id),
    enabled: Boolean(assessment.data),
  });
  const results = useQuery({
    queryKey: ['assessments', assessmentId, 'results'],
    queryFn: () => getAssessmentResults(assessmentId!),
    enabled: Boolean(assessmentId),
  });
  const score = useQuery({
    queryKey: ['assessments', assessmentId, 'score'],
    queryFn: () => getScore(assessmentId!),
    enabled: Boolean(assessmentId),
  });

  const statusMutation = useMutation({
    mutationFn: (status: AssessmentStatus) => updateAssessmentStatus(assessmentId!, status),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['assessments', assessmentId] });
      await queryClient.invalidateQueries({ queryKey: ['assessments'] });
    },
  });

  const computeScoreMutation = useMutation({
    mutationFn: () => computeScore(assessmentId!),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['assessments', assessmentId, 'score'] });
    },
  });

  if (!assessmentId) return null;

  const resultByRequirement = new Map((results.data ?? []).map((r) => [r.requirement_id, r]));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Button startIcon={<ArrowBackIcon />} component={RouterLink} to="/assessments" sx={{ mb: 2 }}>
        Back to assessments
      </Button>

      {assessment.isError && <Alert severity="error">Could not load this assessment.</Alert>}

      {assessment.data && (
        <Stack spacing={3}>
          <Stack direction="row" alignItems="flex-start" justifyContent="space-between">
            <Box>
              <Stack direction="row" alignItems="center" spacing={1.5}>
                <Typography variant="h4">{assessment.data.name}</Typography>
                <Chip label={assessment.data.status.replace('_', ' ')} color={statusColor[assessment.data.status]} />
              </Stack>
              <Typography variant="body2" color="text.secondary" sx={{ mt: 0.5 }}>
                {assessment.data.period_start
                  ? `${assessment.data.period_start} → ${assessment.data.period_end ?? '—'}`
                  : 'No period set'}
              </Typography>
            </Box>
            <Stack direction="row" spacing={1}>
              {NEXT_STATUSES[assessment.data.status].map((transition) => (
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

          <Grid container spacing={2}>
            <Grid item xs={12} sm={4}>
              <Paper elevation={0} sx={{ p: 2, border: '1px solid', borderColor: 'divider' }}>
                <Typography variant="body2" color="text.secondary">
                  Compliance score
                </Typography>
                <Typography variant="h6" fontWeight={800}>
                  {score.data ? `${score.data.score.toFixed(1)}%` : '—'}
                </Typography>
                {score.data && (
                  <Typography variant="caption" color="text.secondary">
                    as of {new Date(score.data.computed_at).toLocaleString()}
                  </Typography>
                )}
              </Paper>
            </Grid>
            <Grid item xs={12} sm={4}>
              <Paper elevation={0} sx={{ p: 2, border: '1px solid', borderColor: 'divider' }}>
                <Typography variant="body2" color="text.secondary">
                  Requirements assessed
                </Typography>
                <Typography variant="h6" fontWeight={800}>
                  {(results.data ?? []).filter((r) => r.status !== 'not_assessed').length}/{results.data?.length ?? 0}
                </Typography>
              </Paper>
            </Grid>
            <Grid item xs={12} sm={4} display="flex" alignItems="center">
              <Button
                variant="outlined"
                onClick={() => computeScoreMutation.mutate()}
                disabled={computeScoreMutation.isPending}
              >
                Recompute score
              </Button>
            </Grid>
          </Grid>

          <Box>
            <Typography variant="h6" sx={{ mb: 2 }}>
              Requirements
            </Typography>
            <Stack spacing={1.5}>
              {(requirements.data ?? []).map((requirement) => {
                const result = resultByRequirement.get(requirement.id);
                if (!result) return null;
                return (
                  <RequirementRow
                    key={requirement.id}
                    requirement={requirement}
                    result={result}
                    assessmentId={assessmentId}
                  />
                );
              })}
              {!requirements.data?.length && (
                <Typography variant="body2" color="text.secondary">
                  This framework version has no requirements loaded.
                </Typography>
              )}
            </Stack>
          </Box>
        </Stack>
      )}
    </Container>
  );
}
