# TISAX en profondeur : introduction et repères

## Un problème déjà rencontré, mais résolu ici par le secteur privé plutôt que par la loi

Le parcours FedRAMP de cette plateforme a déjà développé un problème de duplication des audits de sécurité, résolu par un principe de réciprocité institué par une loi fédérale américaine. L'industrie automobile européenne a connu, au tournant des années 2010, un problème structurellement identique mais dans un contexte entièrement privé : chaque constructeur automobile (Original Equipment Manufacturer — OEM) exigeait de ses fournisseurs et sous-traitants leur propre évaluation de sécurité de l'information, selon des questionnaires et des critères propres à chaque OEM — un fournisseur travaillant simultanément avec plusieurs constructeurs se retrouvait ainsi soumis à des évaluations redondantes, portant très largement sur les mêmes contrôles, sans qu'aucune loi n'impose de mécanisme de mutualisation.

## La réponse de l'industrie : VDA, ENX et la création de TISAX

C'est le **Verband der Automobilindustrie (VDA)**, l'association allemande de l'industrie automobile, qui a porté la création du **Trusted Information Security Assessment Exchange (TISAX)** en 2017, en confiant l'exploitation opérationnelle de l'échange à l'**ENX Association**, un organisme à but non lucratif déjà chargé, depuis les années 2000, de gérer un réseau de télécommunication sécurisé dédié à l'industrie automobile européenne. TISAX applique ainsi, dans un cadre entièrement contractuel et privé plutôt que légal ou réglementaire, un principe directement comparable à celui déjà développé pour FedRAMP : réaliser une évaluation de sécurité une seule fois, puis la partager avec l'ensemble des partenaires commerciaux intéressés — à la différence près, développée plus loin dans ce parcours, que ce partage repose sur un consentement explicite du fournisseur évalué plutôt que sur un registre entièrement public.

## Un référentiel construit sur le catalogue VDA ISA

Au cœur de TISAX se trouve le **VDA Information Security Assessment (VDA ISA)**, un catalogue de contrôles élaboré par le VDA, structuré très largement autour des mêmes domaines que l'Annexe A d'ISO/IEC 27001, déjà développée en détail dans le parcours dédié de cette plateforme, mais enrichi d'exigences spécifiques au secteur automobile — notamment un module entièrement dédié à la **protection des prototypes**, développé au module 5 de ce parcours, qui n'a pas d'équivalent direct parmi les référentiels de sécurité de l'information généralistes déjà étudiés.

## Un dispositif obligatoire de fait, sans fondement légal direct

Contrairement à SOX, RGPD, NIS2 ou DORA, TISAX ne repose sur aucune loi ni aucun règlement : c'est une **exigence contractuelle** imposée par les constructeurs automobiles à leurs fournisseurs, dans une logique qui rappelle directement celle déjà développée pour PCI DSS dans le parcours dédié de cette plateforme — un dispositif d'origine strictement privée et contractuelle, mais dont le caractère de facto obligatoire pour quiconque souhaite vendre à un grand constructeur automobile européen ne laisse, en pratique, guère de marge de choix au fournisseur concerné.

## Trois volets d'évaluation possibles

TISAX ne se limite pas à la sécurité de l'information au sens strict : le catalogue VDA ISA couvre potentiellement trois volets distincts — la **sécurité de l'information** (le volet de base, systématiquement requis), la **protection des prototypes** (pour les fournisseurs manipulant des véhicules ou composants non encore dévoilés publiquement), et la **protection des données à caractère personnel** (un module d'évaluation de conformité au RGPD, déjà développé en détail dans le parcours dédié de cette plateforme, ici intégré comme objectif d'évaluation optionnel au sein du même dispositif TISAX plutôt que comme démarche entièrement séparée).

## Ce que ce parcours couvre

Ce parcours développe le catalogue VDA ISA et le modèle de maturité qui structure son évaluation (module 1), les niveaux d'évaluation (Assessment Levels) et les objectifs d'évaluation disponibles (module 2), le processus d'évaluation et le rôle des Audit Providers accrédités (module 3), le modèle de partage des résultats par labels et consentement explicite ainsi que la durée de validité des évaluations (module 4), le module spécifique de protection des prototypes (module 5), les enjeux contractuels et l'absence de sanction légale directe (module 6), et enfin le mapping avec ISO 27001, le RGPD et les autres référentiels déjà étudiés dans cette plateforme ainsi qu'une feuille de route de mise en conformité (module 7).
