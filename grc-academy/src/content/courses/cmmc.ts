import type { Course } from '../types'

export const cmmc: Course = {
  slug: 'cmmc',
  title: 'CMMC en profondeur',
  subtitle: 'Les trois niveaux, NIST SP 800-171, le C3PAO et la cascade dans la base industrielle de défense',
  description:
    "Un parcours entièrement dédié à la Cybersecurity Maturity Model Certification : ses origines dans l'échec du modèle d'auto-attestation pure face aux pertes majeures d'informations sensibles de la base industrielle de défense américaine, les trois niveaux de certification (Foundational, Advanced, Expert), le catalogue NIST SP 800-171 et les pratiques renforcées de SP 800-172, les voies d'évaluation (auto-évaluation, C3PAO, évaluation gouvernementale par le DIBCAC), le Plan of Action and Milestones et son encadrement strict, la cascade des exigences à travers la chaîne d'approvisionnement de la défense et le Supplier Performance Risk System, la clause DFARS 252.204-7012 et la notification des incidents, et l'articulation avec le NIST RMF, FedRAMP et ISO 27001 déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'L\'échec de l\'auto-attestation pure, la création de CMMC, et la gouvernance du Cyber-AB.',
      lessons: [
        { slug: 'introduction', title: 'CMMC en profondeur : introduction et repères', minutes: 12 },
      ],
    },
    {
      slug: 'niveaux',
      title: 'Module 1 — Les trois niveaux de CMMC 2.0',
      description: 'Niveau 1 Foundational (FCI), et niveaux 2/3 Advanced/Expert (CUI).',
      lessons: [
        { slug: 'niveau-1-foundational', title: 'Les trois niveaux de CMMC 2.0 (1/2) : le niveau Foundational', minutes: 12 },
        { slug: 'niveaux-2-3-advanced-expert', title: 'Les trois niveaux de CMMC 2.0 (2/2) : les niveaux Advanced et Expert', minutes: 12 },
      ],
    },
    {
      slug: 'catalogue-sp800-171',
      title: 'Module 2 — Le catalogue NIST SP 800-171',
      description: 'Structure et quatorze familles, un exemple concret, et les pratiques renforcées de SP 800-172.',
      lessons: [
        { slug: 'catalogue-sp800-171-structure', title: 'Le catalogue NIST SP 800-171 (1/2) : structure et quatorze familles', minutes: 12 },
        { slug: 'exemple-concret-sp800-172', title: 'Le catalogue NIST SP 800-171 (2/2) : un exemple concret et les pratiques renforcées de SP 800-172', minutes: 12 },
      ],
    },
    {
      slug: 'voies-evaluation',
      title: 'Module 3 — Les voies d\'évaluation',
      description: 'Auto-évaluation avec affirmation signée ; C3PAO et évaluation gouvernementale par le DIBCAC.',
      lessons: [
        { slug: 'auto-evaluation', title: 'Les voies d\'évaluation (1/2) : l\'auto-évaluation', minutes: 12 },
        { slug: 'c3pao-dibcac', title: 'Les voies d\'évaluation (2/2) : le C3PAO et l\'évaluation gouvernementale', minutes: 12 },
      ],
    },
    {
      slug: 'poam',
      title: 'Module 4 — Le POA&M et la certification conditionnelle',
      description: 'Score minimal préalable, pratiques jamais éligibles, et délai de remédiation strictement limité.',
      lessons: [
        { slug: 'poam-certification-conditionnelle', title: 'Le Plan of Action and Milestones et la certification conditionnelle', minutes: 12 },
      ],
    },
    {
      slug: 'flow-down',
      title: 'Module 5 — La cascade dans la chaîne d\'approvisionnement',
      description: 'Le flow-down contractuel, le Supplier Performance Risk System, et la responsabilité du maître d\'œuvre.',
      lessons: [
        { slug: 'flow-down-sprs', title: 'La cascade dans la chaîne d\'approvisionnement et le SPRS', minutes: 12 },
      ],
    },
    {
      slug: 'dfars',
      title: 'Module 6 — DFARS 252.204-7012',
      description: 'La clause contractuelle préexistante, la notification en 72 heures, et la préservation des preuves.',
      lessons: [
        { slug: 'dfars-notification-incidents', title: 'DFARS 252.204-7012 et la notification des incidents', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'CMMC face au NIST RMF/FedRAMP/ISO 27001, pièges fréquents, et feuille de route.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'CMMC face aux autres référentiels, et une feuille de route de mise en conformité', minutes: 13 },
      ],
    },
  ],
}
