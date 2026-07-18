import type { Course } from '../types'

export const itil: Course = {
  slug: 'itil',
  title: 'ITIL en profondeur',
  subtitle: 'Le Service Value System, la chaîne de valeur des services, et les 34 pratiques',
  description:
    "Un parcours entièrement dédié à ITIL 4, complément opérationnel naturel de COBIT déjà étudié dans cette plateforme : le Service Value System et les quatre dimensions de la gestion des services, les sept principes directeurs, la chaîne de valeur des services et la notion de flux de valeur, les trente-quatre pratiques (dont la gestion des incidents, des problèmes, le centre de services et la gestion des demandes de service), la facilitation des changements (Change Enablement), la gestion des niveaux de service, le modèle d'amélioration continue, et le mapping avec COBIT, ISO/IEC 20000 et les référentiels de sécurité déjà étudiés.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Origines (CCTA), versions (v1 à ITIL 4), gouvernance du référentiel, et lien avec ISO/IEC 20000.',
      lessons: [
        { slug: 'introduction', title: 'ITIL en profondeur : introduction et repères', minutes: 11 },
      ],
    },
    {
      slug: 'service-value-system',
      title: 'Module 1 — Le Service Value System',
      description: 'Les composants du SVS, les quatre dimensions de la gestion des services, et les sept principes directeurs.',
      lessons: [
        { slug: 'service-value-system', title: 'Le Service Value System (1/2) : structure et quatre dimensions', minutes: 12 },
        { slug: 'principes-directeurs', title: 'Le Service Value System (2/2) : les sept principes directeurs', minutes: 12 },
      ],
    },
    {
      slug: 'service-value-chain',
      title: 'Module 2 — La chaîne de valeur des services',
      description: 'Les six activités (Plan, Improve, Engage, Design & Transition, Obtain/Build, Deliver & Support) et les flux de valeur.',
      lessons: [
        { slug: 'service-value-chain', title: 'La Service Value Chain : le modèle opérationnel central', minutes: 12 },
      ],
    },
    {
      slug: 'pratiques',
      title: 'Module 3 — Les 34 pratiques',
      description: 'Les trois catégories de pratiques, et un focus sur les plus opérationnellement centrales.',
      lessons: [
        { slug: 'pratiques-generales', title: 'Les pratiques d\'ITIL 4 (1/2) : structure et pratiques de management général', minutes: 12 },
        { slug: 'pratiques-operationnelles', title: 'Les pratiques d\'ITIL 4 (2/2) : les pratiques opérationnelles centrales', minutes: 12 },
      ],
    },
    {
      slug: 'change-enablement',
      title: 'Module 4 — La facilitation des changements',
      description: 'Changements standard/normal/urgence, le Change Advisory Board, et l\'articulation avec DevOps.',
      lessons: [
        { slug: 'change-enablement', title: 'La facilitation des changements (Change Enablement)', minutes: 12 },
      ],
    },
    {
      slug: 'niveaux-de-service',
      title: 'Module 5 — Gestion des niveaux de service et autres pratiques',
      description: 'SLA, disponibilité, capacité, continuité, surveillance, mises en production et configuration.',
      lessons: [
        { slug: 'niveaux-de-service', title: 'La gestion des niveaux de service et autres pratiques clés', minutes: 12 },
      ],
    },
    {
      slug: 'amelioration-continue',
      title: 'Module 6 — Le modèle d\'amélioration continue',
      description: 'Les six questions du modèle, et le registre d\'amélioration continue (CIR).',
      lessons: [
        { slug: 'amelioration-continue', title: 'Le modèle d\'amélioration continue', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping, certifications et feuille de route',
      description: 'ITIL face à COBIT/ISO 20000/DevOps, le schéma de certification, et une feuille de route d\'adoption.',
      lessons: [
        { slug: 'mapping-certifications', title: 'ITIL face aux autres référentiels, et les certifications professionnelles', minutes: 12 },
        { slug: 'feuille-de-route', title: 'Construire une feuille de route réaliste d\'adoption d\'ITIL', minutes: 12 },
      ],
    },
  ],
}
