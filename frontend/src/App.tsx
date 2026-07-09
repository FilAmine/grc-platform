import { Navigate, Route, Routes } from 'react-router-dom';
import { RedirectIfAuthenticated } from './auth/RedirectIfAuthenticated';
import { RequireAuth } from './auth/RequireAuth';
import { AppShell } from './layout/AppShell';
import { AssetsPage } from './pages/AssetsPage';
import { AuditDetailPage } from './pages/AuditDetailPage';
import { AuditsPage } from './pages/AuditsPage';
import { ControlsPage } from './pages/ControlsPage';
import { DashboardPage } from './pages/DashboardPage';
import { DocumentDetailPage } from './pages/DocumentDetailPage';
import { DocumentsPage } from './pages/DocumentsPage';
import { LoginPage } from './pages/LoginPage';
import { NotFoundPage } from './pages/NotFoundPage';
import { RegisterOrganizationPage } from './pages/RegisterOrganizationPage';
import { RisksPage } from './pages/RisksPage';

export function App() {
  return (
    <Routes>
      <Route element={<RedirectIfAuthenticated />}>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterOrganizationPage />} />
      </Route>

      <Route element={<RequireAuth />}>
        <Route element={<AppShell />}>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/risks" element={<RisksPage />} />
          <Route path="/controls" element={<ControlsPage />} />
          <Route path="/audits" element={<AuditsPage />} />
          <Route path="/audits/:auditId" element={<AuditDetailPage />} />
          <Route path="/documents" element={<DocumentsPage />} />
          <Route path="/documents/:documentId" element={<DocumentDetailPage />} />
          <Route path="/assets" element={<AssetsPage />} />
        </Route>
      </Route>

      <Route path="/404" element={<NotFoundPage />} />
      <Route path="*" element={<Navigate to="/404" replace />} />
    </Routes>
  );
}
