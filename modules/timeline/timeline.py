class Timeline:
    events: list
    len: int

    def __init__(self):
        self.events = list()
        self.len = 0

    def add_event(self, event):
        self.len += 1
        self.events.append(event)
        self.events.sort(key=lambda eve: eve.date)
