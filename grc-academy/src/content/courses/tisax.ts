import type { Course } from '../types'

export const tisax: Course = {
  slug: 'tisax',
  title: 'TISAX en profondeur',
  subtitle: 'Le catalogue VDA ISA, les niveaux de maturité, et le partage par consentement',
  description:
    "Un parcours entièrement dédié au Trusted Information Security Assessment Exchange : ses origines dans l'industrie automobile européenne (VDA, ENX Association) et le besoin de mutualiser les audits entre OEM et fournisseurs, le catalogue VDA ISA et son modèle de maturité à six niveaux, les niveaux d'évaluation (AL1/AL2/AL3) et les trois objectifs d'évaluation modulaires (sécurité de l'information, protection des prototypes, protection des données), le processus d'évaluation et le rôle des Audit Providers accrédités, le mécanisme de partage des labels par consentement explicite sur le portail ENX et leur durée de validité, le module unique de protection des prototypes, les enjeux contractuels et l'absence de sanction légale directe, et l'articulation avec ISO 27001, PCI DSS et le RGPD déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Origines (VDA, ENX Association), le principe de mutualisation des audits, et le catalogue VDA ISA.',
      lessons: [
        { slug: 'introduction', title: 'TISAX en profondeur : introduction et repères', minutes: 11 },
      ],
    },
    {
      slug: 'catalogue-maturite',
      title: 'Module 1 — Le catalogue VDA ISA et les niveaux de maturité',
      description: 'Structure du catalogue, ses modules spécifiques, et l\'échelle de maturité 0 à 5.',
      lessons: [
        { slug: 'catalogue-vda-isa', title: 'Le catalogue VDA ISA et les niveaux de maturité (1/2) : structure du catalogue', minutes: 12 },
        { slug: 'niveaux-maturite', title: 'Le catalogue VDA ISA et les niveaux de maturité (2/2) : l\'échelle de maturité 0 à 5', minutes: 12 },
      ],
    },
    {
      slug: 'niveaux-objectifs',
      title: 'Module 2 — Niveaux d\'évaluation et objectifs',
      description: 'Assessment Levels (AL1/AL2/AL3) et les trois objectifs d\'évaluation modulaires.',
      lessons: [
        { slug: 'assessment-levels', title: 'Les niveaux d\'évaluation et les objectifs (1/2) : Assessment Levels et besoins de protection', minutes: 12 },
        { slug: 'modules-objectifs', title: 'Les niveaux d\'évaluation et les objectifs (2/2) : les objectifs d\'évaluation modulaires', minutes: 12 },
      ],
    },
    {
      slug: 'processus-audit-providers',
      title: 'Module 3 — Le processus d\'évaluation',
      description: 'Enregistrement sur le portail ENX, et le rôle central des Audit Providers accrédités.',
      lessons: [
        { slug: 'processus-audit-providers', title: 'Le processus d\'évaluation et le rôle des Audit Providers', minutes: 12 },
      ],
    },
    {
      slug: 'partage-resultats',
      title: 'Module 4 — Le partage des résultats',
      description: 'Labels, consentement explicite sur le portail ENX, durée de validité et renouvellement.',
      lessons: [
        { slug: 'partage-labels', title: 'Le partage des résultats (1/2) : labels et consentement explicite', minutes: 12 },
        { slug: 'validite-renouvellement', title: 'Le partage des résultats (2/2) : durée de validité et renouvellement', minutes: 12 },
      ],
    },
    {
      slug: 'protection-prototypes',
      title: 'Module 5 — La protection des prototypes',
      description: 'Un module physique et organisationnel sans équivalent dans les référentiels généralistes.',
      lessons: [
        { slug: 'protection-prototypes', title: 'La protection des prototypes : un module sans équivalent dans les référentiels généralistes', minutes: 12 },
      ],
    },
    {
      slug: 'enjeux-contractuels',
      title: 'Module 6 — Enjeux contractuels',
      description: 'L\'absence de sanction légale directe, et la sanction bien réelle de la perte d\'accès au marché.',
      lessons: [
        { slug: 'enjeux-contractuels', title: 'Les enjeux contractuels et l\'absence de sanction légale directe', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'TISAX face aux autres référentiels de cette plateforme, pièges fréquents, et feuille de route.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'TISAX face aux autres référentiels, et une feuille de route de mise en conformité', minutes: 13 },
      ],
    },
  ],
}
