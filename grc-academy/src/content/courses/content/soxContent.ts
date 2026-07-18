import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/sox/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/sox/m1-l1-certification-302-906.md?raw'
import m2l1 from '../../lessons/sox/m2-l1-section-404.md?raw'
import m2l2 from '../../lessons/sox/m2-l2-coso.md?raw'
import m3l1 from '../../lessons/sox/m3-l1-itgc-domaines.md?raw'
import m3l2 from '../../lessons/sox/m3-l2-separation-des-taches.md?raw'
import m4l1 from '../../lessons/sox/m4-l1-deficiences.md?raw'
import m5l1 from '../../lessons/sox/m5-l1-roles-gouvernance.md?raw'
import m6l1 from '../../lessons/sox/m6-l1-soc1.md?raw'
import m7l1 from '../../lessons/sox/m7-l1-mapping-sanctions.md?raw'
import m7l2 from '../../lessons/sox/m7-l2-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  certification: { 'certification-302-906': m1l1 },
  'section-404': { 'section-404': m2l1, coso: m2l2 },
  itgc: { 'itgc-domaines': m3l1, 'separation-des-taches': m3l2 },
  deficiences: { deficiences: m4l1 },
  'roles-gouvernance': { 'roles-gouvernance': m5l1 },
  soc1: { soc1: m6l1 },
  'mapping-feuille-de-route': { 'mapping-sanctions': m7l1, 'feuille-de-route': m7l2 },
}

export default content
