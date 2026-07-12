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
import { createThreat, getThreats } from '../api/threats';
import type { ThreatCategory, ThreatLikelihood } from '../api/types';

const CATEGORIES: ThreatCategory[] = ['human', 'technical', 'environmental', 'organizational'];
const LIKELIHOODS: ThreatLikelihood[] = ['low', 'medium', 'high'];

const schema = z.object({
  name: z.string().min(2, 'At least 2 characters'),
  description: z.string(),
  category: z.enum(['human', 'technical', 'environmental', 'organizational']),
  likelihood: z.enum(['low', 'medium', 'high']),
});

type FormValues = z.infer<typeof schema>;

const likelihoodColor: Record<ThreatLikelihood, 'default' | 'warning' | 'error'> = {
  low: 'default',
  medium: 'warning',
  high: 'error',
};

export function ThreatsPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const threats = useQuery({ queryKey: ['threats'], queryFn: getThreats });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: { category: 'human', likelihood: 'medium', description: '' },
  });

  const createMutation = useMutation({
    mutationFn: createThreat,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['threats'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Threat catalog</Typography>
          <Typography color="text.secondary">Track threats that could affect the organization.</Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New threat
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Category</TableCell>
              <TableCell>Likelihood</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(threats.data ?? []).map((threat) => (
              <TableRow key={threat.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{threat.name}</Typography>
                  <Typography variant="body2" color="text.secondary">
                    {threat.description}
                  </Typography>
                </TableCell>
                <TableCell>{threat.category}</TableCell>
                <TableCell>
                  <Chip size="small" label={threat.likelihood} color={likelihoodColor[threat.likelihood]} />
                </TableCell>
              </TableRow>
            ))}
            {!threats.data?.length && (
              <TableRow>
                <TableCell colSpan={3}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No threats recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New threat</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Name"
                error={Boolean(errors.name)}
                helperText={errors.name?.message}
                {...register('name')}
              />
              <TextField label="Description" multiline minRows={2} {...register('description')} />
              <TextField label="Category" select defaultValue="human" {...register('category')}>
                {CATEGORIES.map((category) => (
                  <MenuItem key={category} value={category}>
                    {category}
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
