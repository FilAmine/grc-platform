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
import { createTask, getTasks, updateTaskStatus } from '../api/tasks';
import type { TaskStatus } from '../api/types';

const schema = z.object({
  title: z.string().min(2, 'At least 2 characters'),
  assignee: z.string().min(2, 'At least 2 characters'),
  description: z.string(),
  due_date: z.string().optional(),
});

type FormValues = z.infer<typeof schema>;

const statusColor: Record<TaskStatus, 'default' | 'info' | 'success'> = {
  open: 'default',
  in_progress: 'info',
  done: 'success',
};

// Mirrors backend/app/modules/tasks/service.py::TASK_STATUS_MACHINE
const NEXT_STATUSES: Record<TaskStatus, TaskStatus[]> = {
  open: ['in_progress'],
  in_progress: ['done'],
  done: ['in_progress'],
};

export function TasksPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const tasks = useQuery({ queryKey: ['tasks'], queryFn: getTasks });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema), defaultValues: { description: '' } });

  const createMutation = useMutation({
    mutationFn: createTask,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['tasks'] });
      setDialogOpen(false);
      reset();
    },
  });

  const statusMutation = useMutation({
    mutationFn: ({ taskId, status }: { taskId: string; status: TaskStatus }) => updateTaskStatus(taskId, status),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['tasks'] });
    },
  });

  const onSubmit = handleSubmit((values) =>
    createMutation.mutate({ ...values, due_date: values.due_date || null }),
  );

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Tasks</Typography>
          <Typography color="text.secondary">Generic follow-up items, not tied to any one module.</Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New task
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Title</TableCell>
              <TableCell>Assignee</TableCell>
              <TableCell>Due date</TableCell>
              <TableCell>Status</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(tasks.data ?? []).map((task) => (
              <TableRow key={task.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{task.title}</Typography>
                  <Typography variant="body2" color="text.secondary">
                    {task.description}
                  </Typography>
                </TableCell>
                <TableCell>{task.assignee}</TableCell>
                <TableCell>{task.due_date ?? '—'}</TableCell>
                <TableCell>
                  <Select
                    size="small"
                    value={task.status}
                    disabled={statusMutation.isPending}
                    onChange={(event) =>
                      statusMutation.mutate({ taskId: task.id, status: event.target.value as TaskStatus })
                    }
                    sx={{ minWidth: 140 }}
                  >
                    <MenuItem value={task.status}>
                      <Chip size="small" label={task.status.replace('_', ' ')} color={statusColor[task.status]} />
                    </MenuItem>
                    {NEXT_STATUSES[task.status].map((next) => (
                      <MenuItem key={next} value={next}>
                        <Chip size="small" label={next.replace('_', ' ')} color={statusColor[next]} />
                      </MenuItem>
                    ))}
                  </Select>
                </TableCell>
              </TableRow>
            ))}
            {!tasks.data?.length && (
              <TableRow>
                <TableCell colSpan={4}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No tasks recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New task</DialogTitle>
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
                label="Assignee"
                error={Boolean(errors.assignee)}
                helperText={errors.assignee?.message}
                {...register('assignee')}
              />
              <TextField
                label="Due date"
                type="date"
                InputLabelProps={{ shrink: true }}
                {...register('due_date')}
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
