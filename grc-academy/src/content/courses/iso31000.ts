import type { Course } from '../types'

export const iso31000: Course = {
  slug: 'iso-31000',
  title: 'ISO 31000 en profondeur',
  subtitle: 'Les principes, le cadre organisationnel et le processus générique de management du risque',
  description:
    "Un parcours entièrement dédié à ISO 31000, le référentiel générique de management du risque qui sous-tend, sans toujours être nommé, la quasi-totalité des parcours déjà étudiés dans cette plateforme : les huit principes d'une gestion des risques efficace, le cadre organisationnel dans ses six composantes (direction, intégration, conception, mise en œuvre, évaluation, amélioration), l'établissement du contexte et des critères de risque, l'appréciation des risques (identification, analyse, évaluation), le traitement des risques et ses sept options, la surveillance, l'enregistrement et la communication, et le mapping explicite avec EBIOS RM, le NIST RMF, le NIST AI RMF, ISO 22301 et les autres référentiels de risque déjà étudiés dans cette plateforme.",
  modules: [
    {
      slug: 'introduction',
      title: 'Module 0 — Introduction',
      description: 'La grammaire générique déjà utilisée par la plupart des parcours de cette plateforme, et la structure en trois composants.',
      lessons: [
        { slug: 'introduction', title: 'ISO 31000 en profondeur : introduction et repères', minutes: 12 },
      ],
    },
    {
      slug: 'principes',
      title: 'Module 1 — Les huit principes',
      description: 'Intégrée, structurée, adaptée, inclusive, dynamique, meilleure information, facteurs humains, amélioration continue.',
      lessons: [
        { slug: 'huit-principes', title: 'Les huit principes d\'une gestion des risques efficace', minutes: 13 },
      ],
    },
    {
      slug: 'cadre-organisationnel',
      title: 'Module 2 — Le cadre organisationnel',
      description: 'Direction et engagement, intégration, conception ; mise en œuvre, évaluation, amélioration.',
      lessons: [
        { slug: 'cadre-leadership-integration-conception', title: 'Le cadre organisationnel (1/2) : leadership, intégration et conception', minutes: 12 },
        { slug: 'cadre-mise-en-oeuvre-evaluation-amelioration', title: 'Le cadre organisationnel (2/2) : mise en œuvre, évaluation et amélioration', minutes: 12 },
      ],
    },
    {
      slug: 'contexte-criteres',
      title: 'Module 3 — Établir le contexte et les critères',
      description: 'Domaine d\'application, contexte externe/interne, critères de risque et appétence pour le risque.',
      lessons: [
        { slug: 'contexte-criteres-appetence', title: 'Établir le contexte et les critères de risque', minutes: 13 },
      ],
    },
    {
      slug: 'appreciation-risques',
      title: 'Module 4 — L\'appréciation des risques',
      description: 'Identification et analyse ; évaluation et priorisation.',
      lessons: [
        { slug: 'identification-analyse', title: 'L\'appréciation des risques (1/2) : identification et analyse', minutes: 12 },
        { slug: 'evaluation-priorisation', title: 'L\'appréciation des risques (2/2) : évaluation et priorisation', minutes: 12 },
      ],
    },
    {
      slug: 'traitement',
      title: 'Module 5 — Le traitement des risques',
      description: 'Les sept options de traitement, le plan de traitement et le risque résiduel.',
      lessons: [
        { slug: 'options-traitement', title: 'Le traitement des risques (1/2) : les sept options', minutes: 13 },
        { slug: 'plan-traitement-risque-residuel', title: 'Le traitement des risques (2/2) : le plan de traitement et le risque résiduel', minutes: 12 },
      ],
    },
    {
      slug: 'surveillance',
      title: 'Module 6 — Surveillance, enregistrement et communication',
      description: 'Trois activités transversales : monitoring and review, recording and reporting, communication and consultation.',
      lessons: [
        { slug: 'surveillance-enregistrement-communication', title: 'Surveillance, enregistrement et communication', minutes: 12 },
      ],
    },
    {
      slug: 'mapping-feuille-de-route',
      title: 'Module 7 — Mapping et feuille de route',
      description: 'ISO 31000 face à EBIOS RM/NIST RMF/NIST AI RMF/ISO 22301, et une feuille de route transversale.',
      lessons: [
        { slug: 'mapping-feuille-de-route', title: 'ISO 31000 face aux référentiels déjà étudiés dans cette plateforme, et une feuille de route', minutes: 13 },
      ],
    },
  ],
}
