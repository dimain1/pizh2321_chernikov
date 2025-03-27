# the_snake

## Задание 

- Напишите классы `GameObject`, `Apple` и `Snake`, а также их атрибуты и методы.

- Допишите основной цикл игры в функции `main()`

- Всё, к чему можно написать докстринги, должны содержать докстринги.

- Код должен соответствовать PEP8.

```PYTHON
from random import randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 10

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()

GRID_CENTER = (20 * GRID_WIDTH // 2, 20 * GRID_HEIGHT // 2)


# Тут опишите все классы игры.
class GameObject:
    """
    A class to represent a game object.
    """

    def __init__(self, position=(0, 0), body_color=(0, 0, 0)):
        """
        Initialize the GameObject object with a position and body color.

        :param position: The position of the game object.
        :param body_color: The body color of the game object.
        """
        self.position = position
        self.body_color = body_color

    def draw(self):
        """
        Draw the game object.
        """
        pass


class Apple(GameObject):
    """
    A class to represent an apple.
    """

    def randomize_position(self):
        """
        Randomize the position of the apple.
        """
        x = 20 * randint(0, GRID_WIDTH - 1)
        y = 20 * randint(0, GRID_HEIGHT - 1)
        self.position = (x, y)

    def __init__(self):
        """
        Initialize the Apple object with a random position and body color.
        """
        self.randomize_position()
        self.body_color = (255, 0, 0)

    def draw(self):
        """
        Draw the apple.
        """
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """
    A class to represent a snake.
    """

    def __init__(self):
        """
        Initialize the Snake object with a position, body color, length,
        positions, direction, and next direction.
        """
        self.position = GRID_CENTER
        self.eat_apple = False
        self.length = 1
        self.positions = [GRID_CENTER]
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = (0, 255, 0)

    def update_direction(self):
        """
        Update the direction of the snake.
        """
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """
        Move the snake.
        """
        head_position = self.get_head_position()
        x, y = head_position
        dx, dy = self.direction
        modified_head_position = ((x + (GRID_SIZE) * dx) % 640,
                                  (y + (GRID_SIZE) * dy) % 480)
        self.positions.insert(0, modified_head_position)
        if self.eat_apple:
            self.length = self.length + 1
            self.eat_apple = False
        else:
            self.last = self.positions[self.length]
            self.positions.pop(self.length)

    def draw(self):
        """
        Draw the snake.
        """
        for position in self.positions[:-1]:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """
        Return the head position of the snake.

        :return: The head position of the snake.
        """
        return self.positions[0]

    def reset(self):
        """
        Reset the snake.
        """
        for i in self.positions:
            last_rect = pygame.Rect(i, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)
        self.length = 1
        self.positions = [GRID_CENTER]
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = (0, 255, 0)

    def check(self):
        """
        Check if the snake has collided with itself.

        :return: True if the snake has collided with itself, False otherwise.
        """
        for i in range(1, self.length):
            if self.positions[i] == self.get_head_position():
                return True
        return False


def handle_keys(game_object):
    """
    Handle the keys pressed by the user.

    :param game_object: The game object to handle the keys for.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    snake = Snake()
    apple = Apple()

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.update_direction()
        snake.move()
        if snake.get_head_position() == apple.position:
            snake.eat_apple = True
            while apple.position in snake.positions:
                apple.randomize_position()
        if snake.check():
            snake.reset()
        snake.draw()
        apple.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
```


