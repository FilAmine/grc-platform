# La fonction Govern : la nouveauté structurante de CSF 2.0

## Pourquoi une sixième fonction, et pourquoi en premier

Dans les versions 1.0 et 1.1, des éléments de gouvernance existaient déjà, dispersés dans la fonction Identify (catégorie "Governance"). Le CSF 2.0 les a extraits, largement enrichis, et érigés en fonction à part entière, placée délibérément **en premier** dans toute représentation du Core — pas parce que les autres fonctions lui seraient chronologiquement subordonnées, mais parce que Govern **informe la manière dont une organisation met en œuvre les cinq autres fonctions**.

Le NIST justifie ce choix explicitement : la gestion des risques de cybersécurité ne peut pas être une activité purement technique isolée — elle doit être intégrée à la stratégie globale de gestion des risques de l'organisation, avec des attentes claires et une supervision de la direction.

## Les catégories de Govern

### GV.OC — Contexte organisationnel

La mission, les attentes des parties prenantes, les dépendances critiques et les exigences légales/réglementaires/contractuelles sont comprises et priorisent les décisions de gestion du risque. C'est la question "dans quel environnement opérons-nous, et qui sont les parties prenantes dont les attentes comptent" — un préalable à toute analyse de risque sérieuse.

### GV.RM — Stratégie de gestion des risques

Les priorités, contraintes, tolérances au risque et hypothèses de l'organisation sont établies, communiquées, et utilisées pour appuyer les décisions de risque opérationnel. C'est ici que se formalise l'**appétence au risque** — le même concept central que dans la gestion des risques classique (ISO 31000, EBIOS RM).

### GV.RR — Rôles, responsabilités et autorités

Les rôles et responsabilités en matière de cybersécurité sont établis, communiqués et compris, et incluent explicitement la responsabilité de la direction générale et du conseil d'administration — une clarification bienvenue par rapport aux versions précédentes, qui laissaient plus implicite l'implication du niveau exécutif.

### GV.PO — Politique

Les politiques organisationnelles de cybersécurité sont établies, communiquées, et appliquées.

### GV.OV — Supervision (Oversight)

Les résultats des activités de gestion des risques sont utilisés pour informer, améliorer et ajuster la stratégie de gestion des risques — la boucle de retour qui empêche la gouvernance de devenir un exercice figé une fois par an.

### GV.SC — Gestion des risques de la chaîne d'approvisionnement cybersécurité (C-SCRM)

**La catégorie la plus significative ajoutée en 2.0.** Les processus pour identifier, évaluer et gérer les risques de cybersécurité liés à la chaîne d'approvisionnement sont établis et convenus avec les parties prenantes de l'organisation. Concrètement : évaluation de sécurité des fournisseurs et prestataires tiers, exigences contractuelles de sécurité, plan de réponse en cas de compromission d'un tiers, gestion du cycle de vie des composants logiciels tiers (dépendances open source, bibliothèques).

Le déplacement du sujet supply chain vers Govern (plutôt que de le laisser dispersé dans Identify comme en 1.1) reflète une prise de conscience post-incidents majeurs (compromissions par la chaîne logicielle) : la gestion des risques fournisseurs est désormais traitée comme une décision de gouvernance stratégique, pas seulement comme un contrôle opérationnel parmi d'autres.

## Ce que Govern change concrètement dans une organisation

Une organisation qui prend Govern au sérieux ne se contente pas d'écrire une politique de sécurité isolée — elle documente :

- qui, au niveau exécutif, est formellement responsable du risque cybersécurité (pas seulement le RSSI opérationnellement, mais qui rend des comptes au conseil),
- quelle est l'appétence au risque formalisée, utilisée activement pour arbitrer les investissements de sécurité,
- comment les risques liés aux fournisseurs et à la chaîne logicielle sont évalués **avant** la signature d'un contrat, pas seulement après un incident.

## Le lien avec les cinq autres fonctions

Govern n'est pas une fonction isolée qu'on traite une fois puis qu'on oublie — chaque sous-catégorie des cinq autres fonctions (Identify, Protect, Detect, Respond, Recover) est censée être exécutée **dans le cadre** défini par Govern : la stratégie de risque de GV.RM détermine quels actifs identifiés en Identify méritent le plus d'attention ; les rôles définis en GV.RR déterminent qui est responsable d'exécuter les contrôles de Protect ; la supervision de GV.OV consomme les résultats de Detect et Respond pour ajuster la stratégie. C'est cette circulation entre Govern et les autres fonctions qui fait du Core un système cohérent plutôt qu'une liste de cinq domaines indépendants.
