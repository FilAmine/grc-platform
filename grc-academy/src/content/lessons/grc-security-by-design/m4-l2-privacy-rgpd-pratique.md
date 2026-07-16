# Privacy by Design appliqué au RGPD : minimisation, PIA/DPIA, pseudonymisation

## Traduire l'article 25 en décisions d'architecture

L'article 25 du RGPD ("Protection des données dès la conception et par défaut") transforme les principes de Cavoukian en obligation légale. Concrètement, un responsable de traitement doit démontrer que des **mesures techniques et organisationnelles appropriées** ont été mises en œuvre, tant au moment de la détermination des moyens de traitement qu'au moment du traitement lui-même. Voici les mécanismes concrets qui traduisent cette obligation.

## Minimisation des données : une décision de modélisation, pas de politique

La minimisation (module 2) commence dès la conception du schéma de données. Questions à se poser systématiquement avant de créer un champ :

- Ce champ est-il **nécessaire** à la finalité, ou seulement "utile à avoir au cas où" ?
- Peut-on atteindre la même finalité avec une donnée moins précise ? (une tranche d'âge plutôt qu'une date de naissance exacte, un code postal plutôt qu'une adresse complète, si la finalité le permet)
- Cette donnée doit-elle vraiment être **identifiante**, ou une donnée pseudonymisée suffit-elle pour la finalité poursuivie (statistiques, tests, analytics) ?

Une architecture qui applique la minimisation dès la conception réduit mécaniquement la surface de risque : une donnée qui n'existe pas ne peut pas fuiter, ne nécessite pas de contrôle d'accès, et ne pose pas de question de durée de conservation.

## Pseudonymisation vs anonymisation : une distinction technique et juridique cruciale

Ces deux notions sont souvent confondues alors qu'elles ont des conséquences juridiques très différentes :

- **Pseudonymisation** (article 4.5 RGPD) : les données ne peuvent plus être attribuées à une personne sans information supplémentaire, conservée séparément et protégée (par exemple, un identifiant technique remplace le nom, avec une table de correspondance chiffrée et stockée à part). **Les données pseudonymisées restent des données personnelles** au sens du RGPD — le règlement continue de s'appliquer intégralement.
- **Anonymisation** : le processus rend **irréversiblement** impossible la ré-identification, par quelque moyen que ce soit, y compris par recoupement avec d'autres sources. Des données réellement anonymisées **sortent du champ d'application du RGPD**.

En pratique, la véritable anonymisation est techniquement beaucoup plus exigeante qu'on ne le pense — la simple suppression du nom et de l'email ne suffit pas si d'autres attributs (localisation précise + horodatage + comportement) permettent une ré-identification par recoupement. La majorité des systèmes qui prétendent "anonymiser" pratiquent en réalité une pseudonymisation, ce qui a une conséquence directe : les obligations RGPD (durée de conservation, droits des personnes, sécurité) continuent de s'appliquer à ces données.

## PIA / DPIA : quand et comment

L'analyse d'impact relative à la protection des données (AIPD, ou DPIA en anglais) est **obligatoire** lorsque le traitement est susceptible d'engendrer un risque élevé pour les droits et libertés des personnes, notamment :

- évaluation systématique et approfondie d'aspects personnels, y compris le profilage,
- traitement à grande échelle de catégories particulières de données (santé, origine, opinions, orientation sexuelle...),
- surveillance systématique à grande échelle d'une zone accessible au public.

Une DPIA structure l'analyse en quatre temps, très proche de la logique de gestion des risques du module 1 mais spécifiquement centrée sur les droits des personnes plutôt que sur les intérêts de l'organisation :

1. **Description systématique** du traitement et de ses finalités.
2. **Évaluation de la nécessité et de la proportionnalité** — ce traitement, sous cette forme, est-il vraiment nécessaire pour la finalité visée ?
3. **Évaluation des risques** pour les droits et libertés des personnes concernées (pas seulement pour l'organisation).
4. **Mesures pour traiter les risques** — garanties, mesures de sécurité, mécanismes permettant de démontrer la conformité.

Le point souvent mal compris : la DPIA évalue le risque **pour la personne concernée**, pas le risque pour l'organisation (réputationnel, financier) — un changement de perspective qui distingue clairement une DPIA d'une analyse de risque cybersécurité classique, même si les deux exercices se recoupent largement sur les mesures techniques recommandées.

## Durée de conservation : la purge doit être un mécanisme, pas une politique

Une politique qui déclare "les données sont conservées 3 ans" n'a de valeur que si un mécanisme technique applique réellement cette purge — job planifié, règle de cycle de vie sur le stockage, suppression en cascade cohérente entre les systèmes (base de données primaire, sauvegardes, entrepôt analytique, logs). C'est un exemple typique où l'absence de Security/Privacy by Design transforme une exigence de gouvernance simple en dette technique difficile à corriger a posteriori — retrouver et purger rétroactivement des données disséminées dans des dizaines de systèmes non prévus pour cela est un chantier nettement plus coûteux que de concevoir la purge dès le départ.
