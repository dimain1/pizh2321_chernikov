class Themes:
    """
    A class to represent a collection of themes.
    """

    def __init__(self, *themes):
        """
        Initialize the Themes object with a list of themes.

        :param themes: A variable number of theme arguments.
        """
        self._themes = list(themes)

    def add_theme(self, value):
        """
        Add a new theme to the list of themes.

        :param value: The theme to be added.
        """
        self._themes.append(value)

    def shift_one(self):
        """
        Move the last theme to the beginning of the list.
        """
        self._themes.insert(0, self._themes.pop())

    def reverse_order(self):
        """
        Reverse the order of the themes.
        """
        self._themes.reverse()

    def get_themes(self):
        """
        Return the list of themes.

        :return: The list of themes.
        """
        return self._themes

    def get_first(self):
        """
        Return the first theme in the list.

        :return: The first theme.
        """
        return self._themes[0]


class SpecialThemes(Themes):
    """
    A class to represent a collection of special themes.
    """

    def __init__(self, *themes):
        """
        Initialize the SpecialThemes object with a list of themes.

        :param themes: A variable number of theme arguments.
        """
        super().__init__(*themes)

    def add_theme(self, value):
        """
        Add a new theme to the list of themes.

        :param value: The theme to be added.
        """
        if isinstance(value, str):
            super().add_theme(value)
        else:
            raise ValueError("Theme must be a string.")


themes = Themes("weather", "rain")
themes.add_theme("warm")
print(themes.get_themes())
themes.shift_one()
print(themes.get_first())
themes.reverse_order()
print(themes.get_first())