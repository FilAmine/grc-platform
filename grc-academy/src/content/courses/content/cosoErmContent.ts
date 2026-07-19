import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/coso-erm/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/coso-erm/m1-l1-erm-vs-internal-control.md?raw'
import m2l1 from '../../lessons/coso-erm/m2-l1-gouvernance-culture.md?raw'
import m3l1 from '../../lessons/coso-erm/m3-l1-contexte-appetence.md?raw'
import m3l2 from '../../lessons/coso-erm/m3-l2-strategies-alternatives-objectifs.md?raw'
import m4l1 from '../../lessons/coso-erm/m4-l1-identification-severite.md?raw'
import m4l2 from '../../lessons/coso-erm/m4-l2-priorisation-reponses.md?raw'
import m4l3 from '../../lessons/coso-erm/m4-l3-vue-portefeuille.md?raw'
import m5l1 from '../../lessons/coso-erm/m5-l1-revision.md?raw'
import m6l1 from '../../lessons/coso-erm/m6-l1-information-communication-reporting.md?raw'
import m7l1 from '../../lessons/coso-erm/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  'erm-vs-internal-control': { 'erm-vs-internal-control': m1l1 },
  'gouvernance-culture': { 'gouvernance-culture': m2l1 },
  'strategie-objectifs': { 'contexte-appetence': m3l1, 'strategies-alternatives-objectifs': m3l2 },
  performance: { 'identification-severite': m4l1, 'priorisation-reponses': m4l2, 'vue-portefeuille': m4l3 },
  revision: { revision: m5l1 },
  'information-communication': { 'information-communication-reporting': m6l1 },
  'mapping-feuille-de-route': { 'mapping-feuille-de-route': m7l1 },
}

export default content
