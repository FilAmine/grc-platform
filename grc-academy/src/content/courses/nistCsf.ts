import type { Course } from '../types'

export const nistCsf: Course = {
  slug: 'nist-csf',
  title: 'NIST Cybersecurity Framework 2.0 — Guide complet',
  subtitle: 'Le Core, les Tiers, les Profils, et la mise en œuvre pas à pas',
  description:
    "Un parcours dédié au NIST CSF 2.0 : ses origines, ses six fonctions (dont la nouvelle fonction Govern), sa structure de catégories et sous-catégories, les Tiers de rigueur, les Profils et l'analyse d'écarts, le processus de mise en œuvre en sept étapes, et son articulation avec ISO 27001, SOC 2 et la gestion des risques de la chaîne d'approvisionnement.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: "Origines, versions et philosophie du cadre.",
      lessons: [
        { slug: 'origines-philosophie', title: 'NIST CSF : origines et philosophie', minutes: 9 },
      ],
    },
    {
      slug: 'les-six-fonctions',
      title: 'Module 1 — Les six fonctions du Core',
      description: 'Govern, Identify, Protect, Detect, Respond et Recover, en détail.',
      lessons: [
        { slug: 'govern', title: 'La fonction Govern : la nouveauté structurante de CSF 2.0', minutes: 11 },
        { slug: 'identify', title: 'La fonction Identify : savoir ce qu\'on protège', minutes: 10 },
        { slug: 'protect', title: 'La fonction Protect : les mesures de sauvegarde', minutes: 11 },
        { slug: 'detect', title: 'La fonction Detect : identifier qu\'un événement se produit', minutes: 9 },
        { slug: 'respond-recover', title: 'Les fonctions Respond et Recover : contenir et rebondir', minutes: 10 },
      ],
    },
    {
      slug: 'structure-du-core',
      title: 'Module 2 — Catégories, sous-catégories et références informatives',
      description: 'Lire le Core, les identifiants de sous-catégories, et le mapping vers d\'autres référentiels.',
      lessons: [
        { slug: 'categories-references', title: 'Catégories, sous-catégories et références informatives : lire le Core', minutes: 9 },
      ],
    },
    {
      slug: 'tiers-et-profils',
      title: 'Module 3 — Tiers et Profils',
      description: 'Caractériser la rigueur de la gestion des risques, et prioriser les résultats à atteindre.',
      lessons: [
        { slug: 'tiers', title: 'Les Tiers : caractériser la rigueur de la gestion des risques', minutes: 9 },
        { slug: 'profils', title: 'Les Profils : Current, Target, Community, et l\'analyse d\'écarts', minutes: 10 },
      ],
    },
    {
      slug: 'mise-en-oeuvre',
      title: 'Module 4 — Mise en œuvre et articulation avec les autres référentiels',
      description: 'Le processus en sept étapes, et le mapping avec ISO 27001/SOC 2 et la chaîne d\'approvisionnement.',
      lessons: [
        { slug: 'etapes-mise-en-oeuvre', title: 'Mettre en œuvre le CSF : les sept étapes', minutes: 11 },
        { slug: 'mapping-supply-chain', title: 'Le CSF face aux autres référentiels, et l\'approfondissement de la chaîne d\'approvisionnement', minutes: 11 },
      ],
    },
  ],
}
