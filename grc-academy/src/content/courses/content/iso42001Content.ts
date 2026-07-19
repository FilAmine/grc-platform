import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/iso-42001/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/iso-42001/m1-l1-clauses-contexte-leadership.md?raw'
import m1l2 from '../../lessons/iso-42001/m1-l2-clauses-planification-support.md?raw'
import m2l1 from '../../lessons/iso-42001/m2-l1-appreciation-impact-methodologie.md?raw'
import m2l2 from '../../lessons/iso-42001/m2-l2-dimensions-confiance-criteres.md?raw'
import m3l1 from '../../lessons/iso-42001/m3-l1-annexe-a-politiques-organisation.md?raw'
import m3l2 from '../../lessons/iso-42001/m3-l2-annexe-a-cycle-vie-donnees-tiers.md?raw'
import m4l1 from '../../lessons/iso-42001/m4-l1-clauses-9-10.md?raw'
import m5l1 from '../../lessons/iso-42001/m5-l1-certification.md?raw'
import m6l1 from '../../lessons/iso-42001/m6-l1-maintien-sgia.md?raw'
import m7l1 from '../../lessons/iso-42001/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  'clauses-sgia': { 'clauses-contexte-leadership': m1l1, 'clauses-planification-support': m1l2 },
  'appreciation-impact': { 'appreciation-impact-methodologie': m2l1, 'dimensions-confiance-criteres': m2l2 },
  'annexe-a': { 'annexe-a-politiques-organisation': m3l1, 'annexe-a-cycle-vie-donnees-tiers': m3l2 },
  'evaluation-amelioration': { 'clauses-9-10': m4l1 },
  certification: { certification: m5l1 },
  maintien: { 'maintien-sgia': m6l1 },
  'mapping-feuille-de-route': { 'mapping-feuille-de-route': m7l1 },
}

export default content
