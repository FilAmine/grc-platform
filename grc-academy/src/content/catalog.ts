import type { Course } from './types'
import { grcSecurityByDesign } from './courses/grcSecurityByDesign'
import { nistCsf } from './courses/nistCsf'
import { iso27001 } from './courses/iso27001'
import { soc2 } from './courses/soc2'
import { rgpd } from './courses/rgpd'
import { nistRmf } from './courses/nistRmf'
import { cisControls } from './courses/cisControls'
import { nis2 } from './courses/nis2'
import { dora } from './courses/dora'
import { pciDss } from './courses/pciDss'
import { cobit } from './courses/cobit'
import { hipaa } from './courses/hipaa'

export const courses: Course[] = [grcSecurityByDesign, nistCsf, iso27001, soc2, rgpd, nistRmf, cisControls, nis2, dora, pciDss, cobit, hipaa]

export function findCourse(courseSlug: string): Course | undefined {
  return courses.find((c) => c.slug === courseSlug)
}

export * from './types'
