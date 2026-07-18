import type { Course } from '../types'

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
        { slug: 'introduction', title: 'NIS2 en profondeur : introduction et repères', minutes: 10 },
      ],
    },
    {
      slug: 'champ-application',
      title: 'Module 1 — Champ d\'application',
      description: 'Secteurs des Annexes I et II, distinction essentielle/importante, seuils et juridiction.',
      lessons: [
        { slug: 'secteurs-entites', title: 'Champ d\'application (1/2) : secteurs et distinction essentielle/importante', minutes: 12 },
        { slug: 'seuils-juridiction', title: 'Champ d\'application (2/2) : le mécanisme de seuil, les exceptions, et la juridiction', minutes: 12 },
      ],
    },
    {
      slug: 'article-21',
      title: 'Module 2 — Les mesures de gestion des risques (article 21)',
      description: 'L\'approche "tous risques" et les dix domaines de mesures minimales.',
      lessons: [
        { slug: 'article-21-partie1', title: 'Les mesures de gestion des risques de l\'article 21 (1/2)', minutes: 12 },
        { slug: 'article-21-partie2', title: 'Les mesures de gestion des risques de l\'article 21 (2/2)', minutes: 12 },
      ],
    },
    {
      slug: 'gouvernance',
      title: 'Module 3 — Responsabilité des organes de direction',
      description: 'L\'article 20 : approbation, supervision, responsabilité personnelle et formation des dirigeants.',
      lessons: [
        { slug: 'gouvernance', title: 'La responsabilité des organes de direction (article 20)', minutes: 11 },
      ],
    },
    {
      slug: 'notification',
      title: 'Module 4 — Notification des incidents',
      description: 'L\'article 23 : alerte précoce (24h), notification (72h), rapport final (1 mois).',
      lessons: [
        { slug: 'notification-incidents', title: 'La notification des incidents (article 23)', minutes: 12 },
      ],
    },
    {
      slug: 'supervision-sanctions',
      title: 'Module 5 — Supervision et sanctions',
      description: 'Le régime différencié (proactif/réactif) et les amendes administratives.',
      lessons: [
        { slug: 'supervision', title: 'Le régime différencié de supervision', minutes: 12 },
        { slug: 'sanctions', title: 'Les sanctions administratives', minutes: 10 },
      ],
    },
    {
      slug: 'cooperation-europeenne',
      title: 'Module 6 — Coopération européenne',
      description: 'Points de contact uniques, CSIRT, Groupe de coopération, EU-CyCLONe, divulgation des vulnérabilités.',
      lessons: [
        { slug: 'cooperation-europeenne', title: 'L\'écosystème de coopération européenne et la divulgation coordonnée des vulnérabilités', minutes: 11 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'NIS2 face au RGPD/DORA/référentiels techniques, et une feuille de route de mise en conformité.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'NIS2 face aux autres référentiels, et feuille de route de mise en conformité', minutes: 12 },
      ],
    },
  ],
}
