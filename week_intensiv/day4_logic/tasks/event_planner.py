from week_intensiv.day4_logic.tests.tests_event_planner import test_total_participants


class Event:
    """Класс-контейнер для данных о событии"""
    def __init__(self, title: str, date: str, participants: int):
        self.title = title
        self.date = date  # Формат "ГГГГ-ММ-ДД"
        self.participants = participants

class EventPlanner:
    """
    ЗАДАЧА: Аналитика событий.
    1. get_events_on_date(date): возвращает список НАЗВАНИЙ (str) событий на эту дату.
    2. get_total_participants(): возвращает общее число участников всех событий.
    """
    def __init__(self):
        self.events = []

    def add_event(self, event):
        # Добавляет объект Event в список
        self.events.append(event)

    def get_events_on_date(self, date):
        result = []
        for event in self.events:
            if event.date == date:
                result.append(event.title)
        return result

    def get_total_participants(self):
        total = 0
        for event in self.events:
            total += event.participants
        return total
