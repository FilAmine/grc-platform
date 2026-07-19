# Les Profils AI RMF : usage et absence délibérée de Tiers

## Un mécanisme de Profils hérité du NIST CSF, appliqué par système ou par cas d'usage

À l'instar des Profils déjà développés dans les parcours NIST CSF et NIST Privacy Framework de cette plateforme, l'AI RMF permet à une organisation de documenter un **Current Profile** (l'état actuel de la gestion du risque pour un système d'IA donné, au regard des quatre fonctions du Core développées aux modules 2 à 5 de ce parcours) et un **Target Profile** (l'état souhaité, compte tenu du contexte spécifique de ce système, de sa criticité et des exigences légales applicables). L'analyse d'écarts entre les deux Profils oriente ensuite les priorités d'action, selon la même logique déjà rencontrée pour les Profils du NIST CSF et du NIST Privacy Framework.

## Une granularité par système, plutôt qu'à l'échelle de toute l'organisation

Une spécificité notable des Profils AI RMF par rapport à ceux du NIST CSF ou du NIST Privacy Framework, généralement établis à l'échelle de l'organisation dans son ensemble, réside dans leur granularité fréquemment plus fine : une organisation déployant plusieurs systèmes d'IA à des fins différentes (un système de recommandation de contenu à faible enjeu, un système de décision de crédit à fort enjeu) établit typiquement un Profil distinct pour chacun de ces systèmes, compte tenu de leur catégorisation de risque différenciée établie lors de la fonction Map développée au module 3 de ce parcours — une granularité qui rappelle celle déjà rencontrée pour les Profils propres à chaque objectif d'évaluation dans le parcours TISAX de cette plateforme, plutôt qu'un Profil unique valable pour l'ensemble de l'organisation.

## Pourquoi l'AI RMF ne reprend pas l'échelle des Implementation Tiers

Comme déjà signalé au module 0 de ce parcours, l'AI RMF a délibérément choisi de ne pas reprendre l'échelle des Implementation Tiers développée dans le NIST CSF et le NIST Privacy Framework — une échelle à quatre niveaux caractérisant la rigueur générale du processus de gestion des risques d'une organisation. Ce choix reflète une prudence méthodologique assumée par le NIST : au moment de la publication de l'AI RMF en 2023, la discipline de gestion du risque IA restait suffisamment jeune et en évolution rapide pour qu'une échelle de maturité standardisée risque de figer prématurément des pratiques encore largement expérimentales, ou de donner une fausse impression de rigueur comparative entre des organisations dont les pratiques de gestion du risque IA n'étaient en réalité pas encore suffisamment normalisées pour être comparées de façon fiable selon une échelle commune.

## Ce que cette absence de Tiers implique concrètement

En pratique, une organisation ne peut ainsi pas se prévaloir d'un "Tier 3" ou d'un "Tier 4" de maturité en gestion du risque IA, comme elle pourrait le faire pour sa gestion du risque de sécurité au titre du NIST CSF ou de la vie privée au titre du NIST Privacy Framework, tous deux développés dans les parcours dédiés de cette plateforme — la comparaison entre organisations reste, pour l'instant, structurée uniquement autour du contenu des Profils eux-mêmes (quels résultats du Core sont effectivement atteints) plutôt que d'une échelle de rigueur globale synthétique.

## Une évolution future probable, à l'image d'autres référentiels de cette plateforme

Ce choix de conception n'est pas nécessairement figé pour l'avenir : à mesure que la discipline de gestion du risque IA se stabilise et que des pratiques communes émergent à l'échelle du secteur, une future révision de l'AI RMF pourrait introduire une échelle de maturité comparable aux Tiers du CSF — une évolution qui rappellerait celle déjà observée pour l'introduction progressive de nouvelles exigences dans les versions successives de PCI DSS ou du CSCF de SWIFT CSP, développées dans les parcours dédiés de cette plateforme, où un référentiel jeune se rigidifie et se structure progressivement à mesure que la pratique du secteur mûrit.

## Un tableau de synthèse comparant les mécanismes de Profils et de Tiers à travers les cadres du NIST

| Cadre | Profils | Tiers |
|---|---|---|
| NIST CSF | Oui, à l'échelle de l'organisation | Oui, échelle à 4 niveaux |
| NIST Privacy Framework | Oui, à l'échelle de l'organisation | Oui, échelle à 4 niveaux |
| NIST AI RMF | Oui, généralement par système ou cas d'usage | Non, choix délibéré d'omission en version 1.0 |

## Le lien avec le module suivant

Cette architecture méthodologique complète — Core à quatre fonctions, Profils sans Tiers — mérite d'être replacée dans le contexte plus large des autres référentiels déjà étudiés dans cette plateforme, notamment sa relation avec le règlement européen sur l'intelligence artificielle actuellement en cours de déploiement — l'objet du dernier module de ce parcours.
