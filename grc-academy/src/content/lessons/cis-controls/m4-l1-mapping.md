# CIS Controls face aux autres référentiels étudiés dans cette plateforme

## Un tableau de synthèse à six référentiels

Ce parcours étant le sixième dédié à un référentiel spécifique dans cette plateforme (après le NIST CSF, ISO 27001, SOC 2, le RGPD et le NIST RMF), le moment est venu de situer précisément les CIS Controls dans cet ensemble.

| Aspect | CIS Controls v8 | NIST CSF 2.0 | ISO 27001 | SP 800-53 (RMF) |
|---|---|---|---|---|
| Nature | Catalogue priorisé, consensus communautaire | Cadre volontaire, orienté résultat | Norme certifiable | Catalogue prescriptif, obligation légale fédérale |
| Mécanisme de priorisation intégré | Implementation Groups (IG1/IG2/IG3) | Tiers et Profils | Analyse de risque + SoA | Catégorisation FIPS 199 + bases de référence |
| Niveau de détail | 18 contrôles, 153 Safeguards | 6 fonctions, catégories, sous-catégories | 93 contrôles | Plus de 1000 contrôles et améliorations |
| Justification empirique | Community Defense Model, données d'attaques réelles | Généraliste, non lié à une méthode de justification empirique propre | Généraliste | Généraliste |
| Coût d'entrée pour une petite structure | Faible (IG1 directement actionnable) | Modéré (nécessite une méthodologie de risque propre) | Élevé (processus de certification complet) | Très élevé (processus RMF complet) |

## Le Controls Navigator : le mapping officiel du CIS

Le CIS publie et maintient un outil de correspondance, le **CIS Controls Navigator**, qui permet de visualiser directement quels Safeguards correspondent à des contrôles ou catégories d'autres référentiels majeurs — notamment le NIST CSF, SP 800-53, et ISO 27001. Ce mapping officiel confirme, avec un degré de précision supplémentaire, ce que cette plateforme a déjà observé à de nombreuses reprises : la grande majorité des exigences techniques concrètes (contrôle d'accès, journalisation, gestion des vulnérabilités, sécurité applicative) se recoupent largement d'un référentiel à l'autre, avec des formulations et des degrés de détail différents.

## Un exemple de mapping filé sur un même sujet

Pour illustrer concrètement cette correspondance, reprenons un sujet déjà suivi à travers plusieurs parcours de cette plateforme : la gestion des risques liés aux prestataires de services.

| Référentiel | Où ce sujet est traité |
|---|---|
| CIS Controls v8 | Contrôle 15 — Gestion des prestataires de services |
| NIST CSF 2.0 | Catégorie GV.SC (Cybersecurity Supply Chain Risk Management) |
| ISO 27001:2022 | Contrôles 5.19 à 5.23 de l'Annexe A |
| SOC 2 | Common Criterion CC9.2 |
| SP 800-53 (NIST RMF) | Famille SR (Supply Chain Risk Management) |

Ce même sujet de fond — évaluer et gérer le risque introduit par les tiers dont dépend une organisation — trouve, dans chacun des six référentiels étudiés dans cette plateforme, une traduction propre, à un niveau de détail et avec un vocabulaire différents, mais fondée sur la même préoccupation de fond. C'est la confirmation la plus directe possible de ce que cette plateforme a répété à plusieurs reprises : au niveau des pratiques concrètes, ces référentiels convergent largement ; ce qui les distingue, c'est leur structure, leur mode de justification, leur mécanisme de preuve, et leur audience.

## Comment une organisation combine concrètement CIS Controls avec un autre référentiel

Dans la pratique, les CIS Controls sont rarement utilisés comme unique référentiel d'une organisation ayant des obligations de certification ou d'attestation formelles (ISO 27001, SOC 2) — ils sont plus souvent utilisés comme **couche opérationnelle et priorisée** sous un référentiel de gouvernance plus large :

- une organisation qui vise une certification ISO 27001 peut utiliser les CIS Controls et leurs Implementation Groups comme guide pratique pour prioriser l'implémentation technique des contrôles de l'Annexe A, en particulier les contrôles technologiques déjà développés dans le parcours dédié de cette plateforme,
- une organisation qui utilise le NIST CSF comme cadre de communication stratégique peut s'appuyer sur les CIS Controls, via leur alignement direct sur les fonctions du NIST CSF (module 2 de ce parcours), pour définir concrètement quels contrôles techniques mettre en œuvre pour chaque fonction visée,
- une petite structure sans ambition de certification immédiate peut adopter directement le profil IG1 comme unique référentiel de départ, sans passer par une démarche de certification ou d'attestation plus lourde, avant d'envisager, à mesure de sa croissance, une démarche ISO 27001 ou SOC 2 plus formelle.

## Ce que cette position particulière révèle sur la fonction des CIS Controls dans un écosystème GRC

Contrairement aux cinq autres référentiels déjà étudiés dans cette plateforme, qui structurent chacun un processus de preuve externe (certification, attestation, autorisation, obligation légale), les CIS Controls n'ont vocation à produire aucune preuve formelle destinée à un tiers — ils fonctionnent comme un outil de **priorisation opérationnelle interne**, utilisable seul par une petite structure, ou en complément d'un référentiel de gouvernance plus formel pour une organisation déjà engagée dans une démarche de certification ou d'attestation. C'est cette fonction spécifique de guide pratique et priorisé, plutôt qu'un contenu technique fondamentalement différent, qui justifie sa place à part entière dans le paysage des référentiels GRC couverts par cette plateforme.
