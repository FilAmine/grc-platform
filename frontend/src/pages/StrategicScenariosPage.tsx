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
import { getEcosystemParties } from '../api/ecosystem-parties';
import { getFearedEvents } from '../api/feared-events';
import { getRiskOrigins } from '../api/risk-origins';
import { createStrategicScenario, getStrategicScenarios } from '../api/strategic-scenarios';
import type { StrategicScenarioLikelihood } from '../api/types';

const LIKELIHOODS: StrategicScenarioLikelihood[] = ['low', 'medium', 'high', 'critical'];

const schema = z.object({
  risk_origin_id: z.string().min(1, 'Required'),
  feared_event_id: z.string().min(1, 'Required'),
  ecosystem_party_id: z.string(),
  name: z.string().min(2, 'At least 2 characters'),
  description: z.string(),
  likelihood: z.enum(['low', 'medium', 'high', 'critical']),
});

type FormValues = z.infer<typeof schema>;

const likelihoodColor: Record<StrategicScenarioLikelihood, 'default' | 'warning' | 'error'> = {
  low: 'default',
  medium: 'default',
  high: 'warning',
  critical: 'error',
};

export function StrategicScenariosPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const scenarios = useQuery({ queryKey: ['strategic-scenarios'], queryFn: getStrategicScenarios });
  const riskOrigins = useQuery({ queryKey: ['risk-origins'], queryFn: getRiskOrigins });
  const fearedEvents = useQuery({ queryKey: ['feared-events'], queryFn: getFearedEvents });
  const ecosystemParties = useQuery({ queryKey: ['ecosystem-parties'], queryFn: getEcosystemParties });

  // Only retained risk origins are eligible: the backend rejects (409) a
  // strategic scenario built from one that isn't, since Workshop 3 is meant
  // to elaborate the SR/OV pairs Workshop 2 prioritized.
  const retainedRiskOrigins = (riskOrigins.data ?? []).filter((origin) => origin.retained);
  const riskOriginLabelById = new Map(
    retainedRiskOrigins.map((origin) => [origin.id, origin.target_objective]),
  );
  const fearedEventTitleById = new Map((fearedEvents.data ?? []).map((fe) => [fe.id, fe.title]));
  const ecosystemPartyNameById = new Map((ecosystemParties.data ?? []).map((ep) => [ep.id, ep.name]));

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: {
      risk_origin_id: '',
      feared_event_id: '',
      ecosystem_party_id: '',
      name: '',
      description: '',
      likelihood: 'medium',
    },
  });

  const createMutation = useMutation({
    mutationFn: createStrategicScenario,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['strategic-scenarios'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) =>
    createMutation.mutate({ ...values, ecosystem_party_id: values.ecosystem_party_id || null }),
  );

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Strategic scenarios</Typography>
          <Typography color="text.secondary">
            EBIOS RM Workshop 3: elaborates a retained risk origin into a concrete attack path
            targeting a feared event, optionally through an ecosystem party.
          </Typography>
        </Box>
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={() => setDialogOpen(true)}
          disabled={!retainedRiskOrigins.length || !fearedEvents.data?.length}
        >
          New strategic scenario
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Risk origin</TableCell>
              <TableCell>Feared event</TableCell>
              <TableCell>Via ecosystem party</TableCell>
              <TableCell>Likelihood</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(scenarios.data ?? []).map((scenario) => (
              <TableRow key={scenario.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{scenario.name}</Typography>
                  <Typography variant="body2" color="text.secondary">
                    {scenario.description}
                  </Typography>
                </TableCell>
                <TableCell>{riskOriginLabelById.get(scenario.risk_origin_id) ?? scenario.risk_origin_id}</TableCell>
                <TableCell>{fearedEventTitleById.get(scenario.feared_event_id) ?? scenario.feared_event_id}</TableCell>
                <TableCell>
                  {scenario.ecosystem_party_id
                    ? (ecosystemPartyNameById.get(scenario.ecosystem_party_id) ?? scenario.ecosystem_party_id)
                    : '—'}
                </TableCell>
                <TableCell>
                  <Chip size="small" label={scenario.likelihood} color={likelihoodColor[scenario.likelihood]} />
                </TableCell>
              </TableRow>
            ))}
            {!scenarios.data?.length && (
              <TableRow>
                <TableCell colSpan={5}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No strategic scenarios recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New strategic scenario</DialogTitle>
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
                label="Risk origin (retained only)"
                select
                defaultValue=""
                error={Boolean(errors.risk_origin_id)}
                helperText={errors.risk_origin_id?.message}
                {...register('risk_origin_id')}
              >
                {retainedRiskOrigins.map((origin) => (
                  <MenuItem key={origin.id} value={origin.id}>
                    {origin.target_objective}
                  </MenuItem>
                ))}
              </TextField>
              <TextField
                label="Feared event"
                select
                defaultValue=""
                error={Boolean(errors.feared_event_id)}
                helperText={errors.feared_event_id?.message}
                {...register('feared_event_id')}
              >
                {(fearedEvents.data ?? []).map((fearedEvent) => (
                  <MenuItem key={fearedEvent.id} value={fearedEvent.id}>
                    {fearedEvent.title}
                  </MenuItem>
                ))}
              </TextField>
              <TextField
                label="Ecosystem party (optional)"
                select
                defaultValue=""
                {...register('ecosystem_party_id')}
              >
                <MenuItem value="">None (direct attack)</MenuItem>
                {(ecosystemParties.data ?? []).map((ecosystemParty) => (
                  <MenuItem key={ecosystemParty.id} value={ecosystemParty.id}>
                    {ecosystemParty.name}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Likelihood" select defaultValue="medium" {...register('likelihood')}>
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
