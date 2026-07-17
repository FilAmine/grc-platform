import type { Course } from './types'
import { grcSecurityByDesign } from './courses/grcSecurityByDesign'
import { nistCsf } from './courses/nistCsf'
import { iso27001 } from './courses/iso27001'

export const courses: Course[] = [grcSecurityByDesign, nistCsf, iso27001]

export function findCourse(courseSlug: string): Course | undefined {
  return courses.find((c) => c.slug === courseSlug)
}

export * from './types'
