# Le traitement des risques (2/2) : le plan de traitement et le risque résiduel

## Du choix d'une option à un plan de traitement documenté

Une fois l'option ou la combinaison d'options de traitement retenue parmi les sept développées à la leçon précédente de ce parcours, l'organisation doit formaliser un **plan de traitement** précisant les actions concrètes à entreprendre, les responsables désignés pour leur mise en œuvre, les ressources allouées, et les échéances associées. Ce plan de traitement rappelle directement, dans sa fonction, le Plan of Action and Milestones déjà développé dans le parcours FedRAMP de cette plateforme, ou le plan de remédiation déjà développé dans le parcours SWIFT CSP pour l'attestation KYC-SA — un document qui traduit une décision de traitement en engagement concret et vérifiable, plutôt qu'en simple intention.

## L'équilibre entre le coût du traitement et le bénéfice attendu

ISO 31000 impose que le choix et le dimensionnement des options de traitement tiennent compte d'un équilibre entre le coût de leur mise en œuvre et le bénéfice attendu en termes de réduction du risque — un principe de proportionnalité déjà rencontré à de multiples reprises dans cette plateforme, notamment pour l'arbitrage entre le coût d'une stratégie de continuité et le RTO visé dans ISO 22301, ou pour le choix du niveau d'impact FedRAMP proportionné au marché réellement ciblé. Un traitement disproportionné par rapport à la gravité réelle du risque traité constitue un gaspillage de ressources qui pourraient être mieux employées sur des risques plus significatifs.

## Le risque résiduel : ce qui subsiste après traitement

Après la mise en œuvre du plan de traitement, un **risque résiduel** subsiste presque toujours — aucun traitement, aussi rigoureux soit-il, n'élimine jamais totalement un risque. ISO 31000 impose que ce risque résiduel soit explicitement évalué et comparé une nouvelle fois aux critères de risque établis au module 3 de ce parcours, afin de déterminer s'il demeure acceptable ou si un traitement supplémentaire reste nécessaire. Ce principe de risque résiduel rejoint directement celui déjà développé pour l'impossibilité de garantir une sécurité absolue à travers de nombreux parcours de cette plateforme, notamment la mise en garde déjà formulée dans le parcours ISO 27001 selon laquelle une certification n'a jamais promis l'absence totale d'incident, mais seulement la capacité à détecter, traiter et apprendre de celui-ci.

## L'acceptation formelle du risque résiduel par un niveau de gouvernance approprié

L'acceptation du risque résiduel ne doit jamais résulter d'une simple absence de contestation, mais d'une décision **formelle et documentée**, prise par un niveau de gouvernance dont l'autorité est proportionnée à l'ampleur du risque résiduel concerné — un risque résiduel mineur pouvant être accepté par une équipe opérationnelle, tandis qu'un risque résiduel significatif exige l'implication de la direction ou d'un comité de gouvernance dédié. Ce principe de délégation d'autorité proportionnée à la gravité rejoint directement celui déjà développé pour les seuils de délégation évoqués au module 3 de ce parcours, ou pour l'autorité de l'Authorizing Official du NIST RMF, déjà développée dans le parcours dédié de cette plateforme.

## Un exemple concret de traitement combinant plusieurs options

Une organisation confrontée au risque de défaillance d'un fournisseur cloud critique pourrait combiner plusieurs options de traitement développées à la leçon précédente : modifier la probabilité en exigeant contractuellement du fournisseur des engagements de disponibilité renforcés ; modifier les conséquences en développant un plan de continuité prévoyant un basculement vers un fournisseur alternatif ; et partager le risque en souscrivant une couverture d'assurance couvrant les pertes financières en cas d'interruption prolongée — le risque résiduel qui subsiste malgré ces mesures (un délai de basculement minimal incompressible) étant alors formellement accepté par la direction si jugé tolérable.

## Pourquoi ce traitement doit lui-même être réévalué périodiquement

Conformément au principe de dynamisme déjà développé parmi les huit principes du module 1 de ce parcours, un plan de traitement jugé approprié à un instant donné peut devenir insuffisant à mesure que le contexte évolue — un nouveau fournisseur cloud alternatif devenu disponible, une évolution réglementaire modifiant les critères de risque applicables, ou une croissance de l'activité rendant le risque résiduel initial disproportionné par rapport à son ampleur désormais accrue. Cette exigence de réévaluation continue fait directement le lien avec la surveillance et l'enregistrement développés au module suivant de ce parcours.

## Un tableau de synthèse de cette étape

| Élément | Ce qu'il implique |
|---|---|
| Plan de traitement | Actions concrètes, responsables, ressources, échéances |
| Équilibre coût/bénéfice | Un traitement proportionné à la gravité réelle du risque |
| Risque résiduel | Ce qui subsiste après traitement, jamais nul |
| Acceptation formelle | Une décision documentée, par un niveau de gouvernance approprié |

## Le lien avec le module suivant

Ce plan de traitement et l'acceptation du risque résiduel doivent être surveillés dans la durée, enregistrés de façon traçable, et communiqués aux parties prenantes concernées — l'objet du module suivant de ce parcours.
