# L'AI Act face aux autres référentiels, et une feuille de route de mise en conformité

## L'AI Act comparé aux référentiels déjà étudiés dans cette plateforme

| Aspect | AI Act | NIST AI RMF | RGPD | NIS2/DORA |
|---|---|---|---|---|
| Nature | Règlement européen obligatoire | Cadre volontaire américain | Règlement européen obligatoire | Directive/règlement européens obligatoires |
| Approche du risque | Pyramide à quatre niveaux fixés par la loi (Annexe III) | Catégorisation ouverte via la fonction Map | Approche par le risque (AIPD) sans pyramide fixe | Approche par le risque avec seuils de criticité |
| Décision centrale | Marquage CE après évaluation de conformité | Aucune (outil de priorisation) | Conformité continue sous supervision d'une autorité | Autorisation ou supervision continue |
| Évaluateur indépendant | Organisme notifié (catégories sensibles uniquement) | Équipes TEVV (recommandé, non obligatoire) | Aucun (autorités de contrôle a posteriori) | Autorités de supervision, TLPT pour DORA |
| Sanction maximale | 35 M€ ou 7 % du CA mondial | Aucune (outil volontaire) | 20 M€ ou 4 % du CA mondial | Amendes administratives, supervision directe |

Ce tableau confirme, une fois de plus, un principe déjà établi à travers les parcours précédents de cette plateforme : un cadre volontaire (NIST AI RMF) fournit la méthodologie opérationnelle, qu'un règlement contraignant (AI Act) transforme ensuite en obligations légales précises assorties de sanctions substantielles — une dynamique de maturation réglementaire déjà observée pour la relation entre le NIST CSF et DORA, développée dans le parcours dédié de cette plateforme.

## Le mapping avec le NIST AI RMF comme socle méthodologique direct

Comme développé tout au long de ce parcours, le système de gestion des risques de l'article 9 reprend directement la logique cyclique du NIST AI RMF déjà étudié dans le parcours dédié de cette plateforme, et les sept caractéristiques de l'IA digne de confiance (validité, sûreté, sécurité, transparence, explicabilité, respect de la vie privée, équité) trouvent leur traduction juridique précise dans les articles 9 à 15 de l'AI Act. Une organisation ayant déjà déployé le NIST AI RMF de façon rigoureuse dispose ainsi d'une base méthodologique substantielle pour satisfaire les obligations de l'AI Act, sans que l'un ne se substitue jamais légalement à l'autre pour une organisation soumise au règlement européen.

## Le mapping avec le RGPD pour les systèmes traitant des données personnelles

Tout système d'IA à haut risque traitant des données à caractère personnel reste pleinement soumis au RGPD, déjà développé en détail dans le parcours dédié de cette plateforme, en parallèle des obligations propres à l'AI Act — l'analyse d'impact relative à la protection des données (AIPD) du RGPD et le système de gestion des risques de l'article 9 de l'AI Act se recoupent largement dans leur méthodologie, sans se substituer l'un à l'autre : une organisation doit satisfaire les deux textes simultanément, en mutualisant autant que possible sa documentation plutôt qu'en la dupliquant, selon le principe de mapping déjà rencontré à de multiples reprises dans cette plateforme.

## Le mapping avec les référentiels de sécurité de l'information déjà étudiés

L'exigence de cybersécurité de l'article 15, développée au module 2 de ce parcours, recoupe directement les référentiels de sécurité de l'information déjà étudiés dans cette plateforme — une organisation déjà certifiée ISO 27001 ou alignée sur le NIST CSF dispose d'un socle de contrôles techniques largement réutilisable pour démontrer la robustesse et la cybersécurité exigées par l'AI Act pour ses systèmes à haut risque.

## Les pièges les plus fréquents dans une démarche de conformité AI Act

- **Sous-estimer le travail de catégorisation initiale** — ne pas identifier correctement qu'un système relève de l'Annexe III et donc du régime à haut risque, exposant l'organisation à un manquement à l'ensemble des obligations substantielles développées au module 2 de ce parcours.
- **Négliger la requalification du déployeur en fournisseur** — modifier substantiellement un système tiers sans anticiper que cette modification transfère l'intégralité des obligations du fournisseur, un piège déjà signalé au module 3 de ce parcours.
- **Traiter la documentation technique comme un exercice a posteriori** plutôt que comme un livrable construit dès la conception, à l'image du piège déjà signalé pour l'ingénierie de la vie privée dans le parcours NIST Privacy Framework de cette plateforme.
- **Ignorer le régime spécifique aux modèles GPAI** en se concentrant uniquement sur la pyramide des risques par cas d'usage, alors qu'un même modèle fondamental peut relever simultanément des deux régimes.

## Une feuille de route réaliste de mise en conformité

1. **Cartographier l'ensemble des systèmes d'IA développés ou déployés**, et les positionner sur la pyramide des risques (module 1).
2. **Identifier précisément le rôle de l'organisation** — fournisseur, déployeur, importateur ou distributeur — pour chaque système concerné (module 3).
3. **Mettre en place le système de gestion des risques et la gouvernance des données** pour tout système à haut risque, en s'appuyant sur le NIST AI RMF si déjà déployé (module 2).
4. **Constituer la documentation technique, la journalisation et la notice de transparence**, en anticipant leur production dès la conception plutôt qu'après coup (module 2).
5. **Engager l'évaluation de conformité** appropriée — contrôle interne ou organisme notifié selon la catégorie concernée — et obtenir le marquage CE (module 4).
6. **Vérifier le régime applicable aux modèles GPAI** intégrés, y compris le seuil de risque systémique (module 5).
7. **Planifier la mise en conformité selon le calendrier échelonné**, en priorisant les obligations entrant en application le plus tôt (module 6).

## En clôture de ce parcours

Ce parcours a couvert l'AI Act de bout en bout : la pyramide des niveaux de risque et les pratiques interdites, les obligations substantielles imposées aux systèmes à haut risque (système de gestion des risques, gouvernance des données, documentation, transparence, contrôle humain, robustesse), les acteurs et la chaîne de responsabilité, l'évaluation de conformité et le marquage CE, le régime spécifique aux modèles d'IA à usage général, la gouvernance institutionnelle et le calendrier d'application, le régime de sanctions à trois paliers, et enfin son articulation avec le NIST AI RMF, le RGPD et les référentiels de sécurité de l'information déjà étudiés dans cette plateforme. Combiné aux vingt et un autres parcours de cette plateforme, vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels, méthodes et réglementations majeurs qui structurent une démarche GRC moderne — du contrôle interne financier le plus ancien étudié ici jusqu'au texte réglementaire le plus contemporain, celui qui encadre désormais juridiquement, à l'échelle de toute l'Union européenne, les systèmes d'intelligence artificielle dont le risque sociotechnique n'était, il y a quelques années encore, appréhendé que par des cadres méthodologiques volontaires.
