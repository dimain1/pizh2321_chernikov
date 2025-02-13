class Themes:
    def __init__(self, *themes):
        self.themes = list(themes)

    def add_theme(self, value):
        self.themes.append(value)

    def shift_one(self):
        self.themes.insert(0, self.themes.pop())

    def reverse_order(self):
        self.themes.reverse()

    def get_themes(self):
        return self.themes

    def get_first(self):
        return self.themes[0]


themes = Themes("weather", "rain")
themes.add_theme("warm")
print(themes.get_themes())
themes.shift_one()
print(themes.get_first())
