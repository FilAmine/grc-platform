# L'approche personnalisée et l'analyse de risque ciblée (nouveautés de la v4.0)

## Le débat entre prescription et orientation résultat, déjà rencontré à travers cette plateforme

Ce parcours a déjà signalé, à plusieurs reprises, la tension entre référentiels prescriptifs (SP 800-53, l'Annexe A d'ISO 27001) et référentiels orientés résultat (le NIST CSF). Historiquement, PCI DSS se situait clairement du côté prescriptif : chaque sous-exigence dictait une méthode précise de mise en œuvre, sans grande latitude d'interprétation. La version 4.0 introduit une innovation qui déplace, pour la première fois, une partie du référentiel vers une logique orientée résultat — une évolution qui rejoint directement le débat déjà exploré dans les parcours NIST CSF et NIST RMF de cette plateforme.

## L'approche définie (Defined Approach) : la méthode traditionnelle

Par défaut, une entité suit l'**approche définie** — la formulation prescriptive traditionnelle de chaque exigence, avec des procédures de test précises que l'évaluateur applique littéralement pour vérifier la conformité. C'est la méthode suivie par la quasi-totalité des entités depuis les premières versions du référentiel, et elle reste la voie par défaut en v4.0.

## L'approche personnalisée (Customized Approach) : l'innovation de la v4.0

Pour certaines exigences, une entité peut désormais choisir de suivre l'**approche personnalisée** : plutôt que d'implémenter le contrôle exactement tel que formulé par l'approche définie, l'entité conçoit et met en œuvre son **propre contrôle**, à condition de démontrer qu'il répond à l'**objectif de l'approche personnalisée (Customized Approach Objective)** explicitement énoncé pour chaque exigence éligible — un objectif de sécurité de haut niveau, formulé indépendamment de toute méthode de mise en œuvre précise.

Ce mécanisme rappelle directement, dans son principe, le tailoring des bases de référence de contrôles du NIST RMF déjà développé dans le parcours dédié de cette plateforme, ou encore la logique d'exclusion justifiée de la Déclaration d'Applicabilité d'ISO 27001 — sauf que l'approche personnalisée de PCI DSS ne permet pas d'**exclure** un contrôle, seulement de le **remplacer** par un contrôle équivalent, à charge pour l'entité de démontrer rigoureusement cette équivalence.

## Les exigences documentaires renforcées de l'approche personnalisée

Contrairement à l'approche définie, dont les procédures de test sont standardisées et publiées par le PCI SSC, l'approche personnalisée impose à l'entité de produire une documentation substantielle et rigoureuse :

- une **analyse de risque ciblée** spécifique au contrôle personnalisé, documentant pourquoi ce contrôle atteint l'objectif de sécurité visé,
- une description précise du contrôle mis en œuvre et de la logique qui sous-tend son efficacité,
- des **procédures de test sur mesure**, que l'évaluateur (QSA, déjà développé au module 3) doit lui-même valider comme suffisamment rigoureuses avant de les appliquer.

Cette charge documentaire renforcée n'est pas anodine : l'approche personnalisée reste réservée, en pratique, à des organisations disposant d'une réelle maturité en gestion des risques et d'une relation de confiance établie avec leur QSA — un choix qui ne s'improvise pas à la légère, contrairement à ce que sa flexibilité apparente pourrait suggérer.

## L'analyse de risque ciblée (Targeted Risk Analysis) : au-delà du seul cas de l'approche personnalisée

Indépendamment de l'approche personnalisée, la v4.0 introduit, pour un certain nombre d'exigences spécifiques, la possibilité pour l'entité de **définir elle-même la fréquence** d'un contrôle (par exemple, la fréquence de revue des journaux, ou la fréquence de rotation de certaines clés cryptographiques), plutôt que de se voir imposer une fréquence fixe uniforme par le référentiel — à condition de justifier ce choix par une **analyse de risque ciblée** documentée, propre à ce contrôle précis.

Ce mécanisme rejoint directement le principe de proportionnalité déjà rencontré dans les parcours NIS2 et DORA de cette plateforme : plutôt qu'une fréquence uniforme imposée à toutes les organisations indépendamment de leur contexte réel, PCI DSS v4.0 reconnaît qu'une organisation à fort volume de transactions et à profil de risque élevé peut légitimement justifier une fréquence de contrôle plus soutenue qu'une petite structure à profil de risque plus modeste — sans pour autant abandonner l'exigence de fond elle-même.

## Pourquoi cette évolution reste malgré tout marginale par rapport à l'ensemble du référentiel

Il serait excessif de présenter la v4.0 comme une bascule complète de PCI DSS vers un référentiel orienté résultat comparable au NIST CSF — l'approche personnalisée et l'analyse de risque ciblée ne s'appliquent qu'à un sous-ensemble d'exigences explicitement identifiées comme éligibles, et la grande majorité du référentiel demeure structurée selon l'approche définie prescriptive traditionnelle. Cette évolution doit plutôt se lire comme une **reconnaissance ponctuelle** que certaines exigences se prêtent mieux à une formulation orientée résultat que d'autres — un ajustement de méthode, pas une refonte philosophique complète du référentiel.

## Ce que cette innovation révèle sur la maturité croissante des référentiels étudiés dans cette plateforme

L'introduction de l'approche personnalisée en 2022, quelques années après la formalisation des Implementation Groups des CIS Controls (2019) et l'ajout de la fonction Govern au NIST CSF 2.0 (2024), confirme une tendance de fond déjà observée à plusieurs reprises dans cette plateforme : les référentiels les plus établis évoluent progressivement pour intégrer davantage de flexibilité et de proportionnalité au risque réel de chaque organisation, sans pour autant abandonner le socle de rigueur et de preuve documentée qui a fait leur crédibilité initiale.
