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
import { createEcosystemParty, getEcosystemParties } from '../api/ecosystem-parties';
import type { EcosystemPartyCategory, EcosystemPartyLevel } from '../api/types';

const CATEGORIES: EcosystemPartyCategory[] = ['provider', 'subcontractor', 'partner', 'client'];
const LEVELS: EcosystemPartyLevel[] = ['low', 'medium', 'high'];

const schema = z.object({
  name: z.string().min(2, 'At least 2 characters'),
  category: z.enum(['provider', 'subcontractor', 'partner', 'client']),
  dependency_level: z.enum(['low', 'medium', 'high']),
  cyber_maturity: z.enum(['low', 'medium', 'high']),
  description: z.string(),
});

type FormValues = z.infer<typeof schema>;

const dependencyColor: Record<EcosystemPartyLevel, 'default' | 'warning' | 'error'> = {
  low: 'default',
  medium: 'default',
  high: 'warning',
};

// Low maturity is the risky end of this scale (more attractive stepping
// stone for an attacker), so its color mapping is inverted vs. dependency.
const maturityColor: Record<EcosystemPartyLevel, 'default' | 'warning' | 'error'> = {
  low: 'error',
  medium: 'warning',
  high: 'default',
};

export function EcosystemPartiesPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const ecosystemParties = useQuery({ queryKey: ['ecosystem-parties'], queryFn: getEcosystemParties });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: {
      category: 'provider',
      dependency_level: 'medium',
      cyber_maturity: 'medium',
      description: '',
    },
  });

  const createMutation = useMutation({
    mutationFn: createEcosystemParty,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['ecosystem-parties'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Ecosystem parties</Typography>
          <Typography color="text.secondary">
            EBIOS RM Workshop 3's ecosystem cartography: third parties an attack path can use as a
            stepping stone.
          </Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New ecosystem party
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Category</TableCell>
              <TableCell>Dependency</TableCell>
              <TableCell>Cyber maturity</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(ecosystemParties.data ?? []).map((ecosystemParty) => (
              <TableRow key={ecosystemParty.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{ecosystemParty.name}</Typography>
                  <Typography variant="body2" color="text.secondary">
                    {ecosystemParty.description}
                  </Typography>
                </TableCell>
                <TableCell>{ecosystemParty.category}</TableCell>
                <TableCell>
                  <Chip
                    size="small"
                    label={ecosystemParty.dependency_level}
                    color={dependencyColor[ecosystemParty.dependency_level]}
                  />
                </TableCell>
                <TableCell>
                  <Chip
                    size="small"
                    label={ecosystemParty.cyber_maturity}
                    color={maturityColor[ecosystemParty.cyber_maturity]}
                  />
                </TableCell>
              </TableRow>
            ))}
            {!ecosystemParties.data?.length && (
              <TableRow>
                <TableCell colSpan={4}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No ecosystem parties recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New ecosystem party</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Name"
                error={Boolean(errors.name)}
                helperText={errors.name?.message}
                {...register('name')}
              />
              <TextField label="Description" multiline minRows={2} {...register('description')} />
              <TextField label="Category" select defaultValue="provider" {...register('category')}>
                {CATEGORIES.map((category) => (
                  <MenuItem key={category} value={category}>
                    {category}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Dependency level" select defaultValue="medium" {...register('dependency_level')}>
                {LEVELS.map((level) => (
                  <MenuItem key={level} value={level}>
                    {level}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Cyber maturity" select defaultValue="medium" {...register('cyber_maturity')}>
                {LEVELS.map((level) => (
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
