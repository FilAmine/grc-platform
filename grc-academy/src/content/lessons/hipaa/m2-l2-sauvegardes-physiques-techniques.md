# La Security Rule (2/3) : les sauvegardes physiques et techniques

## Les sauvegardes physiques (Physical Safeguards)

### Le contrôle d'accès aux installations (Facility Access Controls)

Des politiques et procédures limitant l'accès physique aux installations où sont hébergés les systèmes contenant des ePHI, tout en garantissant un accès approprié au personnel autorisé — un contrôle qui recoupe directement le contrôle 7.2 de l'Annexe A d'ISO 27001 (entrée physique) et le contrôle 9 de PCI DSS (restriction de l'accès physique), tous deux développés dans les parcours précédents de cette plateforme.

### L'utilisation et la sécurité des postes de travail (Workstation Use and Security)

Des politiques précisant les fonctions à accomplir sur un poste de travail donné, la manière de les accomplir, et les caractéristiques physiques d'un environnement de poste de travail permettant d'accéder à des ePHI — par exemple, positionner les écrans hors de la vue directe des personnes non autorisées dans un espace d'accueil de patients.

### Le contrôle des dispositifs et supports (Device and Media Controls)

Des politiques et procédures régissant la réception et la suppression des supports matériels et dispositifs contenant des ePHI entrant et sortant d'une installation, ainsi que le mouvement de ces dispositifs au sein de l'installation — incluant l'élimination sécurisée des supports en fin de vie et la réutilisation sécurisée des supports (effacement complet avant réaffectation), un point qui recoupe directement le contrôle 7.14 de l'Annexe A d'ISO 27001 (mise au rebut sécurisée du matériel), déjà développé dans le parcours dédié de cette plateforme.

## Les sauvegardes techniques (Technical Safeguards)

### Le contrôle d'accès (Access Control)

Des mécanismes techniques permettant de restreindre l'accès aux ePHI aux seules personnes ou programmes disposant des droits d'accès appropriés, incluant une **identification unique de chaque utilisateur** (interdiction des comptes partagés, un principe déjà rencontré dans plusieurs référentiels de cette plateforme), une **procédure d'accès d'urgence** permettant d'obtenir les ePHI nécessaires en cas de situation critique, une **déconnexion automatique** après une période d'inactivité, et le **chiffrement et déchiffrement** des ePHI.

### Les contrôles d'audit (Audit Controls)

Des mécanismes matériels, logiciels et procéduraux qui enregistrent et examinent l'activité dans les systèmes d'information contenant ou utilisant des ePHI — un contrôle qui recoupe directement la famille AU de SP 800-53 et le contrôle 8.15 de l'Annexe A d'ISO 27001, déjà développés dans les parcours précédents de cette plateforme.

### Les contrôles d'intégrité (Integrity)

Des politiques et procédures pour protéger les ePHI contre une altération ou une destruction non autorisée — un objectif qui recoupe le principe d'intégrité de la triade CID (confidentialité, intégrité, disponibilité) déjà rencontré à travers l'ensemble des référentiels de sécurité étudiés dans cette plateforme.

### L'authentification des personnes ou entités (Person or Entity Authentication)

Des procédures pour vérifier qu'une personne ou une entité cherchant à accéder à des ePHI est bien celle qu'elle prétend être — le socle technique de l'authentification, complété par le contrôle d'accès déjà développé plus haut.

### La sécurité de la transmission (Transmission Security)

Des mesures techniques de sécurité pour se prémunir contre l'accès non autorisé aux ePHI transmises sur un réseau de communication électronique, incluant des contrôles d'intégrité et, lorsque approprié, le chiffrement — un contrôle directement comparable à l'exigence 4 de PCI DSS (protection des données lors de leur transmission), déjà développée dans le parcours dédié de cette plateforme.

## Le chiffrement : une exigence non systématiquement obligatoire, mais lourde de conséquences

Un point de vigilance essentiel, développé plus en détail dans la leçon suivante consacrée à la distinction entre spécifications "Required" et "Addressable" : le **chiffrement** des ePHI, qu'il soit au repos ou en transit, n'est pas formulé comme une exigence absolue et systématique dans le texte de la Security Rule — mais son absence expose l'entité à des conséquences directes en cas de violation de données, développées au module 4 de ce parcours : des ePHI correctement chiffrées selon les standards reconnus par le HHS bénéficient d'une exemption de notification en cas de violation (l'équivalent direct de l'exemption de notification individuelle du RGPD en cas de chiffrement fort, déjà développée dans le parcours dédié de cette plateforme), ce qui explique pourquoi, en pratique, la quasi-totalité des entités couvertes matures choisissent de chiffrer systématiquement leurs ePHI malgré l'absence d'obligation absolue formulée dans le texte lui-même.

## Ce que ce panorama confirme sur la convergence des référentiels

Les sauvegardes physiques et techniques de la Security Rule recoupent, une fois de plus, un socle de bonnes pratiques déjà rencontré à travers l'ensemble des référentiels de sécurité étudiés dans cette plateforme (ISO 27001, NIST CSF, CIS Controls, SP 800-53) — la spécificité de HIPAA réside moins dans le contenu technique de ces sauvegardes que dans leur application ciblée aux seules ePHI, et dans le mécanisme de flexibilité "Required vs Addressable" développé dans la leçon suivante, qui structure la manière dont chaque sauvegarde doit être mise en œuvre selon le contexte propre de chaque entité.
