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
import { getAssets } from '../api/assets';
import { createFearedEvent, getFearedEvents } from '../api/feared-events';
import type { FearedEventCriterion, FearedEventGravity } from '../api/types';

const CRITERIA: FearedEventCriterion[] = ['confidentiality', 'integrity', 'availability'];
const GRAVITIES: FearedEventGravity[] = ['low', 'medium', 'high', 'critical'];

const schema = z.object({
  title: z.string().min(2, 'At least 2 characters'),
  asset_id: z.string().min(1, 'Required'),
  criterion: z.enum(['confidentiality', 'integrity', 'availability']),
  gravity: z.enum(['low', 'medium', 'high', 'critical']),
  description: z.string(),
});

type FormValues = z.infer<typeof schema>;

const gravityColor: Record<FearedEventGravity, 'default' | 'warning' | 'error'> = {
  low: 'default',
  medium: 'default',
  high: 'warning',
  critical: 'error',
};

export function FearedEventsPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const fearedEvents = useQuery({ queryKey: ['feared-events'], queryFn: getFearedEvents });
  const assets = useQuery({ queryKey: ['assets'], queryFn: getAssets });
  const assetNameById = new Map((assets.data ?? []).map((asset) => [asset.id, asset.name]));

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: { criterion: 'confidentiality', gravity: 'medium', description: '', asset_id: '' },
  });

  const createMutation = useMutation({
    mutationFn: createFearedEvent,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['feared-events'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Feared events</Typography>
          <Typography color="text.secondary">
            Undesirable events impacting an asset's confidentiality, integrity, or availability.
          </Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New feared event
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Title</TableCell>
              <TableCell>Asset</TableCell>
              <TableCell>Criterion</TableCell>
              <TableCell>Gravity</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(fearedEvents.data ?? []).map((fearedEvent) => (
              <TableRow key={fearedEvent.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{fearedEvent.title}</Typography>
                  <Typography variant="body2" color="text.secondary">
                    {fearedEvent.description}
                  </Typography>
                </TableCell>
                <TableCell>{assetNameById.get(fearedEvent.asset_id) ?? fearedEvent.asset_id}</TableCell>
                <TableCell>{fearedEvent.criterion}</TableCell>
                <TableCell>
                  <Chip size="small" label={fearedEvent.gravity} color={gravityColor[fearedEvent.gravity]} />
                </TableCell>
              </TableRow>
            ))}
            {!fearedEvents.data?.length && (
              <TableRow>
                <TableCell colSpan={4}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No feared events recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New feared event</DialogTitle>
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
                label="Asset"
                select
                defaultValue=""
                error={Boolean(errors.asset_id)}
                helperText={errors.asset_id?.message}
                {...register('asset_id')}
              >
                {(assets.data ?? []).map((asset) => (
                  <MenuItem key={asset.id} value={asset.id}>
                    {asset.name}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Criterion" select defaultValue="confidentiality" {...register('criterion')}>
                {CRITERIA.map((criterion) => (
                  <MenuItem key={criterion} value={criterion}>
                    {criterion}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Gravity" select defaultValue="medium" {...register('gravity')}>
                {GRAVITIES.map((gravity) => (
                  <MenuItem key={gravity} value={gravity}>
                    {gravity}
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
