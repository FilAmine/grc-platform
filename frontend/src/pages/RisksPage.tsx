import { zodResolver } from '@hookform/resolvers/zod';
import AddIcon from '@mui/icons-material/Add';
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
import { getAssets } from '../api/assets';
import { getFearedEvents } from '../api/feared-events';
import { createRisk, getRisks } from '../api/grc';
import { getThreats } from '../api/threats';
import type { Risk, RiskSeverity } from '../api/types';
import { getVulnerabilities } from '../api/vulnerabilities';

const SEVERITIES: RiskSeverity[] = ['low', 'medium', 'high', 'critical'];

const schema = z.object({
  title: z.string().min(3, 'At least 3 characters'),
  description: z.string().min(1, 'Description is required'),
  severity: z.enum(['low', 'medium', 'high', 'critical']),
  owner: z.string().min(2, 'At least 2 characters'),
  asset_id: z.string(),
  threat_id: z.string(),
  vulnerability_id: z.string(),
  feared_event_id: z.string(),
});

type FormValues = z.infer<typeof schema>;

const severityColor: Record<RiskSeverity, 'default' | 'warning' | 'error'> = {
  low: 'default',
  medium: 'default',
  high: 'warning',
  critical: 'error',
};

export function RisksPage() {
  const queryClient = useQueryClient();
  const [dialogOpen, setDialogOpen] = useState(false);
  const risks = useQuery({ queryKey: ['risks'], queryFn: getRisks });
  const assets = useQuery({ queryKey: ['assets'], queryFn: getAssets });
  const threats = useQuery({ queryKey: ['threats'], queryFn: getThreats });
  const vulnerabilities = useQuery({ queryKey: ['vulnerabilities'], queryFn: getVulnerabilities });
  const fearedEvents = useQuery({ queryKey: ['feared-events'], queryFn: getFearedEvents });

  const assetNameById = new Map((assets.data ?? []).map((a) => [a.id, a.name]));
  const threatNameById = new Map((threats.data ?? []).map((t) => [t.id, t.name]));
  const vulnerabilityNameById = new Map((vulnerabilities.data ?? []).map((v) => [v.id, v.name]));
  const fearedEventTitleById = new Map((fearedEvents.data ?? []).map((fe) => [fe.id, fe.title]));

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: {
      severity: 'medium',
      asset_id: '',
      threat_id: '',
      vulnerability_id: '',
      feared_event_id: '',
    },
  });

  const createMutation = useMutation({
    mutationFn: createRisk,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['risks'] });
      await queryClient.invalidateQueries({ queryKey: ['summary'] });
      setDialogOpen(false);
      reset();
    },
  });

  const onSubmit = handleSubmit((values) =>
    createMutation.mutate({
      ...values,
      asset_id: values.asset_id || null,
      threat_id: values.threat_id || null,
      vulnerability_id: values.vulnerability_id || null,
      feared_event_id: values.feared_event_id || null,
    }),
  );

  function linkChips(risk: Risk) {
    const chips: { label: string }[] = [];
    if (risk.asset_id) chips.push({ label: `Asset: ${assetNameById.get(risk.asset_id) ?? risk.asset_id}` });
    if (risk.threat_id) chips.push({ label: `Threat: ${threatNameById.get(risk.threat_id) ?? risk.threat_id}` });
    if (risk.vulnerability_id) {
      chips.push({
        label: `Vulnerability: ${vulnerabilityNameById.get(risk.vulnerability_id) ?? risk.vulnerability_id}`,
      });
    }
    if (risk.feared_event_id) {
      chips.push({
        label: `Feared event: ${fearedEventTitleById.get(risk.feared_event_id) ?? risk.feared_event_id}`,
      });
    }
    return chips;
  }

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Risk register</Typography>
          <Typography color="text.secondary">Track and triage organizational risks.</Typography>
        </Box>
        <Button variant="contained" startIcon={<AddIcon />} onClick={() => setDialogOpen(true)}>
          New risk
        </Button>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Title</TableCell>
              <TableCell>Owner</TableCell>
              <TableCell>Severity</TableCell>
              <TableCell>Status</TableCell>
              <TableCell>Links</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(risks.data ?? []).map((risk) => (
              <TableRow key={risk.id} hover>
                <TableCell>
                  <Typography fontWeight={600}>{risk.title}</Typography>
                  <Typography variant="body2" color="text.secondary">
                    {risk.description}
                  </Typography>
                </TableCell>
                <TableCell>{risk.owner}</TableCell>
                <TableCell>
                  <Chip size="small" label={risk.severity} color={severityColor[risk.severity]} />
                </TableCell>
                <TableCell>{risk.status}</TableCell>
                <TableCell>
                  <Stack direction="row" spacing={0.5} flexWrap="wrap" useFlexGap>
                    {linkChips(risk).map((chip) => (
                      <Chip key={chip.label} size="small" variant="outlined" label={chip.label} />
                    ))}
                  </Stack>
                </TableCell>
              </TableRow>
            ))}
            {!risks.data?.length && (
              <TableRow>
                <TableCell colSpan={5}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No risks recorded yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={onSubmit} noValidate>
          <DialogTitle>New risk</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Title"
                error={Boolean(errors.title)}
                helperText={errors.title?.message}
                {...register('title')}
              />
              <TextField
                label="Description"
                multiline
                minRows={2}
                error={Boolean(errors.description)}
                helperText={errors.description?.message}
                {...register('description')}
              />
              <TextField
                label="Owner"
                error={Boolean(errors.owner)}
                helperText={errors.owner?.message}
                {...register('owner')}
              />
              <TextField label="Severity" select defaultValue="medium" {...register('severity')}>
                {SEVERITIES.map((severity) => (
                  <MenuItem key={severity} value={severity}>
                    {severity}
                  </MenuItem>
                ))}
              </TextField>

              <Typography variant="subtitle2" color="text.secondary" sx={{ pt: 1 }}>
                EBIOS-RM-flavored links (optional)
              </Typography>
              <TextField label="Asset" select defaultValue="" {...register('asset_id')}>
                <MenuItem value="">None</MenuItem>
                {(assets.data ?? []).map((asset) => (
                  <MenuItem key={asset.id} value={asset.id}>
                    {asset.name}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Threat" select defaultValue="" {...register('threat_id')}>
                <MenuItem value="">None</MenuItem>
                {(threats.data ?? []).map((threat) => (
                  <MenuItem key={threat.id} value={threat.id}>
                    {threat.name}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Vulnerability" select defaultValue="" {...register('vulnerability_id')}>
                <MenuItem value="">None</MenuItem>
                {(vulnerabilities.data ?? []).map((vulnerability) => (
                  <MenuItem key={vulnerability.id} value={vulnerability.id}>
                    {vulnerability.name}
                  </MenuItem>
                ))}
              </TextField>
              <TextField label="Feared event" select defaultValue="" {...register('feared_event_id')}>
                <MenuItem value="">None</MenuItem>
                {(fearedEvents.data ?? []).map((fearedEvent) => (
                  <MenuItem key={fearedEvent.id} value={fearedEvent.id}>
                    {fearedEvent.title}
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
