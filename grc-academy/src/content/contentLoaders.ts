import type { CourseContent } from './types'

// Each loader is a dynamic import() so Vite/Rollup splits every course's
// lesson text (the bulk of the app's weight) into its own chunk, fetched
// only when someone actually opens a lesson from that course.
export const contentLoaders: Record<string, () => Promise<{ default: CourseContent }>> = {
  'grc-security-by-design': () => import('./courses/content/grcSecurityByDesignContent'),
  'nist-csf': () => import('./courses/content/nistCsfContent'),
  'iso-27001': () => import('./courses/content/iso27001Content'),
  'soc-2': () => import('./courses/content/soc2Content'),
  rgpd: () => import('./courses/content/rgpdContent'),
  'nist-rmf': () => import('./courses/content/nistRmfContent'),
  'cis-controls': () => import('./courses/content/cisControlsContent'),
  nis2: () => import('./courses/content/nis2Content'),
  dora: () => import('./courses/content/doraContent'),
  'pci-dss': () => import('./courses/content/pciDssContent'),
}
