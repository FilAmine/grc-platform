import type { Course } from '../types'

export const cobit: Course = {
  slug: 'cobit',
  title: 'COBIT en profondeur',
  subtitle: 'Gouvernance et gestion de l\'IT : le cadre-cible au-dessus des référentiels spécialisés',
  description:
    "Un parcours entièrement dédié à COBIT : la distinction fondatrice entre gouvernance et management et la cascade des objectifs, les cinq domaines et les quarante objectifs de gouvernance et de management (EDM, APO, BAI, DSS, MEA), les sept composants génériques qui réalisent chaque objectif, les facteurs de conception et les Focus Areas qui adaptent le référentiel au contexte de l'entreprise, le modèle de niveaux de capacité aligné sur CMMI, et la position de COBIT comme cadre-cible au-dessus d'ISO 27001, ITIL et des autres référentiels déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Origines (ISACA, 1996), évolution vers COBIT 2019, la distinction gouvernance/management, COBIT comme cadre-cible.',
      lessons: [
        { slug: 'introduction', title: 'COBIT en profondeur : introduction et repères', minutes: 10 },
      ],
    },
    {
      slug: 'gouvernance-management-cascade',
      title: 'Module 1 — Gouvernance, management et cascade des objectifs',
      description: 'EDM vs les domaines de management, et la traduction de la stratégie d\'entreprise en objectifs IT concrets.',
      lessons: [
        { slug: 'gouvernance-management', title: 'Gouvernance et management : la distinction fondatrice', minutes: 12 },
        { slug: 'cascade-objectifs', title: 'La cascade des objectifs', minutes: 12 },
      ],
    },
    {
      slug: 'domaines-objectifs',
      title: 'Module 2 — Les cinq domaines et les quarante objectifs',
      description: 'EDM, APO, BAI, DSS et MEA en détail, avec un focus sur APO13/DSS05 (sécurité).',
      lessons: [
        { slug: 'domaine-apo', title: 'Les cinq domaines et les quarante objectifs (1/3) : APO — Aligner, Planifier et Organiser', minutes: 12 },
        { slug: 'domaine-bai', title: 'Les cinq domaines et les quarante objectifs (2/3) : BAI — Construire, Acquérir et Implémenter', minutes: 12 },
        { slug: 'domaines-dss-mea', title: 'Les cinq domaines et les quarante objectifs (3/3) : DSS et MEA', minutes: 12 },
      ],
    },
    {
      slug: 'composants',
      title: 'Module 3 — Les composants d\'un système de gouvernance',
      description: 'Les sept composants génériques (processus, structures, politiques, information, culture, personnes, infrastructures).',
      lessons: [
        { slug: 'composants', title: 'Les composants d\'un système de gouvernance', minutes: 12 },
      ],
    },
    {
      slug: 'facteurs-conception',
      title: 'Module 4 — Facteurs de conception et Focus Areas',
      description: 'Adapter le référentiel générique au contexte propre de chaque entreprise.',
      lessons: [
        { slug: 'facteurs-conception', title: 'Facteurs de conception et Focus Areas', minutes: 12 },
      ],
    },
    {
      slug: 'niveaux-capacite',
      title: 'Module 5 — Niveaux de capacité et gestion de la performance',
      description: 'Le modèle aligné sur CMMI, et la distinction entre capacité et performance.',
      lessons: [
        { slug: 'niveaux-capacite', title: 'Niveaux de capacité et gestion de la performance', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-certifications',
      title: 'Module 6 — Face aux autres référentiels, et certifications',
      description: 'COBIT comme cadre-cible au-dessus d\'ISO 27001/ITIL/PMI, et les certifications ISACA (CGEIT...).',
      lessons: [
        { slug: 'mapping-certifications', title: 'COBIT face aux autres référentiels, et les certifications professionnelles', minutes: 12 },
      ],
    },
    {
      slug: 'feuille-de-route',
      title: 'Module 7 — Feuille de route d\'adoption',
      description: 'Les étapes typiques d\'une démarche d\'adoption, et les pièges les plus fréquents.',
      lessons: [
        { slug: 'feuille-de-route', title: 'Construire une feuille de route réaliste d\'adoption de COBIT', minutes: 12 },
      ],
    },
  ],
}
