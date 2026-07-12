import { zodResolver } from '@hookform/resolvers/zod';
import { Add as AddIcon } from '@mui/icons-material';
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
  Paper,
  Stack,
  Switch,
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
import { assignRole, createUser, getUsers, removeRole, updateUser } from '../api/users';
import { getRoles } from '../api/rbac';
import type { User } from '../api/types';

const schema = z.object({
  email: z.string().email('Enter a valid email address'),
  full_name: z.string().min(2, 'At least 2 characters'),
  password: z
    .string()
    .min(12, 'At least 12 characters')
    .regex(/[a-z]/, 'Needs a lowercase letter')
    .regex(/[A-Z]/, 'Needs an uppercase letter')
    .regex(/\d/, 'Needs a digit'),
  is_superuser: z.boolean(),
});

type FormValues = z.infer<typeof schema>;

function RolesDialog({ user, onClose }: { user: User; onClose: () => void }) {
  const queryClient = useQueryClient();
  const roles = useQuery({ queryKey: ['roles'], queryFn: getRoles });

  const toggleMutation = useMutation({
    mutationFn: ({ roleId, assigned }: { roleId: string; assigned: boolean }) =>
      assigned ? removeRole(user.id, roleId) : assignRole(user.id, roleId),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['users'] });
    },
  });

  return (
    <Dialog open onClose={onClose} fullWidth maxWidth="sm">
      <DialogTitle>Roles for {user.full_name}</DialogTitle>
      <DialogContent>
        <Stack spacing={0.5} sx={{ mt: 1 }}>
          {(roles.data ?? []).map((role) => {
            const assigned = user.role_ids.includes(role.id);
            return (
              <FormControlLabel
                key={role.id}
                control={
                  <Checkbox
                    checked={assigned}
                    disabled={toggleMutation.isPending}
                    onChange={() => toggleMutation.mutate({ roleId: role.id, assigned })}
                  />
                }
                label={
                  <Stack direction="row" spacing={1} alignItems="center">
                    <Typography>{role.name}</Typography>
                    {role.is_system && <Chip size="small" label="system" variant="outlined" />}
                  </Stack>
                }
              />
            );
          })}
          {!roles.data?.length && (
            <Typography variant="body2" color="text.secondary">
              No roles defined yet.
            </Typography>
          )}
        </Stack>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Done</Button>
      </DialogActions>
    </Dialog>
  );
}

export function UsersPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const [rolesDialogUserId, setRolesDialogUserId] = useState<string | null>(null);

  const users = useQuery({ queryKey: ['users'], queryFn: getUsers });
  const rolesDialogUser = users.data?.find((user) => user.id === rolesDialogUserId) ?? null;
  const roles = useQuery({ queryKey: ['roles'], queryFn: getRoles });
  const roleName = (roleId: string) => roles.data?.find((role) => role.id === roleId)?.name ?? roleId;

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema), defaultValues: { is_superuser: false } });

  const createMutation = useMutation({
    mutationFn: createUser,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['users'] });
      setDialogOpen(false);
      reset();
    },
  });

  const activeMutation = useMutation({
    mutationFn: ({ userId, is_active }: { userId: string; is_active: boolean }) => updateUser(userId, { is_active }),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['users'] });
    },
  });

  const onSubmit = handleSubmit((values) => createMutation.mutate(values));

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Users</Typography>
          <Typography color="text.secondary">Manage who has access to your organization's workspace.</Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New user
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Email</TableCell>
              <TableCell>Roles</TableCell>
              <TableCell>Active</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(users.data ?? []).map((user) => (
              <TableRow key={user.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{user.full_name}</Typography>
                  {user.is_superuser && <Chip size="small" label="superuser" color="error" sx={{ mt: 0.5 }} />}
                </TableCell>
                <TableCell>{user.email}</TableCell>
                <TableCell>
                  <Stack direction="row" spacing={0.5} flexWrap="wrap" useFlexGap>
                    {user.role_ids.map((roleId) => (
                      <Chip key={roleId} size="small" label={roleName(roleId)} />
                    ))}
                    <Chip
                      size="small"
                      variant="outlined"
                      label={user.role_ids.length ? 'Edit' : 'Assign role'}
                      onClick={() => setRolesDialogUserId(user.id)}
                      sx={{ cursor: 'pointer' }}
                    />
                  </Stack>
                </TableCell>
                <TableCell>
                  <Switch
                    checked={user.is_active}
                    disabled={activeMutation.isPending}
                    onChange={(event) =>
                      activeMutation.mutate({ userId: user.id, is_active: event.target.checked })
                    }
                  />
                </TableCell>
              </TableRow>
            ))}
            {!users.data?.length && (
              <TableRow>
                <TableCell colSpan={4}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No users yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New user</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Full name"
                error={Boolean(errors.full_name)}
                helperText={errors.full_name?.message}
                {...register('full_name')}
              />
              <TextField
                label="Email"
                type="email"
                error={Boolean(errors.email)}
                helperText={errors.email?.message}
                {...register('email')}
              />
              <TextField
                label="Password"
                type="password"
                error={Boolean(errors.password)}
                helperText={errors.password?.message ?? 'At least 12 characters, mixing case and a digit'}
                {...register('password')}
              />
              <FormControlLabel
                control={<Checkbox {...register('is_superuser')} />}
                label="Grant superuser access (bypasses all permission checks)"
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

      {rolesDialogUser && <RolesDialog user={rolesDialogUser} onClose={() => setRolesDialogUserId(null)} />}
    </Container>
  );
}
