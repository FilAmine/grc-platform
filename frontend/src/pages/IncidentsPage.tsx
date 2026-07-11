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
  Select,
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
import { createIncident, getIncidents, updateIncidentStatus } from '../api/incidents';
import type { IncidentSeverity, IncidentStatus } from '../api/types';

const SEVERITIES: IncidentSeverity[] = ['low', 'medium', 'high', 'critical'];

const schema = z.object({
  title: z.string().min(2, 'At least 2 characters'),
  severity: z.enum(['low', 'medium', 'high', 'critical']),
  reported_by: z.string().min(2, 'At least 2 characters'),
  description: z.string(),
});

type FormValues = z.infer<typeof schema>;

const severityColor: Record<IncidentSeverity, 'default' | 'warning' | 'error'> = {
  low: 'default',
  medium: 'default',
  high: 'warning',
  critical: 'error',
};

const statusColor: Record<IncidentStatus, 'default' | 'info' | 'success' | 'warning'> = {
  open: 'warning',
  investigating: 'info',
  resolved: 'success',
  closed: 'default',
};

// Mirrors backend/app/modules/incidents/service.py::INCIDENT_STATUS_MACHINE
const NEXT_STATUSES: Record<IncidentStatus, IncidentStatus[]> = {
  open: ['investigating'],
  investigating: ['resolved'],
  resolved: ['closed', 'investigating'],
  closed: [],
};

export function IncidentsPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const incidents = useQuery({ queryKey: ['incidents'], queryFn: getIncidents });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema), defaultValues: { severity: 'medium', description: '' } });

  const createMutation = useMutation({
    mutationFn: createIncident,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['incidents'] });
      setDialogOpen(false);
      reset();
    },
  });

  const statusMutation = useMutation({
    mutationFn: ({ incidentId, status }: { incidentId: string; status: IncidentStatus }) =>
      updateIncidentStatus(incidentId, status),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['incidents'] });
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Incidents</Typography>
          <Typography color="text.secondary">Track and resolve security and operational incidents.</Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New incident
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Title</TableCell>
              <TableCell>Reported by</TableCell>
              <TableCell>Severity</TableCell>
              <TableCell>Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(incidents.data ?? []).map((incident) => (
              <TableRow key={incident.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{incident.title}</Typography>
                  <Typography variant="body2" color="text.secondary">
                    {incident.description}
                  </Typography>
                </TableCell>
                <TableCell>{incident.reported_by}</TableCell>
                <TableCell>
                  <Chip size="small" label={incident.severity} color={severityColor[incident.severity]} />
                </TableCell>
                <TableCell>
                  <Select
                    size="small"
                    value={incident.status}
                    disabled={statusMutation.isPending}
                    onChange={(event) =>
                      statusMutation.mutate({ incidentId: incident.id, status: event.target.value as IncidentStatus })
                    }
                    sx={{ minWidth: 150 }}
                  >
                    <MenuItem value={incident.status}>
                      <Chip size="small" label={incident.status} color={statusColor[incident.status]} />
                    </MenuItem>
                    {NEXT_STATUSES[incident.status].map((next) => (
                      <MenuItem key={next} value={next}>
                        <Chip size="small" label={next} color={statusColor[next]} />
                      </MenuItem>
                    ))}
                  </Select>
                </TableCell>
              </TableRow>
            ))}
            {!incidents.data?.length && (
              <TableRow>
                <TableCell colSpan={4}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No incidents recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New incident</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Title"
                error={Boolean(errors.title)}
                helperText={errors.title?.message}
                {...register('title')}
              />
              <TextField label="Description" multiline minRows={2} {...register('description')} />
              <TextField
                label="Reported by"
                error={Boolean(errors.reported_by)}
                helperText={errors.reported_by?.message}
                {...register('reported_by')}
              />
              <TextField label="Severity" select defaultValue="medium" {...register('severity')}>
                {SEVERITIES.map((severity) => (
                  <MenuItem key={severity} value={severity}>
                    {severity}
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
