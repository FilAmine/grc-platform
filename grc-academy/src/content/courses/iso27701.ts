import type { Course } from '../types'

export const iso27701: Course = {
  slug: 'iso-27701',
  title: 'ISO/IEC 27701 en profondeur',
  subtitle: 'L\'extension d\'ISO 27001 pour la vie privée, les rôles responsable/sous-traitant, et la certification',
  description:
    "Un parcours entièrement dédié à ISO/IEC 27701 : son architecture d'extension d'ISO 27001 plutôt que de norme autonome, l'appréciation des risques spécifique à la vie privée qui distingue le risque vie privée du risque de sécurité, la distinction entre responsable de traitement (Annexe A) et sous-traitant (Annexe B), les contrôles relatifs aux conditions de collecte, aux droits des personnes et au Privacy by Design, les obligations propres aux sous-traitants, le partage, le transfert et la divulgation des données à des tiers (transferts internationaux, sous-traitance ultérieure), le processus de certification combinée avec ISO 27001, et l'articulation avec le RGPD, le NIST Privacy Framework et ISO/IEC 42001 déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'Une voie certifiable pour la vie privée, et pourquoi ISO 27701 est une extension plutôt qu\'une norme autonome.',
      lessons: [
        { slug: 'introduction', title: 'ISO/IEC 27701 en profondeur : introduction et repères', minutes: 12 },
      ],
    },
    {
      slug: 'architecture-extension',
      title: 'Module 1 — L\'architecture d\'extension et le PIMS',
      description: 'Le mécanisme d\'amendement des clauses d\'ISO 27001, et l\'appréciation des risques spécifique à la vie privée.',
      lessons: [
        { slug: 'mecanisme-extension', title: 'L\'architecture d\'extension et le PIMS (1/2) : comment ISO 27701 amende ISO 27001', minutes: 12 },
        { slug: 'appreciation-risques-vie-privee', title: 'L\'architecture d\'extension et le PIMS (2/2) : l\'appréciation des risques spécifique à la vie privée', minutes: 12 },
      ],
    },
    {
      slug: 'roles',
      title: 'Module 2 — Les rôles de responsable et sous-traitant',
      description: 'PII Controller et PII Processor, directement hérités du RGPD, et leur combinaison avec les rôles de l\'AI Act.',
      lessons: [
        { slug: 'roles-responsable-sous-traitant', title: 'Les rôles de responsable de traitement et de sous-traitant', minutes: 12 },
      ],
    },
    {
      slug: 'annexe-a',
      title: 'Module 3 — Les contrôles pour les responsables de traitement',
      description: 'Conditions de collecte et bases légales ; droits des personnes et Privacy by Design.',
      lessons: [
        { slug: 'conditions-collecte-bases-legales', title: 'Les contrôles pour les responsables de traitement (1/2) : conditions de collecte et bases légales', minutes: 12 },
        { slug: 'droits-personnes-privacy-by-design', title: 'Les contrôles pour les responsables de traitement (2/2) : droits des personnes et Privacy by Design', minutes: 12 },
      ],
    },
    {
      slug: 'annexe-b',
      title: 'Module 4 — Les contrôles pour les sous-traitants',
      description: 'Traitement selon instructions, assistance aux droits, notification des violations, sous-traitance ultérieure.',
      lessons: [
        { slug: 'controles-sous-traitants', title: 'Les contrôles pour les sous-traitants (Annexe B)', minutes: 12 },
      ],
    },
    {
      slug: 'partage-transfert',
      title: 'Module 5 — Le partage, le transfert et la divulgation des données',
      description: 'Transferts internationaux ; tiers, sous-traitance ultérieure et divulgation aux autorités.',
      lessons: [
        { slug: 'transferts-internationaux', title: 'Le partage, le transfert et la divulgation des données (1/2) : les transferts internationaux', minutes: 12 },
        { slug: 'sous-traitance-ulterieure-tiers', title: 'Le partage, le transfert et la divulgation des données (2/2) : tiers, sous-traitance ultérieure et autorités publiques', minutes: 12 },
      ],
    },
    {
      slug: 'certification',
      title: 'Module 6 — Le processus de certification combinée',
      description: 'Stage 1/Stage 2 avec ISO 27001, cycle triennal, révision en cours, et intégration avec ISO 42001/22301.',
      lessons: [
        { slug: 'certification', title: 'Le processus de certification combinée avec ISO 27001', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'ISO/IEC 27701 face au RGPD/NIST Privacy Framework/ISO 42001, pièges fréquents, et feuille de route.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'ISO/IEC 27701 face aux autres référentiels, et une feuille de route de mise en œuvre', minutes: 13 },
      ],
    },
  ],
}
