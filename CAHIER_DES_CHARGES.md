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
- La carte 🔥 affiche :
  - la série actuelle ;
  - le message du jour (« Fais ta séance aujourd'hui pour passer à N + 1 jours ») ;
  - le prochain badge de série ;
  - le record.
- Elle apparaît sur « Aujourd'hui » et dans « Suivi ».

### 7.2 Assiduité natation

- **Semaines complètes de suite** avec 2 nages. La semaine en cours compte dès qu'elle est complète.
- **Record** de semaines complètes.
- **Taux d'assiduité sur 8 semaines** : nages faites / nages prévues (lundi et jeudi), compté depuis la première activité notée.
- **Distance nagée** sur le mois en cours et au total, nombre de nages.
- Frise de 8 semaines, avec deux pastilles par semaine.
- Les lundis et jeudis, un rappel « Natation ce soir » s'affiche sur « Aujourd'hui », avec un bouton pour noter la nage.

### 7.3 Badges (16)

| Badge | Condition |
|---|---|
| 🌱 Premier pas | 1re séance de renfo |
| 🔥 Trois de suite | 3 jours consécutifs |
| ⚡ Cinq de suite | 5 jours consécutifs |
| 🏅 Semaine pleine | 7 jours consécutifs |
| 🥈 Quinzaine | 14 jours consécutifs |
| 🏆 Un mois | 30 jours consécutifs |
| 📅 Semaine régulière | 5 jours de renfo dans la même semaine |
| 🔄 Dos et jambes | Courte A et courte B dans la même semaine |
| 🧱 Fondations | 10 séances longues |
| 🎯 25 séances | 25 séances de renfo |
| 💯 Centurion | 100 séances de renfo |
| 🏊 À l'eau | 1re nage notée |
| 🌊 Un mois au bassin | 4 semaines de suite avec 2 nages |
| 🐬 Trimestre aquatique | 12 semaines de suite avec 2 nages |
| 🗺️ 10 km nagés | distance cumulée |
| 🌍 50 km nagés | distance cumulée |

- Un badge gagné reste acquis.
- Chaque badge non obtenu affiche sa barre de progression.
- Un toast annonce chaque nouveau badge à l'enregistrement.
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
