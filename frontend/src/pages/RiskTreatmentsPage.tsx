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
import { z } from 'zod';
import { createRiskTreatment, getRiskTreatments } from '../api/risk-treatments';
import { getStrategicScenarios } from '../api/strategic-scenarios';
import type { RiskTreatmentDecision, RiskTreatmentResidualRisk } from '../api/types';

const DECISIONS: RiskTreatmentDecision[] = ['avoid', 'reduce', 'transfer', 'accept'];
const RESIDUAL_LEVELS: RiskTreatmentResidualRisk[] = ['low', 'medium', 'high', 'critical'];

const schema = z.object({
  strategic_scenario_id: z.string().min(1, 'Required'),
  decision: z.enum(['avoid', 'reduce', 'transfer', 'accept']),
  justification: z.string(),
  residual_risk_level: z.enum(['low', 'medium', 'high', 'critical']),
});

type FormValues = z.infer<typeof schema>;

const decisionColor: Record<RiskTreatmentDecision, 'default' | 'primary' | 'warning' | 'success'> = {
  avoid: 'primary',
  reduce: 'warning',
  transfer: 'default',
  accept: 'success',
};

const residualColor: Record<RiskTreatmentResidualRisk, 'default' | 'warning' | 'error'> = {
  low: 'default',
  medium: 'default',
  high: 'warning',
  critical: 'error',
};

export function RiskTreatmentsPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const riskTreatments = useQuery({ queryKey: ['risk-treatments'], queryFn: getRiskTreatments });
  const strategicScenarios = useQuery({ queryKey: ['strategic-scenarios'], queryFn: getStrategicScenarios });
  const strategicScenarioNameById = new Map(
    (strategicScenarios.data ?? []).map((scenario) => [scenario.id, scenario.name]),
  );

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: {
      strategic_scenario_id: '',
      decision: 'reduce',
      justification: '',
      residual_risk_level: 'medium',
    },
  });

  const createMutation = useMutation({
    mutationFn: createRiskTreatment,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['risk-treatments'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Risk treatments</Typography>
          <Typography color="text.secondary">
            EBIOS RM Workshop 5: the final decision for each strategic scenario — avoid, reduce,
            transfer, or accept — and the residual risk left over after applying it.
          </Typography>
        </Box>
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={() => setDialogOpen(true)}
          disabled={!strategicScenarios.data?.length}
        >
          New risk treatment
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Strategic scenario</TableCell>
              <TableCell>Decision</TableCell>
              <TableCell>Justification</TableCell>
              <TableCell>Residual risk</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(riskTreatments.data ?? []).map((treatment) => (
              <TableRow key={treatment.id} hover>
                <TableCell>
                  {strategicScenarioNameById.get(treatment.strategic_scenario_id) ?? treatment.strategic_scenario_id}
                </TableCell>
                <TableCell>
                  <Chip size="small" label={treatment.decision} color={decisionColor[treatment.decision]} />
                </TableCell>
                <TableCell>{treatment.justification || '—'}</TableCell>
                <TableCell>
                  <Chip
                    size="small"
                    label={treatment.residual_risk_level}
                    color={residualColor[treatment.residual_risk_level]}
                  />
                </TableCell>
              </TableRow>
            ))}
            {!riskTreatments.data?.length && (
              <TableRow>
                <TableCell colSpan={4}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No risk treatments recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New risk treatment</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Strategic scenario"
                select
                defaultValue=""
                error={Boolean(errors.strategic_scenario_id)}
                helperText={errors.strategic_scenario_id?.message}
                {...register('strategic_scenario_id')}
              >
                {(strategicScenarios.data ?? []).map((scenario) => (
                  <MenuItem key={scenario.id} value={scenario.id}>
                    {scenario.name}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Decision" select defaultValue="reduce" {...register('decision')}>
                {DECISIONS.map((decision) => (
                  <MenuItem key={decision} value={decision}>
                    {decision}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Justification" multiline minRows={2} {...register('justification')} />
              <TextField
                label="Residual risk level"
                select
                defaultValue="medium"
                {...register('residual_risk_level')}
              >
                {RESIDUAL_LEVELS.map((level) => (
                  <MenuItem key={level} value={level}>
                    {level}
                  </MenuItem>
                ))}
              </TextField>
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
