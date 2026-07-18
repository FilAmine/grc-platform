import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/fedramp/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/fedramp/m1-l1-fips199-categorisation.md?raw'
import m1l2 from '../../lessons/fedramp/m1-l2-baselines-overlays.md?raw'
import m2l1 from '../../lessons/fedramp/m2-l1-agency-ato.md?raw'
import m2l2 from '../../lessons/fedramp/m2-l2-jab-p-ato.md?raw'
import m3l1 from '../../lessons/fedramp/m3-l1-acteurs-3pao.md?raw'
import m4l1 from '../../lessons/fedramp/m4-l1-surveillance-continue.md?raw'
import m4l2 from '../../lessons/fedramp/m4-l2-poam-changements.md?raw'
import m5l1 from '../../lessons/fedramp/m5-l1-marketplace-reciprocite.md?raw'
import m6l1 from '../../lessons/fedramp/m6-l1-programmes-apparentes.md?raw'
import m7l1 from '../../lessons/fedramp/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  'niveaux-impact': { 'fips199-categorisation': m1l1, 'baselines-overlays': m1l2 },
  'voies-autorisation': { 'agency-ato': m2l1, 'jab-p-ato': m2l2 },
  acteurs: { 'acteurs-3pao': m3l1 },
  'surveillance-continue': { 'surveillance-continue': m4l1, 'poam-changements': m4l2 },
  'marketplace-reciprocite': { 'marketplace-reciprocite': m5l1 },
  'programmes-apparentes': { 'programmes-apparentes': m6l1 },
  'mapping-feuille-de-route': { 'mapping-feuille-de-route': m7l1 },
}

export default content
