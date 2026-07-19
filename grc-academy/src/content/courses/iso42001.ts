import type { Course } from '../types'

export const iso42001: Course = {
  slug: 'iso-42001',
  title: 'ISO/IEC 42001 en profondeur',
  subtitle: 'Le système de management de l\'IA, l\'appréciation d\'impact, et la certification',
  description:
    "Un parcours entièrement dédié à ISO/IEC 42001 : la première norme internationale certifiable de système de management de l'intelligence artificielle (AIMS), les clauses 4 à 7 propres au SGIA, l'appréciation d'impact des systèmes d'IA et ses dimensions de confiance directement héritées du NIST AI RMF, l'Annexe A et ses contrôles organisés par thème (politiques, organisation, ressources, cycle de vie, données, tiers), les clauses 9 et 10 relatives à l'évaluation des performances et à l'amélioration continue, le processus de certification, le défi du maintien dans la durée face à un domaine en évolution rapide, et l'articulation avec le NIST AI RMF, l'AI Act et ISO 27001 déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'La première norme ISO de système de management de l\'IA, et sa place dans la trilogie NIST AI RMF/AI Act/ISO 42001.',
      lessons: [
        { slug: 'introduction', title: 'ISO/IEC 42001 en profondeur : introduction et repères', minutes: 12 },
      ],
    },
    {
      slug: 'clauses-sgia',
      title: 'Module 1 — Les clauses 4 à 7 du SGIA',
      description: 'Contexte, leadership, politique relative à l\'IA, planification et support.',
      lessons: [
        { slug: 'clauses-contexte-leadership', title: 'Les clauses 4 à 7 du SGIA (1/2) : contexte et leadership', minutes: 12 },
        { slug: 'clauses-planification-support', title: 'Les clauses 4 à 7 du SGIA (2/2) : planification et support', minutes: 12 },
      ],
    },
    {
      slug: 'appreciation-impact',
      title: 'Module 2 — L\'appréciation d\'impact des systèmes d\'IA',
      description: 'Méthodologie générale, et les dimensions de confiance héritées du NIST AI RMF.',
      lessons: [
        { slug: 'appreciation-impact-methodologie', title: 'L\'appréciation d\'impact des systèmes d\'IA (1/2) : méthodologie générale', minutes: 12 },
        { slug: 'dimensions-confiance-criteres', title: 'L\'appréciation d\'impact des systèmes d\'IA (2/2) : dimensions de confiance et critères évalués', minutes: 12 },
      ],
    },
    {
      slug: 'annexe-a',
      title: 'Module 3 — L\'Annexe A',
      description: 'Politiques, organisation et ressources ; cycle de vie, données et relations avec les tiers.',
      lessons: [
        { slug: 'annexe-a-politiques-organisation', title: 'L\'Annexe A (1/2) : politiques, organisation et ressources', minutes: 12 },
        { slug: 'annexe-a-cycle-vie-donnees-tiers', title: 'L\'Annexe A (2/2) : cycle de vie, données et relations avec les tiers', minutes: 12 },
      ],
    },
    {
      slug: 'evaluation-amelioration',
      title: 'Module 4 — Évaluation des performances et amélioration',
      description: 'Surveillance, audit interne, revue de direction, suivi post-déploiement, non-conformités.',
      lessons: [
        { slug: 'clauses-9-10', title: 'Les clauses 9 et 10 : évaluation des performances et amélioration continue', minutes: 12 },
      ],
    },
    {
      slug: 'certification',
      title: 'Module 5 — Le processus de certification',
      description: 'Stage 1/Stage 2, cycle triennal, lien avec l\'AI Act, et intégration avec ISO 27001/22301.',
      lessons: [
        { slug: 'certification', title: 'Le processus de certification ISO/IEC 42001', minutes: 12 },
      ],
    },
    {
      slug: 'maintien',
      title: 'Module 6 — Maintenir le SGIA dans la durée',
      description: 'Actualisation continue face à l\'évolution rapide de l\'IA, et veille réglementaire sur l\'AI Act.',
      lessons: [
        { slug: 'maintien-sgia', title: 'Maintenir le SGIA dans la durée face à un domaine en évolution rapide', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'ISO/IEC 42001 face au NIST AI RMF/AI Act/ISO 27001, pièges fréquents, et feuille de route.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'ISO/IEC 42001 face aux autres référentiels, et une feuille de route de mise en œuvre', minutes: 13 },
      ],
    },
  ],
}
