# RGPD : principes fondateurs et obligations

## Un règlement, pas une directive

Le **RGPD** (Règlement Général sur la Protection des Données, 2016/679) est directement applicable dans tous les États membres de l'UE sans transposition nationale — contrairement à une directive. Son champ d'application est extraterritorial : il s'applique dès qu'une organisation traite des données personnelles de résidents de l'UE, **même si l'organisation n'est pas établie en Europe** (article 3).

## Les principes fondateurs (article 5)

Tout traitement de données personnelles doit respecter simultanément :

1. **Licéité, loyauté, transparence** — un traitement doit reposer sur une base légale (consentement, contrat, obligation légale, intérêt légitime, mission d'intérêt public, sauvegarde d'intérêts vitaux) et être compréhensible pour la personne concernée.
2. **Limitation des finalités** — les données sont collectées pour des finalités déterminées, explicites et légitimes, et ne peuvent pas être traitées ultérieurement de manière incompatible avec ces finalités.
3. **Minimisation des données** — seules les données adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités sont collectées. C'est le principe le plus directement traduisible en contrainte technique (voir module 4).
4. **Exactitude** — les données doivent être exactes et tenues à jour ; les données inexactes doivent être effacées ou rectifiées.
5. **Limitation de la conservation** — les données ne sont conservées que le temps nécessaire aux finalités (nécessite une politique de durée de conservation et sa mise en œuvre technique effective — purge automatisée).
6. **Intégrité et confidentialité** — sécurité appropriée contre le traitement non autorisé ou illicite, la perte, la destruction ou les dommages accidentels.
7. **Responsabilité (accountability)** — le responsable de traitement doit être en mesure de **démontrer** le respect des principes précédents, pas seulement de les respecter en théorie.

Ce dernier principe — l'accountability — est ce qui relie le plus directement le RGPD à une logique GRC : il ne suffit pas d'être conforme, il faut pouvoir le prouver, avec une documentation et des preuves d'audit.

## Les droits des personnes concernées

Le RGPD accorde des droits opposables que tout système doit être capable de servir techniquement :

- **Droit d'accès** — obtenir une copie des données traitées.
- **Droit de rectification** — corriger des données inexactes.
- **Droit à l'effacement** ("droit à l'oubli") — sous conditions, obtenir la suppression des données.
- **Droit à la limitation du traitement** — geler temporairement un traitement contesté.
- **Droit à la portabilité** — récupérer ses données dans un format structuré et réutilisable.
- **Droit d'opposition** — s'opposer à certains traitements (notamment le profilage à des fins de marketing direct).

Un système mal conçu (données dupliquées dans des dizaines de systèmes sans registre centralisé, absence de mécanisme de suppression en cascade) rend ces droits pratiquement impossibles à honorer dans les délais légaux (un mois, extensible à trois) — c'est un exemple concret où l'absence de Privacy by Design en amont crée une dette de conformité difficile à rattraper.

## Les obligations clés du responsable de traitement

- **Le registre des traitements** (article 30) — documenter chaque traitement : finalité, catégories de données, destinataires, durée de conservation, mesures de sécurité.
- **L'analyse d'impact relative à la protection des données (AIPD / DPIA)** — obligatoire pour les traitements susceptibles d'engendrer un risque élevé pour les droits et libertés (profilage à grande échelle, données sensibles, surveillance systématique).
- **La notification de violation de données** — à l'autorité de contrôle sous 72h si risque pour les personnes, et aux personnes concernées elles-mêmes si le risque est élevé.
- **Le Data Protection Officer (DPO)** — obligatoire dans certains cas (autorité publique, traitement à grande échelle de données sensibles ou de suivi systématique).
- **Privacy by Design et by Default** (article 25) — l'obligation la plus directement liée à cette formation, détaillée en module 4 : la protection des données doit être intégrée dès la conception du traitement, et les paramètres par défaut doivent être les plus protecteurs.

## Les sanctions

Les amendes administratives peuvent atteindre **20 millions d'euros ou 4 % du chiffre d'affaires annuel mondial**, le montant le plus élevé étant retenu — un niveau de sanction qui place le RGPD parmi les référentiels dont le non-respect a l'impact financier direct le plus significatif, largement au-dessus d'une non-conformité ISO 27001 (qui coûte surtout en opportunités commerciales perdues).
