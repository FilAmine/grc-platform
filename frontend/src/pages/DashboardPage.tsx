import AssessmentIcon from '@mui/icons-material/Assessment';
import BusinessIcon from '@mui/icons-material/Business';
import FactCheckIcon from '@mui/icons-material/FactCheck';
import { Box, Chip, Container, Grid, LinearProgress, Paper, Stack, Typography } from '@mui/material';
import { useQuery } from '@tanstack/react-query';
import type { ReactNode } from 'react';
import { useAuth } from '../auth/AuthContext';
import { getControls, getOrganizations, getRisks, getSummary } from '../api/grc';

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

export function DashboardPage() {
  const { user } = useAuth();
  const summary = useQuery({ queryKey: ['summary'], queryFn: getSummary });
  const organizations = useQuery({ queryKey: ['organizations'], queryFn: getOrganizations });
  const risks = useQuery({ queryKey: ['risks'], queryFn: getRisks });
  const controls = useQuery({ queryKey: ['controls'], queryFn: getControls });
  const loading = summary.isLoading || organizations.isLoading || risks.isLoading || controls.isLoading;

  const organization = organizations.data?.find((org) => org.id === user?.organization_id) ?? organizations.data?.[0];

  return (
    <Box>
      {loading && <LinearProgress />}
      <Container maxWidth="xl" sx={{ py: 4 }}>
        <Stack spacing={4}>
          <Stack direction="row" alignItems="center" justifyContent="space-between">
            <Box>
              <Typography variant="h4">Governance cockpit</Typography>
              <Typography color="text.secondary" sx={{ mt: 1 }}>
                {organization ? `${organization.name} — ` : ''}Operational view of risk, controls, and compliance
                posture.
              </Typography>
            </Box>
            <Chip
              size="small"
              color={summary.data?.posture === 'healthy' ? 'success' : 'warning'}
              label={summary.data?.posture === 'healthy' ? 'Healthy' : 'Attention required'}
            />
          </Stack>

          <Grid container spacing={2}>
            <Grid item xs={12} md={4}>
              <MetricCard icon={<BusinessIcon />} label="Organizations" value={summary.data?.organizations ?? 0} accent="#155e75" />
            </Grid>
            <Grid item xs={12} md={4}>
              <MetricCard icon={<AssessmentIcon />} label="Open risks" value={summary.data?.risks_open ?? 0} accent="#b45309" />
            </Grid>
            <Grid item xs={12} md={4}>
              <MetricCard icon={<FactCheckIcon />} label="Active controls" value={summary.data?.controls_active ?? 0} accent="#15803d" />
            </Grid>
          </Grid>

          <Grid container spacing={2}>
            <Grid item xs={12} lg={6}>
              <Paper elevation={0} sx={{ p: 3, border: '1px solid', borderColor: 'divider' }}>
                <Typography variant="h6" gutterBottom>
                  Recent risks
                </Typography>
                <Stack spacing={1.5}>
                  {(risks.data ?? []).slice(0, 5).map((risk) => (
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
            <Grid item xs={12} lg={6}>
              <Paper elevation={0} sx={{ p: 3, border: '1px solid', borderColor: 'divider' }}>
                <Typography variant="h6" gutterBottom>
                  Recent controls
                </Typography>
                <Stack spacing={1.5}>
                  {(controls.data ?? []).slice(0, 5).map((control) => (
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
