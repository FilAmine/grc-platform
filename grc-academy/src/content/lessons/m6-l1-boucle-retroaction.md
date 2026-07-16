# De la gouvernance à l'implémentation technique : boucler la boucle

## Reconstituer le fil complet

Cette formation a traversé six modules qui, pris séparément, peuvent sembler être des sujets distincts. Ils forment en réalité une seule chaîne causale continue :

1. **La gouvernance** (module 1) fixe l'intention et l'appétence au risque : qui décide, quel niveau de risque est acceptable.
2. **La gestion des risques** (module 1) traduit cette intention en scénarios concrets et en décisions de traitement (réduire, transférer, éviter, accepter).
3. **Les référentiels** (module 2 — ISO 27001, NIST CSF, SOC 2, RGPD) donnent un vocabulaire commun et une structure de preuve pour démontrer que ce traitement est réel et suivi dans le temps.
4. **Security by Design** (module 3) est la discipline qui garantit que les contrôles décidés en amont se traduisent en choix d'architecture réels, au moment de la conception.
5. **Privacy by Design** (module 4) applique cette même discipline spécifiquement aux données personnelles, avec une obligation légale directe (RGPD article 25).
6. **Cloud Security by Design** (module 5) est l'application concrète de tout ce qui précède au terrain le plus courant des architectures modernes — où la frontière de responsabilité, l'IAM et la configuration réseau deviennent les leviers pratiques.

Le point essentiel de cette synthèse : **aucun de ces niveaux ne fonctionne isolément**. Une gouvernance sans traduction technique produit des politiques qui ne sont jamais appliquées. Une architecture Security by Design sans gouvernance produit des choix techniques incohérents, non priorisés, et invérifiables en audit.

## La boucle de rétroaction, pas une chaîne à sens unique

Un schéma erroné, très répandu, présente ces niveaux comme une hiérarchie descendante : la gouvernance décide, la technique exécute. En réalité, l'information doit circuler **dans les deux sens** :

- **Descendant** : la gouvernance fixe des objectifs de risque, qui informent les choix d'architecture.
- **Ascendant** : les contraintes et retours techniques informent la gouvernance. Un architecte qui découvre qu'un objectif de risque est irréaliste ou disproportionné par rapport à l'effort d'implémentation doit pouvoir remonter cette information au comité de gouvernance (module 1), qui peut alors ajuster l'appétence au risque ou allouer davantage de ressources — plutôt que de laisser un contrôle mal implémenté ou contourné en silence.
- **Un incident réel** (module 1, fonction Respond/Recover de NIST CSF) doit systématiquement remonter jusqu'à la gouvernance : quelle décision de risque s'est révélée insuffisante, et pourquoi.

Cette circulation bidirectionnelle est exactement ce que le cycle **PDCA** (Plan-Do-Check-Act, module 1) formalise : Check et Act ne sont pas des étapes administratives, ce sont les mécanismes qui font remonter la réalité technique vers la gouvernance.

## Un exemple filé, du principe à la ligne de configuration

Pour rendre cette chaîne concrète, un seul exemple traversant tous les niveaux :

- **Gouvernance** : le comité des risques fixe que les données de santé traitées par l'organisation constituent un actif à protection maximale (appétence au risque très faible).
- **Risque** : l'analyse de risque identifie un scénario — accès non autorisé à la base de données de santé par un compte compromis.
- **Référentiel** : ISO 27001 Annexe A 8.24 (cryptographie) et 5.15 (contrôle d'accès) s'appliquent ; le RGPD qualifie ces données de catégorie particulière (article 9), imposant une DPIA (module 4).
- **Security by Design** : le threat modeling STRIDE (module 3) identifie l'élévation de privilège et la divulgation d'information comme menaces prioritaires sur ce système.
- **Privacy by Design** : la donnée de santé est pseudonymisée dans les environnements non-production, et minimisée dans les journaux applicatifs (module 4).
- **Cloud Security by Design** : la base de données est placée dans un sous-réseau privé sans accès direct depuis internet, chiffrée au repos avec des clés gérées par le client (BYOK), accessible uniquement via un rôle IAM scopé à ce seul service, avec MFA obligatoire pour tout accès administratif (module 5).

Chaque ligne de cet exemple est la traduction, à un niveau d'abstraction différent, de la même décision initiale : "les données de santé sont un actif à protection maximale". C'est cette cohérence verticale — de la salle du comité de gouvernance jusqu'à la ligne de configuration IAM — qui constitue, en définitive, ce que "Security by Design" veut dire dans la pratique.
