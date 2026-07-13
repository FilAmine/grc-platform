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
import { createOperationalScenario, getOperationalScenarios } from '../api/operational-scenarios';
import { getStrategicScenarios } from '../api/strategic-scenarios';
import type { OperationalScenarioLikelihood } from '../api/types';

const LIKELIHOODS: OperationalScenarioLikelihood[] = ['low', 'medium', 'high', 'critical'];

const schema = z.object({
  strategic_scenario_id: z.string().min(1, 'Required'),
  name: z.string().min(2, 'At least 2 characters'),
  description: z.string(),
  mitre_technique_ids: z.string(),
  technical_likelihood: z.enum(['low', 'medium', 'high', 'critical']),
});

type FormValues = z.infer<typeof schema>;

const likelihoodColor: Record<OperationalScenarioLikelihood, 'default' | 'warning' | 'error'> = {
  low: 'default',
  medium: 'default',
  high: 'warning',
  critical: 'error',
};

function parseTechniqueIds(raw: string): string[] {
  return raw
    .split(',')
    .map((id) => id.trim())
    .filter(Boolean);
}

export function OperationalScenariosPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const operationalScenarios = useQuery({
    queryKey: ['operational-scenarios'],
    queryFn: getOperationalScenarios,
  });
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
      name: '',
      description: '',
      mitre_technique_ids: '',
      technical_likelihood: 'medium',
    },
  });

  const createMutation = useMutation({
    mutationFn: createOperationalScenario,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['operational-scenarios'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) =>
    createMutation.mutate({
      ...values,
      mitre_technique_ids: parseTechniqueIds(values.mitre_technique_ids),
    }),
  );

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Operational scenarios</Typography>
          <Typography color="text.secondary">
            EBIOS RM Workshop 4: elaborates a strategic scenario into a concrete technical attack
            chain, optionally referencing MITRE ATT&amp;CK techniques.
          </Typography>
        </Box>
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={() => setDialogOpen(true)}
          disabled={!strategicScenarios.data?.length}
        >
          New operational scenario
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Strategic scenario</TableCell>
              <TableCell>MITRE ATT&amp;CK techniques</TableCell>
              <TableCell>Technical likelihood</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(operationalScenarios.data ?? []).map((scenario) => (
              <TableRow key={scenario.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{scenario.name}</Typography>
                  <Typography variant="body2" color="text.secondary">
                    {scenario.description}
                  </Typography>
                </TableCell>
                <TableCell>
                  {strategicScenarioNameById.get(scenario.strategic_scenario_id) ?? scenario.strategic_scenario_id}
                </TableCell>
                <TableCell>
                  <Stack direction="row" spacing={0.5} flexWrap="wrap" useFlexGap>
                    {scenario.mitre_technique_ids.length
                      ? scenario.mitre_technique_ids.map((techniqueId) => (
                          <Chip key={techniqueId} size="small" label={techniqueId} variant="outlined" />
                        ))
                      : '—'}
                  </Stack>
                </TableCell>
                <TableCell>
                  <Chip
                    size="small"
                    label={scenario.technical_likelihood}
                    color={likelihoodColor[scenario.technical_likelihood]}
                  />
                </TableCell>
              </TableRow>
            ))}
            {!operationalScenarios.data?.length && (
              <TableRow>
                <TableCell colSpan={4}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No operational scenarios recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New operational scenario</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Name"
                error={Boolean(errors.name)}
                helperText={errors.name?.message}
                {...register('name')}
              />
              <TextField label="Description" multiline minRows={2} {...register('description')} />
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
              <TextField
                label="MITRE ATT&CK technique IDs (comma-separated)"
                placeholder="T1566, T1021, T1486"
                {...register('mitre_technique_ids')}
              />
              <TextField
                label="Technical likelihood"
                select
                defaultValue="medium"
                {...register('technical_likelihood')}
              >
                {LIKELIHOODS.map((likelihood) => (
                  <MenuItem key={likelihood} value={likelihood}>
                    {likelihood}
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
