import pygame

#  CLASSES


class Player(object):
    def __init__(self):
        self.x = windowLenght/2
        self.y = windowHeight/2
        self.size = 10
        self.direction = "right"

    def handle_keys(self):
        keypressed = False
        print(self.direction)
                if event.key == pygame.K_LEFT and keypressed == False:
                    if self.direction != "right":
                        self.direction = "left"
                        keypressed = True
                if event.key == pygame.K_UP and keypressed == False:
                    if self.direction != "down":
                        self.direction = "up"
                        keypressed = True
                if event.key == pygame.K_RIGHT and keypressed == False:
                    if self.direction != "left":
                        self.direction = "right"
                        keypressed = True
                if event.key == pygame.K_DOWN and keypressed == False:
                    if self.direction != "up":
                        self.direction = "down"
                        keypressed = True

    def move(self, surface):
        if self.direction == "left":
            self.x -= self.size
        if self.direction == "up":
            self.y -= self.size
        if self.direction == "right":
            self.x += self.size
        if self.direction == "down":
            self.y += self.size

        self.Snake = pygame.draw.rect(window, white, [self.x, self.y, self.size, self.size])

#  FUNCTIONS


def get_position(List, number, xy):
    elem = List[number]
    return elem[xy]

#  SOME VARIABLES:

windowLenght = 800
windowHeight = 500
window = pygame.display.set_mode((windowLenght, windowHeight))

tick = 5
black = (0, 0, 0)
white = (255, 255, 255)
gray = (150, 150, 150)
green = (0, 255, 0, )
Snake_Size = 10
Snake = [[1, 2], [3, 4]]
Snake_Speed = 1
Lenght = len(Snake)

clock = pygame.time.Clock()
window.fill(black)
outline = pygame.draw.rect(window, green, [0, 0, 800, 500], 10)

#  MEAT OF THE GAME :P
pygame.init()
pygame.display.set_caption("Snake")

player = Player()
clock = pygame.time.Clock()

gameLoop = True
while gameLoop:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            gameLoop = False

    player.handle_keys()
    player.move(window)
    player.handle_keys()
    pygame.display.update()
    clock.tick(tick)
    pygame.display.flip()

pygame.quit()
