import { zodResolver } from '@hookform/resolvers/zod';
import { Alert, Box, Button, Collapse, Divider, Link as MuiLink, Paper, Stack, TextField, Typography } from '@mui/material';
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { Link as RouterLink, useLocation, useNavigate } from 'react-router-dom';
import { z } from 'zod';
import { useAuth } from '../auth/AuthContext';

const schema = z.object({
  email: z.string().email('Enter a valid email address'),
  password: z.string().min(1, 'Password is required'),
});

type FormValues = z.infer<typeof schema>;

const ssoSlugSchema = z.object({
  organization_slug: z.string().min(1, "Enter your organization's slug"),
});

type SsoSlugFormValues = z.infer<typeof ssoSlugSchema>;

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000/api/v1';

export function LoginPage() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [error, setError] = useState<string | null>(null);
  const [ssoOpen, setSsoOpen] = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema) });

  const {
    register: registerSsoSlug,
    handleSubmit: handleSsoSlugSubmit,
    formState: { errors: ssoSlugErrors },
  } = useForm<SsoSlugFormValues>({ resolver: zodResolver(ssoSlugSchema) });

  const onSubmit = handleSubmit(async (values) => {
    setError(null);
    try {
      await login(values.email, values.password);
      const redirectTo = (location.state as { from?: Location })?.from?.pathname ?? '/';
      navigate(redirectTo, { replace: true });
    } catch {
      setError('Invalid email or password.');
    }
  });

  const onSsoSlugSubmit = handleSsoSlugSubmit((values) => {
    // Real browser navigation, not an axios call -- this has to leave the SPA
    // to trigger the identity provider's OAuth redirect.
    window.location.href = `${apiBaseUrl}/auth/sso/${values.organization_slug}/login`;
  });

  return (
    <Box minHeight="100vh" display="grid" sx={{ placeItems: 'center', bgcolor: 'background.default' }}>
      <Paper elevation={0} sx={{ p: 4, width: 380, border: '1px solid', borderColor: 'divider' }}>
        <Typography variant="h5" fontWeight={800} gutterBottom>
          Sign in
        </Typography>
        <Typography color="text.secondary" sx={{ mb: 3 }}>
          Access your organization's GRC workspace.
        </Typography>
        <Box component="form" onSubmit={onSubmit} noValidate>
          <Stack spacing={2}>
            {error && <Alert severity="error">{error}</Alert>}
            <TextField
              label="Email"
              type="email"
              autoComplete="username"
              error={Boolean(errors.email)}
              helperText={errors.email?.message}
              {...register('email')}
            />
            <TextField
              label="Password"
              type="password"
              autoComplete="current-password"
              error={Boolean(errors.password)}
              helperText={errors.password?.message}
              {...register('password')}
            />
            <Button type="submit" variant="contained" size="large" disabled={isSubmitting}>
              Sign in
            </Button>
            <Typography variant="body2" color="text.secondary" align="center">
              New organization?{' '}
              <MuiLink component={RouterLink} to="/register">
                Create one
              </MuiLink>
            </Typography>
          </Stack>
        </Box>

        <Divider sx={{ my: 2 }} />

        <MuiLink
          component="button"
          type="button"
          variant="body2"
          onClick={() => setSsoOpen((open) => !open)}
          sx={{ display: 'block', textAlign: 'center', width: '100%' }}
        >
          Sign in with your organization's SSO
        </MuiLink>
        <Collapse in={ssoOpen}>
          <Box component="form" onSubmit={onSsoSlugSubmit} noValidate sx={{ mt: 2 }}>
            <Stack spacing={2}>
              <TextField
                label="Organization slug"
                placeholder="acme-corp"
                error={Boolean(ssoSlugErrors.organization_slug)}
                helperText={ssoSlugErrors.organization_slug?.message}
                {...registerSsoSlug('organization_slug')}
              />
              <Button type="submit" variant="outlined">
                Continue
              </Button>
            </Stack>
          </Box>
        </Collapse>
      </Paper>
    </Box>
  );
}
