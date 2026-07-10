import {
  Box,
  Button,
  Chip,
  Container,
  Paper,
  Stack,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  Typography,
} from '@mui/material';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { getNotifications, markNotificationRead } from '../api/notifications';

export function NotificationsPage() {
  const queryClient = useQueryClient();
  const notifications = useQuery({ queryKey: ['notifications'], queryFn: getNotifications });

  const markReadMutation = useMutation({
    mutationFn: markNotificationRead,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['notifications'] });
    },
  });

  const unreadCount = (notifications.data ?? []).filter((n) => !n.read_at).length;

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">Notifications</Typography>
          <Typography color="text.secondary">
            {unreadCount ? `${unreadCount} unread` : 'You are all caught up.'}
          </Typography>
        </Box>
      </Stack>

      <Paper elevation={0} sx={{ border: '1px solid', borderColor: 'divider' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Subject</TableCell>
              <TableCell>Message</TableCell>
              <TableCell>Received</TableCell>
              <TableCell>Status</TableCell>
              <TableCell />
            </TableRow>
          </TableHead>
          <TableBody>
            {(notifications.data ?? []).map((notification) => (
              <TableRow key={notification.id} hover sx={{ bgcolor: notification.read_at ? 'transparent' : 'action.hover' }}>
                <TableCell>
                  <Typography fontWeight={notification.read_at ? 400 : 700}>{notification.subject}</Typography>
                </TableCell>
                <TableCell>
                  <Typography variant="body2" color="text.secondary">
                    {notification.body}
                  </Typography>
                </TableCell>
                <TableCell>{new Date(notification.created_at).toLocaleString()}</TableCell>
                <TableCell>
                  <Chip
                    size="small"
                    label={notification.read_at ? 'read' : 'unread'}
                    color={notification.read_at ? 'default' : 'info'}
                  />
                </TableCell>
                <TableCell align="right">
                  {!notification.read_at && (
                    <Button
                      size="small"
                      disabled={markReadMutation.isPending}
                      onClick={() => markReadMutation.mutate(notification.id)}
                    >
                      Mark read
                    </Button>
                  )}
                </TableCell>
              </TableRow>
            ))}
            {!notifications.data?.length && (
              <TableRow>
                <TableCell colSpan={5}>
                  <Typography color="text.secondary" sx={{ py: 2 }}>
                    No notifications yet.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>
    </Container>
  );
}
