from typing import NamedTuple
from rich.console import Group
from rich.panel import Panel
from rich.rule import Rule


class Evenement(NamedTuple):
    
    titre: str
    description: str
    couleur: str
    option: tuple[str]
    consequences: tuple[tuple[int]] | None
    affichageConsequences: str

    def afficher(self):
        
        return Panel(Group(
            Rule(f'[white]{self.titre}[/]', style=self.couleur),
            f'[white]\n{self.description}\n\n{self.affichageConsequences}[/]'
        ), style=self.couleur)
