# SWIFT CSP face aux autres référentiels, et une feuille de route de mise en conformité

## SWIFT CSP comparé aux référentiels déjà étudiés dans cette plateforme

| Aspect | SWIFT CSP | TISAX | PCI DSS | DORA |
|---|---|---|---|---|
| Nature | Dispositif contractuel coopératif (SWIFT) | Dispositif contractuel sectoriel (automobile) | Dispositif contractuel sectoriel (cartes de paiement) | Règlement européen |
| Périmètre couvert | Infrastructure locale de connexion au réseau de messagerie | Sécurité de l'information, prototypes, données | Environnement de données de cartes de paiement | Résilience opérationnelle numérique du secteur financier |
| Vérification | Auto-attestation corroborée par audit interne ou évaluateur externe | Audit Provider accrédité par l'ENX Association | Qualified Security Assessor ou SAQ selon le niveau | Autorités de supervision prudentielle |
| Mode de diffusion des résultats | KYC Registry, visible par les contreparties de correspondance | Portail ENX, consentement explicite bilatéral | Attestation de conformité, diffusion contractuelle | Non applicable (obligation continue) |
| Sanction en cas de non-conformité | Dégradation des relations de correspondance, signalement possible aux autorités | Perte d'accès au marché automobile | Amendes contractuelles, révocation du droit d'accepter les paiements | Amendes administratives, supervision directe des prestataires critiques |

Ce tableau confirme, une fois de plus, un principe déjà établi à travers les parcours précédents de cette plateforme : la nature de l'origine d'un référentiel — ici, une coopérative financière mondiale répondant à un incident de fraude retentissant — détermine directement son mode de gouvernance et de sanction, avec, dans le cas de SWIFT CSP, une position singulière entre le contractuel pur et le quasi réglementaire du fait de la passerelle vers les autorités de supervision développée au module 5 de ce parcours.

## Le mapping avec ISO 27001 et les CIS Controls comme socle technique réutilisable

Comme développé au module 1 de ce parcours, une organisation déjà certifiée ISO 27001 ou déjà alignée sur les CIS Controls, tous deux développés dans les parcours dédiés de cette plateforme, dispose d'un socle de contrôles techniques (segmentation réseau, authentification multifacteur, gestion des vulnérabilités, journalisation) directement réutilisable pour satisfaire une large part du CSCF — une stratégie de mapping plutôt que de duplication déjà rencontrée à de multiples reprises dans cette plateforme, ici appliquée à un catalogue plus resserré et plus spécifiquement orienté vers l'infrastructure de connexion à un réseau de messagerie financière.

## Le mapping avec DORA et SOX pour les institutions financières et les émetteurs cotés

Une institution financière européenne soumise à DORA, ou un émetteur coté américain soumis à SOX, tous deux développés dans les parcours dédiés de cette plateforme, retrouve dans SWIFT CSP une préoccupation complémentaire mais distincte de ses obligations déjà couvertes : DORA porte sur la résilience opérationnelle numérique de l'ensemble de l'entité financière, SOX porte sur la fiabilité du reporting financier et les contrôles généraux informatiques associés, tandis que SWIFT CSP se concentre spécifiquement sur l'infrastructure technique de connexion au réseau de messagerie interbancaire — trois préoccupations complémentaires qui, ensemble, couvrent des dimensions différentes mais convergentes de la fiabilité et de la sécurité d'une institution financière.

## Les pièges les plus fréquents dans une démarche SWIFT CSP

- **Mal identifier son propre type d'architecture** — un choix erroné du type d'architecture (module 1 de ce parcours) conduit à une évaluation incorrecte du périmètre de contrôles réellement applicables, avec un risque de sous-évaluation de sa propre responsabilité.
- **Négliger la vérification de la conformité des prestataires** pour les architectures A2, A3 ou B — un piège déjà signalé au module 1 de ce parcours, rappelant celui des Complementary User Entity Controls déjà développé dans le parcours SOX.
- **Traiter l'attestation KYC-SA comme une simple formalité annuelle** plutôt que comme un exercice de vérification substantiel, exposant l'organisation à une non-conformité découverte tardivement par une contrepartie via le KYC Registry.
- **Sous-estimer l'effort de mise en conformité aux nouveaux contrôles obligatoires** introduits par chaque révision annuelle du CSCF, un piège déjà signalé au module 6 de ce parcours.

## Une feuille de route réaliste de première mise en conformité

1. **Déterminer précisément son type d'architecture** (A1, A2, A3 ou B) et le périmètre de contrôles CSCF qui en découle (module 1 de ce parcours).
2. **Réaliser une auto-évaluation préalable** au regard des contrôles obligatoires et consultatifs des trois objectifs du CSCF (module 2), en s'appuyant sur la documentation ISO 27001 ou CIS Controls existante le cas échéant.
3. **Combler les écarts identifiés**, en documentant un plan de remédiation pour tout contrôle obligatoire non pleinement implémenté.
4. **Choisir la voie de corroboration** la plus adaptée — audit interne indépendant ou évaluateur externe qualifié (module 3) — et conduire la vérification.
5. **Soumettre l'attestation KYC-SA** sur le KYC Registry (module 4), en anticipant sa consultation par les contreparties de correspondance bancaire.
6. **Planifier le cycle annuel de renouvellement**, en intégrant l'analyse des nouveaux contrôles obligatoires introduits par chaque révision annuelle du CSCF (module 6).

## En clôture de ce parcours

Ce parcours a couvert SWIFT CSP de bout en bout : ses origines dans l'incident de la banque centrale du Bangladesh et la nature coopérative de SWIFT, les types d'architecture qui déterminent le périmètre de contrôles applicables, la structure du CSCF en trois objectifs de sécurité et deux catégories de contrôles, le processus d'auto-attestation KYC-SA et les deux voies de corroboration indépendante, le KYC Registry et le mécanisme de partage entre contreparties bancaires, la double sanction commerciale et quasi réglementaire, l'évolution annuelle du catalogue, et enfin son articulation avec les autres référentiels déjà étudiés dans cette plateforme. Combiné aux dix-huit autres parcours de cette plateforme, vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels, méthodes et réglementations majeurs qui structurent une démarche GRC moderne — de la gouvernance financière la plus ancienne (SOX, 2002) jusqu'à la sécurité de l'infrastructure la plus critique de la finance mondiale, le réseau de messagerie interbancaire SWIFT.
