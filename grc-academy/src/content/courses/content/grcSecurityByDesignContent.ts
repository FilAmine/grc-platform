import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/grc-security-by-design/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/grc-security-by-design/m1-l1-gouvernance.md?raw'
import m1l2 from '../../lessons/grc-security-by-design/m1-l2-gestion-des-risques.md?raw'
import m1l3 from '../../lessons/grc-security-by-design/m1-l3-conformite.md?raw'
import m2l1 from '../../lessons/grc-security-by-design/m2-l1-iso27001.md?raw'
import m2l2 from '../../lessons/grc-security-by-design/m2-l2-nist-csf.md?raw'
import m2l3 from '../../lessons/grc-security-by-design/m2-l3-soc2.md?raw'
import m2l4 from '../../lessons/grc-security-by-design/m2-l4-rgpd.md?raw'
import m2l5 from '../../lessons/grc-security-by-design/m2-l5-comparatif.md?raw'
import m3l1 from '../../lessons/grc-security-by-design/m3-l1-principes-sbd.md?raw'
import m3l2 from '../../lessons/grc-security-by-design/m3-l2-defense-en-profondeur.md?raw'
import m4l1 from '../../lessons/grc-security-by-design/m4-l1-privacy-by-design.md?raw'
import m4l2 from '../../lessons/grc-security-by-design/m4-l2-privacy-rgpd-pratique.md?raw'
import m5l1 from '../../lessons/grc-security-by-design/m5-l1-responsabilite-partagee.md?raw'
import m5l2 from '../../lessons/grc-security-by-design/m5-l2-iam-chiffrement-reseau.md?raw'
import m5l3 from '../../lessons/grc-security-by-design/m5-l3-referentiels-cloud.md?raw'
import m6l1 from '../../lessons/grc-security-by-design/m6-l1-boucle-retroaction.md?raw'
import m6l2 from '../../lessons/grc-security-by-design/m6-l2-feuille-de-route.md?raw'

const content: CourseContent = {
  'introduction': {
    'bienvenue': m0l1,
  },
  'grc-fondamentaux': {
    'gouvernance': m1l1,
    'gestion-des-risques': m1l2,
    'conformite': m1l3,
  },
  'normes-referentiels': {
    'iso-27001': m2l1,
    'nist-csf': m2l2,
    'soc-2': m2l3,
    'rgpd': m2l4,
    'comparatif': m2l5,
  },
  'security-by-design': {
    'principes': m3l1,
    'defense-en-profondeur': m3l2,
  },
  'privacy-by-design': {
    'principes-cavoukian': m4l1,
    'rgpd-pratique': m4l2,
  },
  'cloud-security-by-design': {
    'responsabilite-partagee': m5l1,
    'iam-chiffrement-reseau': m5l2,
    'referentiels-cloud': m5l3,
  },
  'synthese': {
    'boucle-retroaction': m6l1,
    'feuille-de-route': m6l2,
  },
}

export default content
