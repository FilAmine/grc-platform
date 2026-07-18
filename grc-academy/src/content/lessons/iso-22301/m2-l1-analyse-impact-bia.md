# L'analyse d'impact sur l'activité (1/2) : la Business Impact Analysis et ses métriques clés

## Le cœur méthodologique du SMCA

L'**analyse d'impact sur l'activité (Business Impact Analysis — BIA)**, exigée par la clause 8.2 d'ISO 22301, constitue l'exercice fondateur de tout système de management de la continuité d'activité — un rôle comparable, dans sa fonction structurante, à celui de l'appréciation des risques dans ISO 27001 ou de l'analyse d'impact relative à la protection des données (AIPD) dans le RGPD, déjà développées dans les parcours dédiés de cette plateforme. La BIA consiste à identifier les activités de l'organisation, à évaluer les conséquences dans le temps d'une interruption de chacune d'entre elles, et à en déduire des priorités de reprise et des ressources minimales nécessaires pour reprendre chaque activité à un niveau acceptable.

## Le concept central de délai maximal d'interruption acceptable (MTPD/MAO)

La BIA introduit un premier concept clé : le **Maximum Tolerable Period of Disruption (MTPD)**, parfois appelé **Maximum Acceptable Outage (MAO)** — le délai au-delà duquel l'interruption d'une activité donnée provoquerait des conséquences jugées inacceptables pour l'organisation (perte financière insupportable, atteinte irréversible à la réputation, manquement à une obligation légale ou contractuelle critique, risque pour la sécurité des personnes). Ce délai varie considérablement d'une activité à l'autre au sein d'une même organisation : le traitement des paiements d'une banque peut avoir un MTPD de quelques minutes, tandis que la production d'un rapport statistique mensuel peut tolérer une interruption de plusieurs semaines sans conséquence significative.

## Le RTO : l'objectif de délai de reprise

À partir du MTPD, l'organisation fixe un **Recovery Time Objective (RTO)** — l'objectif de délai dans lequel elle s'engage à reprendre une activité donnée après une interruption, nécessairement inférieur au MTPD pour conserver une marge de sécurité. Un RTO fixé à un délai proche ou égal au MTPD ne laisse aucune marge d'erreur en situation réelle de crise, où les délais effectivement constatés dépassent presque toujours les prévisions théoriques établies en amont — un principe de marge de sécurité qui rappelle celui déjà développé pour les échéances de remédiation différenciées par gravité dans le parcours FedRAMP de cette plateforme.

## Le RPO : la perte de données maximale tolérable

Pour les activités reposant sur des systèmes d'information, la BIA introduit également le **Recovery Point Objective (RPO)** — le volume maximal de données, exprimé en durée (par exemple, une heure de transactions), que l'organisation accepte de perdre définitivement en cas d'incident, déterminant directement la fréquence des sauvegardes ou de la réplication de données nécessaire pour respecter cet objectif. Un RPO proche de zéro exige une réplication de données quasi instantanée, avec un coût d'infrastructure sensiblement plus élevé qu'un RPO tolérant la perte de plusieurs heures de données — un arbitrage coût/exigence qui rappelle directement celui déjà rencontré pour le choix du niveau d'impact FedRAMP ou du niveau d'évaluation TISAX, proportionnés au besoin réel plutôt que systématiquement maximisés.

## Les ressources minimales à identifier pour chaque activité critique

Au-delà des seuls délais RTO et RPO, la BIA identifie, pour chaque activité jugée critique, les **ressources minimales** nécessaires à sa reprise : effectifs minimaux et compétences requises, systèmes d'information et données indispensables, locaux ou équipements physiques, et dépendances vis-à-vis de tiers externes (fournisseurs, prestataires, partenaires) — une cartographie des dépendances qui rejoint directement la gestion des risques de la chaîne d'approvisionnement déjà développée dans les parcours DORA et NIST RMF de cette plateforme : une activité peut disposer de tous les effectifs et systèmes nécessaires en interne, mais rester bloquée par la défaillance d'un fournisseur critique dont la propre continuité n'a pas été vérifiée.

## Un tableau de synthèse des métriques clés de la BIA

| Métrique | Définition | Ce qu'elle détermine |
|---|---|---|
| MTPD / MAO | Délai au-delà duquel l'interruption devient inacceptable | Le plafond absolu à ne jamais dépasser |
| RTO | Objectif de délai de reprise visé par l'organisation | La rapidité de la stratégie de continuité à mettre en œuvre |
| RPO | Volume de données maximal tolérable à perdre | La fréquence de sauvegarde ou de réplication nécessaire |

## Le lien avec l'appréciation des risques, développée à la leçon suivante

La BIA détermine ce qu'il faut protéger et selon quels délais, mais ne renseigne pas encore sur la probabilité et la nature des menaces susceptibles de provoquer une interruption — c'est l'objet de l'appréciation des risques propre à la continuité d'activité, développée à la leçon suivante de ce parcours, qui complète la BIA pour aboutir à des stratégies de continuité pleinement fondées.
