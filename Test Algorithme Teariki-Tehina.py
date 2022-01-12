
def recettegateau():
    oeufs = 4
    yaourt = 400
    maizena = 40
    moulegateau = 1
    papiersulfurise = 1
    
    if (oeufs < 4 or yaourt < 400 or maizena < 40):  
        print("Il n'y a pas assez d'ingrédients")
        
    else :
        print("Tout les ingrédients sont là, la préparation peut commencer")

        print("On mélange les oeufs avec le yaourt")
        print("on y ajoute la maizena tamisée")

        if (moulegateau < 1):
            print("J'ai oublié les moules à gâteau !! Il vaut mieux en acheter...")
        else :
            print ("Humidier le moule à gâteau")

            if (papiersulfurise < 1):
                print("Je n'ai pas de papier sulfurisé..")
            else :
                print ("Froisser une feuille de papier sulfurisé et la mettre au fond du moule")
                print ("Toutes les conditions sont réunies, on peut donc verser la préparation.") 

                print("Fin de la préparation, passons à la cuisson.")

                #CUISSON
                FourPuissant = True

                print("On enfourne notre préparation au four, le temps de cuisson variera en fonction du type de four que l'on utilise") # "True" signifie que le four est puissant et le temps de cuisson moins long, "False" signifiera que le four est plus petit et donc le temps de cuisson plus long.
                if(FourPuissant == True):
                    compteurTemps = 35
                    temperature = 170
                    print("Le four est puissant notre préparation cuiera pendant 35 minutes à 170°")

                    if(temperature < 170 or temperature > 170):
                        print("il faut ajuster la température")
                    
                    if(compteurTemps < 35 or compteurTemps > 35):
                        print("Attention à la gestion du temps, la préparation doit cuire 35 minutes !!")

                else :
                    compteurTemps = 50
                    temperature = 170
                    print("Le four est plus petit notre préparation cuiera pendant 50 minutes à 170°")

                    if(temperature < 170 or temperature > 170):
                        print("il faut ajuster la température")
                    
                    if(compteurTemps < 50 or compteurTemps > 50):
                        print("Attention à la gestion du temps, la préparation doit cuire 50 minutes !!")

                #AU FRIGO !
                import random
                tempsfrigo = random.randint(1,2)
                tempsfrigo = str(tempsfrigo)
                print("le plat reposera pendant "+ tempsfrigo +" heures ")

                print("C'est terminé !! On peut déguster ce plat.")

if __name__ == '__main__':
    recettegateau()
        

