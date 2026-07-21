import type { Course } from '../types'

export const zeroTrust: Course = {
  slug: 'zero-trust',
  title: 'L\'architecture Zero Trust (NIST SP 800-207) en profondeur',
  subtitle: 'Les sept principes, Policy Engine/Administrator/Enforcement Point, et la migration',
  description:
    "Un parcours entièrement dédié à l'architecture Zero Trust décrite par NIST SP 800-207 : les sept principes fondamentaux qui rompent avec le modèle périmétrique traditionnel (\"château fort et douves\"), l'architecture logique à trois composants (Policy Engine, Policy Administrator, Policy Enforcement Point) et l'algorithme de confiance qui oriente leurs décisions, les quatre approches de déploiement concrètes, la micro-segmentation et le périmètre défini par logiciel, la migration progressive depuis un modèle périmétrique existant, les menaces propres à l'architecture elle-même, le modèle de maturité de la CISA à cinq piliers, et l'articulation avec le NIST CSF, les CIS Controls, FedRAMP, CMMC et DORA déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'L\'échec du modèle périmétrique, le principe "ne jamais faire confiance, toujours vérifier".',
      lessons: [
        { slug: 'introduction', title: 'L\'architecture Zero Trust (NIST SP 800-207) : introduction et repères', minutes: 12 },
      ],
    },
    {
      slug: 'sept-principes',
      title: 'Module 1 — Les sept principes fondamentaux',
      description: 'Toutes les ressources, communication sécurisée, accès sessionnel, politique dynamique, surveillance, authentification stricte, collecte d\'information.',
      lessons: [
        { slug: 'sept-principes-partie1', title: 'Les sept principes fondamentaux (1/2)', minutes: 12 },
        { slug: 'sept-principes-partie2', title: 'Les sept principes fondamentaux (2/2)', minutes: 12 },
      ],
    },
    {
      slug: 'architecture-logique',
      title: 'Module 2 — L\'architecture logique',
      description: 'Policy Engine, Policy Administrator, Policy Enforcement Point, et l\'algorithme de confiance.',
      lessons: [
        { slug: 'architecture-logique-composants', title: 'L\'architecture logique (1/2) : Policy Engine, Policy Administrator, Policy Enforcement Point', minutes: 13 },
        { slug: 'algorithme-confiance', title: 'L\'architecture logique (2/2) : l\'algorithme de confiance et ses sources de données', minutes: 12 },
      ],
    },
    {
      slug: 'approches-deploiement',
      title: 'Module 3 — Les approches de déploiement',
      description: 'Agent/passerelle, enclave, portail de ressources, isolation applicative ; micro-segmentation et SDP.',
      lessons: [
        { slug: 'approches-deploiement', title: 'Les approches de déploiement (1/2) : quatre variantes concrètes', minutes: 12 },
        { slug: 'microsegmentation-sdp', title: 'Les approches de déploiement (2/2) : micro-segmentation et périmètre défini par logiciel', minutes: 12 },
      ],
    },
    {
      slug: 'migration',
      title: 'Module 4 — La migration depuis un modèle périmétrique',
      description: 'Un parcours progressif, la coexistence hybride, et la priorisation par criticité.',
      lessons: [
        { slug: 'migration-perimetre', title: 'La migration depuis un modèle périmétrique traditionnel', minutes: 12 },
      ],
    },
    {
      slug: 'menaces',
      title: 'Module 5 — Les menaces propres à l\'architecture elle-même',
      description: 'Subversion du PE/PA, déni de service, vol d\'identifiants, trafic chiffré, données de politique.',
      lessons: [
        { slug: 'menaces-propres-zta', title: 'Les menaces propres à l\'architecture Zero Trust elle-même', minutes: 12 },
      ],
    },
    {
      slug: 'maturite-cisa',
      title: 'Module 6 — Le modèle de maturité de la CISA',
      description: 'Cinq piliers (identité, équipements, réseaux, applications, données), et quatre niveaux de maturité.',
      lessons: [
        { slug: 'modele-maturite-cisa', title: 'Le modèle de maturité de la CISA', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'Zero Trust face au NIST CSF/CIS Controls/FedRAMP/CMMC/DORA, pièges fréquents, et feuille de route.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'L\'architecture Zero Trust face aux autres référentiels, et une feuille de route de mise en œuvre', minutes: 13 },
      ],
    },
  ],
}
