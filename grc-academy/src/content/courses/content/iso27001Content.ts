import type { CourseContent } from '../../types'
import m0l1 from '../../lessons/iso-27001/m0-l1-introduction.md?raw'
import m1l1 from '../../lessons/iso-27001/m1-l1-clauses-4-6.md?raw'
import m1l2 from '../../lessons/iso-27001/m1-l2-clauses-7-8.md?raw'
import m1l3 from '../../lessons/iso-27001/m1-l3-clauses-9-10.md?raw'
import m2l1 from '../../lessons/iso-27001/m2-l1-organisationnels-1.md?raw'
import m2l2 from '../../lessons/iso-27001/m2-l2-organisationnels-2.md?raw'
import m3l1 from '../../lessons/iso-27001/m3-l1-personnes-physiques.md?raw'
import m4l1 from '../../lessons/iso-27001/m4-l1-technologiques-1.md?raw'
import m4l2 from '../../lessons/iso-27001/m4-l2-technologiques-2.md?raw'
import m5l1 from '../../lessons/iso-27001/m5-l1-soa.md?raw'
import m6l1 from '../../lessons/iso-27001/m6-l1-certification.md?raw'
import m7l1 from '../../lessons/iso-27001/m7-l1-maintien-smsi.md?raw'
import m8l1 from '../../lessons/iso-27001/m8-l1-feuille-de-route.md?raw'

const content: CourseContent = {
  'introduction': {
    'introduction': m0l1,
  },
  'clauses-smsi': {
    'clauses-4-6': m1l1,
    'clauses-7-8': m1l2,
    'clauses-9-10': m1l3,
  },
  'controles-organisationnels': {
    'organisationnels-1': m2l1,
    'organisationnels-2': m2l2,
  },
  'controles-personnes-physiques': {
    'personnes-physiques': m3l1,
  },
  'controles-technologiques': {
    'technologiques-1': m4l1,
    'technologiques-2': m4l2,
  },
  'declaration-applicabilite': {
    'soa': m5l1,
  },
  'certification': {
    'certification': m6l1,
  },
  'maintien': {
    'maintien-smsi': m7l1,
  },
  'feuille-de-route': {
    'feuille-de-route': m8l1,
  },
}

export default content
