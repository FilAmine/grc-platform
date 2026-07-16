import type { Course } from '../types'
import m0l1 from '../lessons/grc-security-by-design/m0-l1-introduction.md?raw'
import m1l1 from '../lessons/grc-security-by-design/m1-l1-gouvernance.md?raw'
import m1l2 from '../lessons/grc-security-by-design/m1-l2-gestion-des-risques.md?raw'
import m1l3 from '../lessons/grc-security-by-design/m1-l3-conformite.md?raw'
import m2l1 from '../lessons/grc-security-by-design/m2-l1-iso27001.md?raw'
import m2l2 from '../lessons/grc-security-by-design/m2-l2-nist-csf.md?raw'
import m2l3 from '../lessons/grc-security-by-design/m2-l3-soc2.md?raw'
import m2l4 from '../lessons/grc-security-by-design/m2-l4-rgpd.md?raw'
import m2l5 from '../lessons/grc-security-by-design/m2-l5-comparatif.md?raw'
import m3l1 from '../lessons/grc-security-by-design/m3-l1-principes-sbd.md?raw'
import m3l2 from '../lessons/grc-security-by-design/m3-l2-defense-en-profondeur.md?raw'
import m4l1 from '../lessons/grc-security-by-design/m4-l1-privacy-by-design.md?raw'
import m4l2 from '../lessons/grc-security-by-design/m4-l2-privacy-rgpd-pratique.md?raw'
import m5l1 from '../lessons/grc-security-by-design/m5-l1-responsabilite-partagee.md?raw'
import m5l2 from '../lessons/grc-security-by-design/m5-l2-iam-chiffrement-reseau.md?raw'
import m5l3 from '../lessons/grc-security-by-design/m5-l3-referentiels-cloud.md?raw'
import m6l1 from '../lessons/grc-security-by-design/m6-l1-boucle-retroaction.md?raw'
import m6l2 from '../lessons/grc-security-by-design/m6-l2-feuille-de-route.md?raw'

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
        { slug: 'bienvenue', title: 'Bienvenue : pourquoi former GRC et Security by Design ensemble ?', minutes: 6, content: m0l1 },
      ],
    },
    {
      slug: 'grc-fondamentaux',
      title: 'Module 1 — Gouvernance, Risque, Conformité',
      description: 'Les fondamentaux : qui décide, comment on évalue un risque, ce que "être conforme" veut dire.',
      lessons: [
        { slug: 'gouvernance', title: 'La gouvernance : qui décide, et sur quelle base', minutes: 9, content: m1l1 },
        { slug: 'gestion-des-risques', title: 'Gestion des risques : méthodologies et cycle de vie', minutes: 10, content: m1l2 },
        { slug: 'conformite', title: 'Conformité : cartographie réglementaire et audits', minutes: 9, content: m1l3 },
      ],
    },
    {
      slug: 'normes-referentiels',
      title: 'Module 2 — Les normes et référentiels clés',
      description: 'ISO/IEC 27001 & 27002, NIST CSF 2.0, SOC 2, RGPD, et comment ils s\'articulent.',
      lessons: [
        { slug: 'iso-27001', title: 'ISO/IEC 27001 & 27002 : le SMSI', minutes: 11, content: m2l1 },
        { slug: 'nist-csf', title: 'NIST CSF 2.0 : les six fonctions', minutes: 10, content: m2l2 },
        { slug: 'soc-2', title: 'SOC 2 : les Trust Services Criteria', minutes: 9, content: m2l3 },
        { slug: 'rgpd', title: 'RGPD : principes fondateurs et obligations', minutes: 11, content: m2l4 },
        { slug: 'comparatif', title: 'Comparatif : comment ces référentiels s\'articulent', minutes: 8, content: m2l5 },
      ],
    },
    {
      slug: 'security-by-design',
      title: 'Module 3 — Security by Design',
      description: 'Les principes fondateurs : shift-left, secure SDLC, threat modeling, defense in depth, zero trust.',
      lessons: [
        { slug: 'principes', title: 'Security by Design : shift-left, secure SDLC, threat modeling', minutes: 10, content: m3l1 },
        { slug: 'defense-en-profondeur', title: 'Défense en profondeur, moindre privilège, fail secure, zero trust', minutes: 10, content: m3l2 },
      ],
    },
    {
      slug: 'privacy-by-design',
      title: 'Module 4 — Privacy by Design',
      description: 'Les 7 principes de Cavoukian et leur traduction opérationnelle dans le RGPD.',
      lessons: [
        { slug: 'principes-cavoukian', title: 'Privacy by Design : les 7 principes de Cavoukian', minutes: 8, content: m4l1 },
        { slug: 'rgpd-pratique', title: 'Privacy by Design appliqué au RGPD : minimisation, PIA/DPIA, pseudonymisation', minutes: 11, content: m4l2 },
      ],
    },
    {
      slug: 'cloud-security-by-design',
      title: 'Module 5 — Security by Design dans le Cloud',
      description: 'Responsabilité partagée, IAM, chiffrement, segmentation réseau, référentiels cloud.',
      lessons: [
        { slug: 'responsabilite-partagee', title: 'Le modèle de responsabilité partagée dans le cloud', minutes: 9, content: m5l1 },
        { slug: 'iam-chiffrement-reseau', title: 'IAM, chiffrement et segmentation réseau dans le cloud', minutes: 11, content: m5l2 },
        { slug: 'referentiels-cloud', title: 'Référentiels cloud : CSA CCM, CIS Benchmarks, bonnes pratiques', minutes: 9, content: m5l3 },
      ],
    },
    {
      slug: 'synthese',
      title: 'Module 6 — Synthèse',
      description: 'Boucler la boucle, de la gouvernance à la configuration technique, et construire son plan d\'action.',
      lessons: [
        { slug: 'boucle-retroaction', title: 'De la gouvernance à l\'implémentation technique : boucler la boucle', minutes: 9, content: m6l1 },
        { slug: 'feuille-de-route', title: 'Construire son propre programme : plan d\'action et feuille de route', minutes: 8, content: m6l2 },
      ],
    },
  ],
}
