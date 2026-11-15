
taches = []

def ajouter_tache():
    titre = input("Titre de la tâche : ")

    if titre.strip() == "":
        print("Erreur : le titre ne peut pas être vide.")
    else:
        taches.append(titre)
        print("Tâche ajoutée avec succès.")

def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche disponible.")
    else:
        print("\nListe des tâches :")
        for i in range(len(taches)):
            print(i + 1, "-", taches[i])

def rechercher_tache():
    mot_cle = input("Mot-clé à rechercher : ")

    if mot_cle.strip() == "":
        print("Veuillez saisir un mot-clé.")
        return

    trouve = False

    for i in range(len(taches)):
        if mot_cle.lower() in taches[i].lower():
            print(i + 1, "-", taches[i])
            trouve = True

    if trouve == False:
        print("Aucune tâche trouvée.")
        
while True:
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        ajouter_tache()

    elif choix == "2":
        afficher_taches()

    elif choix == "3":
        rechercher_tache()

    elif choix == "0":
        print("Au revoir !")
        break

    else:
        print("Choix invalide. Réessayez.")
