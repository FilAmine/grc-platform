import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/ebios-rm/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/ebios-rm/m1-l1-cadrage.md?raw'
import m1l2 from '../../lessons/ebios-rm/m1-l2-socle-securite.md?raw'
import m2l1 from '../../lessons/ebios-rm/m2-l1-sources-de-risque.md?raw'
import m3l1 from '../../lessons/ebios-rm/m3-l1-scenarios-strategiques.md?raw'
import m4l1 from '../../lessons/ebios-rm/m4-l1-scenarios-operationnels.md?raw'
import m5l1 from '../../lessons/ebios-rm/m5-l1-traitement-du-risque.md?raw'
import m6l1 from '../../lessons/ebios-rm/m6-l1-qualifications-certifications.md?raw'
import m6l2 from '../../lessons/ebios-rm/m6-l2-lpm-nis2-certfr.md?raw'
import m7l1 from '../../lessons/ebios-rm/m7-l1-mapping.md?raw'
import m7l2 from '../../lessons/ebios-rm/m7-l2-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: {
    introduction: m0l1,
  },
  'atelier-1': {
    cadrage: m1l1,
    'socle-securite': m1l2,
  },
  'atelier-2': {
    'sources-de-risque': m2l1,
  },
  'atelier-3': {
    'scenarios-strategiques': m3l1,
  },
  'atelier-4': {
    'scenarios-operationnels': m4l1,
  },
  'atelier-5': {
    'traitement-du-risque': m5l1,
  },
  'ecosysteme-anssi': {
    'qualifications-certifications': m6l1,
    'lpm-nis2-certfr': m6l2,
  },
  'mapping-feuille-de-route': {
    mapping: m7l1,
    'feuille-de-route': m7l2,
  },
}

export default content
