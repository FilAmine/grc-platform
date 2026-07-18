import type { Course } from '../types'

export const nistRmf: Course = {
  slug: 'nist-rmf',
  title: 'NIST RMF en profondeur',
  subtitle: 'Le processus d\'autorisation en sept étapes, SP 800-53, et FedRAMP',
  description:
    "Un parcours entièrement dédié au NIST Risk Management Framework : ses origines dans la FISMA, les sept étapes du processus (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor), le catalogue de contrôles SP 800-53 et ses familles les plus structurantes, les rôles nommément désignés (Authorizing Official, ISSO, SAISO...), son application concrète via FedRAMP, l'intégration de la vie privée et de la gestion des risques de la chaîne d'approvisionnement, et une feuille de route réaliste de mise en œuvre.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Origines dans la FISMA, unification des processus antérieurs, la famille de publications NIST.',
      lessons: [
        { slug: 'introduction', title: 'NIST RMF en profondeur : introduction et repères', minutes: 10 },
      ],
    },
    {
      slug: 'sept-etapes',
      title: 'Module 1 — Les sept étapes du RMF',
      description: 'Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor.',
      lessons: [
        { slug: 'prepare-categorize', title: 'Les sept étapes du RMF (1/4) : Prepare et Categorize', minutes: 12 },
        { slug: 'select-implement', title: 'Les sept étapes du RMF (2/4) : Select et Implement', minutes: 12 },
        { slug: 'assess-authorize', title: 'Les sept étapes du RMF (3/4) : Assess et Authorize', minutes: 12 },
        { slug: 'monitor', title: 'Les sept étapes du RMF (4/4) : Monitor', minutes: 11 },
      ],
    },
    {
      slug: 'sp-800-53',
      title: 'Module 2 — Le catalogue SP 800-53',
      description: 'Structure, 20 familles de contrôles, et zoom sur les familles les plus structurantes.',
      lessons: [
        { slug: 'sp80053-structure', title: 'Le catalogue SP 800-53 (1/2) : structure et familles de contrôles', minutes: 11 },
        { slug: 'familles-cles', title: 'Le catalogue SP 800-53 (2/2) : zoom sur les familles les plus structurantes', minutes: 12 },
      ],
    },
    {
      slug: 'roles',
      title: 'Module 3 — Rôles et responsabilités',
      description: 'Authorizing Official, System Owner, ISSO, SAISO, Common Control Provider, évaluateur indépendant.',
      lessons: [
        { slug: 'roles', title: 'Rôles et responsabilités propres au RMF', minutes: 11 },
      ],
    },
    {
      slug: 'fedramp-mapping',
      title: 'Module 4 — RMF face aux autres référentiels, et FedRAMP',
      description: 'Comparaison avec ISO 27001/NIST CSF/SOC 2, et l\'application du RMF au cloud via FedRAMP.',
      lessons: [
        { slug: 'fedramp-mapping', title: 'Le RMF face aux autres référentiels, et son application via FedRAMP', minutes: 12 },
      ],
    },
    {
      slug: 'privacy-supply-chain',
      title: 'Module 5 — Vie privée et chaîne d\'approvisionnement',
      description: 'Le Senior Agency Official for Privacy, la famille PT, la PIA, et la famille SR.',
      lessons: [
        { slug: 'vie-privee', title: 'La vie privée dans le RMF', minutes: 11 },
        { slug: 'supply-chain', title: 'La gestion des risques de la chaîne d\'approvisionnement dans le RMF', minutes: 11 },
      ],
    },
    {
      slug: 'feuille-de-route',
      title: 'Module 6 — Dossier d\'autorisation et feuille de route',
      description: 'Contenu complet d\'un dossier d\'autorisation, durée typique, pièges fréquents, autorisation continue.',
      lessons: [
        { slug: 'feuille-de-route', title: 'Construire un dossier d\'autorisation et une feuille de route réaliste', minutes: 12 },
      ],
    },
  ],
}
