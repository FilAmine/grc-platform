import { zodResolver } from '@hookform/resolvers/zod';
import { Add as AddIcon } from '@mui/icons-material';
import {
  Box,
  Button,
  Checkbox,
  Chip,
  Container,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  FormControlLabel,
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
import { getFearedEvents } from '../api/feared-events';
import { createRiskOrigin, getRiskOrigins } from '../api/risk-origins';
import { getRiskSources } from '../api/risk-sources';
import type { RiskOriginPertinence } from '../api/types';

const PERTINENCES: RiskOriginPertinence[] = ['low', 'medium', 'high', 'critical'];

const schema = z.object({
  risk_source_id: z.string().min(1, 'Required'),
  target_objective: z.string().min(2, 'At least 2 characters'),
  feared_event_id: z.string(),
  pertinence: z.enum(['low', 'medium', 'high', 'critical']),
  retained: z.boolean(),
});

type FormValues = z.infer<typeof schema>;

const pertinenceColor: Record<RiskOriginPertinence, 'default' | 'warning' | 'error'> = {
  low: 'default',
  medium: 'default',
  high: 'warning',
  critical: 'error',
};

export function RiskOriginsPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const riskOrigins = useQuery({ queryKey: ['risk-origins'], queryFn: getRiskOrigins });
  const riskSources = useQuery({ queryKey: ['risk-sources'], queryFn: getRiskSources });
  const fearedEvents = useQuery({ queryKey: ['feared-events'], queryFn: getFearedEvents });
  const riskSourceNameById = new Map((riskSources.data ?? []).map((rs) => [rs.id, rs.name]));
  const fearedEventTitleById = new Map((fearedEvents.data ?? []).map((fe) => [fe.id, fe.title]));

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: {
      risk_source_id: '',
      target_objective: '',
      feared_event_id: '',
      pertinence: 'medium',
      retained: false,
    },
  });

  const createMutation = useMutation({
    mutationFn: createRiskOrigin,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['risk-origins'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) =>
    createMutation.mutate({ ...values, feared_event_id: values.feared_event_id || null }),
  );

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Risk origins</Typography>
          <Typography color="text.secondary">
            EBIOS RM Workshop 2's "couple SR/OV": a risk source paired with what it's after, scored
            for pertinence. "Retained" marks pairs prioritized for further analysis.
          </Typography>
        </Box>
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={() => setDialogOpen(true)}
          disabled={!riskSources.data?.length}
        >
          New risk origin
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Risk source</TableCell>
              <TableCell>Target objective</TableCell>
              <TableCell>Feared event</TableCell>
              <TableCell>Pertinence</TableCell>
              <TableCell>Retained</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(riskOrigins.data ?? []).map((riskOrigin) => (
              <TableRow key={riskOrigin.id} hover>
                <TableCell>{riskSourceNameById.get(riskOrigin.risk_source_id) ?? riskOrigin.risk_source_id}</TableCell>
                <TableCell>{riskOrigin.target_objective}</TableCell>
                <TableCell>
                  {riskOrigin.feared_event_id
                    ? (fearedEventTitleById.get(riskOrigin.feared_event_id) ?? riskOrigin.feared_event_id)
                    : '—'}
                </TableCell>
                <TableCell>
                  <Chip
                    size="small"
                    label={riskOrigin.pertinence}
                    color={pertinenceColor[riskOrigin.pertinence]}
                  />
                </TableCell>
                <TableCell>
                  {riskOrigin.retained ? <Chip size="small" label="retained" color="primary" /> : '—'}
                </TableCell>
              </TableRow>
            ))}
            {!riskOrigins.data?.length && (
              <TableRow>
                <TableCell colSpan={5}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No risk origins recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New risk origin</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Risk source"
                select
                defaultValue=""
                error={Boolean(errors.risk_source_id)}
                helperText={errors.risk_source_id?.message}
                {...register('risk_source_id')}
              >
                {(riskSources.data ?? []).map((riskSource) => (
                  <MenuItem key={riskSource.id} value={riskSource.id}>
                    {riskSource.name}
                  </MenuItem>
                ))}
              </TextField>
              <TextField
                label="Target objective"
                multiline
                minRows={2}
                error={Boolean(errors.target_objective)}
                helperText={errors.target_objective?.message}
                {...register('target_objective')}
              />
              <TextField label="Feared event (optional)" select defaultValue="" {...register('feared_event_id')}>
                <MenuItem value="">None</MenuItem>
                {(fearedEvents.data ?? []).map((fearedEvent) => (
                  <MenuItem key={fearedEvent.id} value={fearedEvent.id}>
                    {fearedEvent.title}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Pertinence" select defaultValue="medium" {...register('pertinence')}>
                {PERTINENCES.map((pertinence) => (
                  <MenuItem key={pertinence} value={pertinence}>
                    {pertinence}
                  </MenuItem>
                ))}
              </TextField>
              <FormControlLabel
                control={<Checkbox {...register('retained')} />}
                label="Retained for Workshop 3"
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
