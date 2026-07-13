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
import { createRiskSource, getRiskSources } from '../api/risk-sources';
import type { RiskSourceActivity, RiskSourceCategory, RiskSourceLevel } from '../api/types';

const CATEGORIES: RiskSourceCategory[] = [
  'state',
  'organized_crime',
  'terrorist',
  'activist',
  'vengeful_individual',
  'amateur',
  'specialized_firm',
];
const LEVELS: RiskSourceLevel[] = ['low', 'moderate', 'significant', 'very_high'];
const ACTIVITIES: RiskSourceActivity[] = ['low', 'medium', 'high'];

const schema = z.object({
  name: z.string().min(2, 'At least 2 characters'),
  category: z.enum([
    'state',
    'organized_crime',
    'terrorist',
    'activist',
    'vengeful_individual',
    'amateur',
    'specialized_firm',
  ]),
  motivation: z.enum(['low', 'moderate', 'significant', 'very_high']),
  resources: z.enum(['low', 'moderate', 'significant', 'very_high']),
  activity: z.enum(['low', 'medium', 'high']),
  description: z.string(),
});

type FormValues = z.infer<typeof schema>;

const levelColor: Record<RiskSourceLevel, 'default' | 'warning' | 'error'> = {
  low: 'default',
  moderate: 'default',
  significant: 'warning',
  very_high: 'error',
};

export function RiskSourcesPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const riskSources = useQuery({ queryKey: ['risk-sources'], queryFn: getRiskSources });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: {
      category: 'organized_crime',
      motivation: 'moderate',
      resources: 'moderate',
      activity: 'medium',
      description: '',
    },
  });

  const createMutation = useMutation({
    mutationFn: createRiskSource,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['risk-sources'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Risk sources</Typography>
          <Typography color="text.secondary">
            EBIOS RM Workshop 2: the catalog of threat actors ("who") that risk origins pair with a
            target objective.
          </Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New risk source
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Category</TableCell>
              <TableCell>Motivation</TableCell>
              <TableCell>Resources</TableCell>
              <TableCell>Activity</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(riskSources.data ?? []).map((riskSource) => (
              <TableRow key={riskSource.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{riskSource.name}</Typography>
                  <Typography variant="body2" color="text.secondary">
                    {riskSource.description}
                  </Typography>
                </TableCell>
                <TableCell>{riskSource.category}</TableCell>
                <TableCell>
                  <Chip size="small" label={riskSource.motivation} color={levelColor[riskSource.motivation]} />
                </TableCell>
                <TableCell>
                  <Chip size="small" label={riskSource.resources} color={levelColor[riskSource.resources]} />
                </TableCell>
                <TableCell>{riskSource.activity}</TableCell>
              </TableRow>
            ))}
            {!riskSources.data?.length && (
              <TableRow>
                <TableCell colSpan={5}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No risk sources recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New risk source</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Name"
                error={Boolean(errors.name)}
                helperText={errors.name?.message}
                {...register('name')}
              />
              <TextField label="Description" multiline minRows={2} {...register('description')} />
              <TextField label="Category" select defaultValue="organized_crime" {...register('category')}>
                {CATEGORIES.map((category) => (
                  <MenuItem key={category} value={category}>
                    {category}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Motivation" select defaultValue="moderate" {...register('motivation')}>
                {LEVELS.map((level) => (
                  <MenuItem key={level} value={level}>
                    {level}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Resources" select defaultValue="moderate" {...register('resources')}>
                {LEVELS.map((level) => (
                  <MenuItem key={level} value={level}>
                    {level}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Activity" select defaultValue="medium" {...register('activity')}>
                {ACTIVITIES.map((activity) => (
                  <MenuItem key={activity} value={activity}>
                    {activity}
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
