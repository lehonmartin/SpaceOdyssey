from copy import deepcopy
from src.Statistic import Statistic
from src.config import STATISTICS, CONSOLE


class Colony:

    def __init__(self) -> None:
        self._stats: list[Statistic] = [Statistic(stat[0], stat[1]) for stat in STATISTICS]
        self._history: list[list[Statistic]] = [deepcopy(self._stats)]

    @property
    def state(self) -> int:
        return sum(2**pwr for pwr, stat in enumerate(self._stats) if stat.is_depleted)

    def display_statistics(self) -> bool:
        if self.state == 0:
            CONSOLE.print("\n".join(str(stat) for stat in self._stats))
            return True
        elif self._history:
            CONSOLE.print("\n".join(str(stat) for stat in self._history.pop(0)))
            return True
        else:
            return False
        
    def apply_consequences(self, consequences: tuple[int]) -> None:
        for statistic, consequence in zip(self._stats, consequences):
            statistic.value = consequence
        self._history.append(deepcopy(self._stats))