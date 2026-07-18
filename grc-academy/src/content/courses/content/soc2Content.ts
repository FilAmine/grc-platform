import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/soc-2/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/soc-2/m1-l1-common-criteria-gouvernance.md?raw'
import m1l2 from '../../lessons/soc-2/m1-l2-common-criteria-techniques.md?raw'
import m2l1 from '../../lessons/soc-2/m2-l1-disponibilite-integrite-confidentialite.md?raw'
import m2l2 from '../../lessons/soc-2/m2-l2-vie-privee.md?raw'
import m3l1 from '../../lessons/soc-2/m3-l1-audit-opinions.md?raw'
import m4l1 from '../../lessons/soc-2/m4-l1-anatomie-rapport.md?raw'
import m5l1 from '../../lessons/soc-2/m5-l1-cadrage-readiness.md?raw'
import m5l2 from '../../lessons/soc-2/m5-l2-preuves-pieges.md?raw'
import m6l1 from '../../lessons/soc-2/m6-l1-soc1-soc3-mapping.md?raw'
import m7l1 from '../../lessons/soc-2/m7-l1-feuille-de-route.md?raw'

const content: CourseContent = {
  'introduction': {
    'introduction': m0l1,
  },
  'common-criteria': {
    'gouvernance': m1l1,
    'techniques': m1l2,
  },
  'categories-confiance': {
    'disponibilite-integrite-confidentialite': m2l1,
    'vie-privee': m2l2,
  },
  'audit': {
    'audit-opinions': m3l1,
  },
  'anatomie-rapport': {
    'anatomie-rapport': m4l1,
  },
  'preparation': {
    'cadrage-readiness': m5l1,
    'preuves-pieges': m5l2,
  },
  'soc1-soc3-mapping': {
    'soc1-soc3-mapping': m6l1,
  },
  'feuille-de-route': {
    'feuille-de-route': m7l1,
  },
}

export default content
