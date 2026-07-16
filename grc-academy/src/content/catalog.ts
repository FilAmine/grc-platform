import type { Course } from './types'
import { grcSecurityByDesign } from './courses/grcSecurityByDesign'
import { nistCsf } from './courses/nistCsf'

export const courses: Course[] = [grcSecurityByDesign, nistCsf]

export function findCourse(courseSlug: string): Course | undefined {
  return courses.find((c) => c.slug === courseSlug)
}

export * from './types'
