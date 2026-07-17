import type { Course } from '../types'
import m0l1 from '../lessons/nis2/m0-l1-introduction.md?raw'
import m1l1 from '../lessons/nis2/m1-l1-secteurs-entites.md?raw'
import m1l2 from '../lessons/nis2/m1-l2-seuils-juridiction.md?raw'
import m2l1 from '../lessons/nis2/m2-l1-article-21-partie1.md?raw'
import m2l2 from '../lessons/nis2/m2-l2-article-21-partie2.md?raw'
import m3l1 from '../lessons/nis2/m3-l1-gouvernance.md?raw'
import m4l1 from '../lessons/nis2/m4-l1-notification-incidents.md?raw'
import m5l1 from '../lessons/nis2/m5-l1-supervision.md?raw'
import m5l2 from '../lessons/nis2/m5-l2-sanctions.md?raw'
import m6l1 from '../lessons/nis2/m6-l1-cooperation-europeenne.md?raw'
import m7l1 from '../lessons/nis2/m7-l1-mapping-feuille-de-route.md?raw'

export const nis2: Course = {
  slug: 'nis2',
  title: 'NIS2 en profondeur',
  subtitle: 'Entités essentielles et importantes, article 21, notification des incidents',
  description:
    "Un parcours entièrement dédié à la directive NIS2 : le champ d'application élargi (secteurs des Annexes I et II, distinction entre entités essentielles et importantes, mécanisme de seuil et juridiction), les dix domaines de mesures de gestion des risques de l'article 21, la responsabilité personnelle des organes de direction (article 20), le processus de notification des incidents en plusieurs paliers (article 23), le régime différencié de supervision et les sanctions, l'écosystème de coopération européenne, et l'articulation avec le RGPD, DORA et les référentiels techniques déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'De NIS1 à NIS2, objectifs de la directive, calendrier de transposition.',
      lessons: [
        { slug: 'introduction', title: 'NIS2 en profondeur : introduction et repères', minutes: 10, content: m0l1 },
      ],
    },
    {
      slug: 'champ-application',
      title: 'Module 1 — Champ d\'application',
      description: 'Secteurs des Annexes I et II, distinction essentielle/importante, seuils et juridiction.',
      lessons: [
        { slug: 'secteurs-entites', title: 'Champ d\'application (1/2) : secteurs et distinction essentielle/importante', minutes: 12, content: m1l1 },
        { slug: 'seuils-juridiction', title: 'Champ d\'application (2/2) : le mécanisme de seuil, les exceptions, et la juridiction', minutes: 12, content: m1l2 },
      ],
    },
    {
      slug: 'article-21',
      title: 'Module 2 — Les mesures de gestion des risques (article 21)',
      description: 'L\'approche "tous risques" et les dix domaines de mesures minimales.',
      lessons: [
        { slug: 'article-21-partie1', title: 'Les mesures de gestion des risques de l\'article 21 (1/2)', minutes: 12, content: m2l1 },
        { slug: 'article-21-partie2', title: 'Les mesures de gestion des risques de l\'article 21 (2/2)', minutes: 12, content: m2l2 },
      ],
    },
    {
      slug: 'gouvernance',
      title: 'Module 3 — Responsabilité des organes de direction',
      description: 'L\'article 20 : approbation, supervision, responsabilité personnelle et formation des dirigeants.',
      lessons: [
        { slug: 'gouvernance', title: 'La responsabilité des organes de direction (article 20)', minutes: 11, content: m3l1 },
      ],
    },
    {
      slug: 'notification',
      title: 'Module 4 — Notification des incidents',
      description: 'L\'article 23 : alerte précoce (24h), notification (72h), rapport final (1 mois).',
      lessons: [
        { slug: 'notification-incidents', title: 'La notification des incidents (article 23)', minutes: 12, content: m4l1 },
      ],
    },
    {
      slug: 'supervision-sanctions',
      title: 'Module 5 — Supervision et sanctions',
      description: 'Le régime différencié (proactif/réactif) et les amendes administratives.',
      lessons: [
        { slug: 'supervision', title: 'Le régime différencié de supervision', minutes: 12, content: m5l1 },
        { slug: 'sanctions', title: 'Les sanctions administratives', minutes: 10, content: m5l2 },
      ],
    },
    {
      slug: 'cooperation-europeenne',
      title: 'Module 6 — Coopération européenne',
      description: 'Points de contact uniques, CSIRT, Groupe de coopération, EU-CyCLONe, divulgation des vulnérabilités.',
      lessons: [
        { slug: 'cooperation-europeenne', title: 'L\'écosystème de coopération européenne et la divulgation coordonnée des vulnérabilités', minutes: 11, content: m6l1 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'NIS2 face au RGPD/DORA/référentiels techniques, et une feuille de route de mise en conformité.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'NIS2 face aux autres référentiels, et feuille de route de mise en conformité', minutes: 12, content: m7l1 },
      ],
    },
  ],
}
