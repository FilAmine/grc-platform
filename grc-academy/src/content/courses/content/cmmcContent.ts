import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/cmmc/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/cmmc/m1-l1-niveau-1-foundational.md?raw'
import m1l2 from '../../lessons/cmmc/m1-l2-niveaux-2-3-advanced-expert.md?raw'
import m2l1 from '../../lessons/cmmc/m2-l1-catalogue-sp800-171-structure.md?raw'
import m2l2 from '../../lessons/cmmc/m2-l2-exemple-concret-sp800-172.md?raw'
import m3l1 from '../../lessons/cmmc/m3-l1-auto-evaluation.md?raw'
import m3l2 from '../../lessons/cmmc/m3-l2-c3pao-dibcac.md?raw'
import m4l1 from '../../lessons/cmmc/m4-l1-poam-certification-conditionnelle.md?raw'
import m5l1 from '../../lessons/cmmc/m5-l1-flow-down-sprs.md?raw'
import m6l1 from '../../lessons/cmmc/m6-l1-dfars-notification-incidents.md?raw'
import m7l1 from '../../lessons/cmmc/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  niveaux: { 'niveau-1-foundational': m1l1, 'niveaux-2-3-advanced-expert': m1l2 },
  'catalogue-sp800-171': { 'catalogue-sp800-171-structure': m2l1, 'exemple-concret-sp800-172': m2l2 },
  'voies-evaluation': { 'auto-evaluation': m3l1, 'c3pao-dibcac': m3l2 },
  poam: { 'poam-certification-conditionnelle': m4l1 },
  'flow-down': { 'flow-down-sprs': m5l1 },
  dfars: { 'dfars-notification-incidents': m6l1 },
  'mapping-feuille-de-route': { 'mapping-feuille-de-route': m7l1 },
}

export default content
