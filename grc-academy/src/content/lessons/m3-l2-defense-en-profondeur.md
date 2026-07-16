# Défense en profondeur, moindre privilège, fail secure, zero trust

## Défense en profondeur (Defense in Depth)

Le principe : aucun contrôle unique n'est infaillible, donc la sécurité d'un système repose sur **plusieurs couches indépendantes**, de sorte que la défaillance d'une couche ne compromette pas l'ensemble.

Exemple concret pour une application web traitant des données personnelles :

1. **Couche réseau** — segmentation, groupes de sécurité restreignant les flux au strict nécessaire.
2. **Couche identité** — authentification forte (MFA), gestion des sessions.
3. **Couche application** — validation des entrées, protection contre l'injection, contrôle d'accès applicatif (autorisation, pas seulement authentification).
4. **Couche donnée** — chiffrement au repos, contrôle d'accès au niveau base de données.
5. **Couche surveillance** — journalisation, détection d'anomalies, alerting.

Si un attaquant contourne la couche réseau (par exemple via un compte compromis), les couches identité et application restent des obstacles. C'est l'inverse d'une architecture à "coquille dure, cœur mou" (hard shell, soft center) où tout repose sur un unique périmètre réseau — modèle aujourd'hui obsolète, en particulier dans le cloud où le périmètre réseau traditionnel n'existe plus vraiment.

## Moindre privilège (Principle of Least Privilege)

Chaque utilisateur, service ou processus ne doit disposer **que** des droits strictement nécessaires à sa fonction, ni plus. Deux corollaires souvent oubliés :

- **Le moindre privilège est temporel autant que fonctionnel** : un accès nécessaire pendant une opération ponctuelle (ex. accès d'urgence en astreinte) devrait expirer automatiquement, pas rester actif indéfiniment "au cas où".
- **Le moindre privilège s'applique aux services autant qu'aux humains** : un rôle IAM attaché à une fonction serverless ne devrait pouvoir accéder qu'aux ressources précises dont cette fonction a besoin — la pratique fréquente d'attacher une politique `*:*` "pour que ça marche" est l'antithèse exacte du principe, et une des causes les plus fréquentes d'incidents cloud graves.

C'est directement le contrôle testé lors d'une revue d'accès périodique exigée par ISO 27001 ou SOC 2 (module 1 et 2) : sans processus technique pour détecter les droits excessifs, la revue devient un exercice déclaratif sans valeur probante.

## Fail secure (vs fail open)

Quand un contrôle de sécurité rencontre une erreur ou une défaillance, il doit échouer dans un état **sécurisé**, pas dans un état permissif :

- Un pare-feu qui, en cas de panne de sa base de règles, **bloque tout le trafic** (fail secure/fail closed) plutôt que de le laisser passer (fail open).
- Un mécanisme d'autorisation qui, en cas d'erreur d'appel au service de permissions, **refuse l'accès par défaut** plutôt que de l'accorder.

Ce principe entre parfois en tension avec la disponibilité (un fail secure peut interrompre un service). C'est un arbitrage de gouvernance explicite : quel est le coût d'un accès refusé à tort, comparé au coût d'un accès accordé à tort ? La réponse dépend de la sensibilité du système — un mécanisme d'authentification pour des données de santé devrait presque toujours pencher vers fail secure.

## Zero Trust

Le modèle Zero Trust part du principe qu'**aucune requête n'est fiable par défaut, y compris à l'intérieur du réseau interne**. Résumé par la formule "never trust, always verify", il remplace le modèle périmétrique classique (tout ce qui est "à l'intérieur" du réseau est réputé fiable) par une vérification systématique de chaque requête, quel que soit son origine :

- **Authentification et autorisation à chaque requête**, pas seulement à l'entrée du réseau.
- **Micro-segmentation** — chaque service ne communique qu'avec les services explicitement autorisés, même au sein d'un même réseau privé.
- **Vérification continue du contexte** — identité, posture de l'appareil, localisation, comportement — plutôt qu'une confiance acquise une fois pour toutes après une authentification initiale.

Zero Trust n'est pas un produit qu'on achète — c'est une architecture qui se construit contrôle par contrôle (IAM fort, micro-segmentation réseau, chiffrement systématique des flux internes, journalisation exhaustive). C'est le modèle de référence pour concevoir des architectures cloud modernes, développé en détail au module 5.

## Comment ces principes s'articulent entre eux

Ces quatre principes ne sont pas des alternatives — ils se combinent :

- La défense en profondeur définit **combien de couches** protègent un actif.
- Le moindre privilège définit **la largeur** de chaque couche (ce qu'elle autorise).
- Fail secure définit **le comportement en cas de défaillance** d'une couche.
- Zero Trust définit **la posture de confiance par défaut** entre toutes les couches, y compris internes.

Un système conçu selon ces quatre principes simultanément n'élimine pas le risque — aucune architecture ne le peut — mais réduit drastiquement la probabilité qu'une défaillance unique se traduise en compromission totale, ce qui est précisément l'objectif d'un traitement de risque efficace au sens du module 1.
