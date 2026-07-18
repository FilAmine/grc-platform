import type { Course } from '../types'

export const sox: Course = {
  slug: 'sox',
  title: 'SOX en profondeur',
  subtitle: 'Certification des dirigeants, section 404, ITGC et COSO',
  description:
    "Un parcours entièrement dédié au Sarbanes-Oxley Act : ses origines (scandales Enron/WorldCom, création du PCAOB), la certification personnelle des dirigeants (sections 302 et 906), la section 404 et le contrôle interne sur le reporting financier structuré par le référentiel COSO, les contrôles généraux informatiques (ITGC) et la séparation des tâches, la classification des déficiences de contrôle (déficience, déficience significative, faiblesse matérielle), les rôles de gouvernance (comité d'audit, audit interne, auditeur externe, PCAOB), le rôle des rapports SOC 1 pour les processus financiers externalisés, et l'articulation avec COBIT, ISO 27001 et ITIL déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Origines (Enron/WorldCom), champ d\'application, création du PCAOB, et implications IT (ITGC).',
      lessons: [
        { slug: 'introduction', title: 'SOX en profondeur : introduction et repères', minutes: 11 },
      ],
    },
    {
      slug: 'certification',
      title: 'Module 1 — Certification et responsabilité personnelle',
      description: 'La certification trimestrielle (302) et pénale (906) du CEO et du CFO.',
      lessons: [
        { slug: 'certification-302-906', title: 'La certification personnelle des dirigeants (sections 302 et 906)', minutes: 12 },
      ],
    },
    {
      slug: 'section-404',
      title: 'Module 2 — La section 404 et le contrôle interne',
      description: '404(a)/404(b), l\'approche descendante fondée sur le risque, et le référentiel COSO.',
      lessons: [
        { slug: 'section-404', title: 'La section 404 (1/2) : l\'évaluation du contrôle interne sur le reporting financier', minutes: 12 },
        { slug: 'coso', title: 'La section 404 (2/2) : le référentiel COSO comme colonne vertébrale', minutes: 12 },
      ],
    },
    {
      slug: 'itgc',
      title: 'Module 3 — Les contrôles généraux informatiques (ITGC)',
      description: 'Les quatre domaines ITGC, la dépendance IT, et la séparation des tâches dans les ERP.',
      lessons: [
        { slug: 'itgc-domaines', title: 'Les contrôles généraux informatiques (1/2) : les quatre domaines', minutes: 12 },
        { slug: 'separation-des-taches', title: 'Les contrôles généraux informatiques (2/2) : la séparation des tâches', minutes: 12 },
      ],
    },
    {
      slug: 'deficiences',
      title: 'Module 4 — Classification des déficiences et remédiation',
      description: 'Déficience, déficience significative, faiblesse matérielle, et le processus de remédiation.',
      lessons: [
        { slug: 'deficiences', title: 'Classification des déficiences de contrôle et remédiation', minutes: 12 },
      ],
    },
    {
      slug: 'roles-gouvernance',
      title: 'Module 5 — Rôles et structure de gouvernance',
      description: 'Direction, comité d\'audit, audit interne, auditeur externe, PCAOB, et la protection des lanceurs d\'alerte.',
      lessons: [
        { slug: 'roles-gouvernance', title: 'Rôles et structure de gouvernance de la conformité SOX', minutes: 12 },
      ],
    },
    {
      slug: 'soc1',
      title: 'Module 6 — Les rapports SOC 1 et la sous-traitance',
      description: 'Pourquoi SOX crée la demande de rapports SOC 1, et les contrôles complémentaires de l\'entité utilisatrice.',
      lessons: [
        { slug: 'soc1', title: 'Les rapports SOC 1 et la sous-traitance de processus financiers', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping, sanctions et feuille de route',
      description: 'SOX face à COBIT/ISO 27001/ITIL, le régime de sanctions, et une feuille de route de mise en conformité.',
      lessons: [
        { slug: 'mapping-sanctions', title: 'SOX face aux autres référentiels, et le régime de sanctions', minutes: 12 },
        { slug: 'feuille-de-route', title: 'Construire une feuille de route réaliste de mise en conformité SOX', minutes: 12 },
      ],
    },
  ],
}
