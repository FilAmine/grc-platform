import type { Course } from '../types'

export const ebiosRm: Course = {
  slug: 'ebios-rm',
  title: 'ANSSI et EBIOS RM en profondeur',
  subtitle: 'La méthode française de gestion des risques, par scénarios et sources de risque',
  description:
    "Un parcours entièrement dédié à l'ANSSI et à sa méthode EBIOS Risk Manager : le rôle institutionnel de l'agence (prévention, défense, réglementation), les cinq ateliers d'EBIOS RM (cadrage et socle de sécurité, sources de risque et objectifs visés, scénarios stratégiques et cartographie de l'écosystème, scénarios opérationnels, traitement du risque et plan d'amélioration continue), l'écosystème de qualifications et certifications de l'ANSSI (PASSI, PDIS, PRIS, SecNumCloud, CSPN), le régime français des Opérateurs d'Importance Vitale comme précurseur de NIS2, le CERT-FR, et l'articulation d'EBIOS RM avec ISO 31000/27005 et le NIST RMF.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'L\'ANSSI (missions, CERT-FR, précurseur de NIS2), et d\'EBIOS à EBIOS RM.',
      lessons: [
        { slug: 'introduction', title: 'ANSSI et EBIOS RM en profondeur : introduction et repères', minutes: 11 },
      ],
    },
    {
      slug: 'atelier-1',
      title: 'Module 1 — Atelier 1 : cadrage et socle de sécurité',
      description: 'Valeurs métier, biens supports, événements redoutés, et le socle de sécurité de référence.',
      lessons: [
        { slug: 'cadrage', title: 'Atelier 1 (1/2) : cadrage, valeurs métier et événements redoutés', minutes: 12 },
        { slug: 'socle-securite', title: 'Atelier 1 (2/2) : le socle de sécurité', minutes: 12 },
      ],
    },
    {
      slug: 'atelier-2',
      title: 'Module 2 — Atelier 2 : sources de risque',
      description: 'Sources de risque (SR), objectifs visés (OV), et la priorisation des couples SR/OV.',
      lessons: [
        { slug: 'sources-de-risque', title: 'Atelier 2 : les sources de risque et leurs objectifs visés', minutes: 12 },
      ],
    },
    {
      slug: 'atelier-3',
      title: 'Module 3 — Atelier 3 : scénarios stratégiques et écosystème',
      description: 'La cartographie de l\'écosystème comme vecteur d\'attaque, et la construction des scénarios stratégiques.',
      lessons: [
        { slug: 'scenarios-strategiques', title: 'Atelier 3 : scénarios stratégiques et cartographie de l\'écosystème', minutes: 12 },
      ],
    },
    {
      slug: 'atelier-4',
      title: 'Module 4 — Atelier 4 : scénarios opérationnels',
      description: 'La traduction technique des scénarios stratégiques, et l\'évaluation de la vraisemblance.',
      lessons: [
        { slug: 'scenarios-operationnels', title: 'Atelier 4 : les scénarios opérationnels', minutes: 12 },
      ],
    },
    {
      slug: 'atelier-5',
      title: 'Module 5 — Atelier 5 : traitement du risque',
      description: 'Les options de traitement, le PACS, et l\'acceptation formelle du risque résiduel.',
      lessons: [
        { slug: 'traitement-du-risque', title: 'Atelier 5 : traitement du risque et amélioration continue', minutes: 12 },
      ],
    },
    {
      slug: 'ecosysteme-anssi',
      title: 'Module 6 — L\'écosystème ANSSI',
      description: 'Qualifications (PASSI/PDIS/PRIS), SecNumCloud, le régime OIV/LPM, NIS2, et le CERT-FR.',
      lessons: [
        { slug: 'qualifications-certifications', title: 'L\'écosystème ANSSI (1/2) : qualifications et certifications', minutes: 12 },
        { slug: 'lpm-nis2-certfr', title: 'L\'écosystème ANSSI (2/2) : le régime LPM/OIV, le rôle dans NIS2, et le CERT-FR', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'EBIOS RM face à ISO 31000/27005 et au NIST RMF, et une feuille de route de première étude.',
      lessons: [
        { slug: 'mapping', title: 'EBIOS RM face aux autres méthodologies de gestion des risques', minutes: 12 },
        { slug: 'feuille-de-route', title: 'Construire une feuille de route réaliste pour une première étude EBIOS RM', minutes: 12 },
      ],
    },
  ],
}
