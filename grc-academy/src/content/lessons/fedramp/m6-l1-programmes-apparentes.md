# Les programmes apparentés : StateRAMP et les niveaux d'impact du DoD

## Un modèle qui a essaimé au-delà du gouvernement fédéral

Le succès relatif du principe "do once, use many times" de FedRAMP, développé tout au long de ce parcours, a directement inspiré la création de programmes apparentés, adaptés à d'autres échelons de gouvernement ou à d'autres besoins de mission spécifiques au sein même du gouvernement fédéral américain — une dynamique de réplication d'un modèle éprouvé qui rappelle, dans son principe, celle déjà observée pour l'inspiration mutuelle entre référentiels de gestion des risques dans plusieurs parcours de cette plateforme.

## StateRAMP : FedRAMP appliqué aux États américains

**StateRAMP**, lancé en 2021 par une organisation à but non lucratif indépendante du gouvernement fédéral, applique une logique directement calquée sur celle de FedRAMP au niveau des États américains et des collectivités locales, qui n'étaient pas couverts par le programme fédéral d'origine. StateRAMP reprend une architecture très similaire — des niveaux d'impact, des bases de référence de contrôles dérivées de SP 800-53, une évaluation par des organismes tiers accrédités, un registre public des CSP autorisés — tout en reconnaissant explicitement une **équivalence substantielle** avec une autorisation FedRAMP déjà obtenue : un CSP autorisé FedRAMP peut ainsi obtenir une reconnaissance StateRAMP avec un effort supplémentaire nettement réduit, selon un principe de réciprocité inter-programmes qui prolonge celui déjà développé au module 5 de ce parcours au-delà des frontières du seul gouvernement fédéral.

## Les niveaux d'impact du Department of Defense (DoD IL)

Le Department of Defense américain applique, pour ses propres besoins, un dispositif distinct — les **DoD Impact Levels (IL2, IL4, IL5, IL6)**, définis par le **DoD Cloud Computing Security Requirements Guide (SRG)** — qui s'appuie sur les bases de référence FedRAMP comme fondation, tout en y ajoutant des exigences supplémentaires propres au contexte de défense, particulièrement marquées aux niveaux les plus élevés :

- **IL2** — correspond globalement à une autorisation FedRAMP Modéré, pour des informations publiques ou à faible sensibilité.
- **IL4** — s'appuie sur la base FedRAMP Modéré enrichie d'exigences supplémentaires, pour des informations non classifiées contrôlées (Controlled Unclassified Information — CUI).
- **IL5** — s'appuie sur la base FedRAMP Élevé enrichie d'exigences substantiellement renforcées, notamment sur la séparation physique ou logique stricte des données du DoD, pour des informations non classifiées particulièrement sensibles pour la mission de défense.
- **IL6** — réservé aux informations classifiées jusqu'au niveau Secret, avec des exigences d'isolation physique qui dépassent largement le cadre des bases de référence FedRAMP standard.

## Pourquoi cette architecture en couches successives plutôt qu'un dispositif entièrement distinct

Cette architecture, dans laquelle chaque niveau d'impact du DoD s'appuie explicitement sur une base de référence FedRAMP existante avant d'y superposer des exigences supplémentaires, illustre un principe déjà rencontré à plusieurs reprises dans cette plateforme : plutôt que de construire un dispositif de contrôles entièrement distinct pour chaque contexte de mission, l'écosystème fédéral américain préfère mutualiser un socle commun (les bases de référence FedRAMP) et documenter les écarts supplémentaires propres à chaque contexte — une logique de superposition qui rappelle directement celle des Focus Areas et facteurs de conception de COBIT, ou celle des overlays de contrôles déjà mentionnés au module 1 de ce parcours.

## Un tableau de synthèse des programmes apparentés

| Programme | Portée | Relation avec FedRAMP |
|---|---|---|
| FedRAMP | Agences civiles fédérales et, de facto, l'ensemble du gouvernement fédéral | Programme de référence |
| StateRAMP | États américains et collectivités locales | Reconnaissance d'équivalence substantielle, effort réduit pour un CSP déjà autorisé FedRAMP |
| DoD IL2/IL4 | Besoins du Department of Defense, sensibilité faible à modérée | S'appuie directement sur les bases FedRAMP Modéré |
| DoD IL5 | Informations non classifiées particulièrement sensibles pour la défense | S'appuie sur la base FedRAMP Élevé, enrichie d'exigences substantielles |
| DoD IL6 | Informations classifiées jusqu'au niveau Secret | Dépasse le cadre FedRAMP, exigences d'isolation physique propres au DoD |

## Ce que cette prolifération de programmes apparentés confirme

Cette prolifération de programmes dérivés, chacun reconnaissant explicitement une équivalence substantielle avec FedRAMP plutôt que d'imposer une évaluation entièrement redondante, confirme la solidité du principe de réciprocité au cœur de ce parcours — un CSP qui investit dans une autorisation FedRAMP Élevé robuste amortit cet investissement sur un ensemble de marchés bien plus large que le seul gouvernement fédéral civil, une considération stratégique que le module suivant de ce parcours permet de replacer dans le contexte plus large des autres référentiels déjà étudiés dans cette plateforme.
