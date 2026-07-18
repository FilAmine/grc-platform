# La Breach Notification Rule

## Une règle introduite par HITECH, plus tardive que celle du RGPD

Contrairement au RGPD, dont l'obligation de notification des violations (articles 33-34, déjà développée dans le parcours dédié de cette plateforme) fait partie intégrante du règlement depuis son origine, HIPAA n'a introduit d'obligation de notification des violations qu'avec le **HITECH Act de 2009**, développé au module 0 de ce parcours — près de six ans après l'entrée en vigueur de la Security Rule elle-même. La règle a ensuite été affinée par l'Omnibus Rule de 2013, notamment sur le critère de déclenchement de la notification, développé plus loin dans cette leçon.

## Qu'est-ce qu'une violation (breach) au sens de HIPAA

Une **violation** est définie comme l'utilisation ou la divulgation impermissible d'informations de santé protégées **non sécurisées (unsecured PHI)** qui compromet la sécurité ou la confidentialité de ces informations. Deux éléments de cette définition méritent d'être développés séparément.

### Les PHI "non sécurisées" : le rôle central du chiffrement

Les PHI sont considérées comme "non sécurisées" si elles n'ont pas été rendues inutilisables, illisibles ou indéchiffrables pour des personnes non autorisées, selon une méthode reconnue par le HHS — principalement le **chiffrement**, conforme à des standards spécifiquement désignés, ou la **destruction** complète du support. Cette architecture crée, pour HIPAA, une **exemption de notification par le chiffrement**, directement comparable à celle déjà développée pour l'article 34 du RGPD dans le parcours dédié de cette plateforme : des PHI correctement chiffrées qui seraient exfiltrées lors d'un incident ne déclenchent aucune obligation de notification, puisqu'elles ne répondent pas, par définition, à la qualification de PHI "non sécurisées".

### Le critère de déclenchement : une évaluation de risque en quatre facteurs

Depuis l'Omnibus Rule de 2013, une utilisation ou divulgation impermissible de PHI non sécurisées est **présumée constituer une violation**, sauf si l'entité couverte ou le Business Associate démontre, sur la base d'une évaluation de risque documentée portant sur au moins quatre facteurs, qu'il existe une **faible probabilité que les informations aient été compromises** :

1. la **nature et l'étendue** des informations de santé protégées concernées, y compris les types d'identifiants et la probabilité de ré-identification,
2. la **personne non autorisée** qui a utilisé les informations ou à qui elles ont été divulguées,
3. si les informations ont **effectivement été consultées ou acquises**, ou si l'opportunité existait seulement sans preuve d'accès réel,
4. la **mesure dans laquelle le risque** pour les informations de santé protégées a été atténué.

Ce mécanisme d'évaluation de risque, qui a remplacé un ancien critère plus subjectif fondé sur le "dommage" pour la personne concernée, rappelle directement, dans sa structure, l'évaluation de risque en plusieurs facteurs déjà développée pour la classification des incidents majeurs de DORA dans le parcours dédié de cette plateforme — les deux mécanismes cherchent à objectiver, à travers des critères précis et documentés, une décision qui reposerait sinon sur une appréciation trop subjective de l'entité concernée.

## Le calendrier de notification

### Notification aux personnes concernées

L'entité couverte doit notifier les personnes concernées **sans délai déraisonnable**, et au plus tard **60 jours calendaires** après la découverte de la violation — un délai sensiblement plus long que celui du RGPD (72 heures pour la notification à l'autorité, développée dans le parcours dédié de cette plateforme), une différence qui reflète la nature distincte des deux mécanismes : le délai HIPAA porte sur la notification complète aux personnes affectées elles-mêmes, tandis que le délai RGPD porte d'abord sur une notification initiale à l'autorité de contrôle, qui peut être complétée par la suite.

### Notification au HHS

Pour une violation affectant **500 personnes ou plus**, l'entité couverte doit notifier le HHS **simultanément** à la notification des personnes concernées (donc également sous 60 jours), et doit en outre notifier les **médias locaux ou nationaux** pertinents pour l'État ou la juridiction concernée — une exigence de publicité sans équivalent direct dans le RGPD ou NIS2 déjà développés dans cette plateforme, qui transforme de facto toute violation de grande ampleur en événement public, le HHS publiant lui-même la liste de ces violations sur un registre accessible publiquement, surnommé de manière informelle le "Wall of Shame".

Pour une violation affectant **moins de 500 personnes**, l'entité couverte peut se contenter d'un signalement **annuel consolidé** au HHS, dans les 60 jours suivant la fin de l'année civile concernée — un régime allégé pour les violations de moindre ampleur, qui rappelle, dans son principe, la distinction déjà rencontrée entre notification individuelle et signalement consolidé pour d'autres référentiels de cette plateforme.

### Le rôle des Business Associates dans la chaîne de notification

Un Business Associate qui découvre une violation doit la notifier à l'entité couverte concernée — et non directement aux personnes affectées, sauf accord contraire prévu dans le BAA (module 3) — sans délai déraisonnable et au plus tard 60 jours après sa découverte, charge ensuite à l'entité couverte de notifier les personnes concernées et, le cas échéant, le HHS et les médias.

## Ce que ce mécanisme révèle en miroir du RGPD

La comparaison entre le régime de notification de HIPAA et celui du RGPD confirme un contraste déjà esquissé dans plusieurs leçons de ce parcours : HIPAA privilégie un délai plus généreux (60 jours) mais une exigence de publicité plus radicale (médias, registre public pour les violations de grande ampleur), tandis que le RGPD impose un délai nettement plus resserré (72 heures) mais réserve la notification initiale à l'autorité de contrôle, sans exigence systématique de publicité médiatique — deux philosophies différentes de la transparence en cas d'incident, développées dans deux contextes juridiques et culturels distincts, mais poursuivant toutes deux le même objectif de fond : permettre aux personnes affectées de se protéger rapidement contre les conséquences d'une violation de leurs données sensibles.
