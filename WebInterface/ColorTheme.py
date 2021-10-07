import json


class ColorTheme:
    colors: dict

    def __init__(self, colors: dict):
        self.colors = colors

    @classmethod
    def from_json(cls, path):
        with open(path, "r") as f:
            return ColorTheme(json.load(f))
