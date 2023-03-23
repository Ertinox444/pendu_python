wordToFind = "test"
fin = False
lettre_chercher = ""
error = 0
max_error = 10


def genere_mot_trouver(mot):
    mot_generer = ""
    for letter in mot:
        mot_generer += "_"
    return mot_generer

def dessine_pendu(nb_erreurs):
    if nb_erreurs == 0:
        ("")
    elif nb_erreurs == 1:
        print("=========")
    elif nb_erreurs == 2:
     
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif nb_erreurs == 3:
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif nb_erreurs == 4:
        print("  +---+")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif nb_erreurs == 5:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif nb_erreurs == 6:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |")
        print("=========")
    elif nb_erreurs == 7:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("      |")
        print("=========")
    elif nb_erreurs == 8:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print("      |")
        print("      |")
        print("=========")
    elif nb_erreurs == 9:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print(" /    |")
        print("      |")
        print("=========")
    elif nb_erreurs == 10:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print(" / \  |")
        print("      |")
        print("=========")


mot = genere_mot_trouver(wordToFind)

while fin == False:
  
    lettre_chercher = str(input("Proposez une lettre :"))
    indice = 0
    lettre_trouvee = False
    for lettre in wordToFind:
        if ((lettre_chercher) == lettre):
            mot = mot[:indice] + lettre + mot[indice+1:]
            lettre_trouvee = True
        indice += 1
        
    if lettre_trouvee == False:
        error += 1
        
        if error == max_error:
            fin = True
            print("Vous avez perdu !")
    if "_" not in mot:
        print("Félicitations, vous avez trouvé le mot !")
        fin = True

    print("Mot :" + mot + "\n-----------------------\nEtat du pendu :") 
    dessine_pendu(error)
    
            


















