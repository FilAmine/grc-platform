# La gouvernance : qui décide, et sur quelle base

## Définir la gouvernance de sécurité

La **gouvernance** est la structure de décision qui définit : qui est responsable de quoi en matière de sécurité et de conformité, comment les décisions sont prises, et comment on vérifie qu'elles sont appliquées. Ce n'est pas un document — c'est un système de responsabilités.

Une gouvernance efficace répond à trois questions pour chaque risque ou obligation :

1. **Qui possède le risque ?** (le "risk owner" — pas l'équipe sécurité par défaut, mais le métier ou la direction concernée)
2. **Qui décide du niveau de risque acceptable ?** (arbitrage, souvent porté par un comité)
3. **Qui vérifie que la décision est appliquée dans le temps ?** (audit interne, contrôle permanent)

## Les structures classiques

### Le comité de sécurité / comité des risques

La plupart des organisations matures mettent en place un comité (mensuel ou trimestriel) réunissant RSSI, DPO, direction métier et parfois direction générale. Son rôle : arbitrer les risques résiduels trop élevés, valider les politiques majeures, suivre les indicateurs (KRI — Key Risk Indicators).

### Le modèle des trois lignes de maîtrise (Three Lines Model)

C'est le modèle de référence (IIA — Institute of Internal Auditors) pour répartir la responsabilité :

- **1ère ligne — les opérationnels** : les équipes qui possèdent et gèrent le risque au quotidien (développeurs, équipes infra, propriétaires de processus métier). Ils appliquent les contrôles.
- **2ème ligne — les fonctions de supervision** : GRC, sécurité, conformité, gestion des risques. Elles définissent le cadre (politiques, méthodologie de risque), challengent la 1ère ligne, et consolident une vision transverse.
- **3ème ligne — l'audit interne** : indépendant des deux premières lignes, il vérifie que le dispositif dans son ensemble fonctionne, sans être impliqué dans sa mise en œuvre.

Ce modèle règle un piège fréquent : confondre "l'équipe sécurité écrit la politique" avec "l'équipe sécurité est responsable de son application". Ce sont les équipes opérationnelles (1ère ligne) qui appliquent — la 2ème ligne fixe le cadre et vérifie, la 3ème ligne audite l'ensemble.

## Politique, standard, procédure : ne pas confondre

Un vocabulaire précis évite des politiques inapplicables :

| Niveau | Rôle | Exemple |
|---|---|---|
| **Politique** | Déclaration d'intention, validée au plus haut niveau, rarement modifiée | "Toute donnée personnelle doit être chiffrée au repos" |
| **Standard** | Exigence mesurable et vérifiable, qui traduit la politique | "Chiffrement AES-256 minimum pour tout volume de stockage contenant des données personnelles" |
| **Procédure** | Étapes opérationnelles précises | "Pour activer le chiffrement sur un bucket S3 : ..." |

Une erreur de gouvernance très commune : rédiger des politiques qui ressemblent à des standards (trop précises, elles deviennent vite obsolètes techniquement) ou des standards qui ressemblent à des politiques (trop vagues, ils ne sont jamais vérifiables en audit).

## Le lien avec Security by Design

La gouvernance fixe l'intention ("nous voulons réduire le risque X à un niveau acceptable Y"). Security by Design est la discipline qui garantit que cette intention se traduit, dès la conception d'un système, en décisions techniques vérifiables — et non en un document que personne ne consulte au moment de choisir une architecture cloud.

C'est pourquoi NIST CSF 2.0 (module suivant) a ajouté en 2024 une fonction entièrement dédiée à ce sujet : **Govern**, placée en amont de toutes les autres, pour rappeler que la gouvernance n'est pas une couche de paperasse ajoutée à la sécurité technique, mais sa condition de cohérence.
