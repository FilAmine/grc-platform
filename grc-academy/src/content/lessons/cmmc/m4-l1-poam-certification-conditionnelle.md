# Le Plan of Action and Milestones et la certification conditionnelle

## Un mécanisme déjà rencontré, mais strictement encadré dans son usage

Le parcours FedRAMP de cette plateforme a déjà développé le **Plan of Action and Milestones (POA&M)** comme mécanisme de suivi de la remédiation des faiblesses identifiées lors d'une évaluation. CMMC reprend ce même mécanisme, sous une forme sensiblement plus encadrée : un contractant candidat au niveau 2, évalué par un C3PAO ou par auto-évaluation, peut obtenir une **certification conditionnelle** malgré l'existence de certaines lacunes non résolues, à condition de documenter un plan de remédiation précis et de respecter des règles strictes limitant l'usage de ce mécanisme.

## Un score minimal requis avant tout recours au POA&M

Contrairement au POA&M de FedRAMP, qui ne connaît pas de seuil de score minimal préalable, CMMC exige qu'un contractant atteigne un **score minimal** sur l'ensemble des 110 exigences de SP 800-171 avant même de pouvoir recourir à un plan de remédiation différé pour les lacunes restantes — un contractant trop éloigné de la conformité globale ne peut jamais se contenter de documenter un plan de remédiation pour l'ensemble de ses lacunes, il doit d'abord démontrer un niveau de maturité de base suffisant.

## Des pratiques jamais éligibles à un plan de remédiation différé

CMMC identifie explicitement certaines pratiques du catalogue SP 800-171 comme **jamais éligibles** à un traitement par POA&M, quelles que soient les circonstances — des exigences jugées si fondamentales (par exemple, l'authentification multifacteur pour les accès à privilèges) que leur absence ne peut jamais être différée, même temporairement, sous peine de compromettre l'intégrité même de l'évaluation. Cette exclusion explicite de certaines pratiques rappelle directement celle déjà développée pour les pratiques interdites de l'article 5 de l'AI Act, où aucune mesure d'atténuation ne peut jamais rendre acceptable une pratique fondamentalement prohibée, développée dans le parcours dédié de cette plateforme — bien qu'ici, il ne s'agisse pas d'une interdiction absolue de l'activité elle-même, mais d'une exigence de conformité immédiate et non différable.

## Un délai de remédiation strictement limité

Pour les lacunes effectivement éligibles au mécanisme, CMMC impose un délai de remédiation strictement limité — généralement 180 jours — au-delà duquel la certification conditionnelle expire automatiquement si les lacunes documentées ne sont pas effectivement corrigées et vérifiées. Ce délai resserré, sensiblement plus court que les échéances différenciées par gravité déjà développées pour le POA&M de FedRAMP dans le parcours dédié de cette plateforme, reflète une volonté délibérée de CMMC d'éviter que ce mécanisme ne devienne une voie de contournement durable de la conformité réelle, plutôt qu'un outil de gestion transitoire d'un nombre limité de lacunes mineures.

## Pourquoi cet encadrement strict répond directement à l'échec du modèle précédent

Cet encadrement particulièrement rigoureux du mécanisme de remédiation différée s'explique directement par l'origine même de CMMC développée au module 0 de ce parcours — le programme a précisément été créé en réponse à l'échec d'un modèle d'auto-attestation trop permissif, où des contractants déclaraient une conformité qui ne correspondait pas à leur réalité opérationnelle. Un mécanisme de POA&M trop souple aurait risqué de recréer, sous une forme différente, la même faille structurelle que CMMC cherche précisément à corriger.

## Un exemple concret d'application

Un contractant candidat au niveau 2, évalué par un C3PAO, pourrait ainsi obtenir une certification conditionnelle malgré l'absence de chiffrement complet de certains supports de sauvegarde — à condition d'avoir atteint le score minimal global exigé, de démontrer que cette lacune ne relève pas des pratiques jamais éligibles au POA&M, et de s'engager sur un plan de remédiation précis à mettre en œuvre dans le délai de 180 jours, faute de quoi sa certification serait automatiquement invalidée.

## Un tableau de synthèse du mécanisme

| Élément | Ce qu'il impose |
|---|---|
| Score minimal préalable | Un niveau de conformité de base requis avant tout recours au POA&M |
| Pratiques jamais éligibles | Des exigences fondamentales exclues explicitement du mécanisme |
| Délai de remédiation | Strictement limité, généralement 180 jours |
| Conséquence d'un dépassement | Invalidation automatique de la certification conditionnelle |

## Le lien avec le module suivant

Cette certification, une fois obtenue de façon définitive ou conditionnelle, doit encore être répercutée à travers l'ensemble de la chaîne d'approvisionnement de la défense — un mécanisme de cascade développé au module suivant de ce parcours.
