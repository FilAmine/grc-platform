import { Link, Outlet } from 'react-router-dom'
import { AppBar, Box, Toolbar, Typography } from '@mui/material'
import ShieldOutlinedIcon from '@mui/icons-material/ShieldOutlined'

export default function Layout() {
  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', height: '100vh' }}>
      <AppBar position="static" color="primary" enableColorOnDark>
        <Toolbar>
          <ShieldOutlinedIcon sx={{ mr: 1.5 }} />
          <Typography
            variant="h6"
            component={Link}
            to="/"
            sx={{ color: 'inherit', textDecoration: 'none', fontWeight: 700 }}
          >
            GRC Academy
          </Typography>
          <Typography variant="body2" sx={{ ml: 2, opacity: 0.85 }}>
            Formation GRC & Security by Design
          </Typography>
        </Toolbar>
      </AppBar>
      <Box sx={{ flex: 1, overflow: 'hidden' }}>
        <Outlet />
      </Box>
    </Box>
  )
}
