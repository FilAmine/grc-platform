import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/nist-rmf/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/nist-rmf/m1-l1-prepare-categorize.md?raw'
import m1l2 from '../../lessons/nist-rmf/m1-l2-select-implement.md?raw'
import m1l3 from '../../lessons/nist-rmf/m1-l3-assess-authorize.md?raw'
import m1l4 from '../../lessons/nist-rmf/m1-l4-monitor.md?raw'
import m2l1 from '../../lessons/nist-rmf/m2-l1-sp80053-structure.md?raw'
import m2l2 from '../../lessons/nist-rmf/m2-l2-familles-cles.md?raw'
import m3l1 from '../../lessons/nist-rmf/m3-l1-roles.md?raw'
import m4l1 from '../../lessons/nist-rmf/m4-l1-fedramp-mapping.md?raw'
import m5l1 from '../../lessons/nist-rmf/m5-l1-vie-privee.md?raw'
import m5l2 from '../../lessons/nist-rmf/m5-l2-supply-chain.md?raw'
import m6l1 from '../../lessons/nist-rmf/m6-l1-feuille-de-route.md?raw'

const content: CourseContent = {
  'introduction': {
    'introduction': m0l1,
  },
  'sept-etapes': {
    'prepare-categorize': m1l1,
    'select-implement': m1l2,
    'assess-authorize': m1l3,
    'monitor': m1l4,
  },
  'sp-800-53': {
    'sp80053-structure': m2l1,
    'familles-cles': m2l2,
  },
  'roles': {
    'roles': m3l1,
  },
  'fedramp-mapping': {
    'fedramp-mapping': m4l1,
  },
  'privacy-supply-chain': {
    'vie-privee': m5l1,
    'supply-chain': m5l2,
  },
  'feuille-de-route': {
    'feuille-de-route': m6l1,
  },
}

export default content
