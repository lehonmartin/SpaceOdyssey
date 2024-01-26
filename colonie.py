from statistique import Statistique
from rich.console import Console
from art import tprint, text2art
from evenement import Evenement
from rich.prompt import Prompt
from random import shuffle
from copy import deepcopy
from time import sleep
from os import system
from json import loads


class Colonnie:
    
    def __init__(self, statistiques: tuple[str], fichierEvenements: str, fichierFins: str) -> None:
        
        self.console = Console(width=75)
        self.statistiques = [
            Statistique(statistique, couleur, len(statistique))
            for statistique, couleur
            in zip(statistiques, ['blue', 'red', 'green', 'yellow', 'purple', 'brown'])
        ]
        self.recapitulatif = [deepcopy(self.statistiques)]
        self.evenements = self.extraction_evenements(fichierEvenements)
        self.fins = self.extraction_fins(fichierFins)
        self.nombreEvenements = len(self.evenements)
        self.progression = 0
        self.enCours = True
        self.commencer()
        
    def extraction_evenements(self, fichierEvenements: str) -> list[Evenement]:
        
        evenements = []
        
        with open(fichierEvenements, encoding='utf-8') as Evenements:

            data = loads(Evenements.read().replace('\n', '').replace('    ', ''))
            
            for ligne in data:
                
                options = (ligne['choixA']['nom'], ligne['choixB']['nom'])
                consequences = (tuple(ligne['choixA']['consequences']), tuple(ligne['choixB']['consequences']))
                evenements.append(Evenement(
                    ligne['titre'], ligne['description'], 'blue',
                    options, consequences,
                    self.affichage_consequences(options, consequences)
                ))

        shuffle(evenements)
        return evenements
    
    def extraction_fins(self, fichierFins: str):

        with open(fichierFins, encoding='utf-8') as Fins:

            return Fins.readlines()

    def commencer(self) -> None:
        
        while self.enCours:
            
            evenement = self.evenements.pop()
            self.affichage(evenement)
            choix = int(Prompt.ask(' ', choices=['A', 'B'], default='A') == 'B')
            self.appliquer_consequences(evenement.consequences[choix])
            self.recapitulatif.append(deepcopy(self.statistiques))
            
            if any([statistique.valeur == 0 for statistique in self.statistiques]):
                
                self.enCours = False
                self.fin_de_partie('Vous avez perdu !', 'Game  Over', 5, 'red')
            
            elif not self.evenements:
                
                self.enCours = False
                self.fin_de_partie('Vous avez gagné !', 'You  Win', 11, 'green')
                
    def fin_de_partie(self, titre, description, descriptionSpace, couleur):
        
        self.affichage(Evenement(
            titre, self.explication_de_fin()+'\n\n'+text2art(' '*descriptionSpace+description),
            couleur, None, None, ' '*10+'- Appuyez sur ENTRER pour voir le récaputulatif -')
        )

        input()

        for statistiques in self.recapitulatif:

            system('cls')
            tprint('Space  Odyssey')
            self.statistiques = statistiques
            self.console.print(self.affichage_statistiques())
            sleep(0.4)

        input(' '*15+'- Appuyez sur ENTRER pour fermer le jeu -')
    
    def explication_de_fin(self):
        
        for i, statistique in enumerate(self.statistiques):

            if statistique.valeur == 0:

                return self.fins[i+1]
        
        return self.fins[0]
    
    def affichage(self, evenement: Evenement):
        
        system('cls')
        tprint('Space  Odyssey')
        self.console.print(self.affichage_statistiques())
        self.console.print(evenement.afficher())
        self.console.print(self.affichage_progression())
    
    def appliquer_consequences(self, consequences: tuple) -> None:
            
        for statistique, modification in zip(self.statistiques, consequences):
            
            statistique.ajouter(modification)
        
        self.progression += 1
    
    def affichage_statistiques(self) -> str:
    
        resultat = ''
        paterne = '{statistique}{espaceStatistique}: |[{couleur}]{progression}{espaceProgression}[/]|\n'
        
        for statistique in self.statistiques:
            
            proportion = round(0.57*statistique.valeur)
            resultat += paterne.format(
                statistique = f'[red]{statistique.nom}[/]' if statistique.valeur < 20 else statistique.nom,
                espaceStatistique = ' '*(12-statistique.longueurNom),
                couleur = statistique.couleur,
                progression = '█'*proportion,
                espaceProgression = ' '*(57-proportion)
            )
        
        return resultat
    
    def affichage_consequences(self, options, consequences) -> str:
        
        resultat = ''
        paterneEntete = '{espaceColonne1}{option1} (A){espaceColonne1}{espaceColonne2}{option2} (B)\n'
        paterneLigne = '{statistique}: +{choix1}{espaceColonne1}|{statistique}: +{choix2}\n'
        
        resultat += paterneEntete.format(
            option1 = options[0],
            option2 = options[1],
            espaceColonne1 = ' '*((30-len(options[0]))//2),
            espaceColonne2 = ' '*((33-len(options[1]))//2)
        ) + '----------------------------------|------------------------------------\n'

        for statistique, choix1, choix2 in zip(self.statistiques, *consequences):
            
            resultat += paterneLigne.format(
                statistique = statistique.nom,
                choix1 = choix1,
                choix2 = choix2,
                espaceColonne1 = ' '*(31-statistique.longueurNom-len(str(choix1).replace('-', '')))
            ).replace('+-', '-')
        
        return resultat[:-1]
    
    def affichage_progression(self) -> str:
        
        proportion = round(57*self.progression/self.nombreEvenements)
        return 'progression : |' + '█'*proportion + ' '*(57-proportion) + '|\n'
    
    
if __name__ == '__main__':
    
    colonie = Colonnie(
        statistiques = ('oxygène', 'nourriture', 'popularité', 'électricité'),
        fichierEvenements = 'evenements.json',
        fichierFins='fins.txt'
    )
