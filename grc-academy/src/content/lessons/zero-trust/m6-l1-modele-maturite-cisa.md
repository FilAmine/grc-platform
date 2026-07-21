# Le modèle de maturité de la CISA

## Un modèle complémentaire, comblant l'absence d'échelle de maturité dans SP 800-207

NIST SP 800-207 décrit l'architecture Zero Trust dans son principe et ses composants, mais ne propose jamais d'échelle de maturité permettant à une organisation d'évaluer précisément sa propre progression. La **Cybersecurity and Infrastructure Security Agency (CISA)**, agence américaine de cybersécurité, a comblé cette absence en publiant son propre **Zero Trust Maturity Model**, structuré autour de cinq piliers et de plusieurs capacités transversales, complétant directement l'architecture logique déjà développée dans ce parcours.

## Les cinq piliers du modèle CISA

- **L'identité** — la gestion des identités des utilisateurs et des équipements, incluant l'authentification multifacteur déjà développée à de multiples reprises dans cette plateforme.
- **Les équipements** — l'inventaire, la surveillance continue de la posture de sécurité et la gestion de la conformité de l'ensemble des équipements accédant aux ressources de l'organisation.
- **Les réseaux** — la segmentation et la micro-segmentation déjà développées au module 3 de ce parcours, ainsi que le chiffrement systématique des communications.
- **Les applications et les charges de travail** — la sécurisation des applications elles-mêmes, y compris à travers les principes de conception sécurisée déjà développés à travers plusieurs référentiels de cette plateforme.
- **Les données** — la classification, le chiffrement et la protection des données elles-mêmes, indépendamment de l'infrastructure qui les héberge.

## Les capacités transversales du modèle

Au-delà de ces cinq piliers, le modèle CISA identifie des capacités transversales qui infusent l'ensemble des piliers plutôt que de constituer une dimension isolée — la **visibilité et l'analyse**, l'**automatisation et l'orchestration**, et la **gouvernance**. Cette architecture à piliers verticaux et capacités transversales rappelle directement celle déjà développée pour la fonction Govern, explicitement transversale, du NIST AI RMF de cette plateforme — une gouvernance qui infuse en permanence l'ensemble des autres dimensions plutôt que d'intervenir comme une étape isolée.

## Quatre niveaux de maturité, pour chaque pilier

Le modèle CISA distingue quatre niveaux de maturité applicables à chacun des cinq piliers — **traditionnel**, où les décisions d'accès reposent encore largement sur une confiance implicite statique ; **initial**, où l'organisation commence à automatiser certaines décisions et à intégrer des attributs contextuels limités ; **avancé**, où l'automatisation et l'intégration contextuelle deviennent substantielles à travers plusieurs piliers ; et **optimal**, où les décisions d'accès sont entièrement dynamiques, automatisées et fondées sur une évaluation contextuelle complète en temps réel, conformément à l'ensemble des sept principes déjà développés au module 1 de ce parcours.

## Pourquoi une organisation progresse rarement de façon uniforme à travers les cinq piliers

L'expérience pratique révèle qu'une organisation atteint rarement un niveau de maturité identique simultanément à travers l'ensemble de ses cinq piliers — une organisation ayant investi massivement dans la gestion des identités peut ainsi se situer au niveau optimal sur ce pilier, tout en demeurant au niveau traditionnel sur la micro-segmentation réseau, plus coûteuse et plus complexe à déployer. Cette progression inégale rappelle directement celle déjà développée pour la vue de portefeuille des risques de COSO ERM, où une évaluation cloisonnée pilier par pilier, sans vision d'ensemble, risquerait de masquer des déséquilibres significatifs dans la maturité globale de l'organisation.

## Un tableau de synthèse du modèle CISA

| Élément | Détail |
|---|---|
| Cinq piliers | Identité, équipements, réseaux, applications et charges de travail, données |
| Capacités transversales | Visibilité et analyse, automatisation et orchestration, gouvernance |
| Quatre niveaux de maturité | Traditionnel, initial, avancé, optimal |

## Comment ce modèle guide concrètement une feuille de route de migration

Une organisation peut utiliser ce modèle pour cartographier précisément son niveau de maturité actuel pilier par pilier, identifier les écarts les plus significatifs par rapport à ses objectifs, et prioriser ses investissements de migration vers les piliers présentant le plus grand écart au regard du risque qu'ils représentent — une démarche d'analyse d'écarts qui rappelle directement celle déjà développée pour les Profils du NIST CSF et du NIST AI RMF, développés dans les parcours dédiés de cette plateforme.

## Le lien avec le module suivant

Ce modèle de maturité, une fois maîtrisé, permet de structurer une feuille de route de migration réaliste, replacée dans le contexte plus large des autres référentiels déjà étudiés dans cette plateforme — l'objet du dernier module de ce parcours.
