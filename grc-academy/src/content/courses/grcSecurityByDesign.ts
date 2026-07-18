import type { Course } from '../types'

export const grcSecurityByDesign: Course = {
  slug: 'grc-security-by-design',
  title: 'Fondamentaux GRC & Security by Design',
  subtitle: 'Gouvernance, risque, conformité — et sécurité dès la conception (privacy, cloud)',
  description:
    "Un parcours complet reliant la gouvernance, la gestion des risques et les référentiels de conformité (ISO 27001, NIST CSF, SOC 2, RGPD) aux pratiques concrètes de Security by Design, Privacy by Design et de sécurité cloud.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: "Pourquoi former GRC et Security by Design ensemble.",
      lessons: [
        { slug: 'bienvenue', title: 'Bienvenue : pourquoi former GRC et Security by Design ensemble ?', minutes: 6 },
      ],
    },
    {
      slug: 'grc-fondamentaux',
      title: 'Module 1 — Gouvernance, Risque, Conformité',
      description: 'Les fondamentaux : qui décide, comment on évalue un risque, ce que "être conforme" veut dire.',
      lessons: [
        { slug: 'gouvernance', title: 'La gouvernance : qui décide, et sur quelle base', minutes: 9 },
        { slug: 'gestion-des-risques', title: 'Gestion des risques : méthodologies et cycle de vie', minutes: 10 },
        { slug: 'conformite', title: 'Conformité : cartographie réglementaire et audits', minutes: 9 },
      ],
    },
    {
      slug: 'normes-referentiels',
      title: 'Module 2 — Les normes et référentiels clés',
      description: 'ISO/IEC 27001 & 27002, NIST CSF 2.0, SOC 2, RGPD, et comment ils s\'articulent.',
      lessons: [
        { slug: 'iso-27001', title: 'ISO/IEC 27001 & 27002 : le SMSI', minutes: 11 },
        { slug: 'nist-csf', title: 'NIST CSF 2.0 : les six fonctions', minutes: 10 },
        { slug: 'soc-2', title: 'SOC 2 : les Trust Services Criteria', minutes: 9 },
        { slug: 'rgpd', title: 'RGPD : principes fondateurs et obligations', minutes: 11 },
        { slug: 'comparatif', title: 'Comparatif : comment ces référentiels s\'articulent', minutes: 8 },
      ],
    },
    {
      slug: 'security-by-design',
      title: 'Module 3 — Security by Design',
      description: 'Les principes fondateurs : shift-left, secure SDLC, threat modeling, defense in depth, zero trust.',
      lessons: [
        { slug: 'principes', title: 'Security by Design : shift-left, secure SDLC, threat modeling', minutes: 10 },
        { slug: 'defense-en-profondeur', title: 'Défense en profondeur, moindre privilège, fail secure, zero trust', minutes: 10 },
      ],
    },
    {
      slug: 'privacy-by-design',
      title: 'Module 4 — Privacy by Design',
      description: 'Les 7 principes de Cavoukian et leur traduction opérationnelle dans le RGPD.',
      lessons: [
        { slug: 'principes-cavoukian', title: 'Privacy by Design : les 7 principes de Cavoukian', minutes: 8 },
        { slug: 'rgpd-pratique', title: 'Privacy by Design appliqué au RGPD : minimisation, PIA/DPIA, pseudonymisation', minutes: 11 },
      ],
    },
    {
      slug: 'cloud-security-by-design',
      title: 'Module 5 — Security by Design dans le Cloud',
      description: 'Responsabilité partagée, IAM, chiffrement, segmentation réseau, référentiels cloud.',
      lessons: [
        { slug: 'responsabilite-partagee', title: 'Le modèle de responsabilité partagée dans le cloud', minutes: 9 },
        { slug: 'iam-chiffrement-reseau', title: 'IAM, chiffrement et segmentation réseau dans le cloud', minutes: 11 },
        { slug: 'referentiels-cloud', title: 'Référentiels cloud : CSA CCM, CIS Benchmarks, bonnes pratiques', minutes: 9 },
      ],
    },
    {
      slug: 'synthese',
      title: 'Module 6 — Synthèse',
      description: 'Boucler la boucle, de la gouvernance à la configuration technique, et construire son plan d\'action.',
      lessons: [
        { slug: 'boucle-retroaction', title: 'De la gouvernance à l\'implémentation technique : boucler la boucle', minutes: 9 },
        { slug: 'feuille-de-route', title: 'Construire son propre programme : plan d\'action et feuille de route', minutes: 8 },
      ],
    },
  ],
}
