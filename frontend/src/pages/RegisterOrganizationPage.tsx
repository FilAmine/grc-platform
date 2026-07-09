import { zodResolver } from '@hookform/resolvers/zod';
import { Alert, Box, Button, Link as MuiLink, Paper, Stack, TextField, Typography } from '@mui/material';
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { Link as RouterLink, useNavigate } from 'react-router-dom';
import { z } from 'zod';
import { useAuth } from '../auth/AuthContext';

const schema = z.object({
  organization_name: z.string().min(2, 'Enter your organization name'),
  organization_slug: z
    .string()
    .min(2, 'Enter a URL-safe slug')
    .regex(/^[a-z0-9-]+$/, 'Lowercase letters, numbers, and hyphens only'),
  admin_full_name: z.string().min(2, 'Enter your full name'),
  admin_email: z.string().email('Enter a valid email address'),
  admin_password: z
    .string()
    .min(12, 'At least 12 characters')
    .regex(/[a-z]/, 'Needs a lowercase letter')
    .regex(/[A-Z]/, 'Needs an uppercase letter')
    .regex(/\d/, 'Needs a digit'),
});

type FormValues = z.infer<typeof schema>;

export function RegisterOrganizationPage() {
  const { registerOrganization } = useAuth();
  const navigate = useNavigate();
  const [error, setError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema) });

  const onSubmit = handleSubmit(async (values) => {
    setError(null);
    try {
      await registerOrganization(values);
      navigate('/', { replace: true });
    } catch {
      setError('Could not create the organization. The email or slug may already be in use.');
    }
  });

  return (
    <Box minHeight="100vh" display="grid" sx={{ placeItems: 'center', bgcolor: 'background.default', py: 4 }}>
      <Paper elevation={0} sx={{ p: 4, width: 420, border: '1px solid', borderColor: 'divider' }}>
        <Typography variant="h5" fontWeight={800} gutterBottom>
          Create your organization
        </Typography>
        <Typography color="text.secondary" sx={{ mb: 3 }}>
          You'll be set up as the Admin of a new tenant.
        </Typography>
        <Box component="form" onSubmit={onSubmit} noValidate>
          <Stack spacing={2}>
            {error && <Alert severity="error">{error}</Alert>}
            <TextField
              label="Organization name"
              error={Boolean(errors.organization_name)}
              helperText={errors.organization_name?.message}
              {...register('organization_name')}
            />
            <TextField
              label="Organization slug"
              placeholder="acme-corp"
              error={Boolean(errors.organization_slug)}
              helperText={errors.organization_slug?.message}
              {...register('organization_slug')}
            />
            <TextField
              label="Your full name"
              error={Boolean(errors.admin_full_name)}
              helperText={errors.admin_full_name?.message}
              {...register('admin_full_name')}
            />
            <TextField
              label="Email"
              type="email"
              autoComplete="username"
              error={Boolean(errors.admin_email)}
              helperText={errors.admin_email?.message}
              {...register('admin_email')}
            />
            <TextField
              label="Password"
              type="password"
              autoComplete="new-password"
              error={Boolean(errors.admin_password)}
              helperText={errors.admin_password?.message ?? 'At least 12 characters, mixing case and a digit'}
              {...register('admin_password')}
            />
            <Button type="submit" variant="contained" size="large" disabled={isSubmitting}>
              Create organization
            </Button>
            <Typography variant="body2" color="text.secondary" align="center">
              Already have an account?{' '}
              <MuiLink component={RouterLink} to="/login">
                Sign in
              </MuiLink>
            </Typography>
          </Stack>
        </Box>
      </Paper>
    </Box>
  );
}
