from dataclasses import dataclass
from src.config import DEFAULT_STAT_VALUE, STAT_DISPLAY_PATERN, STAT_NAME_WIDTH, VAL_SPACE_WIDTH, CRITICAL_VALUE


@dataclass
class Statistic:
    _name: str
    _colour: str
    _value: int = DEFAULT_STAT_VALUE
    _pattern: str = STAT_DISPLAY_PATERN

    def __str__(self) -> str:
        proportion = round(VAL_SPACE_WIDTH * self._value / 100)
        return self._pattern.format(
            stat = f'[red]{self._name}[/]' if self._value < CRITICAL_VALUE else self._name,
            stat_space = ' ' * (STAT_NAME_WIDTH - len(self._name)),
            colour = self._colour,
            val = '█' * proportion,
            val_space = ' ' * (VAL_SPACE_WIDTH - proportion)
        )

    @property
    def is_depleted(self) -> bool:
        return self._value <= 0

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, new_value: int) -> None:
        self._value = max(0, min(self._value + new_value, 100))
