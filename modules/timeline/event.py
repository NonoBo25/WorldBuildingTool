class Event:
    description: str
    date: int

    def __init__(self, description: str, date: int):
        self.description = description
        self.date = date
