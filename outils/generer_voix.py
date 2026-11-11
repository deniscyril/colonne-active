"""Génère les annonces vocales enregistrées de Colonne Active (macOS : commande say + ffmpeg).

Usage : python3 outils/generer_voix.py  ->  écrit outils/voix.json ({phrase: mp3 en base64}),
à recopier dans l'objet VOIX_MP3 de src/colonne-active.html. Ajouter ici toute nouvelle phrase
(nouvel exercice, nouveau côté) : une phrase absente est dite par la synthèse vocale du navigateur,
qui coupe le son sur iPhone.
"""
import base64, hashlib, json, os, subprocess, tempfile

PHRASES = [
    "Repos",
    "C'est parti",
    "Série bonus",
    "Le son fonctionne.",
    "Respiration costale 3D",
    "Côté gauche",
    "Côté droit",
    "Chat-vache lent",
    "Rotation thoracique à quatre pattes",
    "Main gauche derrière la tête",
    "Main droite derrière la tête",
    "Transitions 90/90",
    "Curl-up de McGill",
    "Planche et mountain climber lent",
    "Bird dog",
    "Jambe gauche tendue",
    "Jambe droite tendue",
    "Planche latérale",
    "Appui côté gauche",
    "Appui côté droit",
    "Dead bug",
    "Jambe gauche qui descend",
    "Jambe droite qui descend",
    "Pallof press",
    "Élastique à ta gauche",
    "Élastique à ta droite",
    "Tirage horizontal à l'élastique",
    "Marche valise",
    "Charge main gauche",
    "Charge main droite",
    "Squat lent",
    "Fente statique",
    "Jambe gauche devant",
    "Jambe droite devant",
    "Pont fessier",
    "Jambe d'appui gauche",
    "Jambe d'appui droite",
    "Chaise contre le mur",
    "Mollets excentriques sur une marche",
    "Pied gauche",
    "Pied droit",
    "Planche de Copenhague, levier court",
    "Rebonds élastiques",
    "Auto-massage Blackroll",
    "Étirement des fléchisseurs de hanche",
    "Genou gauche au sol",
    "Genou droit au sol",
    "Posture de l'enfant latéralisée",
    "Mains vers la gauche",
    "Mains vers la droite",
    "Repos en décharge",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "Série 1",
    "Série 2",
    "Série 3",
    "Série 4",
    "Série 5",
    "Série 6",
    "Maintien 1",
    "Maintien 2",
    "Maintien 3",
    "Maintien 4",
    "Maintien 5",
    "Maintien 6",
    "Maintien 7",
    "Maintien 8",
    "Maintien 9",
    "Maintien 10",
    "Maintien 11",
    "Maintien 12"
]

# Orthographe phonétique pour la voix française
PRON = {
    "Transitions 90/90": "Transitions quatre-vingt-dix, quatre-vingt-dix",
    "Curl-up de McGill": "Keurl-eup de Mac Guil",
    "Planche et mountain climber lent": "Planche et mountaine claïmeur lent",
    "Bird dog": "Beurde dogue",
    "Dead bug": "Dède beugue",
    "Pallof press": "Palof presse",
    "Auto-massage Blackroll": "Auto-massage Blaque-rôl",
    "Respiration costale 3D": "Respiration costale 3 D",
}
FILTRE = ("silenceremove=start_periods=1:start_threshold=-50dB,areverse,"
          "silenceremove=start_periods=1:start_threshold=-50dB,areverse,loudnorm=I=-14:TP=-1")

out = {}
with tempfile.TemporaryDirectory() as tmp:
    for p in PHRASES:
        h = hashlib.md5(p.encode()).hexdigest()[:10]
        aiff, mp3 = os.path.join(tmp, h + ".aiff"), os.path.join(tmp, h + ".mp3")
        subprocess.run(["say", "-v", "Thomas", "-r", "185", "-o", aiff, PRON.get(p, p)], check=True)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", aiff, "-af", FILTRE,
                        "-ac", "1", "-ar", "22050", "-b:a", "32k", mp3], check=True)
        out[p] = base64.b64encode(open(mp3, "rb").read()).decode()
dest = os.path.join(os.path.dirname(__file__), "voix.json")
json.dump(out, open(dest, "w"), ensure_ascii=False)
print(len(out), "phrases ->", dest)
