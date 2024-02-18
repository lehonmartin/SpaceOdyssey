from random import shuffle
from json import loads
from src.config import EVENTS_PATH, NUMBER_OF_EVENTS
from src.Event import Event


class EventManager:
    def __init__(self) -> None:
        self._events = self._load_events(EVENTS_PATH)
        self._event = self._events.pop()
    
    @property
    def has_event(self) -> bool:
        return self._event != None
    
    def _load_events(self, events_path: str) -> list[Event]:
        with open(events_path, encoding='utf-8') as event_file:
            events = [Event(event_data) for event_data in loads(event_file.read())]
        shuffle(events)
        return events[:NUMBER_OF_EVENTS]
    
    def next_event(self) -> None:
        self._event = None if not self._events else self._events.pop()
        
    def display_event(self) -> None:
        return self._event.display()
    
    def ask_choice(self) -> tuple[int]:
        choice = self._event.ask_choice()
        return choice
