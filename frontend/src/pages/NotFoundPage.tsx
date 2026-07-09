import { Box, Button, Typography } from '@mui/material';
import { Link as RouterLink } from 'react-router-dom';

export function NotFoundPage() {
  return (
    <Box minHeight="100vh" display="grid" sx={{ placeItems: 'center' }}>
      <Box textAlign="center">
        <Typography variant="h2" fontWeight={800}>
          404
        </Typography>
        <Typography color="text.secondary" sx={{ mb: 3 }}>
          This page does not exist.
        </Typography>
        <Button component={RouterLink} to="/" variant="contained">
          Back to dashboard
        </Button>
      </Box>
    </Box>
  );
}
