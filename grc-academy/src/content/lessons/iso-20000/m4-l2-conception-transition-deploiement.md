# La conception, la construction et la transition des services (2/2) : de la conception au déploiement

## Un processus qui encadre l'introduction ou la modification substantielle d'un service

Au-delà de la gestion des changements ponctuels développée à la leçon précédente de ce parcours, ISO/IEC 20000 impose un processus plus large encadrant la **conception, la construction et la transition** de nouveaux services ou de modifications substantielles de services existants — un processus qui reprend, sous une forme certifiable, les pratiques de conception et transition des services et de gestion des mises en production et des déploiements déjà développées dans le parcours ITIL de cette plateforme.

## La conception du service

La phase de conception impose de traduire les besoins identifiés lors de la planification des services, développée au module 2 de ce parcours, en spécifications précises — les caractéristiques fonctionnelles attendues, les exigences de disponibilité et de performance, les besoins de capacité anticipés, et les mesures de sécurité de l'information nécessaires, développées plus en détail au module 6 de ce parcours. Cette phase de conception doit intégrer ces considérations dès l'origine plutôt que de les ajouter après coup — un principe de prévention précoce déjà rencontré à de multiples reprises dans cette plateforme, notamment pour l'ingénierie de la vie privée du NIST Privacy Framework ou l'appréciation d'impact des systèmes d'IA d'ISO/IEC 42001.

## Le test et la validation avant mise en production

ISO/IEC 20000 impose que tout nouveau service ou modification substantielle fasse l'objet de tests rigoureux avant sa mise en production effective — vérifier que le service fonctionne conformément à sa conception, dans des conditions représentatives de son usage réel, avant d'exposer les utilisateurs finaux à un service potentiellement défaillant. Cette exigence de validation préalable rejoint directement celle déjà développée pour les tests exigés par l'article 9 de l'AI Act avant la mise sur le marché d'un système à haut risque, ou pour l'évaluation de conformité de FedRAMP avant l'autorisation d'un système cloud, tous deux développés dans les parcours dédiés de cette plateforme.

## La gestion des mises en production et des déploiements

Cette exigence couvre la planification précise du déploiement d'un nouveau service ou d'une modification substantielle — le calendrier de déploiement, les ressources mobilisées, la communication vers les utilisateurs concernés, et les critères précis permettant de considérer le déploiement comme réussi. Un déploiement mal planifié, même techniquement fonctionnel, peut engendrer une confusion significative chez les utilisateurs finaux ou une charge disproportionnée sur les équipes de support au moment du lancement — une préoccupation qui rejoint directement celle déjà développée pour la transparence envers les déployeurs de l'AI Act, développée dans le parcours dédié de cette plateforme.

## L'articulation avec la gestion des changements développée à la leçon précédente

Il est utile de préciser que ce processus de conception, construction et transition s'articule directement avec la gestion des changements développée à la leçon précédente de ce parcours, sans jamais s'y substituer : la mise en production effective d'un nouveau service ou d'une modification substantielle passe toujours, in fine, par le processus de gestion des changements, qui vérifie l'autorisation appropriée et la disponibilité d'un plan de retour arrière, quelle que soit l'ampleur du travail de conception et de test qui l'a précédée.

## Un exemple concret illustrant l'ensemble du processus

Le déploiement d'un nouveau service de visioconférence d'entreprise suivrait ainsi une conception précisant les exigences de disponibilité et de capacité attendues compte tenu du nombre d'utilisateurs simultanés anticipés, une phase de test impliquant un groupe pilote représentatif avant le déploiement généralisé, une planification précise du calendrier de déploiement par vagues successives plutôt qu'une bascule uniforme et simultanée pour l'ensemble de l'organisation, et enfin une autorisation formelle via le processus de gestion des changements avant chaque vague de déploiement.

## Un tableau de synthèse de ce processus

| Étape | Ce qu'elle produit |
|---|---|
| Conception | Des spécifications précises intégrant disponibilité, capacité et sécurité dès l'origine |
| Test et validation | La vérification du fonctionnement conforme avant exposition des utilisateurs finaux |
| Gestion des mises en production | Un déploiement planifié, communiqué, et évalué selon des critères de succès précis |

## Le lien avec le module suivant

Une fois un service conçu, construit et déployé, l'organisation doit encore assurer sa résolution rapide en cas d'incident et la satisfaction des demandes des utilisateurs qui en bénéficient au quotidien — l'objet du module suivant de ce parcours.
