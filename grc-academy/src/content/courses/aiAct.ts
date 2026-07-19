import type { Course } from '../types'

export const aiAct: Course = {
  slug: 'ai-act',
  title: 'Le règlement européen sur l\'IA (AI Act) en profondeur',
  subtitle: 'La pyramide des risques, les obligations à haut risque, et le pont avec le NIST AI RMF',
  description:
    "Un parcours entièrement dédié au règlement (UE) 2024/1689 sur l'intelligence artificielle : la pyramide des niveaux de risque et les pratiques interdites, les obligations substantielles imposées aux systèmes à haut risque (système de gestion des risques, gouvernance des données, documentation, journalisation, transparence, contrôle humain, robustesse), les acteurs et la chaîne de responsabilité (fournisseur, déployeur, importateur, distributeur), l'évaluation de conformité et le marquage CE, le régime spécifique aux modèles d'IA à usage général (GPAI), la gouvernance institutionnelle, le calendrier d'application échelonné et le régime de sanctions à trois paliers, et l'articulation avec le NIST AI RMF, le RGPD et les référentiels de sécurité déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Le premier texte légal horizontal sur l\'IA, son calendrier échelonné, et le lien avec le NIST AI RMF.',
      lessons: [
        { slug: 'introduction', title: 'Le règlement européen sur l\'intelligence artificielle (AI Act) : introduction et repères', minutes: 12 },
      ],
    },
    {
      slug: 'pyramide-risques',
      title: 'Module 1 — La pyramide des risques',
      description: 'Les pratiques interdites (article 5), et les niveaux haut risque/limité/minimal.',
      lessons: [
        { slug: 'pratiques-interdites', title: 'La pyramide des risques (1/2) : les pratiques interdites', minutes: 13 },
        { slug: 'haut-risque-limite-minimal', title: 'La pyramide des risques (2/2) : haut risque, risque limité et risque minimal', minutes: 13 },
      ],
    },
    {
      slug: 'obligations-haut-risque',
      title: 'Module 2 — Les obligations des systèmes à haut risque',
      description: 'Système de gestion des risques, gouvernance des données, documentation, transparence, contrôle humain, robustesse.',
      lessons: [
        { slug: 'systeme-gestion-risques-donnees', title: 'Les obligations des systèmes à haut risque (1/2) : gestion des risques et gouvernance des données', minutes: 13 },
        { slug: 'documentation-transparence-controle-humain', title: 'Les obligations des systèmes à haut risque (2/2) : documentation, transparence et contrôle humain', minutes: 13 },
      ],
    },
    {
      slug: 'acteurs',
      title: 'Module 3 — Acteurs et chaîne de responsabilité',
      description: 'Fournisseur, déployeur, importateur, distributeur, et le mécanisme de requalification.',
      lessons: [
        { slug: 'acteurs-chaine-responsabilite', title: 'Les acteurs et la chaîne de responsabilité', minutes: 12 },
      ],
    },
    {
      slug: 'conformite',
      title: 'Module 4 — Évaluation de conformité et marquage CE',
      description: 'Contrôle interne vs organisme notifié, marquage CE, et la base de données européenne.',
      lessons: [
        { slug: 'conformite-marquage-ce', title: 'L\'évaluation de conformité et le marquage CE', minutes: 12 },
      ],
    },
    {
      slug: 'gpai',
      title: 'Module 5 — Les modèles d\'IA à usage général',
      description: 'Obligations générales et régime renforcé pour les modèles GPAI à risque systémique.',
      lessons: [
        { slug: 'modeles-usage-general', title: 'Les modèles d\'IA à usage général (GPAI)', minutes: 12 },
      ],
    },
    {
      slug: 'gouvernance-sanctions',
      title: 'Module 6 — Gouvernance et sanctions',
      description: 'AI Office, autorités nationales, AI Board, calendrier d\'application, et amendes à trois paliers.',
      lessons: [
        { slug: 'gouvernance', title: 'La gouvernance institutionnelle de l\'AI Act', minutes: 12 },
        { slug: 'calendrier-sanctions', title: 'Le calendrier d\'application et le régime de sanctions', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'L\'AI Act face au NIST AI RMF/RGPD/référentiels de sécurité, pièges fréquents, et feuille de route.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'L\'AI Act face aux autres référentiels, et une feuille de route de mise en conformité', minutes: 13 },
      ],
    },
  ],
}
