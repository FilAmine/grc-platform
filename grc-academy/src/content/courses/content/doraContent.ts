import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/dora/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/dora/m1-l1-cadre-gestion-risques.md?raw'
import m1l2 from '../../lessons/dora/m1-l2-exigences-specifiques.md?raw'
import m2l1 from '../../lessons/dora/m2-l1-classification-incidents.md?raw'
import m2l2 from '../../lessons/dora/m2-l2-notification-incidents.md?raw'
import m3l1 from '../../lessons/dora/m3-l1-tests-base.md?raw'
import m3l2 from '../../lessons/dora/m3-l2-tlpt.md?raw'
import m4l1 from '../../lessons/dora/m4-l1-prestataires-tiers.md?raw'
import m4l2 from '../../lessons/dora/m4-l2-supervision-prestataires-critiques.md?raw'
import m5l1 from '../../lessons/dora/m5-l1-partage-supervision-sanctions.md?raw'
import m6l1 from '../../lessons/dora/m6-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: {
    introduction: m0l1,
  },
  'cadre-gestion-risques': {
    'cadre-gestion-risques': m1l1,
    'exigences-specifiques': m1l2,
  },
  incidents: {
    'classification-incidents': m2l1,
    'notification-incidents': m2l2,
  },
  'tests-resilience': {
    'tests-base': m3l1,
    tlpt: m3l2,
  },
  'prestataires-tiers': {
    'prestataires-tiers': m4l1,
    'supervision-prestataires-critiques': m4l2,
  },
  'partage-sanctions': {
    'partage-supervision-sanctions': m5l1,
  },
  'mapping-feuille-de-route': {
    'mapping-feuille-de-route': m6l1,
  },
}

export default content
