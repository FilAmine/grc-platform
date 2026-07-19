# Les trois objectifs de sécurité (1/2) : sécuriser l'environnement et maîtriser les accès

## Objectif 1 — Sécuriser votre environnement : protéger l'infrastructure locale

Le premier objectif du CSCF regroupe les contrôles visant à protéger l'infrastructure technique utilisée pour se connecter au réseau SWIFT, avec plusieurs principes structurants :

- **La segmentation du réseau local (network segmentation)** — isoler l'environnement SWIFT du reste du système d'information de l'utilisateur, afin qu'une compromission d'un autre système de l'organisation ne puisse pas directement atteindre les composants critiques de connectivité SWIFT. Ce principe rejoint directement celui déjà développé pour la segmentation réduisant le périmètre d'audit dans le parcours PCI DSS de cette plateforme, où l'isolement de l'environnement des données de cartes constitue de la même façon un levier de réduction du risque.
- **La sécurisation des postes internes (internal data flow security)** — la protection des flux de données entre les différents composants de l'infrastructure SWIFT elle-même, y compris par le chiffrement des communications internes.
- **La gestion des vulnérabilités et des correctifs** — une exigence de maintien à jour des systèmes composant l'environnement SWIFT, comparable dans son principe à la gestion des vulnérabilités déjà développée dans les CIS Controls et le NIST CSF, tous deux étudiés dans les parcours dédiés de cette plateforme.
- **La protection physique** des équipements critiques (HSM, serveurs de connexion) contre tout accès physique non autorisé.

## Pourquoi cet objectif répond directement à l'incident fondateur du CSP

Cet objectif de sécurisation de l'environnement local répond très directement à l'enseignement central de l'incident de la banque centrale du Bangladesh développé au module 0 de ce parcours : les attaquants n'avaient jamais compromis le réseau SWIFT lui-même, mais les systèmes locaux insuffisamment protégés de la banque victime — une segmentation réseau rigoureuse et une gestion des vulnérabilités effective auraient très probablement empêché, ou au moins considérablement compliqué, la chaîne d'attaque effectivement observée lors de cet incident.

## Objectif 2 — Connaître et limiter les accès : la gestion des identités et des privilèges

Le second objectif du CSCF regroupe les contrôles relatifs à la gestion des identités et des accès, avec plusieurs exigences clés :

- **L'authentification multifacteur** pour tout accès aux systèmes SWIFT, y compris pour les comptes à privilèges les plus sensibles — une exigence désormais quasi universelle parmi les référentiels de sécurité déjà étudiés dans cette plateforme, des CIS Controls à FedRAMP.
- **Le principe du moindre privilège**, limitant les droits d'accès de chaque utilisateur ou compte de service au strict nécessaire pour l'exercice de ses fonctions — un principe déjà développé à de multiples reprises dans cette plateforme, notamment pour la séparation des tâches dans le parcours SOX.
- **La revue périodique des comptes et des privilèges**, afin de détecter et de révoquer les accès devenus obsolètes ou disproportionnés par rapport aux fonctions réellement exercées — une exigence qui rappelle directement celle déjà développée pour la séparation des tâches dans les systèmes ERP du parcours SOX de cette plateforme.
- **La protection renforcée des comptes à privilèges (personnel security)**, notamment ceux capables d'initier ou d'approuver des instructions de paiement, avec des mesures de vérification supplémentaires proportionnées au risque financier direct que ces comptes représentent.

## Pourquoi la gestion des accès occupe une place centrale dans un contexte de paiement

Contrairement à un système d'information généraliste, où une compromission de compte peut avoir des conséquences variées (vol de données, perturbation de service), une compromission de compte donnant accès aux systèmes SWIFT peut directement déboucher sur l'émission d'instructions de paiement frauduleuses irréversibles — un enjeu financier immédiat et souvent considérable qui justifie une rigueur de gestion des accès sensiblement supérieure à celle généralement exigée pour un système d'information ordinaire, y compris par rapport aux exigences déjà rencontrées dans ISO 27001 ou le NIST CSF pour un périmètre plus généraliste.

## Le lien entre ces deux premiers objectifs et le troisième, développé à la leçon suivante

Ces deux premiers objectifs relèvent d'une logique essentiellement préventive — réduire la surface d'attaque et limiter les accès pour empêcher qu'une intrusion ne se produise ou ne se propage. Mais aucun dispositif préventif n'est jamais totalement infaillible, un principe déjà rappelé à de multiples reprises dans cette plateforme : c'est précisément la raison d'être du troisième objectif du CSCF, consacré à la détection et à la réponse, développé à la leçon suivante de ce parcours.
