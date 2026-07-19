# L'ingénierie de la vie privée et le retour sur le Privacy by Design

## Un concept déjà esquissé, mais jamais pleinement outillé, dans cette plateforme

Le premier parcours de cette plateforme a introduit la notion de **Privacy by Design** — l'idée que la protection de la vie privée doit être intégrée dès la conception d'un système ou d'un service, plutôt qu'ajoutée après coup comme une contrainte de conformité. Le NIST Privacy Framework donne à ce principe, souvent évoqué de façon relativement générale, une **méthodologie opérationnelle précise** à travers ce qu'il désigne comme l'**ingénierie de la vie privée (privacy engineering)** — l'application systématique des cinq fonctions du Core, développées aux modules 2 et 3 de ce parcours, dès les phases amont de conception d'un produit ou d'un système, plutôt qu'au stade de sa mise en production.

## Ce que l'ingénierie de la vie privée ajoute concrètement au principe général de Privacy by Design

Là où le Privacy by Design reste souvent formulé comme un principe directeur assez général, l'ingénierie de la vie privée du NIST Privacy Framework le traduit en pratiques concrètes et vérifiables : réaliser l'appréciation du risque vie privée (module 1 de ce parcours) dès la phase de spécification d'un nouveau produit, plutôt qu'après son déploiement ; concevoir l'architecture technique de façon à faciliter nativement les capacités de contrôle exigées par Control-P (développé au module 3), par exemple en structurant dès l'origine les bases de données de façon à permettre une suppression granulaire précise par individu ; et documenter, dès la conception, les data actions prévues pour alimenter la transparence exigée par Communicate-P.

## Le coût de la remédiation tardive, un principe déjà rencontré dans cette plateforme

Cette approche préventive rejoint un principe déjà développé à de multiples reprises dans cette plateforme sous des formes variées : il est presque toujours plus coûteux de corriger une lacune de sécurité ou de conformité après coup que de l'anticiper dès la conception — un principe déjà rencontré pour l'approche descendante et fondée sur le risque de SOX, ou pour la nécessité d'anticiper la documentation dès la mise en œuvre des contrôles ITGC. Appliqué à la vie privée, ce principe prend une acuité particulière : une architecture technique conçue sans considération pour la granularité nécessaire à l'exercice des droits des personnes concernées peut s'avérer extrêmement coûteuse, voire pratiquement impossible, à corriger après un déploiement à grande échelle.

## Le lien direct avec l'analyse d'impact relative à la protection des données du RGPD

Cette approche préventive rejoint directement l'**analyse d'impact relative à la protection des données (AIPD)**, déjà développée en détail dans le parcours RGPD de cette plateforme, qui impose une évaluation formalisée du risque vie privée avant le déploiement de tout traitement susceptible d'engendrer un risque élevé pour les personnes concernées. Le NIST Privacy Framework fournit ainsi une méthodologie complète et outillée — la chaîne data action / problematic data action / préjudice développée au module 1 de ce parcours — qui peut directement structurer le contenu substantiel d'une AIPD, au-delà de la seule obligation procédurale que le RGPD impose sans toujours en détailler la méthodologie sous-jacente.

## Comment cette approche s'articule avec la sécurité dès la conception

L'ingénierie de la vie privée rejoint, sans s'y confondre, le principe de sécurité dès la conception (security by design) déjà développé dans le premier parcours de cette plateforme — les deux approches partagent la même logique d'anticipation précoce, mais poursuivent des objectifs distincts conformément à la distinction fondamentale entre risque de sécurité et risque vie privée développée au module 1 de ce parcours : la sécurité dès la conception vise à empêcher les accès non autorisés et les pertes de données, tandis que l'ingénierie de la vie privée vise à empêcher que le traitement lui-même, même parfaitement sécurisé, ne produise des conséquences problématiques pour les personnes concernées.

## Un exemple concret d'application de l'ingénierie de la vie privée

Une équipe produit concevant une nouvelle fonctionnalité de recommandation personnalisée peut appliquer l'ingénierie de la vie privée en évaluant, dès la phase de conception, les data actions impliquées (quelles données comportementales seront collectées et analysées), en identifiant les problematic data actions potentielles (un risque de profilage excessif ou de discrimination algorithmique, déjà développés au module 1 de ce parcours), et en intégrant nativement des mécanismes de contrôle (Control-P) permettant à l'utilisateur de désactiver la personnalisation — plutôt que d'ajouter ces mécanismes de contrôle après coup, sous la pression d'une plainte d'utilisateur ou d'une exigence réglementaire tardive.

## Le lien avec le module suivant

Cette approche préventive, combinée à l'ensemble des mécanismes déjà développés tout au long de ce parcours, mérite d'être replacée dans le contexte plus large des autres référentiels déjà étudiés dans cette plateforme — l'objet du dernier module de ce parcours.
