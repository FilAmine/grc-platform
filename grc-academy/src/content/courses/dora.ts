import type { Course } from '../types'

export const dora: Course = {
  slug: 'dora',
  title: 'DORA en profondeur',
  subtitle: 'Résilience opérationnelle numérique du secteur financier',
  description:
    "Un parcours entièrement dédié au règlement DORA : le cadre de gestion des risques liés aux TIC et la responsabilité de l'organe de direction, la classification et la notification des incidents majeurs, les tests de résilience opérationnelle numérique (dont les tests de pénétration fondés sur la menace — TLPT), la gestion des risques liés aux prestataires tiers de services TIC et le régime de supervision directe des prestataires critiques, le partage d'informations et les sanctions, et l'articulation avec NIS2, le RGPD et les référentiels techniques déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Règlement vs directive, périmètre des entités financières, proportionnalité, les cinq piliers.',
      lessons: [
        { slug: 'introduction', title: 'DORA en profondeur : introduction et repères', minutes: 10 },
      ],
    },
    {
      slug: 'cadre-gestion-risques',
      title: 'Module 1 — Le cadre de gestion des risques liés aux TIC',
      description: 'Structure alignée sur le NIST CSF, responsabilité de l\'organe de direction (article 5), exigences spécifiques.',
      lessons: [
        { slug: 'cadre-gestion-risques', title: 'Le cadre de gestion des risques liés aux TIC (1/2) : structure et responsabilité de l\'organe de direction', minutes: 12, },
        { slug: 'exigences-specifiques', title: 'Le cadre de gestion des risques liés aux TIC (2/2) : exigences spécifiques', minutes: 12, },
      ],
    },
    {
      slug: 'incidents',
      title: 'Module 2 — Classification et notification des incidents',
      description: 'La grille de critères de classification, et le processus de notification à trois paliers.',
      lessons: [
        { slug: 'classification-incidents', title: 'La classification des incidents liés aux TIC', minutes: 11, },
        { slug: 'notification-incidents', title: 'La notification des incidents majeurs', minutes: 11, },
      ],
    },
    {
      slug: 'tests-resilience',
      title: 'Module 3 — Tests de résilience opérationnelle numérique',
      description: 'Le programme de tests de base, et les tests de pénétration fondés sur la menace (TLPT).',
      lessons: [
        { slug: 'tests-base', title: 'Les tests de résilience opérationnelle numérique : le programme de base', minutes: 11, },
        { slug: 'tlpt', title: 'Les tests de pénétration fondés sur la menace (TLPT)', minutes: 12, },
      ],
    },
    {
      slug: 'prestataires-tiers',
      title: 'Module 4 — Gestion des risques liés aux prestataires tiers',
      description: 'Exigences contractuelles, registre d\'informations, et supervision directe des prestataires critiques.',
      lessons: [
        { slug: 'prestataires-tiers', title: 'La gestion des risques liés aux prestataires tiers de services TIC', minutes: 12, },
        { slug: 'supervision-prestataires-critiques', title: 'Le régime de supervision directe des prestataires TIC critiques', minutes: 12, },
      ],
    },
    {
      slug: 'partage-sanctions',
      title: 'Module 5 — Partage d\'informations et sanctions',
      description: 'Dispositifs volontaires de partage, supervision sectorielle, et régime de sanctions renvoyé au droit national.',
      lessons: [
        { slug: 'partage-supervision-sanctions', title: 'Partage d\'informations, supervision nationale et sanctions', minutes: 12, },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 6 — Mapping et feuille de route',
      description: 'DORA face à NIS2 (lex specialis), au RGPD et aux référentiels techniques, et une feuille de route.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'DORA face aux autres référentiels, et feuille de route de mise en conformité', minutes: 12, },
      ],
    },
  ],
}
