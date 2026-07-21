import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/zero-trust/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/zero-trust/m1-l1-sept-principes-partie1.md?raw'
import m1l2 from '../../lessons/zero-trust/m1-l2-sept-principes-partie2.md?raw'
import m2l1 from '../../lessons/zero-trust/m2-l1-architecture-logique-composants.md?raw'
import m2l2 from '../../lessons/zero-trust/m2-l2-algorithme-confiance.md?raw'
import m3l1 from '../../lessons/zero-trust/m3-l1-approches-deploiement.md?raw'
import m3l2 from '../../lessons/zero-trust/m3-l2-microsegmentation-sdp.md?raw'
import m4l1 from '../../lessons/zero-trust/m4-l1-migration-perimetre.md?raw'
import m5l1 from '../../lessons/zero-trust/m5-l1-menaces-propres-zta.md?raw'
import m6l1 from '../../lessons/zero-trust/m6-l1-modele-maturite-cisa.md?raw'
import m7l1 from '../../lessons/zero-trust/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  'sept-principes': { 'sept-principes-partie1': m1l1, 'sept-principes-partie2': m1l2 },
  'architecture-logique': { 'architecture-logique-composants': m2l1, 'algorithme-confiance': m2l2 },
  'approches-deploiement': { 'approches-deploiement': m3l1, 'microsegmentation-sdp': m3l2 },
  migration: { 'migration-perimetre': m4l1 },
  menaces: { 'menaces-propres-zta': m5l1 },
  'maturite-cisa': { 'modele-maturite-cisa': m6l1 },
  'mapping-feuille-de-route': { 'mapping-feuille-de-route': m7l1 },
}

export default content
