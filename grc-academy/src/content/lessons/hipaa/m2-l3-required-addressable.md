# La Security Rule (3/3) : spécifications Required et Addressable

## Un mécanisme de flexibilité propre à HIPAA

Chaque norme de la Security Rule (les catégories de sauvegardes déjà développées dans les deux leçons précédentes) se décompose en **spécifications de mise en œuvre (implementation specifications)**, classées selon l'une de deux catégories : **Required (exigée)** ou **Addressable (à considérer)** — un mécanisme de flexibilité propre à HIPAA, qui rappelle, dans son principe, plusieurs mécanismes déjà rencontrés dans cette plateforme sous des formes différentes : le tailoring des bases de référence du NIST RMF, les compensating controls d'ISO 27001, ou l'approche personnalisée de PCI DSS v4.0.

## Les spécifications Required : aucune marge d'appréciation

Une spécification classée **Required** doit être mise en œuvre telle quelle, sans exception ni marge d'interprétation — par exemple, la désignation d'un responsable de la sécurité (déjà développée au module 2) ou l'attribution d'un identifiant unique à chaque utilisateur (déjà développée au module 2) sont des spécifications Required : aucune entité couverte ne peut légitimement s'en dispenser, quel que soit son contexte.

## Les spécifications Addressable : une obligation d'évaluation, pas une option facultative

Une confusion très répandue, y compris chez des praticiens expérimentés, consiste à croire qu'une spécification "Addressable" serait **facultative** — c'est une erreur d'interprétation qui expose directement à un manquement. Une spécification Addressable impose à l'entité couverte de suivre un processus en plusieurs étapes, obligatoire dans son principe même s'il peut aboutir à ne pas implémenter la mesure littéralement décrite :

1. **Évaluer** si la spécification constitue une mesure de sauvegarde raisonnable et appropriée dans l'environnement de l'entité, compte tenu de sa taille, sa complexité, ses capacités techniques, le coût des mesures de sécurité, et la probabilité et la criticité des risques potentiels pour les ePHI.
2. Si l'évaluation conclut que la spécification est raisonnable et appropriée, **l'implémenter** telle quelle.
3. Si l'évaluation conclut qu'elle ne l'est pas, **documenter** cette conclusion et implémenter une **mesure alternative équivalente**, qui atteint le même objectif de sécurité par un moyen différent.
4. Si aucune mesure alternative n'est nécessaire pour satisfaire la norme sous-jacente, documenter également cette conclusion.

Ce qui reste absolument obligatoire, quelle que soit l'issue de cette évaluation, c'est la **documentation** de la décision et de son raisonnement — une entité qui n'implémente pas une spécification Addressable sans avoir documenté sérieusement ce processus d'évaluation se trouve en situation de manquement, exactement comme si elle avait ignoré une spécification Required.

## Un exemple concret de ce mécanisme en action

Le chiffrement des ePHI au repos, déjà évoqué à la fin de la leçon précédente, constitue l'exemple le plus fréquemment cité de spécification Addressable : une petite structure de soins primaires, dont l'ensemble des ePHI reste hébergé sur un unique poste de travail dans un local fermé à clé avec un accès physique très restreint, pourrait en théorie documenter que le chiffrement complet du disque n'est pas strictement nécessaire compte tenu de ces autres mesures compensatoires déjà en place — à condition que cette conclusion soit rigoureusement analysée et documentée, pas simplement affirmée par commodité. Une entité hospitalière de grande taille, avec de nombreux postes de travail mobiles et un risque de perte ou de vol nettement plus élevé, ne pourrait raisonnablement pas parvenir à la même conclusion, et devrait implémenter le chiffrement effectivement.

## Le parallèle avec les mécanismes de flexibilité déjà rencontrés dans cette plateforme

Ce mécanisme "Required vs Addressable" rejoint directement, dans son esprit, plusieurs mécanismes déjà développés dans les parcours précédents de cette plateforme :

- le **tailoring** des bases de référence de contrôles du NIST RMF, où chaque contrôle peut être ajusté ou remplacé par un contrôle compensatoire documenté,
- les **compensating controls** déjà évoqués implicitement à travers la Déclaration d'Applicabilité d'ISO 27001, où une exclusion de contrôle doit être justifiée par l'analyse de risque,
- l'**approche personnalisée** de PCI DSS v4.0, qui permet de substituer un contrôle personnalisé à la formulation prescriptive par défaut, sous réserve d'une documentation rigoureuse.

Ce qui distingue HIPAA de ces trois précédents, c'est l'absence de tiers évaluateur systématique validant cette décision (contrairement à l'auditeur ISO 27001, l'Authorizing Official du NIST RMF, ou le QSA de PCI DSS) : l'entité couverte s'auto-évalue, sous sa propre responsabilité, avec le risque que cette évaluation soit examinée a posteriori par l'OCR en cas de plainte, d'audit, ou de violation — un point qui rejoint directement l'importance déjà soulignée de la qualité de la documentation produite, seule protection réelle de l'entité en cas de contestation ultérieure.

## Pourquoi ce mécanisme illustre, une fois de plus, la maturité comparée des référentiels

L'existence de ce mécanisme de flexibilité dès la première version de la Security Rule (2003) — bien avant les Implementation Groups des CIS Controls (2019), le tailoring du NIST RMF (formalisé dans sa structure actuelle en 2018), ou l'approche personnalisée de PCI DSS (2022) — montre que HIPAA a anticipé, dès l'origine, un problème que d'autres référentiels n'ont formalisé que plus tardivement : un référentiel de sécurité prescriptif appliqué uniformément à des organisations de taille et de complexité radicalement différentes (un cabinet médical individuel et un centre hospitalier universitaire relèvent tous deux de HIPAA) ne peut fonctionner sans un mécanisme de proportionnalité intégré dès sa conception.
