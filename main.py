import random

# Fonction qui permet de définir le mot à faire deviner
def choisir_mot(mots) :
    mot = random.choice(mots)
    return mot


#Fonction qui affiche le mot au fur et à mesure du jeu
def affichage(mot, lettre_trouvees) :
    mot_affiche = ''
    for lettre in mot :
        if lettre in lettre_trouvees :
            mot_affiche += lettre
        else :
            mot_affiche += '_'
    return(mot_affiche)

#Fonction qui permet au joueur de proposer une lettre
def proposition_lettre() :
    lettre_proposee = input("Proposez une lettre (caractère en minuscule uniquement) : ")
    while not lettre_proposee.isalpha() or len(lettre_proposee
                                               ) !=1 :
        print("Merci de rentrer unisquement une lettre minuscule")
        lettre_proposee = input("Proposez une lettre (caractère en minuscule uniquement) : ")
    return(lettre_proposee)


#Main
# Ouverture du fichier qui contient les mots à faire deviner
mots = []
with open("mots_pendu.txt", "r") as fichier:
    for ligne in fichier:
        mots.append(ligne.strip())


#Nombres de chances
nbr_chances = 6

lettres_trouvees = []

#Choix du mot pour la partie en cours
mot_aleatoire = choisir_mot(mots)
#Introduction au jeu du pendu
print("Bienvenue dans le jeu du pendu")
print('Le mot à deviner comporte', len(mot_aleatoire), 'lettres.')

while True:
    affichage(mot_aleatoire, lettres_trouvees)
    print("Il vous reste", nbr_chances,"chance(s) restante(s)")

    lettre = proposition_lettre()

    if lettre in lettres_trouvees :
        print("Vous avez déjà trouvé cette lettre.")

    elif lettre in mot_aleatoire :
        lettres_trouvees.append(lettre)
        print("Vous avez trouvé une lettre correcte !")

    else :
        nbr_chances -= 1
        print("Mauvaise réponse, il vous reste",nbr_chances,"chance(s)")

    if nbr_chances == 0:
        print("Vous avez perdu. Le mot était : ", mot_aleatoire)
        break

    if set(mot_aleatoire) == set(lettres_trouvees):
        print('Félicitations ! Vous avez deviné le mot :', mot_aleatoire)
        break