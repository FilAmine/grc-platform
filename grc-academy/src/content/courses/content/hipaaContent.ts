import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/hipaa/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/hipaa/m1-l1-privacy-rule-divulgations.md?raw'
import m1l2 from '../../lessons/hipaa/m1-l2-droits-des-patients.md?raw'
import m2l1 from '../../lessons/hipaa/m2-l1-sauvegardes-administratives.md?raw'
import m2l2 from '../../lessons/hipaa/m2-l2-sauvegardes-physiques-techniques.md?raw'
import m2l3 from '../../lessons/hipaa/m2-l3-required-addressable.md?raw'
import m3l1 from '../../lessons/hipaa/m3-l1-business-associates.md?raw'
import m4l1 from '../../lessons/hipaa/m4-l1-breach-notification.md?raw'
import m5l1 from '../../lessons/hipaa/m5-l1-application-sanctions.md?raw'
import m6l1 from '../../lessons/hipaa/m6-l1-deidentification.md?raw'
import m6l2 from '../../lessons/hipaa/m6-l2-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: {
    introduction: m0l1,
  },
  'privacy-rule': {
    divulgations: m1l1,
    'droits-des-patients': m1l2,
  },
  'security-rule': {
    'sauvegardes-administratives': m2l1,
    'sauvegardes-physiques-techniques': m2l2,
    'required-addressable': m2l3,
  },
  'business-associates': {
    'business-associates': m3l1,
  },
  'breach-notification': {
    'breach-notification': m4l1,
  },
  'application-sanctions': {
    'application-sanctions': m5l1,
  },
  'deidentification-mapping': {
    deidentification: m6l1,
    'mapping-feuille-de-route': m6l2,
  },
}

export default content
