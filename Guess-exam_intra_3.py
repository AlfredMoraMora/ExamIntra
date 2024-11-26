ls_nbr_deviner = [15, 12, 66]
print("Voux avex trois nombres à deviner. ")
score = 0
for i in range (0,3):
    nbr_devine = ls_nbr_deviner[i]
    cpt_tentatives = 0
    while True:
        try:
            nombre = int(input("Entrez un nombre: "))
        except ValueError:
            print("Entrez une valeur valide. ")
            continue
        cpt_tentatives += 1
        if cpt_tentatives >= 5:
            print("Oups! Voux avez dépasé le nombre de tentatives permises!")
            break
        elif nombre < nbr_devine:
            print("trop petit.")
        elif nombre > nbr_devine:
            print("trop grand.")
        elif nombre == nbr_devine:
            print("Bravo! ")
            score += 1
            break

    if i != 2:
        print("\nEssayez de deviner un autre nombre. ")
print("\n Votre score est: ", score, "/3")
print("AufWiedersehen! ")