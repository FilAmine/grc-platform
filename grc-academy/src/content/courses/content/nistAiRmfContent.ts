import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/nist-ai-rmf/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/nist-ai-rmf/m1-l1-risque-sociotechnique-cycle-vie.md?raw'
import m1l2 from '../../lessons/nist-ai-rmf/m1-l2-caracteristiques-ia-digne-de-confiance.md?raw'
import m2l1 from '../../lessons/nist-ai-rmf/m2-l1-fonction-govern.md?raw'
import m3l1 from '../../lessons/nist-ai-rmf/m3-l1-fonction-map-contexte.md?raw'
import m3l2 from '../../lessons/nist-ai-rmf/m3-l2-fonction-map-categorisation.md?raw'
import m4l1 from '../../lessons/nist-ai-rmf/m4-l1-fonction-measure-methodes.md?raw'
import m4l2 from '../../lessons/nist-ai-rmf/m4-l2-fonction-measure-tevv.md?raw'
import m5l1 from '../../lessons/nist-ai-rmf/m5-l1-fonction-manage.md?raw'
import m6l1 from '../../lessons/nist-ai-rmf/m6-l1-profils-ai-rmf.md?raw'
import m7l1 from '../../lessons/nist-ai-rmf/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  'risque-ia': { 'risque-sociotechnique-cycle-vie': m1l1, 'caracteristiques-ia-digne-de-confiance': m1l2 },
  'fonction-govern': { 'fonction-govern': m2l1 },
  'fonction-map': { 'fonction-map-contexte': m3l1, 'fonction-map-categorisation': m3l2 },
  'fonction-measure': { 'fonction-measure-methodes': m4l1, 'fonction-measure-tevv': m4l2 },
  'fonction-manage': { 'fonction-manage': m5l1 },
  profils: { 'profils-ai-rmf': m6l1 },
  'mapping-feuille-de-route': { 'mapping-feuille-de-route': m7l1 },
}

export default content
