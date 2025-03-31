# Created by DragonNoir_off
# link to GitHub profile : https://github.com/DragonNoir-off
# Last edit -> 31/03/2025
# version [ 1 ]

# Version - NumWork

import math

class Formater():
    def f(number,chiffre_after_coma):
        number = number*10**chiffre_after_coma
        number = math.floor(number)
        number = number/10**chiffre_after_coma
        return number

class Calculus:
    def Triangle_Bernoulli__Return_Number_Of_Issue(iteration, success):
        Triangle = [1,1]
        
        for i in range(2, iteration+1):
            temp_Triangle = []
            temp_Triangle.append(1)
            for t in range(1, i):
                temp_Triangle.append(Triangle[t-1] + Triangle[t])
            temp_Triangle.append(1)
            Triangle = temp_Triangle
        
        return Triangle[len(Triangle)-1-success]
    
    def PascalTriangle(iteration, affichage_ligne):
        Triangle = [1,1]
        if not affichage_ligne: print("[1]")
        for i in range(2, iteration+1):
            if not affichage_ligne: print(Triangle)
            temp_Triangle = []
            temp_Triangle.append(1)
            for t in range(1, i):
                temp_Triangle.append(Triangle[t-1] + Triangle[t])
            temp_Triangle.append(1)
            Triangle = temp_Triangle
        print(Triangle)
    
    def Bernoulli(iteration, Success_Chance, Number_of_success):
        Number_of_issue = Calculus.Triangle_Bernoulli__Return_Number_Of_Issue(iteration, Number_of_success)

        Fail_Chance = 1-Success_Chance
        Output = Number_of_issue * (Fail_Chance ** ( iteration - Number_of_success )) * (Success_Chance ** ( Number_of_success ))
        
        print(Formater.f(Output, 3))

class init():
    def start():
        print("-- Renvoie les chances d'apparition de la branche\nCalculus.Bernoulli(iteration dans l'arbre, chance de succès, number de succès)")
        print("-- Renvoie le tableau de pascal de degree N\nCalculus.PascalTriangle(nombre d'itération dans l'arbre, afficher toutes les lignes)")
        print("-- Renvoie le nombre d'issue possible\nCalculus.Triangle_Bernoulli__Return_Number_Of_Issue(nombre d'itération dans l'arbre, nombre de succès)")

init.start()
