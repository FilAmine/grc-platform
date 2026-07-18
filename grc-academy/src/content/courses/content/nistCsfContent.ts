import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/nist-csf/m0-l1-origines-philosophie.md?raw'
import m1l1 from '../../lessons/nist-csf/m1-l1-govern.md?raw'
import m1l2 from '../../lessons/nist-csf/m1-l2-identify.md?raw'
import m1l3 from '../../lessons/nist-csf/m1-l3-protect.md?raw'
import m1l4 from '../../lessons/nist-csf/m1-l4-detect.md?raw'
import m1l5 from '../../lessons/nist-csf/m1-l5-respond-recover.md?raw'
import m2l1 from '../../lessons/nist-csf/m2-l1-categories-references.md?raw'
import m3l1 from '../../lessons/nist-csf/m3-l1-tiers.md?raw'
import m3l2 from '../../lessons/nist-csf/m3-l2-profils.md?raw'
import m4l1 from '../../lessons/nist-csf/m4-l1-etapes-mise-en-oeuvre.md?raw'
import m4l2 from '../../lessons/nist-csf/m4-l2-mapping-supply-chain.md?raw'

const content: CourseContent = {
  'introduction': {
    'origines-philosophie': m0l1,
  },
  'les-six-fonctions': {
    'govern': m1l1,
    'identify': m1l2,
    'protect': m1l3,
    'detect': m1l4,
    'respond-recover': m1l5,
  },
  'structure-du-core': {
    'categories-references': m2l1,
  },
  'tiers-et-profils': {
    'tiers': m3l1,
    'profils': m3l2,
  },
  'mise-en-oeuvre': {
    'etapes-mise-en-oeuvre': m4l1,
    'mapping-supply-chain': m4l2,
  },
}

export default content
