# L'architecture d'extension et le PIMS (1/2) : comment ISO 27701 amende ISO 27001

## Un principe simple : amender plutôt que dupliquer

Le mécanisme central d'ISO/IEC 27701, déjà esquissé au module 0 de ce parcours, consiste à **amender directement le texte des clauses 4 à 10 d'ISO 27001**, déjà développées en détail dans le parcours dédié de cette plateforme, plutôt que d'en réécrire une version parallèle. Concrètement, là où la clause 4.1 d'ISO 27001 impose de déterminer les enjeux internes et externes pertinents pour le SMSI, ISO/IEC 27701 ajoute une exigence complémentaire précise : déterminer également les enjeux propres à la protection de la vie privée, notamment le rôle de l'organisation (responsable de traitement, sous-traitant, ou les deux) vis-à-vis de chaque catégorie de données personnelles traitées.

## Un exemple concret d'amendement, clause par clause

Ce mécanisme d'amendement se retrouve systématiquement à travers l'ensemble des clauses 4 à 10 : la clause 6.1.2 d'ISO 27001, relative à l'appréciation des risques de sécurité de l'information, se voit complétée par une exigence de conduire également une **appréciation des risques spécifique à la vie privée**, développée en détail à la leçon suivante de ce parcours ; la clause 7.2 relative aux compétences se voit complétée par une exigence de sensibilisation spécifique du personnel aux enjeux de protection des données personnelles ; et la clause 9.3 relative à la revue de direction se voit complétée par une exigence d'examen périodique de l'évolution du cadre légal applicable à la vie privée, notamment le RGPD déjà développé dans le parcours dédié de cette plateforme.

## Pourquoi cette organisation ne peut jamais fonctionner de façon autonome

Ce mécanisme d'amendement explique directement pourquoi ISO/IEC 27701 ne peut jamais être mise en œuvre ni certifiée de façon autonome, contrairement à ISO 27001, ISO 22301 ou ISO/IEC 42001, toutes trois développées comme des normes indépendantes dans les parcours dédiés de cette plateforme — le texte d'ISO/IEC 27701 lui-même ne fait sens que lu **en combinaison** avec le texte d'ISO 27001, dont il présuppose l'existence à chaque étape. Une organisation qui souhaiterait obtenir une certification ISO/IEC 27701 sans jamais avoir mis en œuvre ISO 27001 devrait ainsi nécessairement établir les deux systèmes simultanément, plutôt que d'envisager ISO/IEC 27701 comme un projet indépendant.

## Comment cette architecture facilite l'intégration pour les organisations déjà certifiées ISO 27001

Pour une organisation déjà certifiée ISO 27001, ce mécanisme d'extension présente un avantage direct déjà signalé au module 0 de ce parcours : elle réutilise intégralement sa gouvernance existante (revue de direction, programme d'audit interne, gestion documentaire) sans devoir la reconstruire, et se concentre uniquement sur l'ajout des éléments réellement nouveaux propres à la vie privée — l'appréciation des risques spécifique, développée à la leçon suivante, et les contrôles des Annexes A et B, développés aux modules 3 et 4 de ce parcours. Cette économie de moyens rappelle directement celle déjà rencontrée pour l'intégration d'ISO 22301 au sein d'un système de management intégré partageant la revue de direction et le programme d'audit interne d'ISO 27001, développée dans le parcours dédié de cette plateforme.

## L'Annexe D : une table de correspondance officielle avec le RGPD

ISO/IEC 27701 publie, en Annexe D, une table de correspondance directe entre ses propres exigences et les articles du RGPD déjà développé dans le parcours dédié de cette plateforme — une organisation peut ainsi retrouver, pour chaque article du RGPD (bases légales, droits des personnes concernées, sécurité du traitement, transferts internationaux), le ou les contrôles précis d'ISO/IEC 27701 qui y répondent directement. Cette table de correspondance officielle rappelle, dans son principe de mapping documenté et publié par l'organisme normalisateur lui-même, celle déjà développée pour la relation entre le NIST AI RMF et l'AI Act, ou pour les tables de correspondance entre SP 800-53 et ISO 27001 déjà mentionnées dans le parcours NIST RMF de cette plateforme.

## Un tableau de synthèse du mécanisme d'extension

| Élément d'ISO 27001 | Ce qu'ISO/IEC 27701 y ajoute |
|---|---|
| Clause 4.1 (contexte) | Rôle de l'organisation (responsable/sous-traitant) vis-à-vis des données personnelles |
| Clause 6.1.2 (appréciation des risques) | Appréciation des risques spécifique à la vie privée (développée à la leçon suivante) |
| Clause 7.2 (compétences) | Sensibilisation spécifique aux enjeux de protection des données personnelles |
| Clause 9.3 (revue de direction) | Examen de l'évolution du cadre légal applicable, notamment le RGPD |
| Annexe A d'ISO 27001 | Deux Annexes supplémentaires : A (responsables de traitement) et B (sous-traitants), développées aux modules 3 et 4 |

## Le lien avec la leçon suivante

Parmi ces amendements, l'ajout d'une appréciation des risques spécifique à la vie privée constitue l'exigence la plus structurante sur le plan méthodologique — un exercice développé en détail à la leçon suivante de ce parcours.
