import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/iso-20000/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/iso-20000/m1-l1-clauses-contexte-leadership.md?raw'
import m1l2 from '../../lessons/iso-20000/m1-l2-clauses-planification-support.md?raw'
import m2l1 from '../../lessons/iso-20000/m2-l1-planification-catalogue-services.md?raw'
import m3l1 from '../../lessons/iso-20000/m3-l1-processus-relation-fournisseurs.md?raw'
import m4l1 from '../../lessons/iso-20000/m4-l1-gestion-changements.md?raw'
import m4l2 from '../../lessons/iso-20000/m4-l2-conception-transition-deploiement.md?raw'
import m5l1 from '../../lessons/iso-20000/m5-l1-resolution-satisfaction-demandes.md?raw'
import m6l1 from '../../lessons/iso-20000/m6-l1-assurance-service.md?raw'
import m7l1 from '../../lessons/iso-20000/m7-l1-certification.md?raw'
import m7l2 from '../../lessons/iso-20000/m7-l2-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  'clauses-sms': { 'clauses-contexte-leadership': m1l1, 'clauses-planification-support': m1l2 },
  'planification-catalogue': { 'planification-catalogue-services': m2l1 },
  relations: { 'processus-relation-fournisseurs': m3l1 },
  'conception-transition': { 'gestion-changements': m4l1, 'conception-transition-deploiement': m4l2 },
  resolution: { 'resolution-satisfaction-demandes': m5l1 },
  assurance: { 'assurance-service': m6l1 },
  'certification-mapping': { certification: m7l1, 'mapping-feuille-de-route': m7l2 },
}

export default content
