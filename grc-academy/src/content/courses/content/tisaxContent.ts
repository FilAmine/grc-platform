import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/tisax/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/tisax/m1-l1-catalogue-vda-isa.md?raw'
import m1l2 from '../../lessons/tisax/m1-l2-niveaux-maturite.md?raw'
import m2l1 from '../../lessons/tisax/m2-l1-assessment-levels.md?raw'
import m2l2 from '../../lessons/tisax/m2-l2-modules-objectifs.md?raw'
import m3l1 from '../../lessons/tisax/m3-l1-processus-audit-providers.md?raw'
import m4l1 from '../../lessons/tisax/m4-l1-partage-labels.md?raw'
import m4l2 from '../../lessons/tisax/m4-l2-validite-renouvellement.md?raw'
import m5l1 from '../../lessons/tisax/m5-l1-protection-prototypes.md?raw'
import m6l1 from '../../lessons/tisax/m6-l1-enjeux-contractuels.md?raw'
import m7l1 from '../../lessons/tisax/m7-l1-mapping-feuille-de-route.md?raw'

const content: CourseContent = {
  introduction: { introduction: m0l1 },
  'catalogue-maturite': { 'catalogue-vda-isa': m1l1, 'niveaux-maturite': m1l2 },
  'niveaux-objectifs': { 'assessment-levels': m2l1, 'modules-objectifs': m2l2 },
  'processus-audit-providers': { 'processus-audit-providers': m3l1 },
  'partage-resultats': { 'partage-labels': m4l1, 'validite-renouvellement': m4l2 },
  'protection-prototypes': { 'protection-prototypes': m5l1 },
  'enjeux-contractuels': { 'enjeux-contractuels': m6l1 },
  'mapping-feuille-de-route': { 'mapping-feuille-de-route': m7l1 },
}

export default content
