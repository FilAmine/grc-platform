# Les rôles de responsable de traitement et de sous-traitant

## Une distinction directement héritée du RGPD

ISO/IEC 27701 structure l'ensemble de ses contrôles supplémentaires autour d'une distinction de rôle directement empruntée au RGPD, déjà développée en détail dans le parcours dédié de cette plateforme — le **PII Controller (responsable de traitement)**, qui détermine les finalités et les moyens du traitement de données personnelles, et le **PII Processor (sous-traitant)**, qui traite des données personnelles pour le compte et selon les instructions du responsable de traitement. Cette terminologie anglaise (PII pour Personally Identifiable Information) recouvre exactement le même périmètre conceptuel que les données à caractère personnel du RGPD, avec un vocabulaire adapté à un usage international plutôt que strictement européen.

## Pourquoi cette distinction structure l'intégralité de l'Annexe A et de l'Annexe B

Cette distinction de rôle n'est jamais purement théorique dans ISO/IEC 27701 : elle détermine directement quelle Annexe de contrôles s'applique à l'organisation — l'**Annexe A**, développée en détail au module 3 de ce parcours, s'applique exclusivement aux organisations agissant en tant que responsables de traitement ; l'**Annexe B**, développée au module 4, s'applique exclusivement aux organisations agissant en tant que sous-traitants. Une organisation qui cumule les deux rôles pour des traitements différents — par exemple, un fournisseur de services cloud qui traite les données de ses propres employés en tant que responsable de traitement, tout en traitant les données de ses clients en tant que sous-traitant — doit appliquer les deux Annexes simultanément, chacune pour le périmètre de traitement qui lui correspond.

## Le rôle du sous-traitant ultérieur, déjà développé dans le parcours RGPD

ISO/IEC 27701 reconnaît également la situation du **sous-traitant ultérieur (sub-processor)**, déjà esquissée dans le parcours RGPD de cette plateforme à travers l'obligation pour un sous-traitant d'obtenir l'autorisation préalable du responsable de traitement avant de recourir à un sous-traitant ultérieur — une chaîne de sous-traitance qui rappelle directement celle déjà développée pour la cascade contractuelle des exigences TISAX à travers la chaîne d'approvisionnement automobile, ou pour la relation entre CSP et sous-traitants dans FedRAMP, toutes deux développées dans les parcours dédiés de cette plateforme.

## Comment cette distinction se combine avec les rôles déjà développés dans le parcours AI Act

Pour une organisation traitant des données personnelles dans le cadre d'un système d'intelligence artificielle, cette distinction responsable/sous-traitant d'ISO/IEC 27701 se superpose directement à la distinction fournisseur/déployeur déjà développée dans le parcours AI Act de cette plateforme — un fournisseur d'un système d'IA à haut risque traitant des données personnelles agit fréquemment comme sous-traitant vis-à-vis du déployeur qui reste, lui, responsable de traitement au sens du RGPD et d'ISO/IEC 27701. Cette combinaison de rôles multiples, propre à chaque référentiel considéré, illustre la nécessité pour une organisation de cartographier précisément son rôle exact vis-à-vis de chaque cadre réglementaire ou normatif applicable, plutôt que de supposer une cohérence automatique entre eux.

## Pourquoi cette clarification initiale conditionne tout le reste de la démarche

Une organisation qui se tromperait sur son propre rôle — se considérant à tort comme simple sous-traitant alors qu'elle détermine en réalité les finalités du traitement — appliquerait les mauvais contrôles de l'Annexe A ou B, s'exposant à une non-conformité lors de l'audit de certification développé au module 6 de ce parcours. Ce piège de mauvaise qualification initiale rappelle directement celui déjà signalé dans le parcours AI Act de cette plateforme concernant le mécanisme de requalification du déployeur en fournisseur lors d'une modification substantielle d'un système tiers.

## Un tableau de synthèse des deux rôles

| Rôle | Définition | Annexe de contrôles applicable |
|---|---|---|
| PII Controller (responsable de traitement) | Détermine les finalités et les moyens du traitement | Annexe A |
| PII Processor (sous-traitant) | Traite les données pour le compte du responsable, selon ses instructions | Annexe B |
| Sous-traitant ultérieur | Traite les données pour le compte d'un sous-traitant, avec autorisation préalable | Annexe B, avec exigences contractuelles renforcées |

## Le lien avec le module suivant

Une fois ce rôle précisément clarifié, l'organisation peut engager la mise en œuvre des contrôles qui lui sont applicables — en commençant par ceux de l'Annexe A, développés en détail au module suivant de ce parcours.
