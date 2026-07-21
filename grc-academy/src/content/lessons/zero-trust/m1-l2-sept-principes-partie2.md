# Les sept principes fondamentaux (2/2)

## Cinquième principe : la surveillance continue de l'intégrité et de la posture de sécurité

L'organisation doit surveiller et mesurer en continu l'intégrité et l'état de sécurité de l'ensemble des actifs qu'elle possède ou qui lui sont associés — aucun équipement, même précédemment authentifié avec succès, ne doit être considéré comme définitivement fiable sans une vérification continue de son état de sécurité réel (present-il des vulnérabilités connues non corrigées ? un logiciel malveillant a-t-il été détecté depuis la dernière vérification ?). Ce principe rejoint directement celui déjà développé pour la surveillance post-déploiement continue du NIST AI RMF, ou pour le suivi continu de FedRAMP, tous deux développés dans les parcours dédiés de cette plateforme — un dispositif validé à un instant donné n'offre aucune garantie de le demeurer indéfiniment sans vérification continue.

## Sixième principe : l'authentification et l'autorisation sont dynamiques et strictement appliquées avant tout accès

Ce principe impose qu'aucun accès à une ressource ne soit jamais accordé sans un cycle complet d'authentification et d'autorisation, strictement appliqué avant l'octroi de l'accès plutôt que vérifié a posteriori — un cycle qui doit lui-même demeurer dynamique, s'appuyant sur l'authentification multifacteur et sur une réévaluation continue plutôt que sur une validation ponctuelle unique au début d'une session prolongée. Ce principe rejoint directement l'exigence d'authentification multifacteur déjà développée à de multiples reprises dans cette plateforme, notamment pour l'Objectif 2 du CSCF de SWIFT CSP ou pour le contrôle d'accès de la famille correspondante de SP 800-171 dans le parcours CMMC.

## Septième principe : la collecte d'informations pour améliorer la posture de sécurité

L'organisation doit collecter autant d'informations que possible sur l'état actuel de ses actifs, de son infrastructure réseau et de ses communications, et utiliser ces informations pour améliorer continuellement sa posture de sécurité — un principe qui rejoint directement celui déjà développé pour la meilleure information disponible parmi les huit principes d'ISO 31000, ou pour l'exploitation de l'information et de la technologie au titre de COSO ERM, tous deux développés dans les parcours dédiés de cette plateforme.

## Comment ces sept principes s'articulent entre eux comme un système cohérent

Ces sept principes ne fonctionnent jamais isolément les uns des autres — considérer toutes les ressources comme dignes de protection (principe 1) n'a de sens que si chaque accès à ces ressources fait l'objet d'une vérification dynamique et stricte (principe 6), elle-même alimentée par une surveillance continue de la posture de sécurité (principe 5) et par la collecte systématique d'informations (principe 7), permettant à son tour d'affiner la politique dynamique qui détermine chaque décision d'accès (principe 4). Cette interdépendance rappelle directement celle déjà développée pour les quatorze familles de contrôles de SP 800-171 dans le parcours CMMC de cette plateforme, où aucune famille de contrôles ne suffit isolément à garantir une protection réellement efficace.

## Un tableau de synthèse des sept principes

| Principe | Résumé |
|---|---|
| 1 | Toutes les sources de données et services sont des ressources |
| 2 | Toute communication est sécurisée, indépendamment de la localisation réseau |
| 3 | L'accès est accordé sur une base sessionnelle |
| 4 | L'accès est déterminé par une politique dynamique |
| 5 | L'intégrité et la posture de sécurité de tous les actifs sont surveillées en continu |
| 6 | L'authentification et l'autorisation sont dynamiques et strictement appliquées |
| 7 | L'information collectée sert à améliorer continuellement la posture de sécurité |

## Pourquoi ces principes restent volontairement indépendants de toute technologie précise

NIST SP 800-207 formule délibérément ces sept principes sans jamais imposer de technologie ou de produit précis pour les satisfaire — une même organisation peut les implémenter à travers des combinaisons technologiques très différentes, selon son contexte, ses systèmes existants et sa trajectoire de migration. Cette neutralité technologique volontaire rejoint directement celle déjà développée pour les lignes directrices d'ISO 31000, non certifiables et délibérément génériques, développées dans le parcours dédié de cette plateforme.

## Le lien avec le module suivant

Ces sept principes trouvent leur traduction opérationnelle concrète dans une architecture logique à trois composants, qui orchestrent ensemble chaque décision d'accès conformément à ces principes — l'objet du module suivant de ce parcours.
