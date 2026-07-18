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
import { ebiosRm } from './courses/ebiosRm'
import { itil } from './courses/itil'
import { sox } from './courses/sox'
import { fedramp } from './courses/fedramp'
import { tisax } from './courses/tisax'
import { iso22301 } from './courses/iso22301'

export const courses: Course[] = [grcSecurityByDesign, nistCsf, iso27001, soc2, rgpd, nistRmf, cisControls, nis2, dora, pciDss, cobit, hipaa, ebiosRm, itil, sox, fedramp, tisax, iso22301]

export function findCourse(courseSlug: string): Course | undefined {
  return courses.find((c) => c.slug === courseSlug)
}

export * from './types'
