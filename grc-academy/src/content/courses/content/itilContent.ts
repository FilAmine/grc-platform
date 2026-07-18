import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/itil/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/itil/m1-l1-service-value-system.md?raw'
import m1l2 from '../../lessons/itil/m1-l2-principes-directeurs.md?raw'
import m2l1 from '../../lessons/itil/m2-l1-service-value-chain.md?raw'
import m3l1 from '../../lessons/itil/m3-l1-pratiques-generales.md?raw'
import m3l2 from '../../lessons/itil/m3-l2-pratiques-operationnelles.md?raw'
import m4l1 from '../../lessons/itil/m4-l1-change-enablement.md?raw'
import m5l1 from '../../lessons/itil/m5-l1-niveaux-de-service.md?raw'
import m6l1 from '../../lessons/itil/m6-l1-amelioration-continue.md?raw'
import m7l1 from '../../lessons/itil/m7-l1-mapping-certifications.md?raw'
import m7l2 from '../../lessons/itil/m7-l2-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: {
    introduction: m0l1,
  },
  'service-value-system': {
    'service-value-system': m1l1,
    'principes-directeurs': m1l2,
  },
  'service-value-chain': {
    'service-value-chain': m2l1,
  },
  pratiques: {
    'pratiques-generales': m3l1,
    'pratiques-operationnelles': m3l2,
  },
  'change-enablement': {
    'change-enablement': m4l1,
  },
  'niveaux-de-service': {
    'niveaux-de-service': m5l1,
  },
  'amelioration-continue': {
    'amelioration-continue': m6l1,
  },
  'mapping-feuille-de-route': {
    'mapping-certifications': m7l1,
    'feuille-de-route': m7l2,
  },
}

export default content
