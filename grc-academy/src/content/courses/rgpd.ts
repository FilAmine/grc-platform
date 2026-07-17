import type { Course } from '../types'
import m0l1 from '../lessons/rgpd/m0-l1-introduction.md?raw'
import m1l1 from '../lessons/rgpd/m1-l1-champ-application.md?raw'
import m1l2 from '../lessons/rgpd/m1-l2-bases-legales.md?raw'
import m2l1 from '../lessons/rgpd/m2-l1-droits-partie1.md?raw'
import m2l2 from '../lessons/rgpd/m2-l2-droits-partie2.md?raw'
import m3l1 from '../lessons/rgpd/m3-l1-responsable-sous-traitant.md?raw'
import m3l2 from '../lessons/rgpd/m3-l2-dpo.md?raw'
import m4l1 from '../lessons/rgpd/m4-l1-securite-violations.md?raw'
import m4l2 from '../lessons/rgpd/m4-l2-registre-aipd.md?raw'
import m5l1 from '../lessons/rgpd/m5-l1-transferts-internationaux.md?raw'
import m6l1 from '../lessons/rgpd/m6-l1-autorites-guichet-unique.md?raw'
import m6l2 from '../lessons/rgpd/m6-l2-sanctions.md?raw'
import m7l1 from '../lessons/rgpd/m7-l1-feuille-de-route.md?raw'

export const rgpd: Course = {
  slug: 'rgpd',
  title: 'RGPD en profondeur',
  subtitle: 'Bases légales, droits des personnes, DPO, violations, transferts internationaux',
  description:
    "Un parcours entièrement dédié au RGPD, sur des angles complémentaires du premier parcours de cette plateforme : le champ d'application territorial et les six bases légales, les droits des personnes concernées dans leur mécanique procédurale précise, la relation responsable de traitement/sous-traitant et le rôle du DPO, la sécurité du traitement et la notification des violations, le registre des traitements et l'AIPD, les transferts internationaux de données, et la gouvernance des autorités de contrôle jusqu'aux sanctions.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Histoire, structure du texte, définitions clés (donnée personnelle, traitement, responsable, sous-traitant).',
      lessons: [
        { slug: 'introduction', title: 'RGPD en profondeur : introduction, structure et définitions clés', minutes: 10, content: m0l1 },
      ],
    },
    {
      slug: 'champ-bases-legales',
      title: 'Module 1 — Champ d\'application et bases légales',
      description: 'Le champ d\'application territorial (art. 3) et les six bases légales de l\'article 6.',
      lessons: [
        { slug: 'champ-application', title: 'Champ d\'application matériel et territorial', minutes: 11, content: m1l1 },
        { slug: 'bases-legales', title: 'Les six bases légales de traitement, et les catégories de données particulières', minutes: 12, content: m1l2 },
      ],
    },
    {
      slug: 'droits-personnes',
      title: 'Module 2 — Les droits des personnes concernées',
      description: 'Information, accès, rectification, effacement, limitation, portabilité, opposition et décisions automatisées.',
      lessons: [
        { slug: 'droits-partie1', title: 'Les droits des personnes concernées (1/2) : information, accès, rectification, effacement, limitation', minutes: 12, content: m2l1 },
        { slug: 'droits-partie2', title: 'Les droits des personnes concernées (2/2) : portabilité, opposition, décisions automatisées', minutes: 11, content: m2l2 },
      ],
    },
    {
      slug: 'responsable-dpo',
      title: 'Module 3 — Responsable, sous-traitant et DPO',
      description: 'Le contrat de sous-traitance (article 28) et le rôle du Délégué à la Protection des Données.',
      lessons: [
        { slug: 'responsable-sous-traitant', title: 'Responsable de traitement, sous-traitant, et le contrat de sous-traitance', minutes: 12, content: m3l1 },
        { slug: 'dpo', title: 'Le Délégué à la Protection des Données (DPO)', minutes: 10, content: m3l2 },
      ],
    },
    {
      slug: 'securite-accountability',
      title: 'Module 4 — Sécurité, violations et accountability',
      description: 'Sécurité du traitement, notification des violations (72h), registre des traitements et AIPD.',
      lessons: [
        { slug: 'securite-violations', title: 'Sécurité du traitement et notification des violations de données', minutes: 12, content: m4l1 },
        { slug: 'registre-aipd', title: 'Le registre des traitements et l\'analyse d\'impact (AIPD/DPIA)', minutes: 12, content: m4l2 },
      ],
    },
    {
      slug: 'transferts-internationaux',
      title: 'Module 5 — Les transferts internationaux de données',
      description: 'Décisions d\'adéquation, clauses contractuelles types, Schrems I/II et le Data Privacy Framework.',
      lessons: [
        { slug: 'transferts-internationaux', title: 'Les transferts internationaux de données', minutes: 12, content: m5l1 },
      ],
    },
    {
      slug: 'gouvernance-sanctions',
      title: 'Module 6 — Gouvernance et sanctions',
      description: 'Autorités de contrôle, guichet unique, CEPD, amendes administratives et recours collectifs.',
      lessons: [
        { slug: 'autorites-guichet-unique', title: 'Les autorités de contrôle, le guichet unique et le Comité européen', minutes: 11, content: m6l1 },
        { slug: 'sanctions', title: 'Sanctions administratives, responsabilité civile et recours collectifs', minutes: 11, content: m6l2 },
      ],
    },
    {
      slug: 'feuille-de-route',
      title: 'Module 7 — Feuille de route de mise en conformité',
      description: 'Priorisation d\'un programme de conformité RGPD et pièges de planification fréquents.',
      lessons: [
        { slug: 'feuille-de-route', title: 'Construire un programme de conformité RGPD réaliste', minutes: 10, content: m7l1 },
      ],
    },
  ],
}
