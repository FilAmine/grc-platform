import type { Course } from '../types'

export const swiftCsp: Course = {
  slug: 'swift-csp',
  title: 'SWIFT CSP en profondeur',
  subtitle: 'Le CSCF, les Architecture Types, l\'auto-attestation et le KYC Registry',
  description:
    "Un parcours entièrement dédié au Customer Security Programme de SWIFT : ses origines dans l'incident de la banque centrale du Bangladesh et la nature coopérative de SWIFT, les types d'architecture (A1/A2/A3/B) qui déterminent le périmètre de contrôles applicables, la structure du Customer Security Controls Framework (CSCF) en trois objectifs de sécurité et deux catégories de contrôles, le processus d'auto-attestation KYC-SA et les deux voies de corroboration indépendante (audit interne ou évaluateur externe), le KYC Registry et le mécanisme de partage entre contreparties bancaires, la double sanction commerciale et quasi réglementaire, l'évolution annuelle du catalogue, et l'articulation avec ISO 27001, TISAX, PCI DSS et DORA déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'L\'incident de la banque centrale du Bangladesh, la nature coopérative de SWIFT, et la création du CSP.',
      lessons: [
        { slug: 'introduction', title: 'SWIFT CSP en profondeur : introduction et repères', minutes: 11 },
      ],
    },
    {
      slug: 'cscf-architecture',
      title: 'Module 1 — Le catalogue CSCF et les types d\'architecture',
      description: 'Les Architecture Types (A1/A2/A3/B) et la structure du CSCF en objectifs et catégories de contrôles.',
      lessons: [
        { slug: 'architecture-types', title: 'Le catalogue CSCF et les types d\'architecture (1/2) : les Architecture Types', minutes: 12 },
        { slug: 'structure-cscf', title: 'Le catalogue CSCF et les types d\'architecture (2/2) : structure du catalogue', minutes: 12 },
      ],
    },
    {
      slug: 'objectifs-securite',
      title: 'Module 2 — Les trois objectifs de sécurité',
      description: 'Sécuriser l\'environnement, connaître et limiter les accès, détecter et réagir.',
      lessons: [
        { slug: 'objectifs-1-2', title: 'Les trois objectifs de sécurité (1/2) : sécuriser l\'environnement et maîtriser les accès', minutes: 12 },
        { slug: 'objectif-3-detecter-repondre', title: 'Les trois objectifs de sécurité (2/2) : détecter et réagir', minutes: 12 },
      ],
    },
    {
      slug: 'attestation-evaluation',
      title: 'Module 3 — L\'auto-attestation et l\'évaluation indépendante',
      description: 'Le processus KYC-SA, et les deux voies de corroboration (audit interne ou évaluateur externe).',
      lessons: [
        { slug: 'auto-attestation-kyc-sa', title: 'L\'auto-attestation et l\'évaluation indépendante (1/2) : le processus KYC-SA', minutes: 12 },
        { slug: 'evaluation-independante', title: 'L\'auto-attestation et l\'évaluation indépendante (2/2) : les deux voies de corroboration', minutes: 12 },
      ],
    },
    {
      slug: 'kyc-registry',
      title: 'Module 4 — Le KYC Registry',
      description: 'Le partage des attestations entre contreparties bancaires, fondé sur la relation de correspondance.',
      lessons: [
        { slug: 'kyc-registry-partage', title: 'Le KYC Registry et le partage entre correspondants bancaires', minutes: 12 },
      ],
    },
    {
      slug: 'sanctions',
      title: 'Module 5 — Sanctions et supervision',
      description: 'La double sanction commerciale et quasi réglementaire, et la passerelle vers les autorités.',
      lessons: [
        { slug: 'sanctions-supervision', title: 'Les sanctions et le pont vers la supervision réglementaire', minutes: 12 },
      ],
    },
    {
      slug: 'evolution-cscf',
      title: 'Module 6 — L\'évolution annuelle du CSCF',
      description: 'La promotion des contrôles consultatifs vers obligatoires, et le rythme de révision annuel.',
      lessons: [
        { slug: 'evolution-annuelle-cscf', title: 'L\'évolution annuelle du catalogue CSCF', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'SWIFT CSP face aux autres référentiels de cette plateforme, pièges fréquents, et feuille de route.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'SWIFT CSP face aux autres référentiels, et une feuille de route de mise en conformité', minutes: 13 },
      ],
    },
  ],
}
