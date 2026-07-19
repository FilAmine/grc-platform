import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/swift-csp/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/swift-csp/m1-l1-architecture-types.md?raw'
import m1l2 from '../../lessons/swift-csp/m1-l2-structure-cscf.md?raw'
import m2l1 from '../../lessons/swift-csp/m2-l1-objectifs-1-2.md?raw'
import m2l2 from '../../lessons/swift-csp/m2-l2-objectif-3-detecter-repondre.md?raw'
import m3l1 from '../../lessons/swift-csp/m3-l1-auto-attestation-kyc-sa.md?raw'
import m3l2 from '../../lessons/swift-csp/m3-l2-evaluation-independante.md?raw'
import m4l1 from '../../lessons/swift-csp/m4-l1-kyc-registry-partage.md?raw'
import m5l1 from '../../lessons/swift-csp/m5-l1-sanctions-supervision.md?raw'
import m6l1 from '../../lessons/swift-csp/m6-l1-evolution-annuelle-cscf.md?raw'
import m7l1 from '../../lessons/swift-csp/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  'cscf-architecture': { 'architecture-types': m1l1, 'structure-cscf': m1l2 },
  'objectifs-securite': { 'objectifs-1-2': m2l1, 'objectif-3-detecter-repondre': m2l2 },
  'attestation-evaluation': { 'auto-attestation-kyc-sa': m3l1, 'evaluation-independante': m3l2 },
  'kyc-registry': { 'kyc-registry-partage': m4l1 },
  sanctions: { 'sanctions-supervision': m5l1 },
  'evolution-cscf': { 'evolution-annuelle-cscf': m6l1 },
  'mapping-feuille-de-route': { 'mapping-feuille-de-route': m7l1 },
}

export default content
