import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/iso-22301/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/iso-22301/m1-l1-clauses-contexte-leadership.md?raw'
import m1l2 from '../../lessons/iso-22301/m1-l2-clauses-planification-support.md?raw'
import m2l1 from '../../lessons/iso-22301/m2-l1-analyse-impact-bia.md?raw'
import m2l2 from '../../lessons/iso-22301/m2-l2-appreciation-risques-bcm.md?raw'
import m3l1 from '../../lessons/iso-22301/m3-l1-strategies-continuite.md?raw'
import m3l2 from '../../lessons/iso-22301/m3-l2-plans-continuite-gestion-crise.md?raw'
import m4l1 from '../../lessons/iso-22301/m4-l1-exercices-tests.md?raw'
import m5l1 from '../../lessons/iso-22301/m5-l1-evaluation-amelioration.md?raw'
import m6l1 from '../../lessons/iso-22301/m6-l1-certification.md?raw'
import m7l1 from '../../lessons/iso-22301/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  'clauses-smca': { 'clauses-contexte-leadership': m1l1, 'clauses-planification-support': m1l2 },
  'analyse-impact': { 'analyse-impact-bia': m2l1, 'appreciation-risques-bcm': m2l2 },
  'strategies-plans': { 'strategies-continuite': m3l1, 'plans-continuite-gestion-crise': m3l2 },
  exercices: { 'exercices-tests': m4l1 },
  'evaluation-amelioration': { 'evaluation-amelioration': m5l1 },
  certification: { certification: m6l1 },
  'mapping-feuille-de-route': { 'mapping-feuille-de-route': m7l1 },
}

export default content
