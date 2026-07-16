# Security by Design : shift-left, secure SDLC, threat modeling

## Le principe central : la sécurité est une propriété de conception, pas une couche

**Security by Design** signifie que les décisions de sécurité sont prises au moment où les décisions d'architecture sont prises — pas ajoutées après coup sous forme de pare-feu, de scanner ou de correctif d'urgence. Le principe s'oppose directement à ce qu'on appelle parfois le "bolt-on security" (sécurité "boulonnée" après coup), historiquement dominant et responsable de la majorité des architectures difficiles à sécuriser durablement.

La différence de coût est documentée depuis longtemps (IBM Systems Sciences Institute et d'autres études répétées depuis) : corriger un défaut de sécurité identifié en phase de conception coûte un ordre de grandeur de moins que le corriger en production. Ce n'est pas qu'une question financière — un défaut de conception découvert en production implique souvent une refonte d'architecture, alors que le même défaut identifié en conception ne change qu'un diagramme.

## Shift-left : déplacer la sécurité vers l'amont

"Shift-left" désigne le déplacement des activités de sécurité vers les phases amont du cycle de développement (à gauche sur une frise chronologique classique conception → développement → test → déploiement → exploitation) :

- **En conception** : threat modeling (voir plus bas), revue d'architecture, choix de frameworks avec des garanties de sécurité par défaut.
- **En développement** : linters de sécurité, SAST (Static Application Security Testing) intégré à l'IDE ou à la CI, revue de code obligatoire avec un volet sécurité.
- **En intégration continue** : SCA (Software Composition Analysis) pour détecter les dépendances vulnérables, scan de secrets (clés API committées par erreur), DAST (Dynamic Application Security Testing) sur les environnements de test.
- **En déploiement** : validation d'infrastructure as code (Terraform, Helm) avant application, scan d'images de conteneurs.

Le shift-left ne supprime pas les contrôles en exploitation (monitoring, détection d'intrusion) — il réduit le volume de défauts qui atteignent la production, ce qui rend les contrôles en aval plus efficaces parce qu'ils traitent moins de bruit.

## Secure SDLC (Software Development Lifecycle)

Un cycle de développement sécurisé intègre des activités de sécurité à chaque phase, avec des points de contrôle (gates) explicites :

1. **Exigences** — exigences de sécurité et de confidentialité définies dès le cahier des charges (pas seulement des exigences fonctionnelles).
2. **Conception** — threat modeling, revue d'architecture sécurité.
3. **Développement** — pratiques de codage sécurisé, SAST, revue de code.
4. **Test** — tests de sécurité dédiés (pentest, DAST), pas seulement des tests fonctionnels.
5. **Déploiement** — configuration sécurisée par défaut, gestion des secrets, durcissement.
6. **Exploitation** — surveillance, gestion des vulnérabilités, cycle de correctifs (patch management), plan de réponse à incident.

Ce cycle est ce que l'Annexe A 8.25 d'ISO 27001 (module 2) exige formellement — la formulation normative de ce même principe.

## Threat modeling : raisonner depuis l'attaquant

Le threat modeling consiste à identifier, avant l'implémentation, les menaces plausibles contre un système et les contre-mesures nécessaires. La méthode **STRIDE** (développée chez Microsoft) reste la plus enseignée pour structurer cette analyse, catégorie par catégorie :

- **S — Spoofing** (usurpation d'identité) → contre-mesure : authentification forte.
- **T — Tampering** (altération de données) → contre-mesure : intégrité (signatures, hachage, contrôle d'accès en écriture).
- **R — Repudiation** (répudiation d'une action) → contre-mesure : journalisation non falsifiable, horodatage.
- **I — Information Disclosure** (divulgation d'information) → contre-mesure : chiffrement, contrôle d'accès en lecture.
- **D — Denial of Service** (déni de service) → contre-mesure : limitation de débit (rate limiting), redondance.
- **E — Elevation of Privilege** (élévation de privilège) → contre-mesure : moindre privilège, validation stricte des entrées.

En pratique, un threat modeling STRIDE efficace se fait sur un diagramme de flux de données (Data Flow Diagram) du système : pour chaque flux traversant une frontière de confiance (trust boundary — par exemple entre un utilisateur non authentifié et une API), on examine systématiquement les six catégories STRIDE.

## Le lien avec la gouvernance et le risque

Security by Design n'est pas une alternative à la gestion des risques du module 1 — c'est son exécution technique. Le threat modeling *est* une analyse de risque, appliquée à un système précis plutôt qu'à un processus métier abstrait. Un contrôle choisi en Security by Design (chiffrement, moindre privilège) *est* un traitement de risque au sens ISO 31000. Les deux vocabulaires décrivent la même discipline à des niveaux d'abstraction différents.
