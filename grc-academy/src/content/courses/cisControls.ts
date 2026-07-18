import type { Course } from '../types'

export const cisControls: Course = {
  slug: 'cis-controls',
  title: 'CIS Controls en profondeur',
  subtitle: 'Les 18 contrôles, les Implementation Groups, et l\'écosystème CIS',
  description:
    "Un parcours entièrement dédié aux CIS Controls : leurs origines (Consensus Audit Guidelines, SANS Top 20, transfert au CIS), la structure des 18 contrôles et de leurs 153 Safeguards, le système de priorisation par Implementation Groups (IG1/IG2/IG3), l'écosystème CIS au-delà des Controls (Benchmarks, CIS RAM), le mapping avec les autres référentiels, et une feuille de route réaliste de première adoption.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Origines (Consensus Audit Guidelines, SANS Top 20), transfert au CIS, versions et philosophie.',
      lessons: [
        { slug: 'introduction', title: 'CIS Controls en profondeur : introduction et repères', minutes: 10 },
      ],
    },
    {
      slug: 'les-18-controles',
      title: 'Module 1 — Les 18 contrôles',
      description: 'Structure (Contrôles et Safeguards, attributs) et détail des 18 contrôles par groupes de six.',
      lessons: [
        { slug: 'structure', title: 'La structure des CIS Controls v8 : contrôles, Safeguards et attributs', minutes: 11 },
        { slug: 'controles-1-6', title: 'Les 18 contrôles (1/3) : contrôles 1 à 6 — les fondations', minutes: 12 },
        { slug: 'controles-7-12', title: 'Les 18 contrôles (2/3) : contrôles 7 à 12 — le durcissement opérationnel', minutes: 12 },
        { slug: 'controles-13-18', title: 'Les 18 contrôles (3/3) : contrôles 13 à 18 — détection, réponse et maturité', minutes: 12 },
      ],
    },
    {
      slug: 'implementation-groups',
      title: 'Module 2 — Les Implementation Groups',
      description: 'Le système de priorisation IG1/IG2/IG3, et comment choisir son groupe cible.',
      lessons: [
        { slug: 'implementation-groups', title: 'Les Implementation Groups : le système de priorisation intégré', minutes: 12 },
        { slug: 'choisir-son-ig', title: 'Choisir son Implementation Group, et la répartition par fonction de sécurité', minutes: 11 },
      ],
    },
    {
      slug: 'ecosysteme-cis',
      title: 'Module 3 — L\'écosystème CIS',
      description: 'Les CIS Benchmarks (configuration technique) et CIS RAM (justification du caractère raisonnable).',
      lessons: [
        { slug: 'benchmarks', title: 'Les CIS Benchmarks : le niveau de configuration technique précise', minutes: 11 },
        { slug: 'cis-ram', title: 'CIS RAM : justifier le caractère "raisonnable" des Safeguards choisis', minutes: 11 },
      ],
    },
    {
      slug: 'mapping',
      title: 'Module 4 — Face aux autres référentiels',
      description: 'Comparaison et mapping avec NIST CSF, ISO 27001, SOC 2 et le NIST RMF.',
      lessons: [
        { slug: 'mapping', title: 'CIS Controls face aux autres référentiels étudiés dans cette plateforme', minutes: 11 },
      ],
    },
    {
      slug: 'feuille-de-route',
      title: 'Module 5 — Feuille de route de première adoption',
      description: 'Les étapes typiques, pièges fréquents, et l\'articulation avec les autres référentiels.',
      lessons: [
        { slug: 'feuille-de-route', title: 'Construire une feuille de route réaliste avec les CIS Controls', minutes: 11 },
      ],
    },
  ],
}
