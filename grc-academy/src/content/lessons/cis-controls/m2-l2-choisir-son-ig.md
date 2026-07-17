# Choisir son Implementation Group, et la répartition par fonction de sécurité

## Le processus recommandé pour déterminer son groupe cible

Le CIS ne recommande pas de choisir un Implementation Group par pure intuition ou par ambition affichée — la documentation officielle du référentiel propose une série de questions structurantes pour déterminer le profil le plus adapté à une organisation donnée :

- Quel est le **profil de risque** de l'organisation — quel type d'adversaire est raisonnablement susceptible de la cibler, et avec quel niveau de sophistication ?
- Quelle est la **sensibilité des données** traitées, et quel serait l'impact réel d'une atteinte à leur confidentialité, intégrité ou disponibilité ?
- Quelles sont les **ressources disponibles** — budget, personnel dédié à la sécurité, maturité des processus déjà en place ?
- Quelles sont les **obligations réglementaires ou contractuelles** déjà applicables — un point qui recoupe directement la cartographie des obligations développée dans le premier parcours de cette plateforme.

Une petite structure de quelques dizaines de salariés, sans donnée particulièrement sensible et sans exigence réglementaire ou contractuelle forte, se situera raisonnablement à IG1 pour une première itération. Une organisation de taille moyenne engagée dans une démarche ISO 27001 ou SOC 2 (parcours dédiés de cette plateforme) vise généralement IG2 comme socle technique cohérent avec ces démarches. Une organisation critique au sens réglementaire (opérateur d'importance vitale, établissement financier soumis à des exigences renforcées) devrait raisonnablement viser IG3.

## Un point de vigilance : IG1 n'est pas un objectif suffisant pour toute organisation

Une erreur fréquente consiste à considérer IG1 comme une cible universellement acceptable simplement parce qu'elle est présentée comme "essentielle" — alors que le CIS la qualifie explicitement d'hygiène **minimale**, pas de niveau de protection suffisant pour toute organisation. Une entreprise traitant des données de santé ou des données financières sensibles, mais choisissant IG1 uniquement par souci de simplicité ou de coût, s'expose à un niveau de protection manifestement disproportionné par rapport à son profil de risque réel — un piège de sous-évaluation comparable à la catégorisation de complaisance déjà signalée dans le parcours NIST RMF de cette plateforme.

## La répartition des Safeguards par fonction de sécurité (Security Function)

L'attribut de fonction de sécurité, introduit au module 1, permet une analyse complémentaire intéressante : en comptant la répartition des 153 Safeguards entre les cinq fonctions du NIST CSF (Identify, Protect, Detect, Respond, Recover), on observe une concentration nettement plus forte sur **Protect** que sur les autres fonctions — reflet direct de la philosophie du référentiel, largement construite autour de mesures préventives concrètes plutôt que de processus de détection ou de réponse, ces derniers restant néanmoins couverts (notamment par les contrôles 13, 17 du module 1).

Cette répartition déséquilibrée n'est pas un défaut du référentiel — elle reflète une réalité empirique déjà évoquée dans l'introduction de ce parcours : la majorité des attaques opportunistes les plus fréquentes (la cible principale du profil IG1) sont plus efficacement contrées par des mesures préventives simples et bien appliquées (contrôle d'accès, configuration durcie, gestion des correctifs) que par des capacités de détection et de réponse sophistiquées, dont la mise en place suppose une maturité organisationnelle que le profil IG1 ne présuppose justement pas.

## Le CIS Controls Self Assessment Tool (CIS CSAT)

Pour faciliter l'évaluation de sa position par rapport à son Implementation Group cible, le CIS met à disposition un outil gratuit, le **CIS Controls Self Assessment Tool (CSAT)**, qui permet à une organisation de documenter, Safeguard par Safeguard, son niveau de mise en œuvre effective, de suivre sa progression dans le temps, et de visualiser sa couverture par rapport au groupe visé — un outil qui joue, pour les CIS Controls, un rôle comparable à celui d'une matrice de contrôles SOC 2 ou d'une Déclaration d'Applicabilité ISO 27001, déjà développées dans les parcours précédents de cette plateforme, avec l'avantage d'être directement structuré autour des Implementation Groups plutôt que construit entièrement de zéro par chaque organisation.

## Ce que cette logique de priorisation change concrètement pour une petite structure

Pour une organisation qui découvre la gestion de la sécurité de l'information sans expertise GRC interne établie, les Implementation Groups offrent un avantage pratique déterminant par rapport aux autres référentiels déjà étudiés dans cette plateforme : plutôt que de devoir d'abord construire une méthodologie de risque propre (ISO 31000, EBIOS RM) avant même de savoir par où commencer, elle peut directement adopter le profil IG1 comme point de départ éprouvé et reconnu par la communauté de sécurité, puis affiner progressivement sa trajectoire vers IG2 ou IG3 à mesure que sa maturité et ses ressources augmentent — une porte d'entrée nettement plus accessible qu'un premier projet de certification ISO 27001 ou un premier programme SOC 2, déjà développés en détail dans les parcours dédiés de cette plateforme.
