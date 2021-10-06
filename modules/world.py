from timeline.timeline import Timeline


class World:
    name: str
    time_line: Timeline

    def __init__(self, name: str):
        self.name = name
        self.time_line = Timeline()

