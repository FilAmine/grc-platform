# Privacy by Design : les 7 principes de Cavoukian

## Origine et légitimité du concept

Le concept de **Privacy by Design** a été formalisé dans les années 1990-2000 par Ann Cavoukian, alors Commissaire à l'information et à la protection de la vie privée de l'Ontario (Canada). Ce n'est pas un concept marketing récent : il a été formellement reconnu par la résolution de la 32ème Conférence internationale des commissaires à la protection des données et de la vie privée en 2010, puis directement intégré au RGPD (article 25) en 2016 — ce qui en fait une obligation légale dans l'UE, et non plus seulement une bonne pratique recommandée.

## Les sept principes fondateurs

### 1. Proactif, non réactif — préventif, non correctif

Anticiper et prévenir les événements portant atteinte à la vie privée avant qu'ils ne se produisent, plutôt que proposer des remèdes après coup. Concrètement : un threat modeling incluant explicitement les risques de vie privée (pas seulement de sécurité), mené avant l'implémentation.

### 2. La protection de la vie privée comme paramètre par défaut

Les paramètres les plus protecteurs de la vie privée doivent être appliqués **automatiquement**, sans action requise de l'individu. Un utilisateur qui ne configure rien doit bénéficier du niveau de protection maximal — l'inverse de la pratique répandue consistant à activer par défaut le partage ou le profilage, en laissant l'utilisateur "opt-out" s'il s'en rend compte.

### 3. La protection de la vie privée intégrée à la conception

La protection n'est pas une fonctionnalité ajoutée en périphérie — elle fait partie intégrante de l'architecture des systèmes et des pratiques métier, sans diminuer la fonctionnalité du système.

### 4. Fonctionnalité intégrale — somme positive, pas somme nulle

Rejette l'idée d'un compromis binaire entre vie privée et fonctionnalité (ou vie privée et sécurité). L'objectif est de satisfaire les deux, pas de sacrifier l'une pour l'autre — un principe qui demande souvent plus de créativité architecturale qu'une opposition simpliste "sécurité vs vie privée".

### 5. Sécurité intégrale — protection pendant tout le cycle de vie

La protection des données couvre l'ensemble du cycle de vie : de la collecte à la destruction sécurisée, en passant par la conservation et le traitement — pas seulement le moment de la collecte.

### 6. Visibilité et transparence

Les pratiques et technologies mises en œuvre doivent être vérifiables de manière indépendante — la transparence n'est pas seulement une promesse mais un état vérifiable par un tiers (recoupe directement le principe d'accountability du RGPD, module 2).

### 7. Respect de la vie privée des utilisateurs

Placer les intérêts de l'individu au centre : des paramètres par défaut protecteurs, une notification appropriée, des interfaces conviviales pour exercer ses droits — la vie privée conçue autour de l'utilisateur, pas autour de la commodité de l'organisation qui traite les données.

## Pourquoi ces principes restent abstraits sans traduction technique

Les sept principes de Cavoukian sont volontairement formulés à un niveau de principe, pas de contrôle technique — c'est un cadre de pensée, pas une checklist. Leur traduction opérationnelle passe par des mécanismes concrets, développés dans la leçon suivante : minimisation des données dès la modélisation, pseudonymisation, chiffrement, PIA/DPIA formalisée, et durées de conservation appliquées techniquement (purge automatisée plutôt que politique déclarative).

Le point clé pour un architecte ou un développeur : ces principes doivent influencer des décisions prises **avant l'écriture du premier schéma de base de données** — quelles données collecter, sous quelle forme les stocker, qui peut y accéder par défaut — pas être vérifiés a posteriori sur un système déjà conçu.
