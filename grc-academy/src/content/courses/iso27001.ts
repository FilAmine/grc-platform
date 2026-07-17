import type { Course } from '../types'
import m0l1 from '../lessons/iso-27001/m0-l1-introduction.md?raw'
import m1l1 from '../lessons/iso-27001/m1-l1-clauses-4-6.md?raw'
import m1l2 from '../lessons/iso-27001/m1-l2-clauses-7-8.md?raw'
import m1l3 from '../lessons/iso-27001/m1-l3-clauses-9-10.md?raw'
import m2l1 from '../lessons/iso-27001/m2-l1-organisationnels-1.md?raw'
import m2l2 from '../lessons/iso-27001/m2-l2-organisationnels-2.md?raw'
import m3l1 from '../lessons/iso-27001/m3-l1-personnes-physiques.md?raw'
import m4l1 from '../lessons/iso-27001/m4-l1-technologiques-1.md?raw'
import m4l2 from '../lessons/iso-27001/m4-l2-technologiques-2.md?raw'
import m5l1 from '../lessons/iso-27001/m5-l1-soa.md?raw'
import m6l1 from '../lessons/iso-27001/m6-l1-certification.md?raw'
import m7l1 from '../lessons/iso-27001/m7-l1-maintien-smsi.md?raw'
import m8l1 from '../lessons/iso-27001/m8-l1-feuille-de-route.md?raw'

export const iso27001: Course = {
  slug: 'iso-27001',
  title: 'ISO/IEC 27001 en profondeur',
  subtitle: 'Le SMSI clause par clause, l\'Annexe A contrôle par contrôle, et la certification',
  description:
    "Un parcours entièrement dédié à ISO/IEC 27001:2022 : les clauses 4 à 10 en détail, l'intégralité des 93 contrôles de l'Annexe A organisés par thème, la Déclaration d'Applicabilité, le processus de certification (Stage 1/Stage 2, surveillance, recertification), le maintien du SMSI dans la durée, et une feuille de route réaliste de mise en œuvre.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Origines, révisions de la norme, et distinction avec ISO 27002.',
      lessons: [
        { slug: 'introduction', title: 'ISO 27001 en profondeur : introduction et repères historiques', minutes: 9, content: m0l1 },
      ],
    },
    {
      slug: 'clauses-smsi',
      title: 'Module 1 — Les clauses 4 à 10 du SMSI',
      description: 'Contexte, leadership, planification, support, fonctionnement, évaluation des performances et amélioration.',
      lessons: [
        { slug: 'clauses-4-6', title: 'Clauses 4 à 6 : contexte, leadership et planification', minutes: 13, content: m1l1 },
        { slug: 'clauses-7-8', title: 'Clauses 7 et 8 : support et fonctionnement', minutes: 11, content: m1l2 },
        { slug: 'clauses-9-10', title: 'Clauses 9 et 10 : évaluation des performances et amélioration', minutes: 12, content: m1l3 },
      ],
    },
    {
      slug: 'controles-organisationnels',
      title: 'Module 2 — Contrôles organisationnels (Annexe A)',
      description: 'Les 37 contrôles organisationnels : politiques, rôles, actifs, fournisseurs, incidents, continuité, conformité.',
      lessons: [
        { slug: 'organisationnels-1', title: 'Contrôles organisationnels (1/2) : politiques, rôles, actifs et tiers', minutes: 12, content: m2l1 },
        { slug: 'organisationnels-2', title: 'Contrôles organisationnels (2/2) : incidents, continuité et conformité', minutes: 11, content: m2l2 },
      ],
    },
    {
      slug: 'controles-personnes-physiques',
      title: 'Module 3 — Contrôles liés aux personnes et physiques (Annexe A)',
      description: 'Les 8 contrôles liés aux personnes et les 14 contrôles physiques.',
      lessons: [
        { slug: 'personnes-physiques', title: 'Contrôles liés aux personnes et contrôles physiques', minutes: 12, content: m3l1 },
      ],
    },
    {
      slug: 'controles-technologiques',
      title: 'Module 4 — Contrôles technologiques (Annexe A)',
      description: 'Les 34 contrôles technologiques : accès, cryptographie, réseau, développement sécurisé, surveillance.',
      lessons: [
        { slug: 'technologiques-1', title: 'Contrôles technologiques (1/2) : accès, cryptographie, terminaux et réseau', minutes: 12, content: m4l1 },
        { slug: 'technologiques-2', title: 'Contrôles technologiques (2/2) : développement sécurisé et surveillance', minutes: 12, content: m4l2 },
      ],
    },
    {
      slug: 'declaration-applicabilite',
      title: 'Module 5 — La Déclaration d\'Applicabilité',
      description: 'Le document central qui relie risques et contrôles.',
      lessons: [
        { slug: 'soa', title: 'La Déclaration d\'Applicabilité (SoA) en profondeur', minutes: 10, content: m5l1 },
      ],
    },
    {
      slug: 'certification',
      title: 'Module 6 — Le processus de certification',
      description: 'Accréditation, Stage 1/Stage 2, cycle triennal, multi-sites et systèmes intégrés.',
      lessons: [
        { slug: 'certification', title: 'Le processus de certification : audits, accréditation et cycle triennal', minutes: 12, content: m6l1 },
      ],
    },
    {
      slug: 'maintien',
      title: 'Module 7 — Maintenir le SMSI dans la durée',
      description: 'Programme d\'audit interne, revue de direction, non-conformités, indicateurs de maturité.',
      lessons: [
        { slug: 'maintien-smsi', title: 'Maintenir et améliorer le SMSI dans la durée', minutes: 11, content: m7l1 },
      ],
    },
    {
      slug: 'feuille-de-route',
      title: 'Module 8 — Feuille de route de mise en œuvre',
      description: 'Phases d\'un projet de première certification, durée typique, pièges de planification.',
      lessons: [
        { slug: 'feuille-de-route', title: 'Construire une feuille de route réaliste vers la certification', minutes: 11, content: m8l1 },
      ],
    },
  ],
}
