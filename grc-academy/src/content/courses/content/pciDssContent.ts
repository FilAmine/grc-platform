import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/pci-dss/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/pci-dss/m1-l1-exigences-1-4.md?raw'
import m1l2 from '../../lessons/pci-dss/m1-l2-exigences-5-8.md?raw'
import m1l3 from '../../lessons/pci-dss/m1-l3-exigences-9-12.md?raw'
import m2l1 from '../../lessons/pci-dss/m2-l1-scoping-segmentation.md?raw'
import m3l1 from '../../lessons/pci-dss/m3-l1-niveaux-saq.md?raw'
import m3l2 from '../../lessons/pci-dss/m3-l2-qsa-asv.md?raw'
import m4l1 from '../../lessons/pci-dss/m4-l1-approche-personnalisee.md?raw'
import m5l1 from '../../lessons/pci-dss/m5-l1-protection-donnees-sensibles.md?raw'
import m6l1 from '../../lessons/pci-dss/m6-l1-sanctions-mapping.md?raw'
import m7l1 from '../../lessons/pci-dss/m7-l1-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: {
    introduction: m0l1,
  },
  'douze-exigences': {
    'exigences-1-4': m1l1,
    'exigences-5-8': m1l2,
    'exigences-9-12': m1l3,
  },
  scoping: {
    'scoping-segmentation': m2l1,
  },
  'validation-conformite': {
    'niveaux-saq': m3l1,
    'qsa-asv': m3l2,
  },
  'approche-personnalisee': {
    'approche-personnalisee': m4l1,
  },
  'donnees-sensibles': {
    'protection-donnees-sensibles': m5l1,
  },
  'sanctions-mapping': {
    'sanctions-mapping': m6l1,
  },
  'feuille-de-route': {
    'feuille-de-route': m7l1,
  },
}

export default content
