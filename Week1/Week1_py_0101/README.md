# Введение.
## Задание для самостоятельного решения

### Класс "Темы" (Themes)

Экземпляру класса при инициализации передается аргумент список тем для
разговора.
Класс реализует методы:
\- add_theme(value) - добавить тему в конец;
\- shift_one() - сдвинуть темы на одну вправо (последняя становится первой, остальные сдвигаются);
\- reverse_order()- - поменять порядок тем на обратный;
\- get_themes() возвращает список тем;
\- get first() возвращает первую тему.


```PYTHON
#main.py
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
```


