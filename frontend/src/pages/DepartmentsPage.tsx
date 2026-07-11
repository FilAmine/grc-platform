import { zodResolver } from '@hookform/resolvers/zod';
import AddIcon from '@mui/icons-material/Add';
import {
  Box,
  Button,
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
import { createDepartment, getDepartments } from '../api/departments';
import type { Department } from '../api/types';

const schema = z.object({
  name: z.string().min(2, 'At least 2 characters'),
  description: z.string(),
  parent_department_id: z.string(),
});

type FormValues = z.infer<typeof schema>;

// Departments come back as a flat list; there's no server-side tree endpoint,
// so walk parent_department_id client-side to render them indented by depth.
function buildRows(departments: Department[]): { department: Department; depth: number }[] {
  const byParent = new Map<string | null, Department[]>();
  for (const department of departments) {
    const key = department.parent_department_id;
    const siblings = byParent.get(key);
    if (siblings) {
      siblings.push(department);
    } else {
      byParent.set(key, [department]);
    }
  }

  const rows: { department: Department; depth: number }[] = [];
  function walk(parentId: string | null, depth: number) {
    for (const department of byParent.get(parentId) ?? []) {
      rows.push({ department, depth });
      walk(department.id, depth + 1);
    }
  }
  walk(null, 0);
  return rows;
}

export function DepartmentsPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const departments = useQuery({ queryKey: ['departments'], queryFn: getDepartments });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema), defaultValues: { description: '', parent_department_id: '' } });

  const createMutation = useMutation({
    mutationFn: createDepartment,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['departments'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) =>
    createMutation.mutate({
      ...values,
      parent_department_id: values.parent_department_id || null,
    }),
  );

  const rows = buildRows(departments.data ?? []);

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Departments</Typography>
          <Typography color="text.secondary">The organization's department hierarchy.</Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New department
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Description</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map(({ department, depth }) => (
              <TableRow key={department.id} hover>
                <TableCell sx={{ pl: 2 + depth * 3 }}>
                  <Typography fontWeight={600}>{department.name}</Typography>
                </TableCell>
                <TableCell>{department.description}</TableCell>
              </TableRow>
            ))}
            {!rows.length && (
              <TableRow>
                <TableCell colSpan={2}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No departments recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New department</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Name"
                error={Boolean(errors.name)}
                helperText={errors.name?.message}
                {...register('name')}
              />
              <TextField label="Description" multiline minRows={2} {...register('description')} />
              <TextField label="Parent department" select defaultValue="" {...register('parent_department_id')}>
                <MenuItem value="">None</MenuItem>
                {(departments.data ?? []).map((department) => (
                  <MenuItem key={department.id} value={department.id}>
                    {department.name}
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
