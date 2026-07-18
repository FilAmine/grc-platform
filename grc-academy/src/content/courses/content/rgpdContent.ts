import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/rgpd/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/rgpd/m1-l1-champ-application.md?raw'
import m1l2 from '../../lessons/rgpd/m1-l2-bases-legales.md?raw'
import m2l1 from '../../lessons/rgpd/m2-l1-droits-partie1.md?raw'
import m2l2 from '../../lessons/rgpd/m2-l2-droits-partie2.md?raw'
import m3l1 from '../../lessons/rgpd/m3-l1-responsable-sous-traitant.md?raw'
import m3l2 from '../../lessons/rgpd/m3-l2-dpo.md?raw'
import m4l1 from '../../lessons/rgpd/m4-l1-securite-violations.md?raw'
import m4l2 from '../../lessons/rgpd/m4-l2-registre-aipd.md?raw'
import m5l1 from '../../lessons/rgpd/m5-l1-transferts-internationaux.md?raw'
import m6l1 from '../../lessons/rgpd/m6-l1-autorites-guichet-unique.md?raw'
import m6l2 from '../../lessons/rgpd/m6-l2-sanctions.md?raw'
import m7l1 from '../../lessons/rgpd/m7-l1-feuille-de-route.md?raw'

const content: CourseContent = {
  'introduction': {
    'introduction': m0l1,
  },
  'champ-bases-legales': {
    'champ-application': m1l1,
    'bases-legales': m1l2,
  },
  'droits-personnes': {
    'droits-partie1': m2l1,
    'droits-partie2': m2l2,
  },
  'responsable-dpo': {
    'responsable-sous-traitant': m3l1,
    'dpo': m3l2,
  },
  'securite-accountability': {
    'securite-violations': m4l1,
    'registre-aipd': m4l2,
  },
  'transferts-internationaux': {
    'transferts-internationaux': m5l1,
  },
  'gouvernance-sanctions': {
    'autorites-guichet-unique': m6l1,
    'sanctions': m6l2,
  },
  'feuille-de-route': {
    'feuille-de-route': m7l1,
  },
}

export default content
