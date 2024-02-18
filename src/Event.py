from rich.prompt import Prompt
from rich.table import Table
from src.DisplayPanel import DisplayPanel
from src.config import STATISTICS


class Event:
    def __init__(self, data: dict, color: str = 'blue') -> None:
        self._choices: list[str] = data["choices"]
        self._consequences: list[list[int]] = data["consequences"]
        self._display_panel = DisplayPanel(data["title"], color, data["description"], self._consequences_table())
    
    def display(self) -> None: 
        self._display_panel.display()
    
    def ask_choice(self) -> None:
        return self._consequences[
            int(Prompt.ask(
                'Fais ton choix',
                choices=[str(i) for i in range(1, len(self._choices)+1)],
                default='1'
            )) - 1
        ]
    
    def _consequences_table(self) -> Table:
        table_labels = tuple(zip(*STATISTICS))[0]
        rows = (
            [choice] + [str(consequence) for consequence in consequences]
            for choice, consequences
            in zip(self._choices, self._consequences)
        )
        table = Table(title="Consequences", show_lines=True)
        table.add_column('Choix', justify="center")
        for choice_label in table_labels:
            table.add_column(choice_label, justify="center")
        for row in rows:
            table.add_row(*row)
        return table
