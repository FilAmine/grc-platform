# Les menaces propres à l'architecture Zero Trust elle-même

## Une architecture de sécurité qui devient elle-même une cible

NIST SP 800-207 consacre une attention explicite à un principe déjà rencontré à de multiples reprises dans cette plateforme, notamment pour la sécurité des systèmes d'IA développée dans le parcours NIST AI RMF : tout dispositif de sécurité, aussi rigoureux soit-il, devient lui-même une cible privilégiée pour un attaquant suffisamment déterminé — l'architecture Zero Trust ne fait pas exception, et son adoption doit s'accompagner d'une vigilance particulière face à des menaces qui ciblent directement ses propres composants plutôt que les ressources qu'elle protège.

## La subversion du processus décisionnel

La menace la plus directement critique consiste en une tentative de **subversion du Policy Engine ou du Policy Administrator** eux-mêmes, développés au module 2 de ce parcours — un attaquant parvenant à compromettre ces composants centraux pourrait manipuler directement les décisions d'accès accordées, contournant ainsi l'ensemble du dispositif Zero Trust de l'intérieur plutôt que de tenter de le contourner depuis l'extérieur. Cette menace justifie une protection et une surveillance particulièrement renforcées de ces composants centraux, à l'image de la protection renforcée déjà développée pour les comptes à privilèges au titre de l'Objectif 2 du CSCF de SWIFT CSP, développé dans le parcours dédié de cette plateforme.

## Le déni de service contre les composants centraux

Une attaque par déni de service visant spécifiquement le Policy Engine ou le Policy Administrator pourrait empêcher l'ensemble des utilisateurs légitimes d'obtenir une autorisation d'accès, paralysant ainsi l'organisation tout entière — une conséquence potentiellement plus dévastatrice qu'un déni de service classique visant une ressource isolée, précisément parce que ces composants centraux conditionnent l'accès à l'ensemble des ressources protégées par l'architecture. Cette centralisation du risque rappelle directement celle déjà développée pour la vue de portefeuille des risques de COSO ERM, où la concentration d'un risque à un point unique peut engendrer des conséquences disproportionnées par rapport à une exposition répartie.

## Le vol d'identifiants et la menace interne

L'architecture Zero Trust réduit significativement, sans jamais l'éliminer totalement, le risque associé au vol d'identifiants ou à une menace interne malveillante — un attaquant disposant d'identifiants légitimement volés continue de bénéficier de l'accès que ces identifiants autorisent, bien que la surveillance continue et la politique dynamique déjà développées au module 1 de ce parcours (principes 4, 5 et 6) permettent de détecter plus rapidement un comportement anormal associé à ces identifiants compromis, comparé à un modèle périmétrique traditionnel où l'accès, une fois obtenu, resterait largement incontesté.

## La visibilité du trafic chiffré

Le deuxième principe déjà développé au module 1 de ce parcours impose que toute communication soit sécurisée, généralement par chiffrement systématique — mais ce chiffrement généralisé peut paradoxalement compliquer la détection de comportements malveillants dissimulés au sein de flux chiffrés légitimes, un défi qui exige des capacités d'analyse comportementale et de surveillance renforcées, développées au titre du cinquième principe, plutôt qu'une simple inspection du contenu des communications elles-mêmes.

## Le stockage des données de politique comme cible privilégiée

Les systèmes de stockage contenant les politiques d'accès, les journaux d'activité et les données utilisées par l'algorithme de confiance, développés au module 2 de ce parcours, constituent eux-mêmes des cibles privilégiées — un attaquant parvenant à altérer ces données pourrait indirectement influencer les décisions futures du Policy Engine sans jamais compromettre directement ce composant lui-même. Cette menace rejoint directement celle déjà développée pour la protection de l'intégrité des données d'entraînement dans le parcours NIST AI RMF de cette plateforme, où la compromission d'une donnée d'entrée peut fausser durablement une décision automatisée sans jamais compromettre le système décisionnel lui-même.

## Un tableau de synthèse des menaces propres à l'architecture Zero Trust

| Menace | Conséquence potentielle |
|---|---|
| Subversion du PE ou du PA | Manipulation directe des décisions d'accès depuis l'intérieur du dispositif |
| Déni de service contre les composants centraux | Paralysie de l'accès pour l'ensemble des utilisateurs légitimes |
| Vol d'identifiants | Un accès légitimement autorisé, mais détectable plus rapidement qu'en modèle périmétrique |
| Trafic chiffré | Une détection de comportement malveillant rendue plus complexe |
| Compromission des données de politique | Une influence indirecte sur les décisions futures du Policy Engine |

## Le lien avec le module suivant

Face à ces défis et à la complexité de la migration développée au module précédent, un modèle de maturité structuré permet aux organisations d'évaluer et de planifier leur progression vers une architecture Zero Trust pleinement mature — l'objet du module suivant de ce parcours.
