import { zodResolver } from '@hookform/resolvers/zod';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';
import {
  Alert,
  Box,
  Button,
  Container,
  IconButton,
  MenuItem,
  Paper,
  Stack,
  Switch,
  TextField,
  Tooltip,
  Typography,
} from '@mui/material';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { useEffect, useState } from 'react';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { getRoles } from '../api/rbac';
import { configureSso, deleteSso, getSsoConnection } from '../api/sso';

const schema = z.object({
  issuer: z.string().min(1, 'Required').url('Enter a full URL, e.g. https://idp.example.com'),
  client_id: z.string().min(1, 'Required'),
  client_secret: z.string().min(1, 'Required'),
  default_role_id: z.string(),
  is_enabled: z.boolean(),
});

type FormValues = z.infer<typeof schema>;

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000/api/v1';
const CALLBACK_URL = `${apiBaseUrl}/auth/sso/callback`;

export function SsoSettingsPage() {
  const queryClient = useQueryClient();
  const [copied, setCopied] = useState(false);
  const connection = useQuery({ queryKey: ['sso-connection'], queryFn: getSsoConnection });
  const roles = useQuery({ queryKey: ['roles'], queryFn: getRoles });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: { issuer: '', client_id: '', client_secret: '', default_role_id: '', is_enabled: true },
  });

  useEffect(() => {
    if (connection.data) {
      reset({
        issuer: connection.data.issuer,
        client_id: connection.data.client_id,
        client_secret: '',
        default_role_id: connection.data.default_role_id ?? '',
        is_enabled: connection.data.is_enabled,
      });
    }
  }, [connection.data, reset]);

  const saveMutation = useMutation({
    mutationFn: (values: FormValues) =>
      configureSso({ ...values, default_role_id: values.default_role_id || null }),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['sso-connection'] });
    },
  });

  const deleteMutation = useMutation({
    mutationFn: deleteSso,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['sso-connection'] });
      reset({ issuer: '', client_id: '', client_secret: '', default_role_id: '', is_enabled: true });
    },
  });

  const onSubmit = handleSubmit((values) => saveMutation.mutate(values));

  return (
    <Container maxWidth="sm" sx={{ py: 4 }}>
      <Box sx={{ mb: 3 }}>
        <Typography variant="h4">SSO</Typography>
        <Typography color="text.secondary">
          Connect your organization's identity provider (Okta, Azure AD, Google Workspace, or any standards-compliant
          OIDC provider) so members can sign in without a local password.
        </Typography>
      </Box>

      <Paper elevation={0} sx={{ p: 3, mb: 3, border: '1px solid', borderColor: 'divider' }}>
        <Typography variant="subtitle2" gutterBottom>
          Callback URL
        </Typography>
        <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
          Register this as the redirect/callback URI in your identity provider's app configuration.
        </Typography>
        <Stack direction="row" spacing={1} alignItems="center">
          <TextField value={CALLBACK_URL} size="small" fullWidth InputProps={{ readOnly: true }} />
          <Tooltip title={copied ? 'Copied' : 'Copy'}>
            <IconButton
              onClick={() => {
                navigator.clipboard.writeText(CALLBACK_URL);
                setCopied(true);
                setTimeout(() => setCopied(false), 1500);
              }}
            >
              <ContentCopyIcon fontSize="small" />
            </IconButton>
          </Tooltip>
        </Stack>
      </Paper>

      <Paper elevation={0} sx={{ p: 3, border: '1px solid', borderColor: 'divider' }}>
        <Box component="form" onSubmit={onSubmit} noValidate>
          <Stack spacing={2}>
            {connection.data && (
              <Alert severity="info">
                SSO is currently {connection.data.is_enabled ? 'enabled' : 'disabled'} for your organization.
                Re-enter the client secret below to save changes — it's never sent back for editing.
              </Alert>
            )}
            <TextField
              label="Issuer URL"
              placeholder="https://idp.example.com"
              error={Boolean(errors.issuer)}
              helperText={errors.issuer?.message}
              {...register('issuer')}
            />
            <TextField
              label="Client ID"
              error={Boolean(errors.client_id)}
              helperText={errors.client_id?.message}
              {...register('client_id')}
            />
            <TextField
              label="Client secret"
              type="password"
              placeholder={connection.data ? 'Re-enter to change' : ''}
              error={Boolean(errors.client_secret)}
              helperText={errors.client_secret?.message}
              {...register('client_secret')}
            />
            <TextField label="Default role for new SSO users" select defaultValue="" {...register('default_role_id')}>
              <MenuItem value="">
                <em>None — assign manually</em>
              </MenuItem>
              {(roles.data ?? []).map((role) => (
                <MenuItem key={role.id} value={role.id}>
                  {role.name}
                </MenuItem>
              ))}
            </TextField>
            <Stack direction="row" alignItems="center" justifyContent="space-between">
              <Typography>Enabled</Typography>
              <Switch {...register('is_enabled')} />
            </Stack>
            <Stack direction="row" spacing={1}>
              <Button type="submit" variant="contained" disabled={isSubmitting}>
                Save
              </Button>
              {connection.data && (
                <Button color="error" onClick={() => deleteMutation.mutate()} disabled={deleteMutation.isPending}>
                  Remove connection
                </Button>
              )}
            </Stack>
          </Stack>
        </Box>
      </Paper>
    </Container>
  );
}
