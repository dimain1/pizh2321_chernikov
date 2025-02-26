# Задание для самостоятельного решения

## Класс "Темы" (Themes)

Экземпляру класса при инициализации передается аргумент список тем для
разговора.
Класс реализует методы:
\- add_theme(value) - добавить тему в конец;
\- shift_one() - сдвинуть темы на одну вправо (последняя становится первой, остальные сдвигаются);
\- reverse_order()- - поменять порядок тем на обратный;
\- get_themes() возвращает список тем;
\- get first() возвращает первую тему.

Помимо основного задания необходимо реализовать принципы ООП: инкапсуляцию, полиморфизм, наследование, абстракцию, композицию.

```PYTHON
#main.py
from abc import ABC, abstractmethod


class AbstractThemes(ABC):
    """
    An abstract base class to represent a collection of themes.
    """
    __themes: list

    @abstractmethod
    def add_theme(self, value):
        """
        Add a new theme to the list of themes.

        :param value: The theme to be added.
        """
        pass

    @abstractmethod
    def shift_one(self):
        """
        Move the last theme to the beginning of the list.
        """
        pass

    @abstractmethod
    def reverse_order(self):
        """
        Reverse the order of the themes.
        """
        pass

    @abstractmethod
    def get_themes(self):
        """
        Return the list of themes.

        :return: The list of themes.
        """
        pass

    @abstractmethod
    def get_first(self):
        """
        Return the first theme in the list.

        :return: The first theme.
        """
        pass


class Themes(AbstractThemes):
    """
    A class to represent a collection of themes.
    """

    def __init__(self, *themes):
        """
        Initialize the Themes object with a list of themes.

        :param themes: A variable number of theme arguments.
        """
        self.__themes = list(themes)

    def add_theme(self, value):
        """
        Add a new theme to the list of themes.

        :param value: The theme to be added.
        """
        self.__themes.append(value)

    def shift_one(self):
        """
        Move the last theme to the beginning of the list.
        """
        self.__themes.insert(0, self.__themes.pop())

    def reverse_order(self):
        """
        Reverse the order of the themes.
        """
        self.__themes.reverse()

    def get_themes(self):
        """
        Return the list of themes.

        :return: The list of themes.
        """
        return self.__themes

    def get_first(self):
        """
        Return the first theme in the list.

        :return: The first theme.
        """
        return self.__themes[0]


class PopularThemes(Themes):
    """
    A class to represent a collection of popular themes.
    """
    __popularity_rating: int

    def __init__(self, *themes, rating):
        """
        Initialize the PopularThemes object with a list of themes.

        :param themes: A variable number of theme arguments.
        """
        super().__init__(*themes)
        self.__popularity_rating = rating

    def add_theme(self, value):
        """
        Add a new theme to the list of themes.

        :param value: The theme to be added.
        """
        super().add_theme(value)

    def get_popularity_rating(self):
        """
        Return the popularity rating of the themes.

        :return: The popularity rating.
        """
        return self.__popularity_rating

    def set_popularity_rating(self, rating):
        """
        Set the popularity rating of the themes.

        :param rating: The popularity rating to be set.
        """
        self.__popularity_rating = rating


class Discussion:
    """
    A class to represent a discussion.
    """
    themes: PopularThemes

    def __init__(self, themes):
        """
        Initialize the Discussion object with a collection of themes.

        :param themes: A collection of themes.
        """
        self.__themes = themes
        self.__current_theme = self.__themes.get_first()

    def get_current_theme(self):
        """
        Return the current theme of the discussion.

        :return: The current theme.
        """
        return self.__current_theme

    def change_theme(self):
        """
        Change the current theme of the discussion to the next theme.
        """
        self.__themes.shift_one()
        self.__current_theme = self.__themes.get_first() 
```
При выполнении задания необходимо пострить UML-диграмма классов приложения.
<p align="center"> <image src="image.png"> </p>