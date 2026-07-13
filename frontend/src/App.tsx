import { Navigate, Route, Routes } from 'react-router-dom';
import { RedirectIfAuthenticated } from './auth/RedirectIfAuthenticated';
import { RequireAuth } from './auth/RequireAuth';
import { AppShell } from './layout/AppShell';
import { AiChatPage } from './pages/AiChatPage';
import { AssessmentDetailPage } from './pages/AssessmentDetailPage';
import { AssessmentsPage } from './pages/AssessmentsPage';
import { AssetsPage } from './pages/AssetsPage';
import { AuditDetailPage } from './pages/AuditDetailPage';
import { AuditsPage } from './pages/AuditsPage';
import { ControlsPage } from './pages/ControlsPage';
import { DashboardPage } from './pages/DashboardPage';
import { DepartmentsPage } from './pages/DepartmentsPage';
import { DocumentDetailPage } from './pages/DocumentDetailPage';
import { DocumentsPage } from './pages/DocumentsPage';
import { EcosystemPartiesPage } from './pages/EcosystemPartiesPage';
import { FearedEventsPage } from './pages/FearedEventsPage';
import { IncidentsPage } from './pages/IncidentsPage';
import { LoginPage } from './pages/LoginPage';
import { NotFoundPage } from './pages/NotFoundPage';
import { NotificationsPage } from './pages/NotificationsPage';
import { OperationalScenariosPage } from './pages/OperationalScenariosPage';
import { RegisterOrganizationPage } from './pages/RegisterOrganizationPage';
import { RiskOriginsPage } from './pages/RiskOriginsPage';
import { RiskSourcesPage } from './pages/RiskSourcesPage';
import { RisksPage } from './pages/RisksPage';
import { RolesPage } from './pages/RolesPage';
import { SsoCallbackPage } from './pages/SsoCallbackPage';
import { SsoSettingsPage } from './pages/SsoSettingsPage';
import { StrategicScenariosPage } from './pages/StrategicScenariosPage';
import { TasksPage } from './pages/TasksPage';
import { ThreatsPage } from './pages/ThreatsPage';
import { UsersPage } from './pages/UsersPage';
import { VulnerabilitiesPage } from './pages/VulnerabilitiesPage';

export function App() {
  return (
    <Routes>
      <Route element={<RedirectIfAuthenticated />}>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterOrganizationPage />} />
      </Route>

      {/* Not wrapped in RedirectIfAuthenticated/RequireAuth: this must work
          regardless of whether the SPA currently thinks it's authenticated --
          it's what makes that determination, by applying the tokens the
          backend's OIDC callback redirect just handed it. */}
      <Route path="/sso/callback" element={<SsoCallbackPage />} />

      <Route element={<RequireAuth />}>
        <Route element={<AppShell />}>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/risks" element={<RisksPage />} />
          <Route path="/controls" element={<ControlsPage />} />
          <Route path="/audits" element={<AuditsPage />} />
          <Route path="/audits/:auditId" element={<AuditDetailPage />} />
          <Route path="/documents" element={<DocumentsPage />} />
          <Route path="/documents/:documentId" element={<DocumentDetailPage />} />
          <Route path="/incidents" element={<IncidentsPage />} />
          <Route path="/assets" element={<AssetsPage />} />
          <Route path="/departments" element={<DepartmentsPage />} />
          <Route path="/threats" element={<ThreatsPage />} />
          <Route path="/vulnerabilities" element={<VulnerabilitiesPage />} />
          <Route path="/feared-events" element={<FearedEventsPage />} />
          <Route path="/risk-sources" element={<RiskSourcesPage />} />
          <Route path="/risk-origins" element={<RiskOriginsPage />} />
          <Route path="/ecosystem-parties" element={<EcosystemPartiesPage />} />
          <Route path="/strategic-scenarios" element={<StrategicScenariosPage />} />
          <Route path="/operational-scenarios" element={<OperationalScenariosPage />} />
          <Route path="/tasks" element={<TasksPage />} />
          <Route path="/assessments" element={<AssessmentsPage />} />
          <Route path="/assessments/:assessmentId" element={<AssessmentDetailPage />} />
          <Route path="/users" element={<UsersPage />} />
          <Route path="/roles" element={<RolesPage />} />
          <Route path="/ai" element={<AiChatPage />} />
          <Route path="/notifications" element={<NotificationsPage />} />
          <Route path="/settings/sso" element={<SsoSettingsPage />} />
        </Route>
      </Route>

      <Route path="/404" element={<NotFoundPage />} />
      <Route path="*" element={<Navigate to="/404" replace />} />
    </Routes>
  );
}
