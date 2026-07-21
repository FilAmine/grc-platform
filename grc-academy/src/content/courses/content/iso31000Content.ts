import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/iso-31000/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/iso-31000/m1-l1-huit-principes.md?raw'
import m2l1 from '../../lessons/iso-31000/m2-l1-cadre-leadership-integration-conception.md?raw'
import m2l2 from '../../lessons/iso-31000/m2-l2-cadre-mise-en-oeuvre-evaluation-amelioration.md?raw'
import m3l1 from '../../lessons/iso-31000/m3-l1-contexte-criteres-appetence.md?raw'
import m4l1 from '../../lessons/iso-31000/m4-l1-identification-analyse.md?raw'
import m4l2 from '../../lessons/iso-31000/m4-l2-evaluation-priorisation.md?raw'
import m5l1 from '../../lessons/iso-31000/m5-l1-options-traitement.md?raw'
import m5l2 from '../../lessons/iso-31000/m5-l2-plan-traitement-risque-residuel.md?raw'
import m5l3 from '../../lessons/iso-31000/m5-l3-etudes-de-cas-reelles.md?raw'
import m6l1 from '../../lessons/iso-31000/m6-l1-surveillance-enregistrement-communication.md?raw'
import m7l1 from '../../lessons/iso-31000/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  principes: { 'huit-principes': m1l1 },
  'cadre-organisationnel': { 'cadre-leadership-integration-conception': m2l1, 'cadre-mise-en-oeuvre-evaluation-amelioration': m2l2 },
  'contexte-criteres': { 'contexte-criteres-appetence': m3l1 },
  'appreciation-risques': { 'identification-analyse': m4l1, 'evaluation-priorisation': m4l2 },
  traitement: { 'options-traitement': m5l1, 'plan-traitement-risque-residuel': m5l2, 'etudes-de-cas-reelles': m5l3 },
  surveillance: { 'surveillance-enregistrement-communication': m6l1 },
  'mapping-feuille-de-route': { 'mapping-feuille-de-route': m7l1 },
}

export default content
