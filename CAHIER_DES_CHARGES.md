# Cahier des charges — Colonne Active

Webapp personnelle pour **encadrer et suivre des séances de renforcement musculaire** centrées sur le dos, la mobilité, les tendons et les fascias.

## 1. Contexte et objectifs

**Profil de l'utilisateur**
- Adulte sportif atteint d'une **scoliose idiopathique thoracique et lombaire**.
- Pratique régulière de l'endurance depuis une dizaine d'années, qui lui a permis de se maintenir :
  - natation 2 fois par semaine (lundi et jeudi soir, environ 1 h) ;
  - course à pied 2 à 3 fois par semaine.
- L'application doit pérenniser ces routines.

**Objectifs des séances**
1. Solliciter les **muscles profonds du dos**, en particulier les lombaires (multifides, carré des lombes, transverse, obliques).
2. Améliorer la **mobilité** : rachis thoracique, hanches, cage thoracique.
3. Renforcer **tendons et ligaments** : isométries longues, excentriques lents.
4. Maintenir des **fascias** en bonne santé : rebonds élastiques, auto-massage, étirements globaux.
5. Compléter la course et la natation (jambes, haut du dos, stabilité du bassin).

**Contraintes de santé**
- **Toutes les routines sont soumises à la validation d'un kinésithérapeute.** L'application offre un espace pour noter son avis sur chaque exercice.
- Principes appliqués :
  - colonne neutre ;
  - pas de flexion ni de rotation lombaire sous charge ;
  - pas d'étirement forcé en fin d'amplitude ;
  - attendre 30 à 60 min après le lever avant tout mouvement en flexion ;
  - douleur tolérée jusqu'à 3/10 si elle ne persiste pas le lendemain ;
  - arrêt immédiat en cas de signes neurologiques.
- Le travail asymétrique (série supplémentaire de planche latérale côté convexité) est **désactivé par défaut**. Il ne s'active qu'après l'accord du kiné.
- Les données de santé personnelles (côtés des courbures, etc.) ne sont **pas écrites dans le code**. Elles sont saisies dans les Réglages et restent sur l'appareil.

## 2. Matériel disponible

- Kit Blackroll : rouleau et balle de massage.
- Deux haltères de 2 kg.
- Deux élastiques à boucle : un très souple, un moyen.
- Bande élastique 10 kg à 6 positions de résistance. Le sens de la numérotation est à vérifier sur la notice.
- Mobilier courant : chaise, mur, marche d'escalier. Un pack d'eau ou un sac à dos chargé sert de charge pour la marche valise et le goblet squat.

Les Réglages permettent de décocher le rouleau ou la marche. Les exercices concernés affichent alors une variante.

## 3. Séances

### 3.1 Trois séances

| Séance | Durée estimée | Blocs |
|---|---|---|
| **Courte A · Dos** | ≈ 12 min | Réveil (respiration costale 3D, chat-vache) · Gainage profond (planche et mountain climber lent, bird dog, planche latérale) · Hanches (pont fessier, étirement des fléchisseurs de hanche) |
| **Courte B · Jambes** | ≈ 13 min | Réveil (chat-vache, transitions 90/90) · Jambes (squat lent, fente statique) · Gainage profond (bird dog, planche latérale) · Retour au calme (étirement des fléchisseurs de hanche) |
| **Longue** | ≈ 40 min | Mobilité (respiration costale 3D, chat-vache, rotation thoracique, 90/90) · Gainage profond et dos (planche, bird dog, planche latérale, dead bug, Pallof press, tirage élastique, marche valise) · Tendons et ligaments (pont fessier, chaise contre le mur, mollets excentriques) · Fascias et retour au calme (rebonds, auto-massage, étirement du psoas, posture de l'enfant latéralisée, repos en décharge) |

- Les séances courtes se font presque tous les jours.
- La séance longue se fait 1 à 2 fois par semaine.
- Les durées sont calculées automatiquement à partir des doses du niveau en cours.

### 3.2 Semaine type

| Jour | Prévu |
|---|---|
| Lundi | Courte B le matin, natation le soir |
| Mardi | Course, puis courte A |
| Mercredi | Séance longue (jour sans endurance) |
| Jeudi | Courte B le matin, natation le soir |
| Vendredi | Course, puis courte A |
| Samedi | Séance longue |
| Dimanche | Course facultative, puis courte A (sans course, courte B) |

Logique :
- la courte B (jambes) se place les jours sans course ;
- la courte A (dos) se place les jours de course ;
- la page « Aujourd'hui » recommande la séance du jour, et les trois restent accessibles.

### 3.3 Exercices retirés des séances

Ces fiches restent visibles dans la bibliothèque, pour le kiné :
- **Curl-up de McGill** : peu de sensations. Remplacé par la planche et le mountain climber lent.
- **Planche de Copenhague** : mauvaises sensations.

## 4. Bibliothèque d'exercices

Il y a 23 exercices, répartis en 7 catégories :
- Respiration
- Mobilité
- Gainage profond
- Renforcement
- Tendons et ligaments
- Fascias
- Retour au calme

Chaque fiche contient :
- **1 à 3 schémas** (silhouettes SVG) : position de départ, position d'arrivée, flèches de mouvement, accessoires.
- **Étapes numérotées**, **ce qu'il faut sentir** et **ce qu'il faut éviter**.
- **Pourquoi** l'exercice est utile dans ce contexte.
- **Niveaux de progression**, de 2 à 6 selon l'exercice. Le niveau courant se règle avec les boutons − / +.
- **Vidéos** : liens horodatés quand une vidéo précise existe, plus un lien de recherche YouTube ciblé. Les vidéos sont à faire vérifier par le kiné.
- **Avis du kiné** : statut Non évalué / Validé / À adapter / Retiré, avec un champ de remarques.
  - Un exercice « Retiré » disparaît des séances guidées.
  - Les remarques s'affichent pendant la séance.

**Règle de progression**
- Monter d'un niveau quand l'effort est « 🙂 Facile » ou moins sur trois séances de suite, sans hausse de douleur le lendemain.
- Une seule progression par semaine.

Un tableau récapitulatif des trois séances (exercice, dose, avis du kiné) sert de support pour le rendez-vous avec le kiné.

## 5. Lecteur de séance guidée

- **Avant la séance** : douleur lombaire (0–10).
- **Enchaînement automatique** des étapes : préparation (5 à 20 s, réglable) → travail → repos entre séries.
- **Types d'exercice**
  - Maintien (hold) : répétitions de maintiens chronométrés avec relâchement de 3 s.
  - Durée : minuteur continu.
  - Répétitions.
- **Rythme guidé des répétitions** (activé par défaut)
  - 4 s de mise en place avec décompte.
  - Chaque répétition a une durée fixe propre à l'exercice.
  - Bip aigu au début de chaque répétition, bip grave à mi-parcours pour repartir dans l'autre sens.
  - Passage automatique à la suite.
  - Affichage « Aller / Retour » et « 3/8 ».
  - Si le rythme est désactivé : bouton « Série terminée ».
- **Annonces vocales** en français (activées par défaut) : nom de l'exercice, numéro de série, côté, comptage des répétitions et des maintiens, « Repos ». Elles utilisent la synthèse vocale du navigateur.
- **Bips** : décompte des 3 dernières secondes, changements de phase. Vibration si disponible.
- **Écran maintenu allumé** (Wake Lock).
- À côté du minuteur : schémas, étapes, remarques du kiné, vidéos et étape suivante.
- **Commandes** : pause, étape précédente, étape suivante, +15 s, « je suis prêt », quitter (avec enregistrement possible).
- **En fin de séance** : douleur, **effort perçu en 5 emoji**, notes, puis enregistrement.

### 5.1 Son sur iPhone

- Le son est déverrouillé au toucher de « Commencer » :
  - session audio en mode « lecture » (API `navigator.audioSession`, Safari 17+) ;
  - fichier muet joué en boucle pendant la séance, pour que l'interrupteur silencieux ne coupe pas les bips ;
  - trois éléments `<audio>` autorisés pour jouer plus tard les bips de secours.
- **Bips de secours** : si iOS suspend le contexte Web Audio (annonce vocale, notification, veille), le bip est joué par un élément `<audio>` (son pré-calculé en WAV).
- **Bandeau** dans le lecteur quand Web Audio est suspendu ou que la boucle muette reste arrêtée plus de 2,5 s hors annonce (cas du mode silencieux) : « touche ici pour le rétablir ». Tout toucher pendant la séance relance le son.
- **Voix enregistrée** : les 99 phrases de l'app (noms d'exercices, côtés, « Série 1 » à 6, « Série bonus », nombres 1 à 30, « Maintien 1 » à 12, « Repos », « C'est parti ») sont enregistrées avec la voix française « Thomas » de macOS (MP3 22 kHz, `outils/generer_voix.py`) et jouées par Web Audio, comme les bips. Sur iPhone, la synthèse vocale du navigateur interrompt tout le son de la page et, en mode silencieux, les bips ne reviennent pas : les enregistrements évitent ce problème. Une annonce composée (« Série 2, Côté gauche ») enchaîne deux enregistrements. La synthèse vocale ne sert plus que pour une phrase non enregistrée.
- **Synthèse vocale (secours)** : court délai après l'interruption d'une annonce (Safari iOS perd sinon la nouvelle annonce), références gardées sur les annonces en cours, reprise si la synthèse est en pause, voix française choisie.
- **Relance après la voix** : sur iPhone, une annonce vocale interrompt tout le son de la page (Web Audio « interrupted », boucle muette en pause). Après chaque annonce, et à chaque changement d'état du son, l'app relance Web Audio et la boucle muette, et note le résultat dans le journal.
- **Bip puis voix** : une annonce attend la fin du bip qui l'accompagne (+ 150 ms), car iOS baisse ou coupe les autres sons quand la voix démarre. Bips d'au moins 130 ms, plus forts.
- **Écran allumé** : API Wake Lock ; à défaut, vidéo muette en boucle.
- **Réglages** :
  - « Tester le son et la voix » : trois bips puis une phrase ;
  - « Tester un enchaînement de séance » : 16 s qui rejouent annonce, compte à rebours, fin de série et repos ;
  - « Journal du son » : derniers événements (bips et canal utilisé, voix, état Web Audio, veille) pour le diagnostic.

## 6. Suivi

- **Saisie rapide** d'une activité (courte, longue, natation, course) : date, durée, distance, douleur après, effort, notes.
  - **Natation** : durée par défaut **60 min**, distance par défaut **1300 m**, distance saisie en mètres.
  - **Course** : distance saisie en km.
- **Effort perçu** sur 5 niveaux :

  | Niveau | Emoji | Libellé |
  |---|---|---|
  | 1 | 😌 | Très facile |
  | 2 | 🙂 | Facile |
  | 3 | 😐 | Moyen |
  | 4 | 😤 | Difficile |
  | 5 | 🥵 | Très dur |

- **Tuiles hebdomadaires** avec objectifs : courte 5, longue 2, natation 2, course 3.
- **Douleur moyenne** sur 14 jours, comparée aux 14 jours précédents.
- **Grille des 8 dernières semaines** : une pastille par activité et par jour.
- **Courbe de la douleur lombaire** sur les 40 dernières activités.
- **Journal** : 40 dernières entrées, suppression possible. La variante A/B est affichée.

## 7. Motivation

### 7.1 Série de jours de renfo consécutifs

- Une séance courte ou longue enregistrée compte pour la journée.
- La série en cours reste valable tant que la séance du jour n'est pas encore faite.
- La carte de série affiche, à côté d'une médaille hexagonale qui porte le nombre de jours :
  - la série actuelle ;
  - le message du jour (« Fais ta séance aujourd'hui pour passer à N + 1 jours ») ;
  - le prochain badge de série ;
  - le record.
- Elle apparaît sur « Aujourd'hui » et dans « Suivi ».

### 7.2 Assiduité natation

- **Petites vacances scolaires de la zone B** (Toussaint, Noël, hiver, printemps) : pas de séance de natation.
  - Dates du calendrier officiel (data.education.gouv.fr), saisies dans `VACANCES` jusqu'à l'année 2027-2028. À compléter chaque année.
  - Une semaine de vacances est **neutre** : elle ne casse pas la série et n'entre pas dans le taux d'assiduité.
  - Ces jours-là, « Aujourd'hui » affiche « Pas de natation ce soir » au lieu du rappel, et la note du jour est ajustée.
  - La grille des 8 semaines hachure les jours de vacances ; la frise natation marque la semaine « vac. ».
  - La tuile hebdomadaire natation vise le nombre de nages prévues (0 pendant les vacances).
- **Semaines complètes de suite** : toutes les nages prévues de la semaine sont faites. La semaine en cours compte dès qu'elle est complète.
- **Record** de semaines complètes.
- **Taux d'assiduité sur 8 semaines** : nages faites / nages prévues (lundi et jeudi, hors vacances), compté depuis la première activité notée.
- **Distance nagée** sur le mois en cours et au total, nombre de nages.
- Frise de 8 semaines, avec deux pastilles par semaine.
- Les lundis et jeudis hors vacances, un rappel « Natation ce soir » s'affiche sur « Aujourd'hui », avec un bouton pour noter la nage.

### 7.3 Badges (16)

Des médailles dessinées en SVG, dans l'esprit des récompenses d'activité de l'Apple Watch :

- **Forme par famille** : cercle (nombre de séances), hexagone (séries de jours), octogone (régularité dans la semaine), carré arrondi (séances longues), écusson (natation), losange (distance nagée).
- **Métal du cerclage selon le palier** : bronze, argent ou or.
- **Face** en dégradé radial de la couleur du badge, chiffre en relief, pictogramme (flamme, vague, goutte, pousse, haltère, calendrier, briques) et unité en petites capitales, reflet brillant en haut.
- **Badge non obtenu** : même médaille en gris translucide, avec barre et texte de progression.
- **Un toucher** sur un badge l'ouvre en grand sur fond sombre, avec une entrée en rotation 3D. Cette animation est désactivée si le système demande de réduire les animations.
- **Nouveau badge** à l'enregistrement : la même fenêtre s'ouvre (« Nouveau badge », ou « N nouveaux badges » avec les autres en miniature), avec un petit arpège si les sons sont activés.

| Badge | Forme · palier | Condition |
|---|---|---|
| Premier pas | cercle vert · bronze | 1re séance de renfo |
| Trois de suite | hexagone orange · bronze | 3 jours consécutifs |
| Cinq de suite | hexagone rouge · argent | 5 jours consécutifs |
| Semaine pleine | hexagone rose · argent | 7 jours consécutifs |
| Quinzaine | hexagone violet · or | 14 jours consécutifs |
| Un mois | hexagone doré · or | 30 jours consécutifs |
| Semaine régulière | octogone bleu · argent | 5 jours de renfo dans la même semaine |
| Dos et jambes | octogone turquoise · bronze | Courte A et courte B dans la même semaine |
| Fondations | carré pierre · argent | 10 séances longues |
| 25 séances | cercle bleu ciel · argent | 25 séances de renfo |
| Centurion | cercle rouge · or | 100 séances de renfo |
| À l'eau | écusson cyan · bronze | 1re nage notée |
| Un mois au bassin | écusson bleu · argent | 4 semaines complètes de suite (vacances neutres) |
| Trimestre aquatique | écusson indigo · or | 12 semaines complètes de suite (vacances neutres) |
| 10 km nagés | losange vert d'eau · argent | distance cumulée |
| 50 km nagés | losange bleu océan · or | distance cumulée |

- Un badge gagné reste acquis.
- Rappel affiché : la douleur passe avant la série.

## 8. Réglages

- **Convexité de la courbure lombaire** : gauche, droite ou je ne sais pas. Elle oriente :
  - le schéma de colonne ;
  - la consigne de respiration vers les côtés concaves ;
  - la série asymétrique de planche latérale.
- Planche latérale asymétrique (à activer après l'avis du kiné).
- Durée de préparation : 5, 10, 15 ou 20 s.
- Signaux sonores.
- Rythme guidé pour les répétitions.
- Annonces vocales.
- Matériel disponible.
- Réinitialisation des niveaux.
- **Données** : export et import du journal et des réglages en JSON (version hors claude.ai).

## 9. Technique

- **Un seul fichier HTML** (HTML, CSS, JavaScript sans framework ni étape de compilation).
  - Polices Google Fonts : Sora, Inter, JetBrains Mono.
  - Schémas générés en SVG par le code.
- **Deux déploiements à partir de la même source** (`src/colonne-active.html`) :
  1. **Artifact claude.ai** (privé) : données dans la base de l'artifact, lisible par le seul propriétaire, synchronisée entre appareils.
  2. **GitHub Pages** (`index.html` produit par `build.py`) : données dans le `localStorage` du navigateur. Pas de serveur. Export et import JSON pour la sauvegarde.
- **Modèle de données**
  - Entrée de journal :
    `{ id, type: courte|longue|natation|course, variante?: courte|courte_b|longue, date: AAAA-MM-JJ, duree (min), distance (km), douleurAvant, douleurApres (0–10), effort (1–5), exosFaits, exosTotal, notes, ts }`
  - Réglages :
    `{ convexe, asym, sons, rythme, voix, prep, niveaux{exo: niveau}, kine{exo: {s, note}}, materiel{} }`
- **Navigation** par ancre : `#aujourdhui`, `#suivi`, `#exercices`, `#reglages`.
- **Affichage**
  - Thème clair et thème sombre, suivant le système.
  - Mise en page mobile d'abord, sans défilement horizontal.
- **Installation sur l'écran d'accueil** : manifeste web et icônes.

## 10. Évolutions possibles

- Fonctionnement hors ligne (service worker).
- Synchronisation du journal entre la version GitHub et l'artifact.
- Vidéos validées par le kiné, ou vidéos personnelles.
- Exercice dédié aux adducteurs (serrer un ballon entre les genoux) si le kiné le juge utile.
- Rappels (notifications) les jours de séance.

## 11. Historique des demandes

1. Création : deux types de séance (courte quasi quotidienne, longue 1 à 2 fois par semaine), objectifs dos profond, mobilité, tendons, fascias, prise en compte de la scoliose et des sports d'endurance.
2. Adaptation au matériel, documentation détaillée (schémas, étapes, vidéos), espace d'évaluation par le kiné.
3. Curl-up remplacé par la planche puis le mountain climber lent.
4. Ajout du squat et de la fente, dédoublement de la séance courte (A dos / B jambes).
5. Planche de Copenhague retirée des séances.
6. Repères sonores : rythme guidé des répétitions et annonces vocales.
7. Dépôt GitHub avec GitHub Pages, cahier des charges, effort en 5 emoji, valeurs par défaut de la natation (60 min, 1300 m), séries et badges, assiduité natation.
8. Natation suspendue pendant les petites vacances scolaires de la zone B ; badges redessinés en médailles (style récompenses Apple Watch).
9. Son inaudible sur iPhone : déverrouillage audio pour iOS et bouton de test du son.
10. Son présent au début de la séance puis plus rien : bips de secours, voix fiabilisée, bandeau de reprise, test d'enchaînement et journal du son.
11. Bips couverts par la voix sur iPhone : la voix attend la fin du bip ; bips plus longs et plus forts ; journal du son complet.
12. Journal iPhone : la voix interrompt Web Audio et la boucle muette ; relance automatique après chaque annonce.
13. iPhone en mode silencieux confirmé : bandeau « Son coupé par l'iPhone (mode silencieux ?) » quand la relance automatique échoue.
14. Bips toujours coupés en mode silencieux après chaque annonce : voix enregistrée jouée par Web Audio à la place de la synthèse vocale.
