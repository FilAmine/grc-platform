import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/cobit/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/cobit/m1-l1-gouvernance-management.md?raw'
import m1l2 from '../../lessons/cobit/m1-l2-cascade-objectifs.md?raw'
import m2l1 from '../../lessons/cobit/m2-l1-domaine-apo.md?raw'
import m2l2 from '../../lessons/cobit/m2-l2-domaine-bai.md?raw'
import m2l3 from '../../lessons/cobit/m2-l3-domaines-dss-mea.md?raw'
import m3l1 from '../../lessons/cobit/m3-l1-composants.md?raw'
import m4l1 from '../../lessons/cobit/m4-l1-facteurs-conception.md?raw'
import m5l1 from '../../lessons/cobit/m5-l1-niveaux-capacite.md?raw'
import m6l1 from '../../lessons/cobit/m6-l1-mapping-certifications.md?raw'
import m7l1 from '../../lessons/cobit/m7-l1-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: {
    introduction: m0l1,
  },
  'gouvernance-management-cascade': {
    'gouvernance-management': m1l1,
    'cascade-objectifs': m1l2,
  },
  'domaines-objectifs': {
    'domaine-apo': m2l1,
    'domaine-bai': m2l2,
    'domaines-dss-mea': m2l3,
  },
  composants: {
    composants: m3l1,
  },
  'facteurs-conception': {
    'facteurs-conception': m4l1,
  },
  'niveaux-capacite': {
    'niveaux-capacite': m5l1,
  },
  'mapping-certifications': {
    'mapping-certifications': m6l1,
  },
  'feuille-de-route': {
    'feuille-de-route': m7l1,
  },
}

export default content
