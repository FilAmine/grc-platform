# Le partage des résultats (2/2) : durée de validité et renouvellement

## Une validité de trois ans, sans surveillance continue intermédiaire formalisée

Un label TISAX reste généralement valable **trois ans** à compter de la date de l'évaluation, une durée sensiblement plus longue que le rythme de surveillance continue mensuel imposé par FedRAMP, ou même que le cycle annuel de surveillance d'une certification ISO 27001, déjà développés dans les parcours dédiés de cette plateforme. Ce choix d'une validité pluriannuelle sans mécanisme intermédiaire de surveillance continue formalisé constitue l'une des différences les plus notables entre TISAX et les référentiels à dominante gouvernementale ou réglementaire déjà étudiés — une différence directement liée à la nature contractuelle plutôt que légale du dispositif, qui laisse davantage l'initiative de la vérification intermédiaire aux partenaires commerciaux eux-mêmes plutôt qu'à un mécanisme centralisé obligatoire.

## Le rôle des partenaires commerciaux dans la surveillance intermédiaire

En l'absence d'un dispositif de surveillance continue centralisé comparable à celui de FedRAMP, ce sont souvent les OEM eux-mêmes, dans le cadre de leur relation contractuelle directe avec leurs fournisseurs, qui exigent des points de contrôle intermédiaires — par exemple, la notification immédiate de tout incident de sécurité significatif affectant les informations partagées, indépendamment du cycle triennal de renouvellement du label. Ce report de la responsabilité de surveillance intermédiaire vers la relation contractuelle bilatérale plutôt que vers un mécanisme centralisé rappelle, par contraste, l'approche bien plus prescriptive et centralisée de la surveillance continue mensuelle de FedRAMP.

## Le processus de renouvellement

À l'approche de l'échéance de validité, le fournisseur doit engager une **nouvelle évaluation complète**, généralement selon la version la plus récente du catalogue VDA ISA alors en vigueur (module 1 de ce parcours) — un renouvellement qui n'est jamais une simple reconduction administrative, mais une réévaluation intégrale des critères applicables, comparable en cela au renouvellement d'une autorisation FedRAMP après un changement significatif d'architecture, ou à la recertification triennale complète d'ISO 27001 déjà développée dans le parcours dédié de cette plateforme.

## Ce qui déclenche une réévaluation anticipée

Au-delà du cycle triennal normal, certains événements peuvent déclencher la nécessité d'une réévaluation anticipée, avant l'échéance normale de validité : un changement substantiel de périmètre (nouveau site de production, nouvelle activité impliquant des données ou prototypes plus sensibles), un incident de sécurité majeur remettant en cause la confiance accordée au fournisseur, ou l'exigence spécifique d'un nouveau partenaire commercial imposant son propre niveau d'évaluation — un mécanisme qui rappelle directement celui des Significant Change Requests déjà développé dans le parcours FedRAMP de cette plateforme, bien que reposant ici sur l'initiative du partenaire commercial ou du fournisseur lui-même plutôt que sur une notification formalisée obligatoire.

## Le risque d'un label expiré ou révoqué au sein de la chaîne d'approvisionnement

Un fournisseur dont le label TISAX arrive à expiration sans renouvellement, ou dont le label serait révoqué à la suite d'un manquement grave constaté, s'expose à une remise en cause directe de sa relation commerciale avec les OEM qui exigent ce label comme condition contractuelle — une conséquence développée plus en détail au module 6 de ce parcours, qui rappelle, dans son principe de sanction purement contractuelle plutôt que légale, celle déjà rencontrée pour la perte du droit d'accepter les paiements par carte en cas de manquement grave à PCI DSS.

## Un tableau de synthèse

| Aspect | TISAX | FedRAMP (comparaison) |
|---|---|---|
| Durée de validité du résultat | Généralement 3 ans | Autorisation continue, sous réserve de la surveillance mensuelle |
| Mécanisme de surveillance intermédiaire centralisé | Absent (repose sur la relation contractuelle bilatérale) | Livrables mensuels obligatoires |
| Déclencheur de réévaluation anticipée | Changement de périmètre, incident majeur, exigence d'un nouveau partenaire | Significant Change Request formalisée |
| Conséquence d'un label expiré ou révoqué | Remise en cause de la relation commerciale avec les OEM concernés | Suspension ou révocation de l'ATO |

## Le lien avec le module suivant

Ce cycle de validité et de renouvellement s'applique de façon particulièrement sensible à l'un des objectifs d'évaluation les plus spécifiques de TISAX — la protection des prototypes —, dont les exigences propres méritent d'être développées en détail dans le module suivant de ce parcours.
