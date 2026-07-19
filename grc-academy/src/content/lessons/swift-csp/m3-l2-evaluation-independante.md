# L'auto-attestation et l'évaluation indépendante (2/2) : les deux voies de corroboration

## Deux voies possibles, à la discrétion de l'utilisateur

Depuis le renforcement du dispositif évoqué à la leçon précédente, chaque utilisateur SWIFT doit faire corroborer son attestation KYC-SA par l'une de deux voies possibles, à son choix : un **audit interne indépendant**, ou une **évaluation par un assesseur externe qualifié** — une flexibilité de choix qui distingue SWIFT CSP des dispositifs plus rigides déjà étudiés dans cette plateforme, où la voie d'évaluation indépendante est généralement imposée sans alternative (le 3PAO pour FedRAMP, le QSA pour PCI DSS, l'organisme de certification pour ISO 27001).

## La voie de l'audit interne indépendant

Un utilisateur peut recourir à sa propre fonction d'audit interne, à condition que celle-ci soit **fonctionnellement indépendante** de l'équipe informatique responsable de l'implémentation des contrôles CSCF évalués — un principe de séparation des rôles déjà développé à de multiples reprises dans cette plateforme, notamment pour l'audit interne SOX, chargé de tester les contrôles ITGC sans être lui-même partie prenante de leur mise en œuvre opérationnelle. Cette voie convient particulièrement aux grandes institutions financières disposant déjà d'une fonction d'audit interne mature et suffisamment outillée pour couvrir le périmètre technique spécifique du CSCF.

## La voie de l'évaluateur externe qualifié

Pour les utilisateurs ne disposant pas d'une fonction d'audit interne suffisamment indépendante ou compétente sur le périmètre technique du CSCF — notamment les utilisateurs de plus petite taille —, SWIFT permet le recours à un **assesseur externe**, dont la qualification repose sur des critères de compétence et d'indépendance publiés par SWIFT, sans toutefois reposer sur un mécanisme d'accréditation aussi institutionnalisé que celui du 3PAO de FedRAMP ou du QSA de PCI DSS, développés dans les parcours dédiés de cette plateforme. SWIFT maintient néanmoins un répertoire de prestataires d'évaluation ayant démontré leur expérience du CSCF, comparable dans son principe, bien que moins formalisé, au registre des Audit Providers accrédités par l'ENX Association pour TISAX.

## Pourquoi cette flexibilité, moins institutionnalisée que d'autres référentiels de cette plateforme

Cette absence d'un mécanisme d'accréditation aussi rigide que ceux déjà rencontrés dans cette plateforme s'explique directement par la nature coopérative de SWIFT, déjà évoquée au module 0 de ce parcours : SWIFT elle-même n'est pas un régulateur doté d'un pouvoir de sanction administrative, mais une infrastructure mutualisée dont les règles de sécurité, bien que contraignantes, restent gouvernées par consensus au sein de sa communauté d'utilisateurs plutôt que par une autorité centrale unique dotée d'un pouvoir d'accréditation exclusif comparable au FedRAMP PMO ou à l'ENX Association.

## Ce que cette évaluation vérifie concrètement

Que la voie choisie soit l'audit interne ou l'évaluateur externe, l'exercice consiste à vérifier, pour chaque contrôle obligatoire du CSCF déclaré comme implémenté dans l'attestation KYC-SA, l'existence de preuves tangibles de cette implémentation — configuration réseau démontrant la segmentation déclarée, journaux d'authentification multifacteur, résultats de scans de vulnérabilités récents — selon une logique de vérification par la preuve déjà développée à de multiples reprises dans cette plateforme, notamment pour le Stage 2 de la certification ISO 27001 ou l'évaluation sur site AL3 de TISAX.

## Un tableau de synthèse des deux voies de corroboration

| Voie | Qui la conduit | Convient particulièrement à |
|---|---|---|
| Audit interne indépendant | La propre fonction d'audit interne de l'utilisateur, indépendante de l'IT | Les grandes institutions disposant d'un audit interne mature |
| Évaluateur externe qualifié | Un prestataire tiers répondant aux critères de qualification SWIFT | Les utilisateurs de taille plus modeste, sans audit interne suffisamment outillé |

## Le lien avec le module suivant

Une fois l'attestation soumise et corroborée, elle est publiée sur le KYC Registry, où elle devient consultable, selon des règles de partage précises, par les contreparties bancaires de l'utilisateur — un mécanisme développé au module suivant de ce parcours.
