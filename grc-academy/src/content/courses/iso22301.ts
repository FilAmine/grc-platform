import type { Course } from '../types'

export const iso22301: Course = {
  slug: 'iso-22301',
  title: 'ISO 22301 en profondeur',
  subtitle: 'Le SMCA clause par clause, la BIA, les stratégies de continuité et la certification',
  description:
    "Un parcours entièrement dédié à ISO 22301 : ses origines dans BS 25999 et la High Level Structure partagée avec ISO 27001, les clauses 4 à 7 du système de management de la continuité d'activité (SMCA), l'analyse d'impact sur l'activité (BIA) et ses métriques clés (MTPD, RTO, RPO), l'appréciation des risques propre à la continuité, les stratégies et plans de continuité ainsi que la structure de gestion de crise, le programme d'exercices et de tests, les clauses 9 et 10 relatives à l'évaluation des performances et à l'amélioration continue, le processus de certification, et l'articulation avec ISO 27001, DORA et ITIL déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Origines (BS 25999), la High Level Structure partagée avec ISO 27001, et distinction avec la sécurité de l\'information.',
      lessons: [
        { slug: 'introduction', title: 'ISO 22301 en profondeur : introduction et repères', minutes: 11 },
      ],
    },
    {
      slug: 'clauses-smca',
      title: 'Module 1 — Les clauses 4 à 7 du SMCA',
      description: 'Contexte, leadership, planification et support propres au système de management de la continuité d\'activité.',
      lessons: [
        { slug: 'clauses-contexte-leadership', title: 'Les clauses 4 à 7 du SMCA (1/2) : contexte et leadership', minutes: 12 },
        { slug: 'clauses-planification-support', title: 'Les clauses 4 à 7 du SMCA (2/2) : planification et support', minutes: 12 },
      ],
    },
    {
      slug: 'analyse-impact',
      title: 'Module 2 — L\'analyse d\'impact sur l\'activité',
      description: 'La BIA, ses métriques clés (MTPD, RTO, RPO), et l\'appréciation des risques propre à la continuité.',
      lessons: [
        { slug: 'analyse-impact-bia', title: 'L\'analyse d\'impact sur l\'activité (1/2) : la Business Impact Analysis et ses métriques clés', minutes: 13 },
        { slug: 'appreciation-risques-bcm', title: 'L\'analyse d\'impact sur l\'activité (2/2) : l\'appréciation des risques propre à la continuité', minutes: 12 },
      ],
    },
    {
      slug: 'strategies-plans',
      title: 'Module 3 — Stratégies et plans de continuité',
      description: 'Les stratégies de continuité (sites, systèmes, personnes, fournisseurs), les plans opérationnels et la gestion de crise.',
      lessons: [
        { slug: 'strategies-continuite', title: 'Les stratégies de continuité d\'activité', minutes: 13 },
        { slug: 'plans-continuite-gestion-crise', title: 'Les plans de continuité et la structure de gestion de crise', minutes: 13 },
      ],
    },
    {
      slug: 'exercices',
      title: 'Module 4 — Le programme d\'exercices et de tests',
      description: 'Des exercices sur table à l\'exercice grandeur nature, et le rôle du retour d\'expérience.',
      lessons: [
        { slug: 'exercices-tests', title: 'Le programme d\'exercices et de tests', minutes: 12 },
      ],
    },
    {
      slug: 'evaluation-amelioration',
      title: 'Module 5 — Évaluation des performances et amélioration',
      description: 'Les clauses 9 et 10 : surveillance, audit interne, revue de direction, non-conformités et amélioration continue.',
      lessons: [
        { slug: 'evaluation-amelioration', title: 'Les clauses 9 et 10 : évaluation des performances et amélioration continue', minutes: 12 },
      ],
    },
    {
      slug: 'certification',
      title: 'Module 6 — Le processus de certification',
      description: 'Stage 1/Stage 2, non-conformités, cycle triennal, multi-sites et systèmes de management intégrés.',
      lessons: [
        { slug: 'certification', title: 'Le processus de certification ISO 22301', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'ISO 22301 face à ISO 27001/DORA/ITIL, pièges fréquents, et feuille de route de mise en œuvre.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'ISO 22301 face aux autres référentiels, et une feuille de route de mise en œuvre', minutes: 13 },
      ],
    },
  ],
}
