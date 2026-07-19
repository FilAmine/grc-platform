import type { Course } from '../types'

export const nistPrivacy: Course = {
  slug: 'nist-privacy',
  title: 'NIST Privacy Framework en profondeur',
  subtitle: 'Le modèle de risque vie privée, le Core en cinq fonctions, et le pont avec le NIST CSF',
  description:
    "Un parcours entièrement dédié au NIST Privacy Framework : le modèle de risque vie privée et sa distinction fondamentale avec le risque de sécurité, la chaîne data action / problematic data action / préjudice et sa méthodologie d'appréciation, les cinq fonctions du Core (Govern-P, Identify-P, Control-P, Communicate-P, Protect-P comme pont explicite vers le NIST CSF), les Profils et les Implementation Tiers, la gestion des risques de l'écosystème de traitement des données, l'ingénierie de la vie privée comme aboutissement opérationnel du Privacy by Design, et l'articulation avec le NIST CSF, le RGPD et ISO/IEC 27701 déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Origines (2020, compagnon du NIST CSF), et pourquoi un cadre séparé de la sécurité était nécessaire.',
      lessons: [
        { slug: 'introduction', title: 'NIST Privacy Framework en profondeur : introduction et repères', minutes: 11 },
      ],
    },
    {
      slug: 'modele-risque',
      title: 'Module 1 — Le modèle de risque vie privée',
      description: 'La distinction risque vie privée / risque de sécurité, les data actions, et la méthodologie d\'appréciation.',
      lessons: [
        { slug: 'risque-vie-privee-data-actions', title: 'Le modèle de risque vie privée (1/2) : distinguer le risque vie privée du risque de sécurité', minutes: 13 },
        { slug: 'methodologie-appreciation-risque', title: 'Le modèle de risque vie privée (2/2) : méthodologie d\'appréciation du risque', minutes: 12 },
      ],
    },
    {
      slug: 'core-govern-identify',
      title: 'Module 2 — Le Core : Govern-P et Identify-P',
      description: 'Structure générale du Core, la gouvernance de la vie privée et la cartographie des données.',
      lessons: [
        { slug: 'core-govern-identify', title: 'Le Core : structure générale, Govern-P et Identify-P', minutes: 13 },
      ],
    },
    {
      slug: 'core-control-communicate-protect',
      title: 'Module 3 — Le Core : Control-P, Communicate-P et Protect-P',
      description: 'La capacité d\'action sur les données, la transparence, et le pont explicite vers le NIST CSF.',
      lessons: [
        { slug: 'control-communicate', title: 'Le Core (2/3) : Control-P et Communicate-P', minutes: 12 },
        { slug: 'protect-pont-csf', title: 'Le Core (3/3) : Protect-P, le pont explicite vers le NIST CSF', minutes: 12 },
      ],
    },
    {
      slug: 'profils-tiers',
      title: 'Module 4 — Profils et Implementation Tiers',
      description: 'Current/Target Profile, l\'analyse d\'écarts, et les quatre Implementation Tiers.',
      lessons: [
        { slug: 'profils', title: 'Les Profils : Current, Target et l\'analyse d\'écarts', minutes: 12 },
        { slug: 'tiers', title: 'Les Implementation Tiers : caractériser la rigueur de la gestion du risque vie privée', minutes: 12 },
      ],
    },
    {
      slug: 'ecosysteme',
      title: 'Module 5 — L\'écosystème de traitement des données',
      description: 'La gestion du risque vie privée posé par les prestataires tiers (Data Processing Ecosystem Risk Management).',
      lessons: [
        { slug: 'ecosysteme-traitement-donnees', title: 'La gestion des risques de l\'écosystème de traitement des données', minutes: 12 },
      ],
    },
    {
      slug: 'ingenierie-vie-privee',
      title: 'Module 6 — L\'ingénierie de la vie privée',
      description: 'Le retour sur le Privacy by Design, désormais outillé par une méthodologie opérationnelle précise.',
      lessons: [
        { slug: 'ingenierie-vie-privee', title: 'L\'ingénierie de la vie privée et le retour sur le Privacy by Design', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'Le NIST Privacy Framework face au NIST CSF/RGPD/ISO 27701, pièges fréquents, et feuille de route.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'Le NIST Privacy Framework face aux autres référentiels, et une feuille de route de mise en œuvre', minutes: 13 },
      ],
    },
  ],
}
