import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/nis2/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/nis2/m1-l1-secteurs-entites.md?raw'
import m1l2 from '../../lessons/nis2/m1-l2-seuils-juridiction.md?raw'
import m2l1 from '../../lessons/nis2/m2-l1-article-21-partie1.md?raw'
import m2l2 from '../../lessons/nis2/m2-l2-article-21-partie2.md?raw'
import m3l1 from '../../lessons/nis2/m3-l1-gouvernance.md?raw'
import m4l1 from '../../lessons/nis2/m4-l1-notification-incidents.md?raw'
import m5l1 from '../../lessons/nis2/m5-l1-supervision.md?raw'
import m5l2 from '../../lessons/nis2/m5-l2-sanctions.md?raw'
import m6l1 from '../../lessons/nis2/m6-l1-cooperation-europeenne.md?raw'
import m7l1 from '../../lessons/nis2/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  'introduction': {
    'introduction': m0l1,
  },
  'champ-application': {
    'secteurs-entites': m1l1,
    'seuils-juridiction': m1l2,
  },
  'article-21': {
    'article-21-partie1': m2l1,
    'article-21-partie2': m2l2,
  },
  'gouvernance': {
    'gouvernance': m3l1,
  },
  'notification': {
    'notification-incidents': m4l1,
  },
  'supervision-sanctions': {
    'supervision': m5l1,
    'sanctions': m5l2,
  },
  'cooperation-europeenne': {
    'cooperation-europeenne': m6l1,
  },
  'mapping-feuille-de-route': {
    'mapping-feuille-de-route': m7l1,
  },
}

export default content
