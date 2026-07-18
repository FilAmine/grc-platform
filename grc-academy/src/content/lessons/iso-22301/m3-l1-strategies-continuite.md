# Les stratégies de continuité d'activité

## De l'analyse à la décision : choisir comment protéger chaque activité critique

Une fois la BIA et l'appréciation des risques réalisées (module 2 de ce parcours), la clause 8.3 d'ISO 22301 impose à l'organisation de déterminer et de sélectionner des **stratégies de continuité** pour chaque activité critique identifiée — c'est-à-dire les grandes options de traitement qui permettront de respecter les délais RTO et RPO fixés, avant même de rédiger le détail opérationnel des plans de continuité, développés à la leçon suivante de ce parcours. Ce choix de stratégie constitue une décision structurante, généralement engageant un investissement significatif, qui doit être validée par la direction dans le cadre de son engagement au titre de la clause 5, déjà développée au module 1 de ce parcours.

## Les stratégies relatives aux locaux et sites

Pour les activités dépendant d'un site physique, plusieurs stratégies sont envisageables selon le RTO visé et le budget disponible :

- **Le site de secours à froid (cold site)** — un local disponible mais dépourvu d'équipement opérationnel immédiat, nécessitant un délai d'installation avant reprise ; adapté à des RTO longs (plusieurs jours à plusieurs semaines).
- **Le site de secours à tiède (warm site)** — un local partiellement équipé, permettant une reprise en quelques heures à quelques jours.
- **Le site de secours à chaud (hot site) ou le fonctionnement en miroir** — une réplique quasi immédiatement opérationnelle du site principal, permettant une reprise en quelques minutes à quelques heures, au prix d'un investissement continu bien plus élevé.
- **Le travail à distance** — pour de nombreuses activités tertiaires, la capacité du personnel à travailler depuis son domicile ou tout autre lieu peut constituer, à elle seule, une stratégie de continuité suffisante et nettement moins coûteuse qu'un site de secours dédié.

## Les stratégies relatives aux systèmes d'information

Le parcours ITIL de cette plateforme a déjà mentionné la pratique de gestion de la continuité des services comme l'une des 34 pratiques du référentiel ; ISO 22301 en développe la substance méthodologique à travers des stratégies telles que la **réplication de données en temps réel ou différé** (déterminée directement par le RPO fixé lors de la BIA), le **basculement automatique ou manuel vers une infrastructure de secours** (déterminé par le RTO), ou le recours à des **prestataires cloud** dont la propre résilience — potentiellement certifiée ISO 22301, FedRAMP ou évaluée dans le cadre de la gestion des risques des prestataires tiers de DORA, déjà développée dans les parcours dédiés de cette plateforme — devient un élément constitutif de la propre stratégie de continuité de l'organisation cliente.

## Les stratégies relatives aux personnes et aux compétences

Une stratégie de continuité doit également anticiper l'indisponibilité de personnel clé, notamment par la **polyvalence croisée (cross-training)** des équipes sur les activités les plus critiques, l'identification de personnel de remplacement formé, ou le recours à des ressources externes temporaires pré-identifiées — une préoccupation qui rejoint, dans son principe de réduction de la dépendance à une personne unique, celle déjà développée pour la séparation des tâches dans le parcours SOX de cette plateforme, bien qu'appliquée ici à la continuité opérationnelle plutôt qu'au contrôle interne financier.

## Les stratégies relatives aux fournisseurs et prestataires critiques

Pour les activités dépendant de fournisseurs identifiés comme critiques lors de la BIA, la stratégie de continuité peut inclure la **diversification des fournisseurs** (éviter la dépendance à un fournisseur unique pour une ressource critique), l'exigence contractuelle que ce fournisseur dispose lui-même d'un dispositif de continuité robuste (une exigence qui rappelle directement celle déjà développée pour les Complementary User Entity Controls des rapports SOC 1 dans le parcours SOX de cette plateforme), ou la constitution de stocks de sécurité pour les ressources matérielles critiques.

## L'arbitrage coût / rapidité de reprise comme fil conducteur

L'ensemble de ces choix de stratégie s'articule autour d'un même arbitrage fondamental, déjà esquissé au module 2 de ce parcours : plus le RTO ou le RPO visé est court, plus l'investissement nécessaire pour l'atteindre est élevé — un principe de proportionnalité qui rappelle celui déjà rencontré à de multiples reprises dans cette plateforme, et qui justifie précisément la rigueur de la BIA : sans une hiérarchisation précise des activités réellement critiques, une organisation risquerait soit de sur-investir dans des stratégies de continuité disproportionnées pour des activités secondaires, soit, à l'inverse, de sous-investir dans la protection d'activités véritablement vitales.

## Le lien avec la leçon suivante

Une fois les stratégies choisies, l'organisation doit encore les traduire en plans de continuité opérationnels détaillés, ainsi qu'en une structure de gestion de crise capable de piloter effectivement leur activation le jour où une perturbation survient réellement — l'objet de la leçon suivante de ce parcours.
