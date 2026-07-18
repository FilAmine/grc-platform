import type { Course } from '../types'

export const soc2: Course = {
  slug: 'soc-2',
  title: 'SOC 2 en profondeur',
  subtitle: 'Common Criteria, catégories de confiance, audit et anatomie du rapport',
  description:
    "Un parcours entièrement dédié à SOC 2 : les Common Criteria (CC1 à CC9) alignés sur le référentiel COSO, les cinq catégories de Trust Services Criteria en détail (Sécurité, Disponibilité, Intégrité de traitement, Confidentialité, Vie privée), le déroulement réel d'un audit (méthodes de test, échantillonnage, types d'opinion), l'anatomie complète d'un rapport, la préparation pratique d'un audit, et la distinction avec SOC 1 et SOC 3.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Origines (SAS 70, SSAE 18), attestation vs certification, qui audite un rapport SOC 2.',
      lessons: [
        { slug: 'introduction', title: 'SOC 2 en profondeur : introduction et repères', minutes: 9 },
      ],
    },
    {
      slug: 'common-criteria',
      title: 'Module 1 — Les Common Criteria',
      description: 'CC1 à CC9, alignés sur les cinq composantes du référentiel COSO.',
      lessons: [
        { slug: 'gouvernance', title: 'Les Common Criteria (1/2) : la gouvernance selon COSO', minutes: 12 },
        { slug: 'techniques', title: 'Les Common Criteria (2/2) : les contrôles techniques spécifiques aux Trust Services', minutes: 12 },
      ],
    },
    {
      slug: 'categories-confiance',
      title: 'Module 2 — Les cinq catégories de critères de confiance',
      description: 'Disponibilité, Intégrité de traitement, Confidentialité et Vie privée en détail.',
      lessons: [
        { slug: 'disponibilite-integrite-confidentialite', title: 'Les critères additionnels : Disponibilité, Intégrité de traitement, Confidentialité', minutes: 11 },
        { slug: 'vie-privee', title: 'La catégorie Vie privée (Privacy) en détail', minutes: 11 },
      ],
    },
    {
      slug: 'audit',
      title: 'Module 3 — Le déroulement de l\'audit',
      description: 'Méthodes de test, échantillonnage, exceptions et types d\'opinion.',
      lessons: [
        { slug: 'audit-opinions', title: 'Le déroulement de l\'audit : méthodes de test et types d\'opinion', minutes: 11 },
      ],
    },
    {
      slug: 'anatomie-rapport',
      title: 'Module 4 — Anatomie du rapport',
      description: 'Les sections d\'un rapport SOC 2, les critères de description, CUEC et CSOC.',
      lessons: [
        { slug: 'anatomie-rapport', title: 'Anatomie complète d\'un rapport SOC 2', minutes: 12 },
      ],
    },
    {
      slug: 'preparation',
      title: 'Module 5 — Préparer un audit SOC 2',
      description: 'Cadrage, évaluation de préparation, matrice de contrôles, collecte de preuves.',
      lessons: [
        { slug: 'cadrage-readiness', title: 'Préparer un audit SOC 2 (1/2) : cadrage et évaluation de préparation', minutes: 11 },
        { slug: 'preuves-pieges', title: 'Préparer un audit SOC 2 (2/2) : collecte de preuves et pièges fréquents', minutes: 11 },
      ],
    },
    {
      slug: 'soc1-soc3-mapping',
      title: 'Module 6 — SOC 1, SOC 3 et mapping',
      description: 'La différence avec SOC 1 et SOC 3, les bridge letters, et le mapping avec ISO 27001/NIST CSF.',
      lessons: [
        { slug: 'soc1-soc3-mapping', title: 'SOC 1, SOC 3, bridge letters, et mapping avec d\'autres référentiels', minutes: 12 },
      ],
    },
    {
      slug: 'feuille-de-route',
      title: 'Module 7 — Feuille de route de mise en œuvre',
      description: 'La trajectoire Type I puis Type II, durée typique, pièges de planification.',
      lessons: [
        { slug: 'feuille-de-route', title: 'Construire une feuille de route réaliste pour un premier programme SOC 2', minutes: 11 },
      ],
    },
  ],
}
