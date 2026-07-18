# Sanctions contractuelles et PCI DSS face aux autres référentiels

## L'absence de sanction légale directe : la conséquence la plus structurante de la nature contractuelle du référentiel

Ce parcours a insisté, dès le module 0, sur la nature contractuelle plutôt que légale de PCI DSS. Cette nature a une conséquence directe sur le régime de sanctions, radicalement différente de tout ce qui a été développé dans les parcours RGPD, NIS2 et DORA de cette plateforme : le **PCI SSC lui-même n'inflige aucune amende** — ce n'est ni une autorité de contrôle, ni un régulateur public, et il n'en a d'ailleurs pas le pouvoir légal.

## Le mécanisme réel de sanction : des pénalités contractuelles répercutées en cascade

Les sanctions en cas de non-conformité PCI DSS découlent entièrement de la chaîne contractuelle déjà décrite au module 0 : les **marques de cartes** peuvent imposer des pénalités financières aux **banques acquéreuses** avec lesquelles un commerçant ou un prestataire non conforme travaille — des pénalités que la banque acquéreuse répercute ensuite, via son propre contrat, sur le commerçant ou le prestataire fautif. Ces pénalités ne sont **ni publiques, ni plafonnées par un texte réglementaire** comparable aux plafonds du RGPD ou de NIS2 déjà développés dans les parcours dédiés de cette plateforme — leur montant est négocié de gré à gré entre la marque de carte et la banque acquéreuse, puis entre celle-ci et le commerçant, et varie considérablement selon la gravité du manquement, le volume de transactions concerné, et l'existence ou non d'une compromission de données effective.

## Les conséquences au-delà de la seule pénalité financière

Au-delà des pénalités financières contractuelles, une non-conformité PCI DSS peut entraîner :

- une **augmentation des frais de transaction** appliqués par la banque acquéreuse, tant que la non-conformité persiste,
- des **exigences renforcées de validation** (par exemple, le passage d'un simple SAQ à un RoC complet réalisé par un QSA, même pour une entité qui n'y serait normalement pas soumise selon son seul volume de transactions),
- dans les cas les plus graves, en particulier après une compromission de données avérée, la **révocation pure et simple du droit d'accepter les paiements** par carte de la marque concernée — une sanction commerciale radicale, sans équivalent dans les référentiels déjà étudiés dans cette plateforme, où la pire conséquence reste généralement une amende ou une interdiction temporaire d'exercice pour un dirigeant, mais jamais l'exclusion complète et immédiate d'un marché entier.

## Un régime de sanctions qui n'exclut pas d'autres régimes réglementaires

Une non-conformité PCI DSS ayant conduit à une fuite de données personnelles de titulaires de carte peut également déclencher, en parallèle et indépendamment du régime contractuel propre à PCI DSS, une notification et une éventuelle sanction au titre du RGPD (développé dans le parcours dédié de cette plateforme) — les deux régimes, l'un contractuel et sectoriel, l'autre légal et général, s'appliquent cumulativement sans que l'un ne dispense de l'autre, à l'image de ce qui a déjà été observé pour l'articulation entre NIS2 et le RGPD dans le parcours dédié.

## PCI DSS face aux référentiels génériques déjà étudiés dans cette plateforme

| Aspect | PCI DSS | ISO 27001 | NIST CSF |
|---|---|---|---|
| Origine | Consortium industriel privé (PCI SSC) | Organisation internationale de normalisation | Agence fédérale américaine |
| Nature | Exigence contractuelle | Norme certifiable | Cadre volontaire |
| Périmètre | Données de cartes de paiement uniquement | Sécurité de l'information au sens large | Sécurité de l'information au sens large |
| Niveau de prescription | Très élevé, centaines de sous-exigences | Modéré, orienté résultat | Faible, résultats de haut niveau |
| Sanction en cas de non-conformité | Pénalités contractuelles, jusqu'à la révocation du droit d'accepter les paiements | Perte de la certification | Aucune (cadre volontaire) |

Cette comparaison confirme, une fois de plus, un principe déjà dégagé à plusieurs reprises dans cette plateforme : la nature de l'origine d'un référentiel (organisation de normalisation, agence publique, consortium industriel, législateur) détermine directement son niveau de prescription et la nature de ses mécanismes de sanction, bien plus que son contenu technique de fond, largement convergent d'un référentiel à l'autre.

## Le mapping technique avec les référentiels génériques

Bien que le PCI SSC ne publie pas de table de correspondance officielle comparable au Controls Navigator des CIS Controls déjà développé dans le parcours dédié de cette plateforme, la grande majorité des exigences techniques de PCI DSS recoupent directement des contrôles déjà rencontrés dans les autres référentiels de cette plateforme : le contrôle d'accès (exigences 7-8) avec le contrôle 6 des CIS Controls et la famille AC de SP 800-53, la gestion des vulnérabilités (exigence 11) avec le contrôle 7 des CIS Controls, la journalisation (exigence 10) avec la famille AU de SP 800-53. Une organisation déjà certifiée ISO 27001 ou alignée sur les CIS Controls dispose donc, comme observé à de multiples reprises dans cette plateforme pour d'autres référentiels sectoriels, d'une base de contrôles largement réutilisable pour construire sa conformité PCI DSS — à condition d'ajouter les exigences spécifiquement propres au secteur des paiements développées dans ce parcours (protection du PAN, interdiction de conservation des SAD, tests de segmentation).
