# Le NIST Privacy Framework face aux autres référentiels, et une feuille de route de mise en œuvre

## Le NIST Privacy Framework comparé aux référentiels déjà étudiés dans cette plateforme

| Aspect | NIST Privacy Framework | NIST CSF | RGPD | ISO/IEC 27701 |
|---|---|---|---|---|
| Nature | Cadre volontaire | Cadre volontaire | Règlement européen obligatoire | Norme certifiable, extension d'ISO 27001 |
| Objet central | Risque vie privée pour les individus, distinct du risque de sécurité | Risque de sécurité de l'information | Protection des données personnelles, droits des personnes | Système de gestion de la vie privée (PIMS) |
| Structure | Core (5 fonctions), Profils, Tiers | Core (6 fonctions), Profils, Tiers | Bases légales, droits, obligations du responsable/sous-traitant | Extension des clauses et contrôles d'ISO 27001/27002 |
| Décision centrale | Aucune (outil de priorisation) | Aucune (outil de priorisation) | Conformité légale, sous supervision d'une autorité de contrôle | Certification par un organisme accrédité |
| Sanction en cas de manquement | Aucune (outil volontaire) | Aucune (outil volontaire) | Amendes administratives plafonnées | Perte de certification |

Ce tableau confirme, une fois de plus, un principe déjà établi à travers les parcours précédents de cette plateforme : un outil méthodologique volontaire (NIST Privacy Framework, NIST CSF) et un cadre légal contraignant (RGPD) ne s'opposent jamais, mais se complètent — le premier structure la démarche opérationnelle de gestion du risque, le second impose des obligations légales que cette démarche aide à satisfaire.

## Le mapping avec le NIST CSF, déjà développé tout au long de ce parcours

Comme développé aux modules 0, 2 et 3 de ce parcours, le NIST Privacy Framework partage avec le NIST CSF une architecture identique (Core, Profils, Tiers) et une fonction directement empruntée (Protect-P). Une organisation ayant déjà déployé le CSF, développé en détail dans le parcours dédié de cette plateforme, bénéficie ainsi d'une courbe d'apprentissage considérablement réduite pour adopter le Privacy Framework, et peut réutiliser directement les compétences, les outils et parfois même les équipes déjà mobilisées pour le CSF.

## Le mapping avec le RGPD comme cadre légal de référence

Pour une organisation européenne, le NIST Privacy Framework ne remplace jamais les obligations légales du RGPD déjà développées en détail dans le parcours dédié de cette plateforme, mais leur fournit une structure méthodologique opérationnelle — le registre des traitements du RGPD rejoint directement Identify-P, les droits des personnes concernées rejoignent Control-P, les obligations de transparence de l'article 13 et 14 rejoignent Communicate-P, et l'analyse d'impact relative à la protection des données trouve dans la méthodologie développée au module 1 de ce parcours (data action, problematic data action, préjudice) un outillage substantiel qu'elle ne détaille pas toujours elle-même.

## Le mapping avec ISO/IEC 27701 pour une organisation cherchant une certification

Contrairement au NIST Privacy Framework, **ISO/IEC 27701** constitue une extension certifiable d'ISO 27001, déjà développée dans le parcours dédié de cette plateforme, ajoutant des clauses et contrôles spécifiques à la gestion de la vie privée (Privacy Information Management System — PIMS). Une organisation souhaitant une reconnaissance formelle et certifiable de sa gestion du risque vie privée, plutôt qu'un outil de priorisation interne, se tournera davantage vers ISO/IEC 27701 — le NIST Privacy Framework et ISO/IEC 27701 ne sont cependant jamais mutuellement exclusifs : le premier peut structurer la démarche méthodologique interne, tandis que le second en constitue l'aboutissement certifiable pour les organisations qui en ont besoin vis-à-vis de leurs clients ou partenaires.

## Les pièges les plus fréquents dans une démarche NIST Privacy Framework

- **Confondre risque vie privée et risque de sécurité** — un piège déjà signalé au module 1 de ce parcours, qui conduit une organisation à croire, à tort, que sa maturité en sécurité de l'information suffit à couvrir son risque vie privée.
- **Négliger Govern-P au profit des fonctions plus opérationnelles** — un piège déjà signalé au module 2 de ce parcours, qui conduit à des initiatives ponctuelles non pérennisées faute de gouvernance affirmée.
- **Traiter Control-P comme une simple case à cocher de conformité** — sans disposer de la granularité technique réelle nécessaire pour honorer les capacités de contrôle promises, un piège déjà signalé au module 3 de ce parcours.
- **Négliger la gestion du risque de l'écosystème de traitement des données** — en se concentrant exclusivement sur les systèmes internes de l'organisation, sans étendre la vigilance aux prestataires tiers, un piège déjà signalé au module 5 de ce parcours.

## Une feuille de route réaliste de première mise en œuvre

1. **Établir la gouvernance** au titre de Govern-P — désigner un responsable, formaliser une politique, intégrer le risque vie privée dans la gestion des risques globale de l'organisation (module 2).
2. **Cartographier les données et les data actions** au titre d'Identify-P, en s'appuyant le cas échéant sur un registre des traitements RGPD déjà existant (module 2).
3. **Réaliser l'appréciation du risque vie privée**, en identifiant les problematic data actions les plus susceptibles d'engendrer un préjudice significatif (module 1).
4. **Construire un Current Profile et un Target Profile**, et prioriser les écarts à combler selon la gravité du risque identifié (module 4).
5. **Déployer les capacités de Control-P et Communicate-P**, en vérifiant la granularité technique réelle des mécanismes mis en place (module 3).
6. **Réutiliser directement Protect-P** si le NIST CSF est déjà déployé, plutôt que de dupliquer les contrôles de sécurité (module 3).
7. **Étendre la démarche à l'écosystème de traitement des données**, en évaluant et en encadrant contractuellement les prestataires tiers (module 5).

## En clôture de ce parcours

Ce parcours a couvert le NIST Privacy Framework de bout en bout : le modèle de risque vie privée et la distinction fondamentale avec le risque de sécurité, la chaîne data action / problematic data action / préjudice et sa méthodologie d'appréciation, les cinq fonctions du Core (Govern-P, Identify-P, Control-P, Communicate-P, Protect-P), les Profils et les Implementation Tiers, la gestion des risques de l'écosystème de traitement des données, l'ingénierie de la vie privée comme aboutissement opérationnel du Privacy by Design déjà esquissé dans cette plateforme, et enfin son articulation avec le NIST CSF, le RGPD et ISO/IEC 27701. Combiné aux dix-neuf autres parcours de cette plateforme, vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels, méthodes et réglementations majeurs qui structurent une démarche GRC moderne — de la sécurité de l'information la plus classique jusqu'à la reconnaissance, plus récente mais tout aussi structurante, que le risque pour les personnes dont on traite les données mérite un cadre de gestion à part entière, distinct de la seule sécurité technique.
