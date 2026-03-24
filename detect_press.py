import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

def detect_press():

    # Valeur par défaut (aucune touche)
    direction = None

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                direction = "UP"

            elif event.key == pygame.K_DOWN:
                direction = "DOWN"

            elif event.key == pygame.K_LEFT:
                direction = "LEFT"

            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"

    return direction
