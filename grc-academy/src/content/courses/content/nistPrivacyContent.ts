import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/nist-privacy/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/nist-privacy/m1-l1-risque-vie-privee-data-actions.md?raw'
import m1l2 from '../../lessons/nist-privacy/m1-l2-methodologie-appreciation-risque.md?raw'
import m2l1 from '../../lessons/nist-privacy/m2-l1-core-govern-identify.md?raw'
import m3l1 from '../../lessons/nist-privacy/m3-l1-control-communicate.md?raw'
import m3l2 from '../../lessons/nist-privacy/m3-l2-protect-pont-csf.md?raw'
import m4l1 from '../../lessons/nist-privacy/m4-l1-profils.md?raw'
import m4l2 from '../../lessons/nist-privacy/m4-l2-tiers.md?raw'
import m5l1 from '../../lessons/nist-privacy/m5-l1-ecosysteme-traitement-donnees.md?raw'
import m6l1 from '../../lessons/nist-privacy/m6-l1-ingenierie-vie-privee.md?raw'
import m7l1 from '../../lessons/nist-privacy/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  'modele-risque': { 'risque-vie-privee-data-actions': m1l1, 'methodologie-appreciation-risque': m1l2 },
  'core-govern-identify': { 'core-govern-identify': m2l1 },
  'core-control-communicate-protect': { 'control-communicate': m3l1, 'protect-pont-csf': m3l2 },
  'profils-tiers': { profils: m4l1, tiers: m4l2 },
  ecosysteme: { 'ecosysteme-traitement-donnees': m5l1 },
  'ingenierie-vie-privee': { 'ingenierie-vie-privee': m6l1 },
  'mapping-feuille-de-route': { 'mapping-feuille-de-route': m7l1 },
}

export default content
