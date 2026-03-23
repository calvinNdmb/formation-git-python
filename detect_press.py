import pygame

# Initialisation de pygame
pygame.init()

# Création d'une fenêtre de jeu
screen = pygame.display.set_mode((400, 400))

# Titre de la fenêtre
pygame.display.set_caption("Détection des touches")


def detect_press():
    # Valeur par défaut : aucune touche appuyée
    direction = None

    # On récupère tous les événements
    for event in pygame.event.get():

        # Si l'utilisateur ferme la fenêtre
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Si une touche du clavier est appuyée
        if event.type == pygame.KEYDOWN:

            # Si flèche du haut
            if event.key == pygame.K_UP:
                direction = "UP"

            # Si flèche du bas
            elif event.key == pygame.K_DOWN:
                direction = "DOWN"

            # Si flèche gauche
            elif event.key == pygame.K_LEFT:
                direction = "LEFT"

            # Si flèche droite
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"

    # On retourne la direction détectée
    return direction


# Boucle principale du programme
while True:
    direction = detect_press()

    # Si une direction a été détectée, on l'affiche
    if direction is not None:
        print("Direction détectée :", direction)