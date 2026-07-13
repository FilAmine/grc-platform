import {
  AccountTree as AccountTreeIcon,
  AltRoute as AltRouteIcon,
  Assessment as AssessmentIcon,
  Balance as BalanceIcon,
  BugReport as BugReportIcon,
  Dashboard as DashboardIcon,
  Description as DescriptionIcon,
  FactCheck as FactCheckIcon,
  Gavel as GavelIcon,
  GppMaybe as GppMaybeIcon,
  GpsFixed as GpsFixedIcon,
  Hub as HubIcon,
  Logout as LogoutIcon,
  Notifications as NotificationsIcon,
  People as PeopleIcon,
  PersonSearch as PersonSearchIcon,
  ReportProblem as ReportProblemIcon,
  Rule as RuleIcon,
  Security as SecurityIcon,
  Shield as ShieldIcon,
  SmartToy as SmartToyIcon,
  Storage as StorageIcon,
  TaskAlt as TaskAltIcon,
  Terminal as TerminalIcon,
  VpnKey as VpnKeyIcon,
  WarningAmber as WarningAmberIcon,
} from '@mui/icons-material';
import {
  AppBar,
  Avatar,
  Box,
  Drawer,
  IconButton,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Menu,
  MenuItem,
  Toolbar,
  Typography,
} from '@mui/material';
import { useState } from 'react';
import { Link as RouterLink, Outlet, useLocation, useNavigate } from 'react-router-dom';
import { useAuth } from '../auth/AuthContext';

const DRAWER_WIDTH = 240;

const NAV_ITEMS = [
  { to: '/', label: 'Dashboard', icon: <DashboardIcon /> },
  { to: '/risks', label: 'Risk register', icon: <AssessmentIcon /> },
  { to: '/controls', label: 'Controls', icon: <FactCheckIcon /> },
  { to: '/audits', label: 'Audits', icon: <GavelIcon /> },
  { to: '/documents', label: 'Documents', icon: <DescriptionIcon /> },
  { to: '/incidents', label: 'Incidents', icon: <ReportProblemIcon /> },
  { to: '/assets', label: 'Assets', icon: <StorageIcon /> },
  { to: '/departments', label: 'Departments', icon: <AccountTreeIcon /> },
  { to: '/threats', label: 'Threats', icon: <WarningAmberIcon /> },
  { to: '/vulnerabilities', label: 'Vulnerabilities', icon: <BugReportIcon /> },
  { to: '/feared-events', label: 'Feared Events', icon: <GppMaybeIcon /> },
  { to: '/risk-sources', label: 'Risk Sources', icon: <PersonSearchIcon /> },
  { to: '/risk-origins', label: 'Risk Origins', icon: <GpsFixedIcon /> },
  { to: '/ecosystem-parties', label: 'Ecosystem Parties', icon: <HubIcon /> },
  { to: '/strategic-scenarios', label: 'Strategic Scenarios', icon: <AltRouteIcon /> },
  { to: '/operational-scenarios', label: 'Operational Scenarios', icon: <TerminalIcon /> },
  { to: '/risk-treatments', label: 'Risk Treatments', icon: <BalanceIcon /> },
  { to: '/tasks', label: 'Tasks', icon: <TaskAltIcon /> },
  { to: '/assessments', label: 'Assessments', icon: <RuleIcon /> },
  { to: '/users', label: 'Users', icon: <PeopleIcon /> },
  { to: '/roles', label: 'Roles', icon: <SecurityIcon /> },
  { to: '/ai', label: 'AI Assistant', icon: <SmartToyIcon /> },
  { to: '/notifications', label: 'Notifications', icon: <NotificationsIcon /> },
  { to: '/settings/sso', label: 'SSO', icon: <VpnKeyIcon /> },
];

export function AppShell() {
  const { user, logout } = useAuth();
  const location = useLocation();
  const navigate = useNavigate();
  const [menuAnchor, setMenuAnchor] = useState<HTMLElement | null>(null);

  const handleLogout = async () => {
    setMenuAnchor(null);
    await logout();
    navigate('/login', { replace: true });
  };

  return (
    <Box display="flex" minHeight="100vh">
      <Drawer
        variant="permanent"
        sx={{
          width: DRAWER_WIDTH,
          flexShrink: 0,
          [`& .MuiDrawer-paper`]: { width: DRAWER_WIDTH, boxSizing: 'border-box', borderRight: '1px solid', borderColor: 'divider' },
        }}
      >
        <Toolbar>
          <ShieldIcon color="primary" sx={{ mr: 1.5 }} />
          <Typography variant="h6" fontWeight={800}>
            GRC Platform
          </Typography>
        </Toolbar>
        <List>
          {NAV_ITEMS.map((item) => (
            <ListItemButton
              key={item.to}
              component={RouterLink}
              to={item.to}
              selected={
                item.to === '/' ? location.pathname === '/' : location.pathname.startsWith(item.to)
              }
            >
              <ListItemIcon>{item.icon}</ListItemIcon>
              <ListItemText primary={item.label} />
            </ListItemButton>
          ))}
        </List>
      </Drawer>

      <Box flexGrow={1}>
        <AppBar
          position="static"
          color="inherit"
          elevation={0}
          sx={{ borderBottom: '1px solid', borderColor: 'divider' }}
        >
          <Toolbar sx={{ justifyContent: 'flex-end' }}>
            <IconButton onClick={(event) => setMenuAnchor(event.currentTarget)} size="small">
              <Avatar sx={{ width: 32, height: 32, bgcolor: 'primary.main', fontSize: 14 }}>
                {user?.full_name?.slice(0, 1).toUpperCase() ?? '?'}
              </Avatar>
            </IconButton>
            <Menu anchorEl={menuAnchor} open={Boolean(menuAnchor)} onClose={() => setMenuAnchor(null)}>
              <MenuItem disabled>{user?.email}</MenuItem>
              <MenuItem onClick={handleLogout}>
                <ListItemIcon>
                  <LogoutIcon fontSize="small" />
                </ListItemIcon>
                Log out
              </MenuItem>
            </Menu>
          </Toolbar>
        </AppBar>
        <Outlet />
      </Box>
    </Box>
  );
}
