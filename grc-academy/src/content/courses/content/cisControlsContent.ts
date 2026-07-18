import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/cis-controls/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/cis-controls/m1-l1-structure.md?raw'
import m1l2 from '../../lessons/cis-controls/m1-l2-controles-1-6.md?raw'
import m1l3 from '../../lessons/cis-controls/m1-l3-controles-7-12.md?raw'
import m1l4 from '../../lessons/cis-controls/m1-l4-controles-13-18.md?raw'
import m2l1 from '../../lessons/cis-controls/m2-l1-implementation-groups.md?raw'
import m2l2 from '../../lessons/cis-controls/m2-l2-choisir-son-ig.md?raw'
import m3l1 from '../../lessons/cis-controls/m3-l1-benchmarks.md?raw'
import m3l2 from '../../lessons/cis-controls/m3-l2-cis-ram.md?raw'
import m4l1 from '../../lessons/cis-controls/m4-l1-mapping.md?raw'
import m5l1 from '../../lessons/cis-controls/m5-l1-feuille-de-route.md?raw'

const content: CourseContent = {
  'introduction': {
    'introduction': m0l1,
  },
  'les-18-controles': {
    'structure': m1l1,
    'controles-1-6': m1l2,
    'controles-7-12': m1l3,
    'controles-13-18': m1l4,
  },
  'implementation-groups': {
    'implementation-groups': m2l1,
    'choisir-son-ig': m2l2,
  },
  'ecosysteme-cis': {
    'benchmarks': m3l1,
    'cis-ram': m3l2,
  },
  'mapping': {
    'mapping': m4l1,
  },
  'feuille-de-route': {
    'feuille-de-route': m5l1,
  },
}

export default content
