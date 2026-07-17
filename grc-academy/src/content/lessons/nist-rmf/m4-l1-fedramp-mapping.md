# Le RMF face aux autres référentiels, et son application via FedRAMP

## Comparer le RMF aux référentiels déjà étudiés dans cette plateforme

| Aspect | NIST RMF | NIST CSF 2.0 | ISO 27001 | SOC 2 |
|---|---|---|---|---|
| Nature | Processus obligatoire (contexte fédéral américain) | Cadre volontaire | Norme certifiable | Rapport d'attestation |
| Décision centrale | Autorisation formelle par un AO nommément désigné | Aucune décision formalisée par le cadre lui-même | Certification par un organisme accrédité | Opinion d'audit par un cabinet CPA |
| Niveau de prescription | Très élevé (SP 800-53, plus de 1000 contrôles) | Faible (résultats de haut niveau) | Modéré (93 contrôles, orienté résultat) | Modéré (contrôles définis par l'organisation) |
| Vocabulaire du risque | Catégorisation FIPS 199, bases de référence de contrôles | Tiers et Profils | Appréciation des risques ISO 31000/27005 | Common Criteria alignés sur COSO |

Ce tableau confirme un principe déjà dégagé dans les parcours précédents de cette plateforme : la rigueur et le niveau de prescription d'un référentiel sont directement corrélés à son origine — un texte né d'une obligation légale stricte (le RMF, la FISMA) tend vers la prescription détaillée et une gouvernance nommément responsabilisée, tandis qu'un cadre volontaire (NIST CSF) ou un rapport d'attestation flexible (SOC 2) laisse davantage de latitude à l'organisation.

## Le mapping entre catalogues de contrôles

Le NIST lui-même publie et maintient des tables de correspondance officielles entre SP 800-53 et d'autres référentiels majeurs, notamment ISO/IEC 27001, permettant à une organisation qui maintient déjà l'un des deux catalogues de contrôles de cartographier son travail vers l'autre sans le dupliquer intégralement — la même logique de mapping plutôt que de duplication déjà développée à plusieurs reprises dans cette plateforme, ici appliquée entre les deux catalogues de contrôles les plus détaillés parmi les référentiels étudiés.

## FedRAMP : le RMF appliqué au cloud

Le **Federal Risk and Authorization Management Program (FedRAMP)**, lancé en 2011, applique directement les principes du RMF aux fournisseurs de services cloud (Cloud Service Providers — CSP) souhaitant héberger des charges de travail d'agences fédérales américaines. C'est l'un des points de convergence les plus concrets entre ce parcours et le module Cloud Security by Design du premier parcours de cette plateforme.

### Les deux voies d'autorisation

- **La voie Agence (Agency Authorization)** — une agence fédérale spécifique sponsorise le processus d'autorisation d'un CSP pour ses propres besoins ; l'agence elle-même joue le rôle d'Authorizing Official.
- **La voie JAB (Joint Authorization Board)** — réservée aux CSP à forte demande potentielle à travers de nombreuses agences, un conseil conjoint (représentants du Department of Defense, du Department of Homeland Security, et de la General Services Administration) délivre une **autorisation provisoire (Provisional Authorization to Operate — P-ATO)**, que chaque agence fédérale peut ensuite adopter par réciprocité (le principe de réciprocité déjà développé au module 1) sans reconduire intégralement le processus d'évaluation.

### Les niveaux d'impact FedRAMP

FedRAMP reprend directement la logique de catégorisation FIPS 199 du RMF (module 1), avec des bases de référence de contrôles FedRAMP spécifiques adaptées au contexte cloud pour les niveaux **Faible, Modéré et Élevé** — le niveau Élevé, en particulier, couvre les données les plus sensibles (données relatives à l'application de la loi, à la santé publique, aux systèmes financiers critiques) et impose la base de référence de contrôles la plus exigeante.

### Le rôle du 3PAO

L'évaluation indépendante (l'étape Assess du RMF, module 1) est réalisée par une **Third-Party Assessment Organization (3PAO)**, un organisme d'évaluation accrédité spécifiquement pour FedRAMP — un rôle comparable, dans sa fonction d'indépendance, au cabinet d'audit SOC 2 ou à l'organisme de certification ISO 27001 déjà rencontrés dans les parcours précédents de cette plateforme, à la différence que l'accréditation FedRAMP est gérée par un programme fédéral dédié plutôt que par un organisme national d'accréditation généraliste.

### La surveillance continue mensuelle

Une fois l'autorisation FedRAMP obtenue, le CSP doit maintenir un programme de surveillance continue avec des livrables **mensuels** transmis à l'agence sponsor ou au JAB : résultats de scans de vulnérabilités, mise à jour du POA&M, et rapport de l'état des contrôles — une cadence de surveillance nettement plus fréquente et formalisée que le rythme annuel des audits de surveillance ISO 27001 ou même que la période d'observation d'un audit SOC 2 Type II, déjà développés dans les parcours précédents de cette plateforme.

## Pourquoi un fournisseur cloud vise souvent plusieurs référentiels simultanément

Un fournisseur de services cloud d'envergure internationale maintient très souvent, simultanément, une certification ISO 27001, un rapport SOC 2 Type II, et une autorisation FedRAMP — chacun répondant à un marché et une exigence différents (marché international pour ISO 27001, marché B2B nord-américain pour SOC 2, marché fédéral américain pour FedRAMP). Comme déjà observé pour la stratégie de mapping entre ISO 27001, NIST CSF et SOC 2 dans les parcours précédents, ce fournisseur ne construit pas trois dispositifs de sécurité distincts : il maintient un socle de contrôles techniques largement commun, avec une couche de documentation spécifique à chaque référentiel pour produire les preuves attendues par chaque processus d'audit ou d'autorisation — une stratégie d'autant plus indispensable que le volume de contrôles exigé par FedRAMP (hérité directement de SP 800-53) est le plus élevé de tous les référentiels étudiés dans cette plateforme.
