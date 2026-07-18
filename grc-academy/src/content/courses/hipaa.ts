import type { Course } from '../types'

export const hipaa: Course = {
  slug: 'hipaa',
  title: 'HIPAA en profondeur',
  subtitle: 'Privacy Rule, Security Rule, Business Associates et notification des violations',
  description:
    "Un parcours entièrement dédié à HIPAA : les origines et l'évolution du texte (HITECH, Omnibus Rule), les entités couvertes et les Business Associates, la Privacy Rule (triptyque Treatment/Payment/Healthcare Operations, minimum nécessaire, droits des patients), la Security Rule et ses trois catégories de sauvegardes ainsi que le mécanisme Required/Addressable, le contrat obligatoire avec les Business Associates (BAA), la règle de notification des violations, le régime d'application et de sanctions de l'OCR, les méthodes de dé-identification, et l'articulation avec le RGPD et les référentiels techniques déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Origines (1996), HITECH (2009), Omnibus Rule (2013), OCR, entités couvertes/Business Associates, PHI/ePHI.',
      lessons: [
        { slug: 'introduction', title: 'HIPAA en profondeur : introduction et repères', minutes: 11 },
      ],
    },
    {
      slug: 'privacy-rule',
      title: 'Module 1 — La Privacy Rule',
      description: 'Le triptyque Treatment/Payment/Healthcare Operations, le minimum nécessaire, et les droits des patients.',
      lessons: [
        { slug: 'divulgations', title: 'La Privacy Rule (1/2) : divulgations autorisées et minimum nécessaire', minutes: 12 },
        { slug: 'droits-des-patients', title: 'La Privacy Rule (2/2) : les droits des patients', minutes: 12 },
      ],
    },
    {
      slug: 'security-rule',
      title: 'Module 2 — La Security Rule',
      description: 'Sauvegardes administratives, physiques et techniques, et le mécanisme Required/Addressable.',
      lessons: [
        { slug: 'sauvegardes-administratives', title: 'La Security Rule (1/3) : les sauvegardes administratives et l\'analyse de risque', minutes: 12 },
        { slug: 'sauvegardes-physiques-techniques', title: 'La Security Rule (2/3) : les sauvegardes physiques et techniques', minutes: 12 },
        { slug: 'required-addressable', title: 'La Security Rule (3/3) : spécifications Required et Addressable', minutes: 12 },
      ],
    },
    {
      slug: 'business-associates',
      title: 'Module 3 — Business Associates et BAA',
      description: 'La responsabilité directe introduite par HITECH, et le contenu contractuel minimal du BAA.',
      lessons: [
        { slug: 'business-associates', title: 'Business Associates et le contrat obligatoire (BAA)', minutes: 12 },
      ],
    },
    {
      slug: 'breach-notification',
      title: 'Module 4 — La règle de notification des violations',
      description: 'L\'évaluation de risque en quatre facteurs, l\'exemption par chiffrement, et le calendrier de notification.',
      lessons: [
        { slug: 'breach-notification', title: 'La Breach Notification Rule', minutes: 12 },
      ],
    },
    {
      slug: 'application-sanctions',
      title: 'Module 5 — Application et sanctions',
      description: 'L\'OCR, les sanctions civiles graduées, les sanctions pénales, et les accords de résolution.',
      lessons: [
        { slug: 'application-sanctions', title: 'Application du dispositif et régime de sanctions', minutes: 12 },
      ],
    },
    {
      slug: 'deidentification-mapping',
      title: 'Module 6 — Dé-identification, mapping et feuille de route',
      description: 'Safe Harbor et Expert Determination, puis HIPAA face au RGPD et aux référentiels techniques.',
      lessons: [
        { slug: 'deidentification', title: 'La dé-identification des données de santé', minutes: 12 },
        { slug: 'mapping-feuille-de-route', title: 'HIPAA face aux autres référentiels, et feuille de route de mise en conformité', minutes: 12 },
      ],
    },
  ],
}
