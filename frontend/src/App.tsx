import AssessmentIcon from '@mui/icons-material/Assessment';
import BusinessIcon from '@mui/icons-material/Business';
import FactCheckIcon from '@mui/icons-material/FactCheck';
import ShieldIcon from '@mui/icons-material/Shield';
import {
  AppBar,
  Box,
  Chip,
  Container,
  Grid,
  LinearProgress,
  Paper,
  Stack,
  Toolbar,
  Typography,
} from '@mui/material';
import { useQuery } from '@tanstack/react-query';
import type { ReactNode } from 'react';
import { getControls, getOrganizations, getRisks, getSummary } from './api/grc';

function MetricCard({
  icon,
  label,
  value,
  accent,
}: {
  icon: ReactNode;
  label: string;
  value: string | number;
  accent: string;
}) {
  return (
    <Paper elevation={0} sx={{ p: 3, border: '1px solid', borderColor: 'divider' }}>
      <Stack direction="row" alignItems="center" spacing={2}>
        <Box
          sx={{
            width: 44,
            height: 44,
            borderRadius: 2,
            display: 'grid',
            placeItems: 'center',
            color: 'white',
            bgcolor: accent,
          }}
        >
          {icon}
        </Box>
        <Box>
          <Typography variant="body2" color="text.secondary">
            {label}
          </Typography>
          <Typography variant="h5" fontWeight={800}>
            {value}
          </Typography>
        </Box>
      </Stack>
    </Paper>
  );
}

export function App() {
  const summary = useQuery({ queryKey: ['summary'], queryFn: getSummary });
  const organizations = useQuery({ queryKey: ['organizations'], queryFn: getOrganizations });
  const risks = useQuery({ queryKey: ['risks'], queryFn: getRisks });
  const controls = useQuery({ queryKey: ['controls'], queryFn: getControls });
  const loading = summary.isLoading || organizations.isLoading || risks.isLoading || controls.isLoading;

  return (
    <Box minHeight="100vh">
      <AppBar position="static" color="inherit" elevation={0} sx={{ borderBottom: '1px solid', borderColor: 'divider' }}>
        <Toolbar>
          <ShieldIcon color="primary" sx={{ mr: 1.5 }} />
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            GRC Platform
          </Typography>
          <Chip
            size="small"
            color={summary.data?.posture === 'healthy' ? 'success' : 'warning'}
            label={summary.data?.posture === 'healthy' ? 'Healthy' : 'Attention required'}
          />
        </Toolbar>
        {loading && <LinearProgress />}
      </AppBar>

      <Container maxWidth="xl" sx={{ py: 4 }}>
        <Stack spacing={4}>
          <Box>
            <Typography variant="h4">Governance cockpit</Typography>
            <Typography color="text.secondary" sx={{ mt: 1 }}>
              Operational view of organizational risk, controls, and compliance posture.
            </Typography>
          </Box>

          <Grid container spacing={2}>
            <Grid item xs={12} md={4}>
              <MetricCard
                icon={<BusinessIcon />}
                label="Organizations"
                value={summary.data?.organizations ?? 0}
                accent="#155e75"
              />
            </Grid>
            <Grid item xs={12} md={4}>
              <MetricCard
                icon={<AssessmentIcon />}
                label="Open risks"
                value={summary.data?.risks_open ?? 0}
                accent="#b45309"
              />
            </Grid>
            <Grid item xs={12} md={4}>
              <MetricCard
                icon={<FactCheckIcon />}
                label="Active controls"
                value={summary.data?.controls_active ?? 0}
                accent="#15803d"
              />
            </Grid>
          </Grid>

          <Grid container spacing={2}>
            <Grid item xs={12} lg={4}>
              <Paper elevation={0} sx={{ p: 3, border: '1px solid', borderColor: 'divider' }}>
                <Typography variant="h6" gutterBottom>
                  Organizations
                </Typography>
                <Stack spacing={1.5}>
                  {(organizations.data ?? []).map((organization) => (
                    <Box key={organization.id}>
                      <Typography fontWeight={700}>{organization.name}</Typography>
                      <Typography variant="body2" color="text.secondary">
                        {organization.slug}
                      </Typography>
                    </Box>
                  ))}
                  {!organizations.data?.length && <Typography color="text.secondary">No organizations yet.</Typography>}
                </Stack>
              </Paper>
            </Grid>
            <Grid item xs={12} lg={4}>
              <Paper elevation={0} sx={{ p: 3, border: '1px solid', borderColor: 'divider' }}>
                <Typography variant="h6" gutterBottom>
                  Risk register
                </Typography>
                <Stack spacing={1.5}>
                  {(risks.data ?? []).map((risk) => (
                    <Box key={risk.id}>
                      <Stack direction="row" alignItems="center" justifyContent="space-between" spacing={1}>
                        <Typography fontWeight={700}>{risk.title}</Typography>
                        <Chip size="small" label={risk.severity} />
                      </Stack>
                      <Typography variant="body2" color="text.secondary">
                        {risk.owner} · {risk.status}
                      </Typography>
                    </Box>
                  ))}
                  {!risks.data?.length && <Typography color="text.secondary">No risks recorded.</Typography>}
                </Stack>
              </Paper>
            </Grid>
            <Grid item xs={12} lg={4}>
              <Paper elevation={0} sx={{ p: 3, border: '1px solid', borderColor: 'divider' }}>
                <Typography variant="h6" gutterBottom>
                  Controls
                </Typography>
                <Stack spacing={1.5}>
                  {(controls.data ?? []).map((control) => (
                    <Box key={control.id}>
                      <Stack direction="row" alignItems="center" justifyContent="space-between" spacing={1}>
                        <Typography fontWeight={700}>{control.name}</Typography>
                        <Chip size="small" label={control.framework} />
                      </Stack>
                      <Typography variant="body2" color="text.secondary">
                        {control.status}
                      </Typography>
                    </Box>
                  ))}
                  {!controls.data?.length && <Typography color="text.secondary">No controls defined.</Typography>}
                </Stack>
              </Paper>
            </Grid>
          </Grid>
        </Stack>
      </Container>
    </Box>
  );
}
