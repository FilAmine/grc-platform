# L'écosystème ANSSI (2/2) : le régime LPM/OIV, le rôle dans NIS2, et le CERT-FR

## Le régime des Opérateurs d'Importance Vitale : un précurseur national de NIS2

Déjà annoncé dans l'introduction de ce parcours, le régime des **Opérateurs d'Importance Vitale (OIV)**, instauré par la **Loi de Programmation Militaire (LPM) de 2013**, mérite d'être développé en détail tant il éclaire, par contraste, la genèse de NIS2 déjà étudiée dans le parcours dédié de cette plateforme. Un OIV est un opérateur — public ou privé — dont l'indisponibilité risquerait de diminuer d'une façon importante le potentiel de guerre ou économique, la sécurité ou la capacité de survie de la Nation, désigné individuellement par l'autorité administrative sur proposition sectorielle, dans des secteurs jugés vitaux (énergie, transport, finance, santé, communications électroniques, notamment).

### Les obligations imposées aux OIV

Les OIV doivent notamment : mettre en œuvre des **règles de sécurité** fixées par arrêté sectoriel (couvrant des sujets directement comparables aux dix domaines de l'article 21 de NIS2 déjà développés dans le parcours dédié de cette plateforme), déclarer à l'ANSSI leurs systèmes d'information d'importance vitale, et **notifier sans délai à l'ANSSI** tout incident de sécurité affectant ces systèmes — une obligation de notification qui préfigure directement, avec près d'une décennie d'avance, le mécanisme de notification des incidents majeurs de NIS2 développé dans le parcours dédié de cette plateforme, bien que selon des modalités et un calendrier propres au droit français plutôt que le calendrier harmonisé à 24h/72h/1 mois de la directive européenne.

## Le rôle de l'ANSSI dans la transposition française de NIS2

L'ANSSI joue un rôle central et direct dans la mise en œuvre française de la directive NIS2, déjà développée dans le parcours dédié de cette plateforme : elle agit comme **autorité nationale de référence** pour un large périmètre de secteurs couverts par la directive, reprenant et élargissant, dans les faits, une logique de supervision de la cybersécurité des acteurs critiques qu'elle exerçait déjà depuis 2013 pour le périmètre plus restreint des OIV. Le régime OIV de la LPM et le régime des entités essentielles et importantes de NIS2 (développé dans le parcours dédié de cette plateforme) coexistent aujourd'hui, avec une articulation précisée par le droit français de transposition — une organisation française potentiellement soumise aux deux régimes simultanément doit vérifier précisément comment ils s'articulent pour son secteur et son profil précis, plutôt que de supposer qu'un seul des deux textes suffit à couvrir l'ensemble de ses obligations.

## Le CERT-FR : le centre de réponse aux incidents de l'ANSSI

Le **CERT-FR** (Computer Emergency Response Team - France) est le centre gouvernemental de réponse aux incidents de sécurité informatique, opéré par l'ANSSI. Il joue un rôle comparable à celui des CSIRT nationaux déjà développés dans le parcours NIS2 de cette plateforme, avec plusieurs missions concrètes :

- la publication d'**avis et d'alertes de sécurité** (CERTFR-Avis, CERTFR-Alerte) informant des vulnérabilités critiques affectant des produits largement déployés,
- la publication de **bulletins d'actualité** hebdomadaires synthétisant les événements de sécurité marquants,
- la coordination de la **divulgation responsable des vulnérabilités**, un rôle directement comparable à celui du CSIRT national coordinateur pour la divulgation coordonnée des vulnérabilités déjà développé dans le parcours NIS2 de cette plateforme,
- l'assistance aux victimes d'incidents de sécurité, en particulier pour les OIV et les entités essentielles/importantes déjà mentionnées plus haut dans cette leçon.

## Un exemple concret de la manière dont ces dispositifs s'articulent

Une entreprise française du secteur de l'énergie, désignée OIV au titre de la LPM et simultanément qualifiée d'entité essentielle au titre de la transposition française de NIS2, doit notifier tout incident significatif à l'ANSSI — qui joue ici le rôle d'autorité compétente à la fois pour le régime national OIV et pour le régime européen NIS2. Le CERT-FR, en tant que centre opérationnel de l'ANSSI, réceptionne et traite ces notifications, peut publier une alerte si la vulnérabilité à l'origine de l'incident est susceptible d'affecter d'autres organisations, et coordonne, le cas échéant, une réponse à l'incident avec l'appui d'un prestataire PRIS qualifié (développé dans la leçon précédente) si l'entreprise ne dispose pas en interne des capacités de réponse nécessaires.

## Ce que cette architecture institutionnelle révèle sur le modèle français

Contrairement à NIS2, qui organise une architecture de coopération distribuée entre vingt-sept États membres avec des points de contact uniques et des CSIRT nationaux multiples (développée dans le parcours dédié de cette plateforme), le modèle français concentre l'essentiel de ces fonctions — méthode de gestion des risques (EBIOS RM), qualification des prestataires, régulation des opérateurs critiques (OIV et rôle national pour NIS2), et réponse aux incidents (CERT-FR) — au sein d'une **seule agence**, l'ANSSI. Cette concentration institutionnelle, rare parmi les modèles nationaux européens, explique en grande partie pourquoi une méthode comme EBIOS RM, une qualification comme SecNumCloud, et un centre de réponse comme le CERT-FR forment un écosystème aussi cohérent et interconnecté — une caractéristique distinctive du modèle français de cybersécurité, à mettre en regard des architectures institutionnelles plus distribuées déjà rencontrées pour NIS2 ou pour le secteur financier européen sous DORA, tous deux développés dans les parcours dédiés de cette plateforme.
