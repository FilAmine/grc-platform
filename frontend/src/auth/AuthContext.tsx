import { useQuery, useQueryClient } from '@tanstack/react-query';
import { createContext, useCallback, useContext, useMemo, useState, type ReactNode } from 'react';
import { getMe, login as apiLogin, logout as apiLogout, registerOrganization as apiRegisterOrganization } from '../api/auth';
import type { RegisterOrganizationRequest, User } from '../api/types';
import { clearTokens, getAccessToken, getRefreshToken, setTokens } from './tokenStorage';

type AuthContextValue = {
  user: User | undefined;
  isLoading: boolean;
  isAuthenticated: boolean;
  login: (email: string, password: string) => Promise<void>;
  registerOrganization: (payload: RegisterOrganizationRequest) => Promise<void>;
  logout: () => Promise<void>;
};

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const queryClient = useQueryClient();
  // Reactive presence flag: a plain `getAccessToken()` read at render time does
  // not cause a re-render when it changes, so login/register/logout would set
  // localStorage but the component would keep rendering as if nothing happened
  // until something unrelated forced a re-render. Track it as state instead.
  const [hasToken, setHasToken] = useState(() => Boolean(getAccessToken()));

  const meQuery = useQuery({
    queryKey: ['auth', 'me'],
    queryFn: getMe,
    enabled: hasToken,
    retry: false,
  });

  const login = useCallback(
    async (email: string, password: string) => {
      const tokens = await apiLogin(email, password);
      setTokens({ accessToken: tokens.access_token, refreshToken: tokens.refresh_token });
      setHasToken(true);
      await queryClient.invalidateQueries({ queryKey: ['auth', 'me'] });
    },
    [queryClient],
  );

  const registerOrganization = useCallback(
    async (payload: RegisterOrganizationRequest) => {
      const tokens = await apiRegisterOrganization(payload);
      setTokens({ accessToken: tokens.access_token, refreshToken: tokens.refresh_token });
      setHasToken(true);
      await queryClient.invalidateQueries({ queryKey: ['auth', 'me'] });
    },
    [queryClient],
  );

  const logout = useCallback(async () => {
    const refreshToken = getRefreshToken();
    clearTokens();
    setHasToken(false);
    queryClient.setQueryData(['auth', 'me'], undefined);
    queryClient.clear();
    if (refreshToken) {
      await apiLogout(refreshToken).catch(() => undefined);
    }
  }, [queryClient]);

  const value = useMemo<AuthContextValue>(
    () => ({
      user: meQuery.data,
      isLoading: hasToken && meQuery.isLoading,
      isAuthenticated: hasToken && Boolean(meQuery.data),
      login,
      registerOrganization,
      logout,
    }),
    [meQuery.data, meQuery.isLoading, hasToken, login, registerOrganization, logout],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth(): AuthContextValue {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}
