import type { Course } from '../types'

export const pciDss: Course = {
  slug: 'pci-dss',
  title: 'PCI DSS en profondeur',
  subtitle: 'Les douze exigences, le scoping, et la validation de conformité',
  description:
    "Un parcours entièrement dédié à PCI DSS : son origine contractuelle propre au secteur des paiements par carte (PCI SSC, marques de cartes), les douze exigences organisées en six objectifs de contrôle, le scoping et la segmentation réseau comme leviers de réduction de périmètre, les niveaux de validation et les types de questionnaires d'auto-évaluation (SAQ), le rôle du QSA et des scans ASV, l'approche personnalisée et l'analyse de risque ciblée introduites par la v4.0, la protection des données de titulaires de carte, et le régime de sanctions contractuelles propre à ce référentiel.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Le PCI SSC, la nature contractuelle du référentiel, versions, CDE/CHD/SAD.',
      lessons: [
        { slug: 'introduction', title: 'PCI DSS en profondeur : introduction et repères', minutes: 10 },
      ],
    },
    {
      slug: 'douze-exigences',
      title: 'Module 1 — Les douze exigences',
      description: 'Les six objectifs de contrôle et leurs douze exigences, en détail.',
      lessons: [
        { slug: 'exigences-1-4', title: 'Les douze exigences (1/3) : réseau sécurisé et protection des données de compte', minutes: 12 },
        { slug: 'exigences-5-8', title: 'Les douze exigences (2/3) : gestion des vulnérabilités et contrôle d\'accès', minutes: 12 },
        { slug: 'exigences-9-12', title: 'Les douze exigences (3/3) : surveillance, tests et politique de sécurité', minutes: 12 },
      ],
    },
    {
      slug: 'scoping',
      title: 'Module 2 — Scoping et segmentation réseau',
      description: 'L\'environnement des données de titulaires de cartes (CDE) et les stratégies de réduction du périmètre.',
      lessons: [
        { slug: 'scoping-segmentation', title: 'Scoping et segmentation réseau', minutes: 12 },
      ],
    },
    {
      slug: 'validation-conformite',
      title: 'Module 3 — Validation de conformité',
      description: 'Niveaux de validation, types de SAQ, rôle du QSA et scans ASV.',
      lessons: [
        { slug: 'niveaux-saq', title: 'Validation de conformité (1/2) : niveaux et questionnaires d\'auto-évaluation', minutes: 12 },
        { slug: 'qsa-asv', title: 'Validation de conformité (2/2) : le rôle du QSA et les scans ASV', minutes: 11 },
      ],
    },
    {
      slug: 'approche-personnalisee',
      title: 'Module 4 — L\'approche personnalisée (v4.0)',
      description: 'Approche définie vs personnalisée, et l\'analyse de risque ciblée.',
      lessons: [
        { slug: 'approche-personnalisee', title: 'L\'approche personnalisée et l\'analyse de risque ciblée (nouveautés de la v4.0)', minutes: 12 },
      ],
    },
    {
      slug: 'donnees-sensibles',
      title: 'Module 5 — Protection des données sensibles',
      description: 'Le PAN, la tokenisation, le chiffrement point à point, et l\'interdiction de conservation des SAD.',
      lessons: [
        { slug: 'protection-donnees-sensibles', title: 'La protection des données sensibles en détail : PAN, SAD et tokenisation', minutes: 12 },
      ],
    },
    {
      slug: 'sanctions-mapping',
      title: 'Module 6 — Sanctions et mapping',
      description: 'Le régime de sanctions contractuelles, et la comparaison avec les référentiels génériques.',
      lessons: [
        { slug: 'sanctions-mapping', title: 'Sanctions contractuelles et PCI DSS face aux autres référentiels', minutes: 11 },
      ],
    },
    {
      slug: 'feuille-de-route',
      title: 'Module 7 — Feuille de route de mise en conformité',
      description: 'Les étapes typiques d\'un premier projet, et les pièges les plus fréquents.',
      lessons: [
        { slug: 'feuille-de-route', title: 'Construire une feuille de route réaliste de mise en conformité PCI DSS', minutes: 11 },
      ],
    },
  ],
}
