class Event:
    description: str
    date: int
    name: str

    def __init__(self, name: str, description: str, date: int):
        self.name = name
        self.description = description
        self.date = date
