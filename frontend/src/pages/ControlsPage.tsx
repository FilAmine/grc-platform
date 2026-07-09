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
import { createControl, getControls } from '../api/grc';

const schema = z.object({
  name: z.string().min(3, 'At least 3 characters'),
  description: z.string().min(1, 'Description is required'),
  framework: z.string().min(2, 'Enter a framework code, e.g. iso27001'),
});

type FormValues = z.infer<typeof schema>;

export function ControlsPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const controls = useQuery({ queryKey: ['controls'], queryFn: getControls });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema) });

  const createMutation = useMutation({
    mutationFn: createControl,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['controls'] });
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
          <Typography variant="h4">Controls</Typography>
          <Typography color="text.secondary">Controls implemented across your organization.</Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New control
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Framework</TableCell>
              <TableCell>Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(controls.data ?? []).map((control) => (
              <TableRow key={control.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{control.name}</Typography>
                  <Typography variant="body2" color="text.secondary">
                    {control.description}
                  </Typography>
                </TableCell>
                <TableCell>
                  <Chip size="small" label={control.framework} />
                </TableCell>
                <TableCell>{control.status}</TableCell>
              </TableRow>
            ))}
            {!controls.data?.length && (
              <TableRow>
                <TableCell colSpan={3}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No controls defined yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New control</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Name"
                error={Boolean(errors.name)}
                helperText={errors.name?.message}
                {...register('name')}
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
                label="Framework"
                placeholder="iso27001"
                error={Boolean(errors.framework)}
                helperText={errors.framework?.message}
                {...register('framework')}
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
