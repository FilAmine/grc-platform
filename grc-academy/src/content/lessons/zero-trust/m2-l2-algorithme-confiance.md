# L'architecture logique (2/2) : l'algorithme de confiance et ses sources de données

## Le cœur méthodologique du Policy Engine

L'**algorithme de confiance**, développé au sein du Policy Engine déjà présenté à la leçon précédente de ce parcours, constitue le mécanisme précis par lequel chaque demande d'accès est évaluée — une fonction qui prend en entrée de multiples sources de données contextuelles et produit en sortie une décision d'accorder, de refuser, ou de limiter l'accès demandé.

## Une approche par critères plutôt que par score, ou l'inverse

NIST SP 800-207 distingue deux grandes approches possibles pour cet algorithme de confiance : une approche **fondée sur des critères (criteria-based)**, qui exige la satisfaction de l'ensemble de conditions précises et non négociables (par exemple, un équipement à jour de ses correctifs de sécurité et une authentification multifacteur réussie) avant d'accorder tout accès ; et une approche **fondée sur un score (score-based)**, qui calcule une note de confiance globale à partir de multiples facteurs pondérés, l'accès étant accordé si cette note dépasse un seuil déterminé. Cette distinction rejoint directement celle déjà développée pour les méthodes d'analyse des risques d'ISO 31000, qui peuvent être qualitatives, quantitatives, ou mixtes selon le contexte considéré, développée dans le parcours dédié de cette plateforme.

## Les principales sources de données alimentant l'algorithme

L'algorithme de confiance s'appuie typiquement sur de multiples sources d'information, chacune apportant un éclairage complémentaire sur le contexte de la demande d'accès :

- **Le système de diagnostic et d'atténuation continus (Continuous Diagnostics and Mitigation — CDM)** — l'état de sécurité actualisé de l'équipement demandeur (correctifs appliqués, vulnérabilités connues, logiciels installés).
- **La conformité réglementaire ou sectorielle** — le respect, par l'organisation ou par l'équipement concerné, des exigences applicables déjà développées à travers de nombreux référentiels de cette plateforme.
- **Le renseignement sur les menaces (threat intelligence)** — des informations externes sur des campagnes d'attaque en cours ou des indicateurs de compromission connus.
- **Les journaux d'activité** — le comportement historique de l'utilisateur ou de l'équipement, permettant de détecter un écart significatif par rapport à un profil habituel.
- **La politique de gestion des données** — les règles propres à l'organisation encadrant l'accès à des catégories de données particulièrement sensibles.
- **L'infrastructure à clés publiques (PKI) et la gestion des identités** — les certificats et les attributs d'identité vérifiés de l'utilisateur ou de l'équipement demandeur.

## Le lien direct avec la gestion des identités déjà développée dans cette plateforme

Cette dernière source rejoint directement la gestion des identités déjà développée à travers de nombreux parcours de cette plateforme — le contrôle d'accès de la famille correspondante de SP 800-171 dans le parcours CMMC, ou l'authentification multifacteur déjà exigée par le CSCF de SWIFT CSP — mais l'architecture Zero Trust ajoute à cette gestion des identités classique une dimension contextuelle et dynamique supplémentaire, plutôt que de se limiter à une vérification statique d'identité.

## Un exemple concret d'algorithme fondé sur des critères combinés

Un algorithme de confiance pourrait ainsi exiger, de façon cumulative et non négociable, une authentification multifacteur réussie, un équipement conforme à la politique de sécurité de l'organisation (correctifs à jour, chiffrement du disque activé), et une localisation géographique cohérente avec le profil habituel de l'utilisateur — l'absence d'une seule de ces conditions entraînant automatiquement le refus de l'accès, quelle que soit la satisfaction des autres critères, selon une logique de critères non compensables plutôt qu'un score global où une faiblesse sur un facteur pourrait être compensée par une force sur un autre.

## Pourquoi cet algorithme doit rester suffisamment transparent et explicable

Un algorithme de confiance excessivement opaque, dont les décisions ne pourraient jamais être expliquées aux utilisateurs légitimement refusés, exposerait l'organisation à des frictions opérationnelles significatives et à une perte de confiance envers le dispositif lui-même — une préoccupation d'explicabilité qui rejoint directement celle déjà développée pour la caractéristique d'explicabilité de l'IA digne de confiance dans le parcours NIST AI RMF de cette plateforme, bien qu'appliquée ici à une décision d'accès plutôt qu'à une décision de nature plus large.

## Un tableau de synthèse des sources de données de l'algorithme de confiance

| Source | Ce qu'elle apporte |
|---|---|
| CDM | L'état de sécurité actualisé de l'équipement demandeur |
| Conformité réglementaire | Le respect des exigences applicables |
| Renseignement sur les menaces | Le contexte de menace externe actuel |
| Journaux d'activité | Le comportement historique, pour détecter un écart anormal |
| Politique de gestion des données | Les règles propres aux catégories de données sensibles |
| PKI et gestion des identités | Les attributs d'identité vérifiés du demandeur |

## Le lien avec le module suivant

Cette architecture logique, une fois maîtrisée dans son principe, peut être déployée selon plusieurs approches concrètes différentes, adaptées au contexte technique de chaque organisation — développées au module suivant de ce parcours.
