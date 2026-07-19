import type { Course } from '../types'

export const nistAiRmf: Course = {
  slug: 'nist-ai-rmf',
  title: 'NIST AI RMF en profondeur',
  subtitle: 'Le risque sociotechnique de l\'IA, Govern-Map-Measure-Manage, et l\'IA digne de confiance',
  description:
    "Un parcours entièrement dédié au NIST AI Risk Management Framework : la nature sociotechnique et émergente du risque IA, le cycle de vie étendu des systèmes d'intelligence artificielle et les sept caractéristiques de l'IA digne de confiance, la fonction transversale Govern, la fonction Map et l'établissement du contexte, la fonction Measure et ses méthodes quantitatives et qualitatives (dont les équipes TEVV), la fonction Manage et le traitement du risque, les Profils AI RMF et l'absence délibérée de Tiers, et l'articulation avec le NIST CSF, le NIST Privacy Framework, le RGPD et le règlement européen sur l'IA déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Origines (2023), un troisième cadre volontaire du NIST, et l\'architecture Core à quatre fonctions.',
      lessons: [
        { slug: 'introduction', title: 'NIST AI RMF en profondeur : introduction et repères', minutes: 12 },
      ],
    },
    {
      slug: 'risque-ia',
      title: 'Module 1 — Le risque de l\'IA',
      description: 'La nature sociotechnique du risque, le cycle de vie étendu, et les sept caractéristiques de l\'IA digne de confiance.',
      lessons: [
        { slug: 'risque-sociotechnique-cycle-vie', title: 'Le risque de l\'IA (1/2) : une nature sociotechnique et un cycle de vie étendu', minutes: 13 },
        { slug: 'caracteristiques-ia-digne-de-confiance', title: 'Le risque de l\'IA (2/2) : les caractéristiques de l\'IA digne de confiance', minutes: 13 },
      ],
    },
    {
      slug: 'fonction-govern',
      title: 'Module 2 — La fonction Govern',
      description: 'Une gouvernance transversale plutôt qu\'une étape isolée, et la diversité des parties prenantes.',
      lessons: [
        { slug: 'fonction-govern', title: 'La fonction Govern : une gouvernance transversale plutôt qu\'une étape isolée', minutes: 12 },
      ],
    },
    {
      slug: 'fonction-map',
      title: 'Module 3 — La fonction Map',
      description: 'Établir le contexte, catégoriser le système, et documenter modèles et données d\'entraînement.',
      lessons: [
        { slug: 'fonction-map-contexte', title: 'La fonction Map (1/2) : établir le contexte', minutes: 12 },
        { slug: 'fonction-map-categorisation', title: 'La fonction Map (2/2) : catégoriser et documenter le système', minutes: 12 },
      ],
    },
    {
      slug: 'fonction-measure',
      title: 'Module 4 — La fonction Measure',
      description: 'Méthodes quantitatives et qualitatives, équipes TEVV, et surveillance post-déploiement continue.',
      lessons: [
        { slug: 'fonction-measure-methodes', title: 'La fonction Measure (1/2) : méthodes quantitatives et qualitatives', minutes: 12 },
        { slug: 'fonction-measure-tevv', title: 'La fonction Measure (2/2) : surveillance continue et suivi post-déploiement', minutes: 12 },
      ],
    },
    {
      slug: 'fonction-manage',
      title: 'Module 5 — La fonction Manage',
      description: 'Atténuer, transférer, éviter ou accepter le risque, et le cycle continu Map-Measure-Manage.',
      lessons: [
        { slug: 'fonction-manage', title: 'La fonction Manage : traiter le risque et allouer les ressources', minutes: 12 },
      ],
    },
    {
      slug: 'profils',
      title: 'Module 6 — Les Profils AI RMF',
      description: 'Current/Target Profile par système, et pourquoi l\'AI RMF n\'a délibérément pas repris les Tiers.',
      lessons: [
        { slug: 'profils-ai-rmf', title: 'Les Profils AI RMF : usage et absence délibérée de Tiers', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'Le NIST AI RMF face au NIST CSF/Privacy Framework/RGPD/AI Act, pièges fréquents, et feuille de route.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'Le NIST AI RMF face aux autres référentiels, et une feuille de route de mise en œuvre', minutes: 13 },
      ],
    },
  ],
}
