from event import Event


class Timeline:
    events: list(Event)

    def __init__(self):
        self.events = list[Event]()

    def add_event(self, event: Event):
        self.events.append(event)
        self.events.sort(key=lambda eve: eve.date)

