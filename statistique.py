from dataclasses import dataclass


@dataclass
class Statistique:
    
    nom: str
    couleur: str
    longueurNom: int
    valeur: int = 60
    
    def ajouter(self, modification) -> None:
        
        nouvelleValeur = self.valeur + int(modification)
        
        if 0 <= nouvelleValeur <= 100:
            
            self.valeur += int(modification)

        else:
            
            self.valeur = int(nouvelleValeur > 100) * 100

    def forcer_valeur(self, valeur) -> None:
        
        self.valeur = int(valeur)