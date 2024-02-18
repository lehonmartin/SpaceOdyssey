from rich.panel import Panel
from rich.console import Group
from rich.rule import Rule
from rich.align import Align
from dataclasses import dataclass
from src.config import CONSOLE


@dataclass
class DisplayPanel:
    _title: str
    _color: str
    _description: str
    _content: str
    
    def display(self):
        CONSOLE.print(Panel(
            Group(
                Rule(f'[white]{self._title}[/]', style=self._color),
                Align.center(f'\n[white]{self._description}[/]\n\n'),
                Align.center(self._content)
            ),
            style=self._color
        ))