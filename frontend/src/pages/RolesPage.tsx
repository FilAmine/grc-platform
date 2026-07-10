import { zodResolver } from '@hookform/resolvers/zod';
import AddIcon from '@mui/icons-material/Add';
import {
  Box,
  Button,
  Checkbox,
  Chip,
  Container,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  FormControlLabel,
  FormGroup,
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
import { useMemo, useState } from 'react';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { createRole, getPermissions, getRoles, setRolePermissions } from '../api/rbac';
import type { Permission, Role } from '../api/types';

function groupByResource(permissions: Permission[]): Map<string, Permission[]> {
  const groups = new Map<string, Permission[]>();
  for (const permission of permissions) {
    const [resource] = permission.code.split(':');
    const bucket = groups.get(resource) ?? [];
    bucket.push(permission);
    groups.set(resource, bucket);
  }
  return groups;
}

function PermissionChecklist({
  permissions,
  selected,
  onToggle,
  disabled,
}: {
  permissions: Permission[];
  selected: Set<string>;
  onToggle: (code: string) => void;
  disabled?: boolean;
}) {
  const groups = useMemo(() => groupByResource(permissions), [permissions]);
  return (
    <Stack spacing={1.5}>
      {Array.from(groups.entries())
        .sort(([a], [b]) => a.localeCompare(b))
        .map(([resource, items]) => (
          <Box key={resource}>
            <Typography variant="subtitle2" sx={{ textTransform: 'capitalize', mb: 0.5 }}>
              {resource}
            </Typography>
            <FormGroup row>
              {items.map((permission) => (
                <FormControlLabel
                  key={permission.code}
                  control={
                    <Checkbox
                      size="small"
                      checked={selected.has(permission.code)}
                      disabled={disabled}
                      onChange={() => onToggle(permission.code)}
                    />
                  }
                  label={permission.code.split(':')[1]}
                  title={permission.description}
                />
              ))}
            </FormGroup>
          </Box>
        ))}
    </Stack>
  );
}

const schema = z.object({
  name: z.string().min(2, 'At least 2 characters'),
  description: z.string().optional(),
});
type FormValues = z.infer<typeof schema>;

function EditPermissionsDialog({ role, permissions, onClose }: { role: Role; permissions: Permission[]; onClose: () => void }) {
  const queryClient = useQueryClient();
  const [selected, setSelected] = useState(new Set(role.permission_codes));

  const mutation = useMutation({
    mutationFn: () => setRolePermissions(role.id, Array.from(selected)),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['roles'] });
      onClose();
    },
  });

  const toggle = (code: string) => {
    setSelected((prev) => {
      const next = new Set(prev);
      if (next.has(code)) next.delete(code);
      else next.add(code);
      return next;
    });
  };

  return (
    <Dialog open onClose={onClose} fullWidth maxWidth="md">
      <DialogTitle>Permissions for {role.name}</DialogTitle>
      <DialogContent>
        <Box sx={{ mt: 1 }}>
          <PermissionChecklist permissions={permissions} selected={selected} onToggle={toggle} />
        </Box>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button variant="contained" onClick={() => mutation.mutate()} disabled={mutation.isPending}>
          Save
        </Button>
      </DialogActions>
    </Dialog>
  );
}

export function RolesPage() {
  const queryClient = useQueryClient();
  const [createOpen, setCreateOpen] = useState(false);
  const [editRoleId, setEditRoleId] = useState<string | null>(null);
  const [createSelected, setCreateSelected] = useState<Set<string>>(new Set());

  const roles = useQuery({ queryKey: ['roles'], queryFn: getRoles });
  const permissions = useQuery({ queryKey: ['permissions'], queryFn: getPermissions });
  const editRole = roles.data?.find((role) => role.id === editRoleId) ?? null;

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema) });

  const createMutation = useMutation({
    mutationFn: (values: FormValues) =>
      createRole({ ...values, permission_codes: Array.from(createSelected) }),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['roles'] });
      setCreateOpen(false);
      setCreateSelected(new Set());
      reset();
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  const toggleCreateSelected = (code: string) => {
    setCreateSelected((prev) => {
      const next = new Set(prev);
      if (next.has(code)) next.delete(code);
      else next.add(code);
      return next;
    });
  };

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Roles</Typography>
          <Typography color="text.secondary">
            System roles are shared across every organization and cannot be edited. Custom roles are yours to define.
          </Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setCreateOpen(true)}>
          New role
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Description</TableCell>
              <TableCell>Type</TableCell>
              <TableCell>Permissions</TableCell>
              <TableCell />
            </TableRow>
          </TableHead>
          <TableBody>
            {(roles.data ?? []).map((role) => (
              <TableRow key={role.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{role.name}</Typography>
                </TableCell>
                <TableCell>{role.description || '—'}</TableCell>
                <TableCell>
                  <Chip size="small" label={role.is_system ? 'system' : 'custom'} color={role.is_system ? 'default' : 'info'} />
                </TableCell>
                <TableCell>{role.permission_codes.length}</TableCell>
                <TableCell align="right">
                  <Button
                    size="small"
                    disabled={role.is_system}
                    onClick={() => setEditRoleId(role.id)}
                  >
                    {role.is_system ? 'Not editable' : 'Edit permissions'}
                  </Button>
                </TableCell>
              </TableRow>
            ))}
            {!roles.data?.length && (
              <TableRow>
                <TableCell colSpan={5}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No roles defined yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={createOpen} onClose={() => setCreateOpen(false)} fullWidth maxWidth="md">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New role</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Name"
                error={Boolean(errors.name)}
                helperText={errors.name?.message}
                {...register('name')}
              />
              <TextField label="Description (optional)" {...register('description')} />
              <Box>
                <Typography variant="subtitle2" gutterBottom>
                  Permissions
                </Typography>
                <PermissionChecklist
                  permissions={permissions.data ?? []}
                  selected={createSelected}
                  onToggle={toggleCreateSelected}
                />
              </Box>
            </Stack>
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setCreateOpen(false)}>Cancel</Button>
            <Button type="submit" variant="contained" disabled={isSubmitting}>
              Create
            </Button>
          </DialogActions>
        </Box>
      </Dialog>

      {editRole && (
        <EditPermissionsDialog role={editRole} permissions={permissions.data ?? []} onClose={() => setEditRoleId(null)} />
      )}
    </Container>
  );
}
