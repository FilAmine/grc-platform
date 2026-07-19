# La fonction Manage : traiter le risque et allouer les ressources

## Transformer la mesure en décision et en action

La fonction **Manage** clôt le cycle opérationnel de l'AI RMF : elle consiste à allouer des ressources aux risques cartographiés (Map) et mesurés (Measure), sur une base régulière et récurrente plutôt que ponctuelle, et à prioriser la réponse à ces risques en fonction de leur gravité et de leur probabilité. Cette fonction rejoint directement, dans son rôle de traitement du risque une fois celui-ci identifié et quantifié, celle déjà développée pour l'étape Implement du NIST RMF ou pour les stratégies de continuité d'ISO 22301, toutes deux développées dans les parcours dédiés de cette plateforme.

## Les quatre options classiques de traitement du risque, appliquées à l'IA

Manage reprend les quatre options de traitement du risque déjà rencontrées de façon générale dans la gestion des risques — **atténuer** le risque (modifier le modèle, ses données d'entraînement, ou ses conditions de déploiement pour réduire un biais ou une vulnérabilité identifiée), **transférer** le risque (par exemple via une clause contractuelle avec un fournisseur de modèle tiers, ou une couverture d'assurance), **éviter** le risque (renoncer purement et simplement à déployer un système dont les risques mesurés s'avèrent disproportionnés par rapport aux bénéfices attendus), ou **accepter** le risque en connaissance de cause, lorsque son niveau reste jugé tolérable au regard de l'appétence pour le risque de l'organisation, elle-même définie au titre de la fonction Govern développée au module 2 de ce parcours.

## L'option d'éviter le risque, une décision parfois plus radicale que dans d'autres référentiels

L'option consistant à éviter purement et simplement le risque en renonçant au déploiement d'un système d'IA mérite une attention particulière dans le contexte de l'AI RMF, par rapport aux référentiels de sécurité de l'information plus classiques déjà étudiés dans cette plateforme : un système présentant des biais discriminatoires persistants, malgré des tentatives d'atténuation, ou dont l'usage détourné potentiel s'avère trop difficile à contenir, peut justifier une décision de retrait pur et simple du système, plutôt qu'un simple ajustement technique — une décision qui rappelle, dans son caractère parfois radical, celle déjà développée pour la révocation d'une autorisation FedRAMP en cas de manquement persistant, développée dans le parcours dédié de cette plateforme, mais ici prise proactivement par l'organisation elle-même plutôt qu'imposée par un tiers.

## La priorisation des risques selon la même logique de gravité et de probabilité

Comme pour la plupart des méthodologies de gestion des risques déjà étudiées dans cette plateforme — la matérialité de SOX, la classification des risques d'EBIOS RM, ou la priorisation par la gravité du POA&M de FedRAMP —, Manage exige de prioriser le traitement des risques identifiés selon une combinaison de leur probabilité de survenance et de la gravité de leur impact potentiel sur les personnes concernées, plutôt que de traiter l'ensemble des risques identifiés avec une intensité uniforme et indifférenciée.

## Le plan de réponse aux incidents propre à l'IA

Manage impose également l'élaboration d'un plan de réponse structuré pour les incidents impliquant un système d'IA — la découverte d'un biais discriminatoire significatif après déploiement, un usage détourné à grande échelle, ou une attaque adverse compromettant la fiabilité du modèle — un plan qui rejoint directement, dans son principe, celui déjà développé pour la planification de la réponse aux incidents dans le parcours SWIFT CSP, ou pour les plans de continuité d'ISO 22301, tous deux développés dans les parcours dédiés de cette plateforme, mais adapté aux spécificités des incidents propres à l'apprentissage automatique — retrait ou recalibrage rapide du modèle, communication transparente envers les personnes affectées, conformément à la caractéristique de responsabilité et de transparence développée au module 1 de ce parcours.

## Le cycle continu entre Map, Measure et Manage

Il est essentiel de souligner que Manage ne constitue jamais une étape terminale isolée : les décisions de traitement du risque qui en résultent (un modèle recalibré, un déploiement restreint à un contexte plus étroit) doivent être réintégrées dans un nouveau cycle Map, pour vérifier que le contexte d'usage a bien été correctement redéfini, puis Measure, pour vérifier que les ajustements ont effectivement réduit les risques mesurés — un cycle itératif continu, plutôt qu'un processus linéaire à sens unique, qui rappelle directement le cycle d'amélioration continue déjà développé pour la clause 10 d'ISO 27001 et d'ISO 22301 dans les parcours dédiés de cette plateforme.

## Le lien avec le module suivant

Ce cycle Govern-Map-Measure-Manage, une fois pleinement maîtrisé, peut être structuré et documenté à travers un mécanisme de Profils, directement inspiré de ceux déjà développés dans le NIST CSF et le NIST Privacy Framework — un mécanisme développé au module suivant de ce parcours.
