class Themes:
    def __init__(self, *themes):
        self.themes = list(themes)

    def add_theme(self, theme):
        self.themes.append(theme)

    def shift_one(self):
        self.themes.insert(0, self.themes.pop())
    
    def reverse_order(self):
        self.themes.reverse()

    def get_themes(self):
        return self.themes
    
    def get_first(self):
        return self.themes[0]


themes = Themes("tea", "coffee", "juice")
themes.add_theme("alcohol")
print(themes.get_themes())
themes.shift_one()
print(themes.get_themes())
themes.reverse_order()
print(themes.get_themes())
print(themes.get_first())