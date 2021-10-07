from timeline.timeline import Timeline


class Part:
    description: str
    name: str

    def __init__(self, name, description):
        self.description = description


class World:
    name: str
    time_line: Timeline

    def __init__(self, name: str):
        self.name = name
        self.time_line = Timeline()
