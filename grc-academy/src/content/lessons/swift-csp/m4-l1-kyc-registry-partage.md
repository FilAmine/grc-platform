# Le KYC Registry et le partage entre correspondants bancaires

## Une plateforme née d'un besoin plus large que la seule sécurité

Le **KYC Registry** de SWIFT n'a pas été conçu à l'origine spécifiquement pour le Customer Security Programme : cette plateforme préexistante permettait déjà aux institutions financières de partager entre elles des informations de connaissance client (Know Your Customer) nécessaires à leurs obligations de lutte contre le blanchiment d'argent, dans le cadre de leurs relations de banque correspondante. Le Customer Security Programme a été intégré à cette infrastructure existante à travers l'application **KYC-SA**, déjà développée au module 3 de ce parcours, plutôt que de créer une plateforme entièrement nouvelle et dédiée — un choix pragmatique de réutilisation d'infrastructure qui rappelle, dans son principe d'économie de moyens, celui déjà rencontré pour l'intégration du module de protection des données au sein du même dispositif TISAX plutôt que par une démarche RGPD entièrement séparée.

## Un mécanisme de partage fondé sur la relation de correspondance bancaire

Contrairement au FedRAMP Marketplace, un registre entièrement public, ou au portail ENX de TISAX, où le partage repose sur une invitation bilatérale explicite entre un fournisseur et chacun de ses partenaires, le KYC Registry structure la visibilité des attestations autour des **relations de correspondance bancaire préexistantes** : une institution financière qui entretient une relation de correspondant avec une autre institution peut consulter son statut d'attestation CSCF dans le cadre de sa propre diligence raisonnable, sans nécessiter une invitation ponctuelle distincte pour chaque consultation — un mécanisme qui s'appuie ainsi directement sur les relations commerciales et de confiance déjà établies au sein de la communauté SWIFT plutôt que sur un registre ouvert à tout tiers intéressé.

## Ce que révèle une attestation consultée par une contrepartie

Une contrepartie consultant le statut d'attestation d'une institution partenaire découvre typiquement le niveau global de conformité déclaré (attestation complète, attestation avec plans de remédiation en cours pour certains contrôles obligatoires, ou défaut d'attestation), la voie de corroboration retenue (audit interne ou évaluateur externe, développées au module 3 de ce parcours), et la date de la dernière attestation soumise — une transparence qui permet à chaque institution d'intégrer le niveau de maturité de sécurité de ses contreparties dans ses propres décisions de gestion du risque de contrepartie, au même titre que les critères financiers ou réglementaires traditionnellement pris en compte dans une relation de correspondance bancaire.

## Pourquoi cette transparence entre pairs constitue un mécanisme d'application efficace

Ce mécanisme de transparence entre contreparties constitue, en pratique, l'un des leviers d'application les plus efficaces du dispositif CSP, sans qu'aucune autorité centrale n'ait besoin d'intervenir directement : une institution découvrant qu'une contrepartie n'a pas soumis d'attestation à jour, ou qu'elle affiche des lacunes significatives sur des contrôles obligatoires, peut légitimement restreindre ou renégocier les termes de sa relation de correspondance — un mécanisme d'application par les pairs qui rappelle, dans son principe de pression exercée par l'écosystème plutôt que par une autorité centrale unique, celui déjà développé pour la cascade d'exigences contractuelles à travers la chaîne d'approvisionnement automobile dans le parcours TISAX de cette plateforme.

## Un tableau comparatif des mécanismes de partage déjà rencontrés dans cette plateforme

| Référentiel | Mécanisme de partage | Fondement de la visibilité |
|---|---|---|
| FedRAMP | Marketplace public | Registre ouvert, consultable par toute agence fédérale |
| TISAX | Portail ENX, invitation bilatérale | Consentement explicite du fournisseur, partenaire par partenaire |
| SWIFT CSP | KYC Registry | Relation de correspondance bancaire préexistante |

## Le lien avec le module suivant

Cette transparence entre contreparties bancaires n'est cependant pas le seul mécanisme d'application du dispositif CSP — SWIFT elle-même conserve la capacité, dans certaines circonstances, de signaler directement le défaut de conformité d'un utilisateur aux autorités de régulation compétentes, un pont vers la supervision réglementaire développé au module suivant de ce parcours.
