{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww16180\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Ce code Python impl\'e9mente le jeu du pendu. Le principe est le suivant : l\'92utilisateur doit deviner un pot en proposants des lettres. Il a 6 chances par manches. \
\
CONTENU DU CODE \
\
Lorsque l\'92on ex\'e9cute le code, les \'e9tapes suivantes sont effectu\'e9es :\
1. Le contenu du fichier qui poss\'e8de les mots \'e0 faire deviner est stock\'e9 dans une liste \'ab\'a0mots\'a0\'bb. \
2. Un nombre fixe de chances est d\'e9fini pour la partie en cours. \
3. Une liste code appel\'e9e \'91lettre_trouvees\'92 est initialis\'e9e pour stocker les lettres devin\'e9es par le joueur.\
4. On appelle la fonction \'91choisir_mot(mots)\'92 pour d\'e9finir quel est le mot \'e0 deviner. Ce mot est stock\'e9 dans la variable \'91mot_aleatoire\'92. \
5. Le jeu du pendu commence, on indique au joueur le nombre de lettre qui compose le mot \'e0 deviner.\
6. Le joueur est invit\'e9 \'e0 chaque tour \'e0 proposer une lettre gr\'e2ce \'e0 la fonction \'91proposition_lettre()\'92. SI la lettre est dans le mot, elle est ajout\'e9e \'e0 \'91lettre_trouvees\'92, sinon le joueur perd une chance.\
7. \'c0 chaque tour de boucle, la fonction \'91affichage(mot_aleatoire, lettre_trouvees)\'92 affiche le mot en cours de devinette et le nombre de chances restantes.\
8.Si le joueur n\'92a lus de chances, il a perdu, sinon il gagne. Le mot est finalement devin\'e9. \
\
UTILISATION\
\
Pour bien utiliser le code, il faut : \
\'95 Poss\'e9der le fichier \'91mots_pendu.txt\'92 dans le m\'eame fichier que le code python. Il faut que les mots soient en minuscules et s\'e9par\'e9s par un saut de ligne, sans espace.\
\'95 Ex\'e9cuter le code python.\
\'95 Indiquer uniquement des lettres minuscules.}