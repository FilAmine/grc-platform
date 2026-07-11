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
import { createVulnerability, getVulnerabilities } from '../api/vulnerabilities';
import type { VulnerabilitySeverity, VulnerabilityStatus } from '../api/types';

const SEVERITIES: VulnerabilitySeverity[] = ['low', 'medium', 'high', 'critical'];

const schema = z.object({
  name: z.string().min(2, 'At least 2 characters'),
  description: z.string(),
  severity: z.enum(['low', 'medium', 'high', 'critical']),
});

type FormValues = z.infer<typeof schema>;

const severityColor: Record<VulnerabilitySeverity, 'default' | 'warning' | 'error'> = {
  low: 'default',
  medium: 'default',
  high: 'warning',
  critical: 'error',
};

const statusColor: Record<VulnerabilityStatus, 'default' | 'warning' | 'success'> = {
  open: 'warning',
  mitigated: 'default',
  accepted: 'default',
  closed: 'success',
};

export function VulnerabilitiesPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const vulnerabilities = useQuery({ queryKey: ['vulnerabilities'], queryFn: getVulnerabilities });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema), defaultValues: { severity: 'medium', description: '' } });

  const createMutation = useMutation({
    mutationFn: createVulnerability,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['vulnerabilities'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Vulnerability register</Typography>
          <Typography color="text.secondary">Track known vulnerabilities and their remediation status.</Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New vulnerability
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Severity</TableCell>
              <TableCell>Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(vulnerabilities.data ?? []).map((vulnerability) => (
              <TableRow key={vulnerability.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{vulnerability.name}</Typography>
                  <Typography variant="body2" color="text.secondary">
                    {vulnerability.description}
                  </Typography>
                </TableCell>
                <TableCell>
                  <Chip size="small" label={vulnerability.severity} color={severityColor[vulnerability.severity]} />
                </TableCell>
                <TableCell>
                  <Chip size="small" label={vulnerability.status} color={statusColor[vulnerability.status]} />
                </TableCell>
              </TableRow>
            ))}
            {!vulnerabilities.data?.length && (
              <TableRow>
                <TableCell colSpan={3}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No vulnerabilities recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New vulnerability</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Name"
                error={Boolean(errors.name)}
                helperText={errors.name?.message}
                {...register('name')}
              />
              <TextField label="Description" multiline minRows={2} {...register('description')} />
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
