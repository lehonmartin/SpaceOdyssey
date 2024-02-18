from os import system
from json import loads
from time import sleep
from random import randint
from rich.align import Align
from src.config import ENDS_PATH, GAME_OVER, YOU_WIN, CLEAR_COMMAND, GAME_TITLE, CONSOLE
from src.Colony import Colony
from src.EventManager import EventManager
from src.DisplayPanel import DisplayPanel


class Game:
    def __init__(self) -> None:
        self._colony = Colony()
        self._event_manager = EventManager()
        self._ends = self._load_ends(ENDS_PATH)
    
    def _load_ends(self, ends_path) -> None:
        with open(ends_path, encoding='utf-8') as ends_file:
            descriptions = loads(ends_file.read())
        ends = {
            int(i) : ['Game Over !', 'red', f'\n{description[randint(0, len(description)-1)]}', GAME_OVER]
            for i, description in descriptions.items()
            if i != "0"
        }
        ends[0] = ['You Win !', 'green', f'\n{descriptions["0"][randint(0, len(descriptions["0"])-1)]}', YOU_WIN]
        return ends
    
    def _base_display(self) -> None:
        system(CLEAR_COMMAND)
        print(GAME_TITLE)
        return self._colony.display_statistics()
    
    def start(self) -> None:
        while not self._colony.state and self._event_manager.has_event:
            self._base_display()
            self._event_manager.display_event()
            choice = self._event_manager.ask_choice()
            self._colony.apply_consequences(choice)
            self._event_manager.next_event()
        self._base_display()
        DisplayPanel(*self._ends[self._colony.state]).display()
        CONSOLE.input(Align.center("\n-- Appuillez sur [Entrée] pour voir l'historique --"))
        while self._base_display():
            sleep(0.5)