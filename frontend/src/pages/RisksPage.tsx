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
import { createRisk, getRisks } from '../api/grc';
import type { RiskSeverity } from '../api/types';

const SEVERITIES: RiskSeverity[] = ['low', 'medium', 'high', 'critical'];

const schema = z.object({
  title: z.string().min(3, 'At least 3 characters'),
  description: z.string().min(1, 'Description is required'),
  severity: z.enum(['low', 'medium', 'high', 'critical']),
  owner: z.string().min(2, 'At least 2 characters'),
});

type FormValues = z.infer<typeof schema>;

const severityColor: Record<RiskSeverity, 'default' | 'warning' | 'error'> = {
  low: 'default',
  medium: 'default',
  high: 'warning',
  critical: 'error',
};

export function RisksPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const risks = useQuery({ queryKey: ['risks'], queryFn: getRisks });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema), defaultValues: { severity: 'medium' } });

  const createMutation = useMutation({
    mutationFn: createRisk,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['risks'] });
      await queryClient.invalidateQueries({ queryKey: ['summary'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Risk register</Typography>
          <Typography color="text.secondary">Track and triage organizational risks.</Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New risk
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Title</TableCell>
              <TableCell>Owner</TableCell>
              <TableCell>Severity</TableCell>
              <TableCell>Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(risks.data ?? []).map((risk) => (
              <TableRow key={risk.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{risk.title}</Typography>
                  <Typography variant="body2" color="text.secondary">
                    {risk.description}
                  </Typography>
                </TableCell>
                <TableCell>{risk.owner}</TableCell>
                <TableCell>
                  <Chip size="small" label={risk.severity} color={severityColor[risk.severity]} />
                </TableCell>
                <TableCell>{risk.status}</TableCell>
              </TableRow>
            ))}
            {!risks.data?.length && (
              <TableRow>
                <TableCell colSpan={4}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No risks recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New risk</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Title"
                error={Boolean(errors.title)}
                helperText={errors.title?.message}
                {...register('title')}
              />
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
