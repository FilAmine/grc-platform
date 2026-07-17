# Construire une feuille de route réaliste avec les CIS Controls

## L'avantage distinctif : un point de départ immédiatement actionnable

Contrairement aux cinq autres référentiels déjà étudiés dans cette plateforme, dont la première étape suppose généralement de construire une méthodologie de risque propre (analyse de risque ISO 27001, catégorisation FIPS 199 du RMF) ou de cadrer un périmètre d'audit (SOC 2), les CIS Controls offrent un avantage pratique déterminant pour une organisation qui découvre la sécurité de l'information de façon structurée : le profil **IG1** (module 2) constitue un point de départ immédiatement actionnable, sans préalable méthodologique lourd.

## Les étapes typiques d'une première adoption

### Étape 1 — Cartographier l'existant par rapport à IG1

Avant tout investissement nouveau, évaluer précisément quels Safeguards du profil IG1 sont déjà couverts, même partiellement ou informellement, par les pratiques existantes de l'organisation — un exercice similaire, dans son principe, à l'évaluation de préparation (readiness assessment) déjà développée dans le parcours SOC 2 de cette plateforme, mais généralement plus rapide à mener compte tenu du nombre plus restreint de Safeguards concernés (environ 56 pour IG1).

### Étape 2 — Combler les écarts IG1 en priorité absolue

Concentrer l'effort initial exclusivement sur les Safeguards IG1 manquants, en résistant à la tentation de disperser l'effort sur des Safeguards IG2 ou IG3 jugés plus intéressants ou plus visibles techniquement, mais moins prioritaires au regard du principe même de la priorisation par Implementation Groups (module 2) : un socle IG1 incomplet rend largement illusoire tout investissement dans des contrôles plus avancés.

### Étape 3 — Utiliser CIS CSAT pour suivre la progression

S'appuyer sur l'outil gratuit CIS Controls Self Assessment Tool (module 2) pour documenter et suivre dans le temps la couverture réelle des Safeguards, plutôt que de maintenir un suivi ad hoc dispersé entre plusieurs équipes sans vision consolidée.

### Étape 4 — Réévaluer le profil cible à mesure de la maturité

Une fois IG1 solidement couvert et maintenu dans la durée (pas seulement atteint ponctuellement), réévaluer si le profil cible de l'organisation devrait évoluer vers IG2, en fonction de l'évolution de son contexte (croissance, nouvelles obligations contractuelles, engagement dans une démarche ISO 27001 ou SOC 2 parallèle) — un processus de révision comparable, dans son esprit, à la réévaluation périodique des Tiers du NIST CSF déjà développée dans le parcours dédié de cette plateforme.

### Étape 5 — Documenter les écarts justifiés via CIS RAM

Pour les Safeguards du profil cible qui ne seraient délibérément pas mis en œuvre, documenter cette décision selon la méthode CIS RAM (module 3) plutôt que de la laisser implicite — une pratique qui protège l'organisation en cas de contestation ultérieure, et qui rejoint directement la discipline de justification documentée des exclusions déjà développée pour la Déclaration d'Applicabilité d'ISO 27001 dans le parcours dédié de cette plateforme.

## Les pièges les plus fréquents

- **Viser IG2 ou IG3 d'emblée par ambition, sans base IG1 réellement consolidée** — un piège symétrique à celui déjà signalé pour une catégorisation RMF de complaisance : ici, l'erreur consiste à sur-investir prématurément dans des Safeguards avancés (tests d'intrusion réguliers, surveillance réseau sophistiquée) alors que des lacunes basiques persistent (inventaire des actifs incomplet, comptes dormants non désactivés) — les Safeguards avancés produisent alors un bénéfice de risque limité tant que les fondations restent fragiles.
- **Traiter le CIS CSAT comme un exercice ponctuel** — documenter une fois la couverture des Safeguards, puis ne jamais la mettre à jour, un piège de "projet qui s'arrête à l'évaluation initiale" déjà signalé à plusieurs reprises pour d'autres référentiels dans cette plateforme.
- **Ignorer les Benchmarks au profit des seuls Controls** — se limiter à une lecture de haut niveau des 18 contrôles sans jamais descendre au niveau de configuration technique précise qu'offrent les Benchmarks correspondants (module 3), produisant une conformité déclarative sans traduction technique réellement vérifiable.

## Combiner les CIS Controls avec les autres parcours de cette plateforme

Pour une organisation déjà engagée dans une démarche ISO 27001 ou un programme SOC 2 (parcours dédiés de cette plateforme), les CIS Controls et leurs Implementation Groups offrent un moyen concret de prioriser l'ordre d'implémentation des contrôles techniques exigés par ces référentiels plus formels — plutôt que d'implémenter les contrôles de l'Annexe A ou les Common Criteria dans un ordre arbitraire, s'appuyer sur la logique de priorisation déjà éprouvée des Implementation Groups permet de traiter en premier les fondations les plus déterminantes pour la réduction du risque réel, avant les contrôles plus avancés.

## En clôture de ce parcours

Ce parcours a couvert les CIS Controls de bout en bout : leurs origines dans les Consensus Audit Guidelines et le transfert de gouvernance vers le CIS, la structure des 18 contrôles et de leurs 153 Safeguards, le système de priorisation par Implementation Groups qui constitue l'innovation la plus distinctive du référentiel, l'écosystème complet du CIS au-delà des seuls Controls (Benchmarks et CIS RAM), le mapping avec les référentiels déjà étudiés dans cette plateforme, et une feuille de route réaliste de première adoption. Combiné aux six autres parcours de cette plateforme — les fondamentaux GRC et Security by Design, le NIST CSF 2.0, ISO 27001 en profondeur, SOC 2 en profondeur, le RGPD en profondeur, et le NIST RMF en profondeur — vous disposez désormais d'une compréhension à la fois large et approfondie de l'ensemble des référentiels majeurs qui structurent une démarche GRC moderne, du plus stratégique et volontaire (NIST CSF) jusqu'au plus opérationnel et immédiatement actionnable (CIS Controls).
