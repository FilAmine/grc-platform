# Gestion des risques : méthodologies et cycle de vie

## Qu'est-ce qu'un risque, précisément ?

Un risque n'est ni une menace, ni une vulnérabilité, ni un incident. C'est leur combinaison :

> **Risque = Menace × Vulnérabilité × Impact** (formulation qualitative la plus répandue)

- **Menace** : un acteur ou événement capable de causer un dommage (un attaquant, une erreur humaine, une panne matérielle, un événement climatique).
- **Vulnérabilité** : une faiblesse qui permettrait à la menace de se concrétiser (un correctif manquant, un droit d'accès trop large, une architecture sans segmentation).
- **Impact** : la conséquence si la menace exploite la vulnérabilité (perte financière, atteinte à la vie privée, interruption d'activité, sanction réglementaire).

Sans vulnérabilité exploitable, une menace ne produit pas de risque significatif. Sans impact, une vulnérabilité n'est qu'une observation technique.

## Le cycle de vie du risque

Toutes les méthodologies sérieuses (ISO 31000, NIST RMF, EBIOS RM) suivent le même squelette :

1. **Identification** — recenser les risques via des ateliers, des cartographies d'actifs, des retours d'incidents, une veille sur les menaces.
2. **Analyse** — estimer la probabilité et l'impact, souvent sur une échelle qualitative (faible/moyen/élevé/critique) ou quantitative (pertes financières estimées, méthode FAIR par exemple).
3. **Évaluation** — comparer le niveau de risque estimé à l'appétence au risque (risk appetite) définie par la gouvernance : est-ce acceptable tel quel ?
4. **Traitement** — choisir une stratégie :
   - **Réduire** : mettre en place un contrôle (ex. chiffrement, MFA, segmentation réseau).
   - **Transférer** : assurance, clause contractuelle avec un sous-traitant.
   - **Éviter** : ne pas lancer le projet ou la fonctionnalité qui porte le risque.
   - **Accepter** : le risque résiduel est jugé tolérable et documenté comme tel, avec validation formelle par le risk owner.
5. **Suivi et revue** — un risque n'est jamais figé : nouvelles menaces, nouveaux actifs, nouveaux contrôles. Le registre de risques doit être vivant, pas un document annuel oublié dans un classeur.

## Les méthodologies principales

### ISO 31000

Norme générique (pas seulement cybersécurité) qui pose les principes et le cadre de management du risque. Elle ne prescrit pas d'échelle de cotation précise — chaque organisation adapte.

### NIST RMF (Risk Management Framework)

Très utilisé aux États-Unis et dans les environnements fortement réglementés. Structuré en étapes : Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor. Fortement lié à NIST 800-53 pour le catalogue de contrôles.

### EBIOS RM (méthode française, ANSSI)

Approche par scénarios, particulièrement adaptée aux menaces sophistiquées (cyberattaques ciblées). Elle articule :

- **Socle de sécurité** : les mesures de base attendues indépendamment du contexte de menace.
- **Scénarios stratégiques** : chemins d'attaque plausibles portés par des sources de risque motivées (état, cybercriminel, concurrent).
- **Scénarios opérationnels** : traduction technique détaillée de ces chemins d'attaque, contre lesquels on dimensionne des mesures de sécurité spécifiques.

EBIOS RM a l'intérêt pédagogique de forcer à raisonner "depuis l'attaquant" plutôt que "depuis la checklist" — un réflexe utile même hors du contexte réglementaire français.

## Le piège du registre de risques déconnecté

Un registre de risques mal construit liste des lignes comme *"risque : cyberattaque"* — trop vague pour être actionnable. Un registre utile relie explicitement :

- l'actif concerné (quelle donnée, quel système),
- le scénario précis (comment la menace exploiterait quelle vulnérabilité),
- le contrôle existant et son niveau d'efficacité réel (pas supposé),
- le risque résiduel après contrôle,
- le propriétaire qui a formellement accepté ce risque résiduel.

C'est cette dernière colonne — le propriétaire et son acceptation explicite — qui manque le plus souvent, et qui est pourtant la seule chose qu'un auditeur ISO 27001 ou SOC 2 vérifiera avec insistance.
