# La surveillance continue (1/2) : un rythme mensuel

## L'étape Monitor du RMF, portée à son rythme le plus soutenu

Le parcours NIST RMF de cette plateforme a déjà développé l'étape **Monitor**, dernière et continue des sept étapes du processus, par laquelle un système autorisé fait l'objet d'une surveillance permanente de l'efficacité de ses contrôles plutôt que d'une évaluation figée à la date de l'autorisation initiale. FedRAMP applique ce même principe avec un degré de formalisation et une fréquence sensiblement plus soutenus que la plupart des autres référentiels déjà étudiés dans cette plateforme : là où un audit de surveillance ISO 27001 intervient annuellement, et où même une période d'observation SOC 2 Type II s'étend généralement sur six à douze mois, FedRAMP impose des **livrables mensuels**.

## Les trois livrables mensuels du dispositif de surveillance continue

Chaque mois, un CSP autorisé doit transmettre à l'agence sponsor (ou au FedRAMP Board pour les autorisations obtenues via cette voie) trois catégories de livrables :

- **Les résultats de scans de vulnérabilités**, couvrant les composants réseau, systèmes d'exploitation et applications web du périmètre autorisé — une exigence de scan continu qui rappelle, par sa fréquence, les scans trimestriels des Approved Scanning Vendors déjà développés dans le parcours PCI DSS de cette plateforme, ici portés à un rythme mensuel.
- **La mise à jour du Plan of Action and Milestones (POA&M)**, développé plus en détail à la leçon suivante, documentant l'état d'avancement de la remédiation de chaque faiblesse identifiée.
- **Un rapport de l'état des contrôles**, généralement structuré autour d'un sous-ensemble de contrôles jugés particulièrement critiques ou volatils (souvent désignés "contrôles clés" ou "contrôles à fort risque"), dont l'efficacité est revérifiée à un rythme plus rapproché que l'ensemble du catalogue de contrôles applicable.

## L'évaluation annuelle complémentaire

En complément de ce rythme mensuel, FedRAMP impose une **évaluation annuelle** plus complète, réalisée par le 3PAO déjà développé au module 3 de ce parcours, qui revérifie un échantillon représentatif de l'ensemble des contrôles de la base de référence applicable — un rythme à deux vitesses (surveillance mensuelle allégée et évaluation annuelle approfondie) qui rappelle, dans son principe de gradation, celui déjà rencontré pour la distinction entre le monitoring continu et l'audit périodique complet dans plusieurs référentiels de cette plateforme, notamment la distinction entre les contrôles ITGC testés en continu et l'évaluation annuelle de la section 404 dans le parcours SOX.

## Pourquoi ce rythme soutenu se justifie dans le contexte cloud

Cette fréquence exceptionnellement soutenue s'explique directement par la nature du service évalué : un environnement cloud évolue en permanence — nouveaux composants déployés, correctifs de sécurité appliqués, configurations modifiées — à un rythme sans commune mesure avec celui d'un système d'information traditionnel hébergé sur une infrastructure physique stable. Un dispositif de surveillance annuel, adapté à un système peu évolutif, laisserait ainsi une fenêtre d'exposition inacceptable dans un environnement cloud en évolution continue — un raisonnement qui rejoint directement celui déjà développé pour la fréquence de test des contrôles techniques dans les environnements les plus dynamiques à travers plusieurs parcours de cette plateforme.

## La conséquence directe sur la charge opérationnelle du CSP

Ce rythme mensuel impose au CSP autorisé une charge opérationnelle continue significative, généralement assumée par une équipe dédiée à la conformité FedRAMP travaillant en coordination étroite avec l'ISSO déjà développé au module 3 de ce parcours — une charge qui explique en grande partie pourquoi de nombreux fournisseurs cloud plus modestes hésitent à engager une démarche FedRAMP malgré l'attrait du marché fédéral américain, préférant parfois cibler dans un premier temps la base de référence LI-SaaS allégée développée au module 1 de ce parcours.

## Le lien avec la leçon suivante

Ce dispositif de surveillance continue produit naturellement, mois après mois, de nouvelles observations sur l'état des contrôles — la gestion structurée de ces observations, à travers le Plan of Action and Milestones et le mécanisme des Significant Change Requests, fait l'objet de la leçon suivante de ce parcours.
