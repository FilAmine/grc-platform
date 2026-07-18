import type { Course } from '../types'

export const fedramp: Course = {
  slug: 'fedramp',
  title: 'FedRAMP en profondeur',
  subtitle: 'Niveaux d\'impact, voies d\'autorisation, 3PAO et surveillance continue',
  description:
    "Un parcours entièrement dédié au Federal Risk and Authorization Management Program : ses origines dans l'initiative « Cloud First » et le principe « do once, use many times », la catégorisation par niveaux d'impact (Faible, Modéré, Élevé, LI-SaaS) et les bases de référence de contrôles adaptées au cloud, les deux voies d'autorisation (Agence et FedRAMP Board), les acteurs de l'écosystème et le rôle central du 3PAO, le dispositif de surveillance continue mensuelle et la gestion du POA&M, le FedRAMP Marketplace et le principe de réciprocité, les programmes apparentés (StateRAMP, les niveaux d'impact du Department of Defense), et l'articulation avec le NIST RMF, ISO 27001 et SOC 2 déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Origines (Cloud First, OMB), le principe « do once, use many times », et l\'élargissement légal du programme.',
      lessons: [
        { slug: 'introduction', title: 'FedRAMP en profondeur : introduction et repères', minutes: 11 },
      ],
    },
    {
      slug: 'niveaux-impact',
      title: 'Module 1 — Catégorisation par niveaux d\'impact',
      description: 'FIPS 199 appliqué au cloud, les bases de référence Faible/Modéré/Élevé, et FedRAMP Tailored (LI-SaaS).',
      lessons: [
        { slug: 'fips199-categorisation', title: 'La catégorisation par niveaux d\'impact (1/2) : FIPS 199 appliqué au cloud', minutes: 12 },
        { slug: 'baselines-overlays', title: 'La catégorisation par niveaux d\'impact (2/2) : bases de référence et adaptations cloud', minutes: 12 },
      ],
    },
    {
      slug: 'voies-autorisation',
      title: 'Module 2 — Les voies d\'autorisation',
      description: 'La voie Agence et la voie du FedRAMP Board (P-ATO), leurs avantages et limites respectifs.',
      lessons: [
        { slug: 'agency-ato', title: 'Les voies d\'autorisation (1/2) : la voie Agence', minutes: 12 },
        { slug: 'jab-p-ato', title: 'Les voies d\'autorisation (2/2) : le FedRAMP Board et l\'autorisation provisoire', minutes: 12 },
      ],
    },
    {
      slug: 'acteurs',
      title: 'Module 3 — Acteurs et écosystème',
      description: 'CSP, agence sponsor, 3PAO, ISSO et FedRAMP PMO.',
      lessons: [
        { slug: 'acteurs-3pao', title: 'Acteurs et écosystème : le rôle central du 3PAO', minutes: 12 },
      ],
    },
    {
      slug: 'surveillance-continue',
      title: 'Module 4 — La surveillance continue',
      description: 'Livrables mensuels, POA&M, échéances de remédiation, et Significant Change Requests.',
      lessons: [
        { slug: 'surveillance-continue', title: 'La surveillance continue (1/2) : un rythme mensuel', minutes: 12 },
        { slug: 'poam-changements', title: 'La surveillance continue (2/2) : le POA&M et les changements significatifs', minutes: 12 },
      ],
    },
    {
      slug: 'marketplace-reciprocite',
      title: 'Module 5 — Le FedRAMP Marketplace et la réciprocité',
      description: 'Le registre public des autorisations, et comment il concrétise le principe de réciprocité.',
      lessons: [
        { slug: 'marketplace-reciprocite', title: 'Le FedRAMP Marketplace et le principe de réciprocité', minutes: 11 },
      ],
    },
    {
      slug: 'programmes-apparentes',
      title: 'Module 6 — Programmes apparentés',
      description: 'StateRAMP et les niveaux d\'impact du Department of Defense (DoD IL2 à IL6).',
      lessons: [
        { slug: 'programmes-apparentes', title: 'Les programmes apparentés : StateRAMP et les niveaux d\'impact du DoD', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'FedRAMP face aux autres référentiels de cette plateforme, pièges fréquents, et feuille de route d\'autorisation.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'FedRAMP face aux autres référentiels, et une feuille de route de mise en conformité', minutes: 13 },
      ],
    },
  ],
}
