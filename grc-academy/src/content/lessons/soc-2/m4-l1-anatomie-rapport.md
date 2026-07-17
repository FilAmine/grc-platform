# Anatomie complète d'un rapport SOC 2

## Un document structuré en sections normalisées

Un rapport SOC 2, qu'il soit Type I ou Type II, suit une structure en sections largement standardisée d'un cabinet d'audit à l'autre — une fois qu'on sait la lire, on retrouve rapidement l'information recherchée dans n'importe quel rapport SOC 2, quel que soit son émetteur.

### Section I — Assertion de la direction (Management's Assertion)

La direction de l'organisation auditée déclare formellement que la description du système présentée en section III est fidèle, et que les contrôles décrits étaient (Type I) ou ont été (Type II) adaptés pour atteindre les objectifs des critères retenus. C'est la direction de l'entité auditée — pas l'auditeur — qui porte la responsabilité première de cette assertion ; le rôle de l'auditeur est précisément de l'examiner et de donner son opinion indépendante dessus.

### Section II — Rapport de l'auditeur de service indépendant (Independent Service Auditor's Report)

C'est le rapport d'audit proprement dit : l'opinion de l'auditeur (développée au module 3), le périmètre de l'examen, la période couverte (Type II), les responsabilités respectives de la direction et de l'auditeur, et toute réserve ou exception significative. C'est la section la plus courte du document mais la plus scrutée par un lecteur pressé — elle contient, en quelques paragraphes, la conclusion de l'ensemble de l'exercice.

### Section III — Description du système (Description of the System)

La section la plus longue et la plus riche d'information du rapport. Les critères de description (Description Criteria, DC1 à DC9) exigent qu'elle couvre notamment :

- **DC1** — les services fournis par l'organisation,
- **DC2** — les principaux engagements de service et exigences système,
- **DC3** — les composants du système : infrastructure, logiciels, personnes, procédures et données,
- **DC4** — les limites (boundaries) du système couvert par le rapport,
- **DC5** — la manière dont le système capture et traite les événements pertinents,
- **DC6** — les engagements liés à l'intégrité de traitement, le cas échéant,
- **DC7** — les contrôles mis en correspondance avec les critères retenus,
- **DC8** — les contrôles complémentaires attendus de l'entité utilisatrice (CUEC, développés plus bas),
- **DC9** — les contrôles complémentaires attendus d'une organisation sous-traitante (CSOC, développés plus bas).

C'est cette section qui permet à un client de comprendre précisément quel périmètre technique et organisationnel est réellement couvert par le rapport — un point de vigilance essentiel, car un rapport SOC 2 peut légitimement exclure des systèmes ou des filiales hors du périmètre défini, sans que cela n'apparaisse ailleurs que dans cette description détaillée.

### Section IV — Description des tests des contrôles et de leurs résultats (Type II uniquement)

Propre au Type II, cette section liste, contrôle par contrôle, la méthode de test utilisée par l'auditeur (enquête, observation, inspection, réexécution — module 3) et le résultat obtenu, y compris toute exception relevée. C'est la section qui permet à un lecteur exigeant (souvent l'équipe sécurité d'un client, pas seulement ses acheteurs) de vérifier la rigueur réelle de l'audit, plutôt que de se fier uniquement à l'opinion résumée en section II.

### Section V — Autres informations fournies par la direction (optionnelle, non auditée)

Une section facultative où la direction peut ajouter des informations complémentaires, non couvertes par l'opinion de l'auditeur — par exemple, la réponse détaillée de la direction à une exception relevée en section IV, ou des informations sur des projets d'amélioration en cours. Le lecteur doit garder à l'esprit que le contenu de cette section, à la différence des sections précédentes, n'est **pas** couvert par l'opinion d'audit.

## Les contrôles complémentaires : CUEC et CSOC

### CUEC — Complementary User Entity Controls

Des contrôles que l'organisation auditée attend de ses **clients** pour que l'ensemble du dispositif de sécurité fonctionne comme prévu — par exemple, "le client est responsable de la gestion de ses propres comptes utilisateurs au sein de l'application" ou "le client est responsable de configurer les paramètres de sécurité optionnels mis à sa disposition". Un client qui reçoit un rapport SOC 2 de son fournisseur doit vérifier qu'il satisfait bien les CUEC qui le concernent — sans quoi il porte lui-même une part du risque que le rapport ne couvre pas.

### CSOC — Complementary Subservice Organization Controls

Des contrôles attendus d'une **organisation sous-traitante** dont dépend le service audité — typiquement un fournisseur cloud sous-jacent (AWS, Azure, GCP). C'est ici qu'intervient le choix entre deux méthodes de traitement des sous-traitants :

- **Méthode de l'exclusion (carve-out method)** — les contrôles du sous-traitant sont exclus du périmètre d'audit ; le rapport documente les CSOC attendus de ce sous-traitant, et le client doit obtenir une assurance séparée sur ce sous-traitant (généralement le propre rapport SOC 2 du fournisseur cloud lui-même) pour disposer d'une image complète.
- **Méthode inclusive (inclusive method)** — les contrôles du sous-traitant sont directement inclus et testés dans le périmètre du rapport, ce qui suppose une coopération étroite entre l'auditeur de l'organisation et le sous-traitant lui-même (rarement utilisée pour de grands fournisseurs cloud, plus fréquente pour des sous-traitants plus petits et directement accessibles à l'audit).

La méthode de l'exclusion est de très loin la plus fréquente en pratique pour les fournisseurs cloud majeurs, qui publient eux-mêmes leur propre rapport SOC 2 couvrant leur infrastructure — un exemple concret et direct du modèle de responsabilité partagée développé dans le premier parcours de cette plateforme : le rapport SOC 2 d'une organisation cliente d'un cloud public documente explicitement, via les CSOC, la frontière entre ce que son propre audit couvre et ce qui reste couvert par l'audit du fournisseur cloud sous-jacent.

## Pourquoi savoir lire cette structure change la manière d'évaluer un fournisseur

Un acheteur ou un responsable sécurité qui reçoit le rapport SOC 2 d'un fournisseur ne devrait jamais se contenter de vérifier l'opinion en section II — une lecture rigoureuse examine la section III pour vérifier que le périmètre couvre bien les systèmes réellement utilisés, la section IV (en Type II) pour évaluer la sévérité des exceptions relevées, et les CUEC/CSOC pour comprendre précisément quelle part du risque reste à sa charge ou à celle d'un sous-traitant non directement couvert par ce rapport.
