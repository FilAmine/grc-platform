# Les sept étapes du RMF (4/4) : Monitor

## Une étape continue, pas un point final

L'étape 7, Monitor, boucle le processus RMF sur lui-même : elle ne clôt pas le cycle après l'obtention de l'autorisation d'exploitation (étape 6), elle instaure une **surveillance continue** qui alimente en permanence une réévaluation du risque, potentiellement jusqu'à déclencher une nouvelle itération complète des étapes précédentes si le contexte évolue significativement.

## La surveillance continue de la sécurité de l'information (ISCM)

**SP 800-137** définit le cadre de l'**Information Security Continuous Monitoring (ISCM)**, structuré autour de six étapes propres :

1. **Définir** une stratégie de surveillance continue, cohérente avec l'appétence au risque de l'organisation (un principe de gouvernance déjà rencontré dans le premier parcours de cette plateforme).
2. **Établir** un programme de surveillance, avec des métriques et une fréquence de mesure adaptées à chaque contrôle.
3. **Implémenter** le programme, en s'appuyant autant que possible sur l'automatisation de la collecte de données.
4. **Analyser** les données collectées et **rendre compte** des résultats aux parties prenantes concernées.
5. **Répondre** aux résultats de l'analyse, par des actions correctives si nécessaire.
6. **Réviser et mettre à jour** la stratégie de surveillance elle-même, en fonction des enseignements tirés.

Cette structure en boucle rappelle directement le cycle PDCA d'ISO 27001, ou les clauses 9 et 10 de cette même norme (évaluation des performances et amélioration), déjà développées dans le parcours dédié de cette plateforme — une preuve supplémentaire que, malgré des vocabulaires distincts, les référentiels matures convergent presque toujours vers le même principe : une boucle de vérification et d'amélioration continue plutôt qu'un contrôle figé une fois pour toutes.

## La fréquence de surveillance différenciée par contrôle

Le RMF n'impose pas une fréquence uniforme de surveillance pour tous les contrôles — chaque contrôle se voit assigner une fréquence d'évaluation propre dans la stratégie de surveillance continue, généralement fondée sur sa **volatilité** (à quelle vitesse son état de conformité peut changer) et sa **criticité** pour la sécurité du système. Un contrôle de configuration technique automatiquement vérifiable (par exemple, la configuration de chiffrement d'un volume de stockage) peut être surveillé en continu ou quasi-continu via des outils automatisés, tandis qu'un contrôle plus organisationnel (la formation du personnel à la sécurité, par exemple) peut raisonnablement rester évalué à une fréquence annuelle.

## L'autorisation continue (ongoing authorization)

Une évolution significative de la pratique du RMF ces dernières années consiste à faire évoluer l'autorisation d'un événement ponctuel, valable pour une durée fixe (typiquement trois ans dans la pratique historique), vers une **autorisation continue (ongoing authorization)** : tant que la surveillance continue démontre que le système maintient son niveau de risque résiduel acceptable, son autorisation reste valide sans nécessiter une réévaluation complète et périodique — l'autorisation devient elle-même un processus continu plutôt qu'un jalon isolé. Cette évolution répond à un problème structurel bien identifié : un cycle de réautorisation complète tous les trois ans laisse un système fonctionner, dans l'intervalle, sur la base d'une photographie de son risque potentiellement obsolète face à l'évolution rapide des menaces et des systèmes eux-mêmes.

Le ministère de la Défense américain a poussé ce principe plus loin encore avec le concept d'**autorisation continue (Continuous ATO — cATO)**, réservé aux systèmes disposant d'un pipeline de développement et de déploiement suffisamment mature (une intégration continue avec des contrôles de sécurité automatisés, une surveillance en temps réel de la posture de sécurité) pour justifier une confiance soutenue de l'Authorizing Official sans jalon de réévaluation périodique traditionnel — un point de convergence direct avec les pratiques DevSecOps et Security by Design développées dans le premier parcours de cette plateforme : plus un système est instrumenté pour produire une preuve continue de son état de sécurité, moins il a besoin d'un processus d'autorisation ponctuel et lourd pour justifier la confiance qu'on lui accorde.

## Les événements déclencheurs d'une réautorisation complète

Malgré la tendance vers l'autorisation continue, certains événements déclenchent encore, dans la pratique du RMF, une réévaluation substantielle, voire une reprise complète du processus depuis l'étape de catégorisation :

- un **changement significatif** de l'architecture du système, de son périmètre d'autorisation, ou des types de données qu'il traite,
- la découverte d'une **vulnérabilité critique** dont la correction affecte substantiellement la posture de sécurité documentée,
- un **incident de sécurité majeur** affectant le système,
- l'expiration du cycle de réautorisation traditionnel, pour les systèmes qui ne bénéficient pas encore d'un régime d'autorisation continue.

## Comment cette dernière étape referme la boucle du RMF

L'étape Monitor ne se contente pas de vérifier que rien n'a changé — ses résultats alimentent directement la stratégie de gestion des risques au niveau organisationnel définie à l'étape Prepare (module 1), créant une boucle de rétroaction complète du niveau technique le plus fin (la surveillance d'un contrôle précis sur un système donné) jusqu'au niveau stratégique de l'organisation entière — exactement le même principe de boucle de rétroaction bidirectionnelle entre gouvernance et exécution technique, déjà développé comme fil conducteur de la synthèse du premier parcours de cette plateforme, ici formalisé dans le vocabulaire spécifique et prescriptif du RMF.
