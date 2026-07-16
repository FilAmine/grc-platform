# Conformité : cartographie réglementaire et audits

## Conformité n'est pas sécurité

Une confusion fréquente : croire qu'être conforme à ISO 27001 ou au RGPD signifie être "en sécurité". C'est faux dans les deux sens :

- On peut être **conforme sans être sécurisé** : cocher toutes les cases d'un audit tout en ayant des contrôles superficiels ou mal appliqués en pratique (le fameux "compliance theater").
- On peut être **sécurisé sans être formellement conforme** : avoir d'excellentes pratiques techniques sans la documentation, les preuves d'audit ou le formalisme exigé par un référentiel.

La conformité est un **langage de preuve** : elle sert à démontrer, à un tiers (client, régulateur, auditeur, partenaire), qu'un niveau de sécurité donné est atteint et maintenu dans le temps. Security by Design vise la réalité technique ; la conformité vise la démonstrabilité de cette réalité.

## Cartographier ses obligations

Avant de choisir un référentiel à suivre, il faut cartographier ce à quoi on est *effectivement* soumis :

- **Obligations légales et réglementaires** : RGPD (si données personnelles de résidents UE), NIS2 (opérateurs de services essentiels/importants en UE), DORA (secteur financier UE), HDS (hébergement de données de santé en France), etc.
- **Obligations contractuelles** : un client grand compte peut exiger SOC 2 Type II ou ISO 27001 comme condition contractuelle, indépendamment de toute obligation légale.
- **Obligations sectorielles** : PCI DSS pour le paiement par carte, HIPAA pour la santé aux États-Unis.
- **Engagements volontaires** : une certification choisie comme argument commercial ou différenciateur (ISO 27001 est souvent dans cette catégorie pour les éditeurs SaaS B2B).

Cette cartographie détermine le référentiel prioritaire — inutile de viser SOC 2 Type II en premier si aucun client ne le demande et qu'aucune loi ne l'impose, alors que le RGPD, lui, s'applique dès qu'on traite des données de résidents européens, sans possibilité de choisir.

## Les types d'audits

### Audit interne

Réalisé par l'organisation elle-même (souvent la 3ème ligne de maîtrise), sans enjeu de certification externe. Sert à préparer les audits externes et à maintenir le dispositif entre deux cycles de certification.

### Audit de certification (externe)

Réalisé par un organisme accrédité (ex. pour ISO 27001). Aboutit à un certificat valable généralement 3 ans, avec des **audits de surveillance** annuels intermédiaires.

### Audit SOC 2

Différent d'une certification : c'est un **rapport d'attestation** produit par un cabinet d'audit (souvent un cabinet comptable habilité), pas un certificat. Il existe deux types :

- **Type I** : évalue si les contrôles sont *conçus* correctement, à un instant T.
- **Type II** : évalue si les contrôles ont *fonctionné efficacement* sur une période (typiquement 6 à 12 mois) — nettement plus exigeant, et c'est celui que les clients sérieux demandent.

## Le cycle PDCA (Plan-Do-Check-Act)

ISO 27001 (comme la plupart des systèmes de management) repose sur ce cycle continu, hérité de la qualité (Deming) :

1. **Plan** : définir le périmètre, la politique, évaluer les risques, sélectionner les contrôles.
2. **Do** : implémenter les contrôles et les processus.
3. **Check** : auditer (interne), mesurer les indicateurs, détecter les écarts.
4. **Act** : corriger les non-conformités, améliorer le dispositif.

La conformité n'est donc jamais un état atteint une fois pour toutes — c'est une boucle. Un système certifié qui arrête de tourner cette boucle (plus de revue de risques, plus d'audit interne) perdra sa certification à l'audit de surveillance suivant, et surtout perdra la protection réelle que la boucle est censée maintenir.

## Ce que retient un auditeur

En pratique, un auditeur cherche des **preuves**, pas des intentions. Une politique qui dit "nous révisons les accès trimestriellement" sans ticket, export ou log démontrant que la revue a eu lieu ne vaut rien en audit. C'est la raison pour laquelle la traçabilité (logs, tickets, versions de documents, dates de validation) est autant un sujet Security by Design — comment le système génère-t-il ces preuves nativement — qu'un sujet de gouvernance.
