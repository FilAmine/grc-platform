import type { Course } from './types'
import { grcSecurityByDesign } from './courses/grcSecurityByDesign'
import { nistCsf } from './courses/nistCsf'
import { iso27001 } from './courses/iso27001'
import { soc2 } from './courses/soc2'
import { rgpd } from './courses/rgpd'

export const courses: Course[] = [grcSecurityByDesign, nistCsf, iso27001, soc2, rgpd]

export function findCourse(courseSlug: string): Course | undefined {
  return courses.find((c) => c.slug === courseSlug)
}

export * from './types'
