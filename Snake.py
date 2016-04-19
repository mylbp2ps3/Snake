import pygame

#  CLASSES


class Player(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((64, 54, 16, 16))

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-Snake_Speed, 0)
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(Snake_Speed, 0)
        if key[pygame.K_UP]:
            self.rect.move_ip(0, -Snake_Speed)
        if key[pygame.K_DOWN]:
            self.rect.move_ip(0, Snake_Speed)

    def draw(self, surface):
        pygame.draw.rect(window, (0, 0, 128), self.rect)

#  FUNCTIONS


def get_position(List, number, xy):
    elem = List[number]
    return elem[xy]

#  SOME VARIABLES:
windowLenght = 800
windowHeight = 500
window = pygame.display.set_mode((windowLenght, windowHeight))

tick = 60
black = (0, 0, 0)
white = (255, 255, 255)
gray = (150, 150, 150)
green = (0, 255, 0)
Snake_Size = 10
Snake = [[1, 2], [3, 4]]
Snake_Speed = 1
Lenght = len(Snake)

clock = pygame.time.Clock()
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

    player.draw(window)
    player.handle_keys()
    pygame.display.update()
    clock.tick(tick)
    pygame.display.flip()

pygame.quit()
