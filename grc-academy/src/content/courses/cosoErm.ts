import type { Course } from '../types'

export const cosoErm: Course = {
  slug: 'coso-erm',
  title: 'COSO ERM en profondeur',
  subtitle: 'La gestion des risques d\'entreprise intégrée à la stratégie et à la performance',
  description:
    "Un parcours entièrement dédié à COSO Enterprise Risk Management – Integrating with Strategy and Performance (2017) : sa distinction fondamentale avec COSO Internal Control déjà étudié dans les parcours SOC 2 et SOX de cette plateforme, la composante Gouvernance et culture, la composante Stratégie et fixation des objectifs avec l'appétence, la tolérance et la capacité de risque et l'évaluation de stratégies alternatives, la composante Performance avec l'identification, l'évaluation de la sévérité, la priorisation, les réponses au risque et la vue de portefeuille, la composante Révision, la composante Information, communication et reporting, et l'articulation avec ISO 31000, SOX et DORA déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Un second référentiel COSO, distinct de COSO Internal Control, orienté stratégie et création de valeur.',
      lessons: [
        { slug: 'introduction', title: 'COSO ERM en profondeur : introduction et repères', minutes: 12 },
      ],
    },
    {
      slug: 'erm-vs-internal-control',
      title: 'Module 1 — COSO ERM face à COSO Internal Control',
      description: 'Pourquoi ces deux référentiels du même organisme ne sont jamais interchangeables.',
      lessons: [
        { slug: 'erm-vs-internal-control', title: 'COSO ERM face à COSO Internal Control', minutes: 12 },
      ],
    },
    {
      slug: 'gouvernance-culture',
      title: 'Module 2 — Gouvernance et culture',
      description: 'Supervision du conseil, structures opérationnelles, culture souhaitée, compétences.',
      lessons: [
        { slug: 'gouvernance-culture', title: 'Gouvernance et culture', minutes: 13 },
      ],
    },
    {
      slug: 'strategie-objectifs',
      title: 'Module 3 — Stratégie et fixation des objectifs',
      description: 'Contexte métier, appétence/tolérance/capacité de risque, stratégies alternatives et objectifs métier.',
      lessons: [
        { slug: 'contexte-appetence', title: 'Stratégie et fixation des objectifs (1/2) : contexte métier et appétence pour le risque', minutes: 13 },
        { slug: 'strategies-alternatives-objectifs', title: 'Stratégie et fixation des objectifs (2/2) : stratégies alternatives et objectifs métier', minutes: 12 },
      ],
    },
    {
      slug: 'performance',
      title: 'Module 4 — Performance',
      description: 'Identification et sévérité, priorisation et réponses, et la vue de portefeuille des risques.',
      lessons: [
        { slug: 'identification-severite', title: 'Performance (1/3) : identifier les risques et évaluer leur sévérité', minutes: 12 },
        { slug: 'priorisation-reponses', title: 'Performance (2/3) : prioriser les risques et choisir les réponses', minutes: 12 },
        { slug: 'vue-portefeuille', title: 'Performance (3/3) : la vue de portefeuille des risques', minutes: 12 },
      ],
    },
    {
      slug: 'revision',
      title: 'Module 5 — Révision',
      description: 'Changements substantiels, revue du risque et de la performance, amélioration du dispositif ERM.',
      lessons: [
        { slug: 'revision', title: 'Révision', minutes: 12 },
      ],
    },
    {
      slug: 'information-communication',
      title: 'Module 6 — Information, communication et reporting',
      description: 'Exploiter l\'information et la technologie, communiquer, et produire un reporting intégré risque/performance.',
      lessons: [
        { slug: 'information-communication-reporting', title: 'Information, communication et reporting', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'COSO ERM face à ISO 31000/SOX/DORA, pièges fréquents, et feuille de route de mise en œuvre.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'COSO ERM face aux autres référentiels, et une feuille de route de mise en œuvre', minutes: 13 },
      ],
    },
  ],
}
