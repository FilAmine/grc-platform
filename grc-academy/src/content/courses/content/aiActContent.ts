import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/ai-act/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/ai-act/m1-l1-pratiques-interdites.md?raw'
import m1l2 from '../../lessons/ai-act/m1-l2-haut-risque-limite-minimal.md?raw'
import m2l1 from '../../lessons/ai-act/m2-l1-systeme-gestion-risques-donnees.md?raw'
import m2l2 from '../../lessons/ai-act/m2-l2-documentation-transparence-controle-humain.md?raw'
import m3l1 from '../../lessons/ai-act/m3-l1-acteurs-chaine-responsabilite.md?raw'
import m4l1 from '../../lessons/ai-act/m4-l1-conformite-marquage-ce.md?raw'
import m5l1 from '../../lessons/ai-act/m5-l1-modeles-usage-general.md?raw'
import m6l1 from '../../lessons/ai-act/m6-l1-gouvernance.md?raw'
import m6l2 from '../../lessons/ai-act/m6-l2-calendrier-sanctions.md?raw'
import m7l1 from '../../lessons/ai-act/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  'pyramide-risques': { 'pratiques-interdites': m1l1, 'haut-risque-limite-minimal': m1l2 },
  'obligations-haut-risque': { 'systeme-gestion-risques-donnees': m2l1, 'documentation-transparence-controle-humain': m2l2 },
  acteurs: { 'acteurs-chaine-responsabilite': m3l1 },
  conformite: { 'conformite-marquage-ce': m4l1 },
  gpai: { 'modeles-usage-general': m5l1 },
  'gouvernance-sanctions': { gouvernance: m6l1, 'calendrier-sanctions': m6l2 },
  'mapping-feuille-de-route': { 'mapping-feuille-de-route': m7l1 },
}

export default content
