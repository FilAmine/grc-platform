import type { Course } from '../types'

export const iso20000: Course = {
  slug: 'iso-20000',
  title: 'ISO/IEC 20000 en profondeur',
  subtitle: 'Le système de management des services, le catalogue de services, et la certification',
  description:
    "Un parcours entièrement dédié à ISO/IEC 20000, refermant la trilogie COBIT/ITIL/ISO 20000 déjà esquissée dans cette plateforme : les clauses 4 à 7 du système de management des services (SMS) alignées sur la High Level Structure, la planification des services et le catalogue de services, les processus de relation avec les clients et les fournisseurs (dont le Service Integration and Management en environnement multi-fournisseurs), la gestion des changements ainsi que la conception, la construction et la transition des services, la résolution des incidents et des problèmes et la satisfaction des demandes de service, les trois piliers de l'assurance du service (disponibilité, continuité, sécurité de l'information), le processus de certification, et l'articulation avec ITIL, COBIT, ISO 27001 et ISO 22301 déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'La voie certifiable de la trilogie COBIT/ITIL/ISO 20000, et la High Level Structure partagée.',
      lessons: [
        { slug: 'introduction', title: 'ISO/IEC 20000 en profondeur : introduction et repères', minutes: 12 },
      ],
    },
    {
      slug: 'clauses-sms',
      title: 'Module 1 — Les clauses 4 à 7 du SMS',
      description: 'Contexte et périmètre (y compris les services fournis par des tiers), leadership, planification et support.',
      lessons: [
        { slug: 'clauses-contexte-leadership', title: 'Les clauses 4 à 7 du SMS (1/2) : contexte et leadership', minutes: 12 },
        { slug: 'clauses-planification-support', title: 'Les clauses 4 à 7 du SMS (2/2) : planification et support', minutes: 12 },
      ],
    },
    {
      slug: 'planification-catalogue',
      title: 'Module 2 — Planification des services et catalogue',
      description: 'Le catalogue de services, la budgétisation, et la gestion de la demande et de la capacité.',
      lessons: [
        { slug: 'planification-catalogue-services', title: 'La planification des services et le catalogue de services', minutes: 12 },
      ],
    },
    {
      slug: 'relations',
      title: 'Module 3 — Les processus de relation',
      description: 'Gestion de la relation métier, gestion des fournisseurs, et le Service Integration and Management (SIAM).',
      lessons: [
        { slug: 'processus-relation-fournisseurs', title: 'Les processus de relation : fournisseurs et parties prenantes métier', minutes: 13 },
      ],
    },
    {
      slug: 'conception-transition',
      title: 'Module 4 — Conception, construction et transition des services',
      description: 'La gestion des changements, et le processus de conception, test et mise en production.',
      lessons: [
        { slug: 'gestion-changements', title: 'La conception, la construction et la transition des services (1/2) : la gestion des changements', minutes: 12 },
        { slug: 'conception-transition-deploiement', title: 'La conception, la construction et la transition des services (2/2) : de la conception au déploiement', minutes: 12 },
      ],
    },
    {
      slug: 'resolution',
      title: 'Module 5 — Résolution et satisfaction des demandes',
      description: 'Incidents, problèmes et demandes de service : trois processus distincts, et le rôle du centre de services.',
      lessons: [
        { slug: 'resolution-satisfaction-demandes', title: 'La résolution des incidents et des problèmes, et la satisfaction des demandes', minutes: 13 },
      ],
    },
    {
      slug: 'assurance',
      title: 'Module 6 — L\'assurance du service',
      description: 'Disponibilité, continuité des services, et sécurité de l\'information appliquée aux services.',
      lessons: [
        { slug: 'assurance-service', title: 'L\'assurance du service', minutes: 12 },
      ],
    },
    {
      slug: 'certification-mapping',
      title: 'Module 7 — Certification et mapping',
      description: 'Le processus de certification, et le mapping avec ITIL/COBIT/ISO 27001/ISO 22301.',
      lessons: [
        { slug: 'certification', title: 'Le processus de certification ISO/IEC 20000', minutes: 12 },
        { slug: 'mapping-feuille-de-route', title: 'ISO/IEC 20000 face aux autres référentiels, et une feuille de route de mise en œuvre', minutes: 13 },
      ],
    },
  ],
}
