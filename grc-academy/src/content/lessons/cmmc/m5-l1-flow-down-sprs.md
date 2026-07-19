# La cascade dans la chaîne d'approvisionnement et le SPRS

## Une exigence qui se propage à travers l'ensemble de la chaîne de sous-traitance

CMMC impose que les exigences de certification se propagent, par un mécanisme appelé **flow-down**, à travers l'ensemble de la chaîne d'approvisionnement de la défense — un maître d'œuvre (prime contractor) directement titulaire d'un contrat avec le Department of Defense doit exiger de chacun de ses sous-traitants manipulant des informations non classifiées contrôlées qu'ils obtiennent eux-mêmes le niveau de certification CMMC approprié à leur propre périmètre de traitement. Cette cascade contractuelle à travers la chaîne d'approvisionnement rappelle directement celle déjà développée pour TISAX à travers la chaîne d'approvisionnement automobile, ou pour les sous-traitants ultérieurs d'ISO/IEC 27701, toutes deux développées dans les parcours dédiés de cette plateforme.

## Pourquoi cette cascade constitue le cœur de la logique du programme

Cette propagation systématique répond directement au constat qui a motivé la création de CMMC développée au module 0 de ce parcours — les incidents majeurs de perte d'informations sensibles provenaient fréquemment non pas des plus grands industriels de défense, disposant de ressources de sécurité substantielles, mais de leurs sous-traitants de rang inférieur, moins bien équipés et moins rigoureusement contrôlés. Un dispositif qui ne s'appliquerait qu'aux seuls maîtres d'œuvre directement titulaires d'un contrat fédéral, sans jamais s'étendre à leurs sous-traitants effectivement en contact avec les informations sensibles, laisserait ainsi subsister précisément la vulnérabilité que CMMC cherche à corriger.

## Le Supplier Performance Risk System comme registre centralisé

Les résultats des évaluations CMMC — qu'elles proviennent d'une auto-évaluation, d'un C3PAO ou du DIBCAC, toutes développées au module 3 de ce parcours — sont soumis dans le **Supplier Performance Risk System (SPRS)**, une plateforme centralisée gérée par le Department of Defense qui recense le statut de conformité de l'ensemble des contractants de la base industrielle de défense. Ce registre joue, pour l'écosystème CMMC, un rôle comparable à celui du FedRAMP Marketplace développé dans le parcours dédié de cette plateforme — un registre centralisé permettant aux maîtres d'œuvre de vérifier rapidement le statut de conformité de leurs sous-traitants potentiels, plutôt que de devoir reconduire eux-mêmes une vérification complète.

## Une visibilité restreinte aux acteurs légitimement concernés, plutôt qu'un registre entièrement public

Contrairement au FedRAMP Marketplace, entièrement public et consultable par toute agence fédérale sans restriction, le SPRS reste accessible uniquement aux acteurs légitimement impliqués dans la chaîne contractuelle concernée — le gouvernement fédéral lui-même, et les maîtres d'œuvre ayant un besoin contractuel légitime de vérifier le statut de leurs propres sous-traitants. Cette restriction d'accès rappelle davantage celle déjà développée pour le KYC Registry de SWIFT CSP, fondé sur les relations de correspondance bancaire préexistantes, que le registre entièrement public de FedRAMP, tous deux développés dans les parcours dédiés de cette plateforme.

## La responsabilité du maître d'œuvre dans la vérification de ses sous-traitants

Un maître d'œuvre demeure responsable de vérifier que chacun de ses sous-traitants dispose effectivement du niveau de certification CMMC requis avant de lui confier des informations non classifiées contrôlées — une responsabilité qui rappelle directement celle déjà développée pour la vérification de la conformité des prestataires dans les Architecture Types A2 et A3 de SWIFT CSP, ou pour les contrôles complémentaires attendus de l'entité utilisatrice des rapports SOC 1 développés dans le parcours SOX de cette plateforme : la responsabilité de la conformité ne se délègue jamais entièrement à un sous-traitant, même certifié.

## Un exemple concret de cette cascade en action

Un grand industriel de l'aérospatiale, maître d'œuvre d'un programme militaire majeur, exigerait ainsi de chacun de ses sous-traitants de rang 1 fournissant des composants sensibles qu'ils obtiennent une certification de niveau 2, et vérifierait leur statut via le SPRS avant toute attribution de contrat — ces mêmes sous-traitants de rang 1, s'ils recourent eux-mêmes à des sous-traitants de rang 2 manipulant des informations non classifiées contrôlées, devraient à leur tour répercuter cette même exigence, selon une cascade qui peut ainsi s'étendre sur plusieurs niveaux de sous-traitance successifs.

## Un tableau de synthèse

| Élément | Fonction |
|---|---|
| Flow-down | Propagation contractuelle de l'exigence de certification à travers la chaîne de sous-traitance |
| SPRS | Registre centralisé du statut de conformité, à accès restreint aux acteurs légitimes |
| Responsabilité du maître d'œuvre | Vérifier le statut de ses sous-traitants avant toute attribution de contrat |

## Le lien avec le module suivant

Cette cascade de responsabilités s'articule directement avec une obligation contractuelle plus large déjà en vigueur avant même la création de CMMC — la clause DFARS 252.204-7012, développée au module suivant de ce parcours.
