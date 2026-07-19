import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/iso-27701/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/iso-27701/m1-l1-mecanisme-extension.md?raw'
import m1l2 from '../../lessons/iso-27701/m1-l2-appreciation-risques-vie-privee.md?raw'
import m2l1 from '../../lessons/iso-27701/m2-l1-roles-responsable-sous-traitant.md?raw'
import m3l1 from '../../lessons/iso-27701/m3-l1-conditions-collecte-bases-legales.md?raw'
import m3l2 from '../../lessons/iso-27701/m3-l2-droits-personnes-privacy-by-design.md?raw'
import m4l1 from '../../lessons/iso-27701/m4-l1-controles-sous-traitants.md?raw'
import m5l1 from '../../lessons/iso-27701/m5-l1-transferts-internationaux.md?raw'
import m5l2 from '../../lessons/iso-27701/m5-l2-sous-traitance-ulterieure-tiers.md?raw'
import m6l1 from '../../lessons/iso-27701/m6-l1-certification.md?raw'
import m7l1 from '../../lessons/iso-27701/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  'architecture-extension': { 'mecanisme-extension': m1l1, 'appreciation-risques-vie-privee': m1l2 },
  roles: { 'roles-responsable-sous-traitant': m2l1 },
  'annexe-a': { 'conditions-collecte-bases-legales': m3l1, 'droits-personnes-privacy-by-design': m3l2 },
  'annexe-b': { 'controles-sous-traitants': m4l1 },
  'partage-transfert': { 'transferts-internationaux': m5l1, 'sous-traitance-ulterieure-tiers': m5l2 },
  certification: { certification: m6l1 },
  'mapping-feuille-de-route': { 'mapping-feuille-de-route': m7l1 },
}

export default content
