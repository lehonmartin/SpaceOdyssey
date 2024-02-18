#----------------------------------------------------------------------#
#                               Imports                                #
#----------------------------------------------------------------------#

# Nom de l'OS
from os import name
# Fonction de construction de chemin de fichier inter-os
from os.path import join
# Console d'affichage
from rich.console import Console
# Fonction d'ASCII art
from art import text2art


#----------------------------------------------------------------------#
#                            Configuration                             #
#----------------------------------------------------------------------#

# ASCII art du titre du jeu
GAME_TITLE = text2art(5 * ' ' + 'Space   Odyssey')
# ASCII art du Game Over
GAME_OVER = text2art('GAME   OVER')
# ASCII art du Tou Win
YOU_WIN = text2art('YOU   WIN')
# Nom et couleur des statistiques du jeu
STATISTICS = (
    ('oxygène', 'blue'),
    ('nourriture', 'red'),
    ('popularité', 'green'),
    ('électricité', 'yellow')
)
# Valeur des statistiques au début du jeu
DEFAULT_STAT_VALUE = 70
# Nombre d'évènements par partie (None = tous)
NUMBER_OF_EVENTS = None


#----------------------------------------------------------------------#
#                              Apparence                               #
#----------------------------------------------------------------------#

# Largeur de la connsole
CONSOLE = Console(width=90)
# Paterne d'affichage des statistiques
STAT_DISPLAY_PATERN = 8 * ' ' + '{stat}{stat_space}: |[{colour}]{val}{val_space}[/]|\n'
# Largeur du nom des statistiques
STAT_NAME_WIDTH = 12
# Largeur des barres de statistiques
VAL_SPACE_WIDTH = 57
# Valeure à partir de laquelle une statistique est dans l'état critique
CRITICAL_VALUE = 25


#----------------------------------------------------------------------#
#                              Technique                               #
#----------------------------------------------------------------------#

# Commande d'effacage de la console
CLEAR_COMMAND = 'cls' if name == 'nt' else 'clear'
# Chemin des évènements
EVENTS_PATH = join('data', 'events.json')
# Liste des scénari de fin
ENDS_PATH = join('data', 'ends.json')
