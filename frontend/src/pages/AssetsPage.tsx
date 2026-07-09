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
  Tooltip,
  Typography,
} from '@mui/material';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { createAsset, getAssets, updateAssetLifecycle } from '../api/assets';
import type { AssetLifecycleStage, AssetType, ClassificationLevel } from '../api/types';

const ASSET_TYPES: AssetType[] = ['hardware', 'software', 'cloud_service', 'application', 'business_asset', 'service'];
const CLASSIFICATION_LEVELS: ClassificationLevel[] = ['low', 'medium', 'high'];
const LIFECYCLE_STAGES: AssetLifecycleStage[] = ['planned', 'in_use', 'maintenance', 'retired', 'disposed'];

const schema = z.object({
  name: z.string().min(2, 'At least 2 characters'),
  asset_type: z.enum(['hardware', 'software', 'cloud_service', 'application', 'business_asset', 'service']),
  owner: z.string().min(2, 'At least 2 characters'),
  supplier: z.string().optional(),
  description: z.string().optional(),
  confidentiality: z.enum(['low', 'medium', 'high']),
  integrity: z.enum(['low', 'medium', 'high']),
  availability: z.enum(['low', 'medium', 'high']),
});

type FormValues = z.infer<typeof schema>;

const classificationColor: Record<ClassificationLevel, 'default' | 'warning' | 'error'> = {
  low: 'default',
  medium: 'warning',
  high: 'error',
};

const lifecycleColor: Record<AssetLifecycleStage, 'default' | 'info' | 'success' | 'warning' | 'error'> = {
  planned: 'default',
  in_use: 'success',
  maintenance: 'warning',
  retired: 'default',
  disposed: 'error',
};

const typeLabel: Record<AssetType, string> = {
  hardware: 'Hardware',
  software: 'Software',
  cloud_service: 'Cloud service',
  application: 'Application',
  business_asset: 'Business asset',
  service: 'Service',
};

export function AssetsPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const assets = useQuery({ queryKey: ['assets'], queryFn: getAssets });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: { confidentiality: 'low', integrity: 'low', availability: 'low' },
  });

  const createMutation = useMutation({
    mutationFn: createAsset,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['assets'] });
      setDialogOpen(false);
      reset();
    },
  });

  const lifecycleMutation = useMutation({
    mutationFn: ({ assetId, stage }: { assetId: string; stage: AssetLifecycleStage }) =>
      updateAssetLifecycle(assetId, stage),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['assets'] });
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Assets</Typography>
          <Typography color="text.secondary">
            Hardware, software, cloud services, applications, and business assets.
          </Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New asset
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Type</TableCell>
              <TableCell>Owner</TableCell>
              <TableCell>CIA</TableCell>
              <TableCell>Lifecycle</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(assets.data ?? []).map((asset) => (
              <TableRow key={asset.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{asset.name}</Typography>
                  {asset.supplier && (
                    <Typography variant="body2" color="text.secondary">
                      Supplier: {asset.supplier}
                    </Typography>
                  )}
                </TableCell>
                <TableCell>
                  <Chip size="small" label={typeLabel[asset.asset_type]} />
                </TableCell>
                <TableCell>{asset.owner}</TableCell>
                <TableCell>
                  <Stack direction="row" spacing={0.5}>
                    <Tooltip title={`Confidentiality: ${asset.confidentiality}`}>
                      <Chip size="small" label={`C:${asset.confidentiality[0].toUpperCase()}`} color={classificationColor[asset.confidentiality]} />
                    </Tooltip>
                    <Tooltip title={`Integrity: ${asset.integrity}`}>
                      <Chip size="small" label={`I:${asset.integrity[0].toUpperCase()}`} color={classificationColor[asset.integrity]} />
                    </Tooltip>
                    <Tooltip title={`Availability: ${asset.availability}`}>
                      <Chip size="small" label={`A:${asset.availability[0].toUpperCase()}`} color={classificationColor[asset.availability]} />
                    </Tooltip>
                  </Stack>
                </TableCell>
                <TableCell>
                  <Select
                    size="small"
                    value={asset.lifecycle_stage}
                    disabled={lifecycleMutation.isPending}
                    onChange={(event) =>
                      lifecycleMutation.mutate({ assetId: asset.id, stage: event.target.value as AssetLifecycleStage })
                    }
                    sx={{ minWidth: 130 }}
                  >
                    {LIFECYCLE_STAGES.map((stage) => (
                      <MenuItem key={stage} value={stage}>
                        <Chip size="small" label={stage.replace('_', ' ')} color={lifecycleColor[stage]} />
                      </MenuItem>
                    ))}
                  </Select>
                </TableCell>
              </TableRow>
            ))}
            {!assets.data?.length && (
              <TableRow>
                <TableCell colSpan={5}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No assets recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New asset</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Name"
                error={Boolean(errors.name)}
                helperText={errors.name?.message}
                {...register('name')}
              />
              <TextField label="Type" select defaultValue="hardware" {...register('asset_type')}>
                {ASSET_TYPES.map((type) => (
                  <MenuItem key={type} value={type}>
                    {typeLabel[type]}
                  </MenuItem>
                ))}
              </TextField>
              <TextField
                label="Owner"
                error={Boolean(errors.owner)}
                helperText={errors.owner?.message}
                {...register('owner')}
              />
              <TextField label="Supplier (optional)" {...register('supplier')} />
              <TextField label="Description (optional)" multiline minRows={2} {...register('description')} />
              <Stack direction="row" spacing={2}>
                <TextField label="Confidentiality" select defaultValue="low" fullWidth {...register('confidentiality')}>
                  {CLASSIFICATION_LEVELS.map((level) => (
                    <MenuItem key={level} value={level}>
                      {level}
                    </MenuItem>
                  ))}
                </TextField>
                <TextField label="Integrity" select defaultValue="low" fullWidth {...register('integrity')}>
                  {CLASSIFICATION_LEVELS.map((level) => (
                    <MenuItem key={level} value={level}>
                      {level}
                    </MenuItem>
                  ))}
                </TextField>
                <TextField label="Availability" select defaultValue="low" fullWidth {...register('availability')}>
                  {CLASSIFICATION_LEVELS.map((level) => (
                    <MenuItem key={level} value={level}>
                      {level}
                    </MenuItem>
                  ))}
                </TextField>
              </Stack>
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
