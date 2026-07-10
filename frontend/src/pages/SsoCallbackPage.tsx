import { Alert, Box, Button, CircularProgress, Link as MuiLink, Paper, Stack, Typography } from '@mui/material';
import { useEffect, useRef, useState } from 'react';
import { Link as RouterLink, useNavigate } from 'react-router-dom';
import { useAuth } from '../auth/AuthContext';

export function SsoCallbackPage() {
  const { applyTokens } = useAuth();
  const navigate = useNavigate();
  const [error, setError] = useState<string | null>(null);
  const handled = useRef(false);

  useEffect(() => {
    if (handled.current) return;
    handled.current = true;

    const fragment = new URLSearchParams(window.location.hash.replace(/^#/, ''));
    const accessToken = fragment.get('access_token');
    const refreshToken = fragment.get('refresh_token');
    const oidcError = fragment.get('error');

    if (oidcError) {
      setError(oidcError);
      return;
    }
    if (!accessToken || !refreshToken) {
      setError('The identity provider did not return valid tokens.');
      return;
    }

    applyTokens({ access_token: accessToken, refresh_token: refreshToken, token_type: 'bearer' }).then(() => {
      navigate('/', { replace: true });
    });
  }, [applyTokens, navigate]);

  return (
    <Box minHeight="100vh" display="grid" sx={{ placeItems: 'center', bgcolor: 'background.default' }}>
      <Paper elevation={0} sx={{ p: 4, width: 420, border: '1px solid', borderColor: 'divider' }}>
        {error ? (
          <Stack spacing={2}>
            <Typography variant="h6" fontWeight={800}>
              Sign-in failed
            </Typography>
            <Alert severity="error">{error}</Alert>
            <Button component={RouterLink} to="/login" variant="contained">
              Back to sign in
            </Button>
            <Typography variant="body2" color="text.secondary">
              If this keeps happening, check the SSO connection settings with your organization's admin, or{' '}
              <MuiLink component={RouterLink} to="/login">
                sign in with a password
              </MuiLink>{' '}
              instead.
            </Typography>
          </Stack>
        ) : (
          <Stack spacing={2} alignItems="center">
            <CircularProgress size={28} />
            <Typography color="text.secondary">Completing sign-in...</Typography>
          </Stack>
        )}
      </Paper>
    </Box>
  );
}
