def newCoords(x, y, input):  
    
    # Si le joueur appuie à droite
    if input == "RIGHT":
        return (x + 1, y)  # On avance de 1 sur l'axe X
    
    # Si le joueur appuie à gauche
    elif input == "LEFT":
        return (x - 1, y)  # On recule de 1 sur l'axe X
    
    # Si le joueur appuie en haut
    elif input == "UP":
        return (x, y - 1)  # On monte (Y diminue)
    
    # Si le joueur appuie en bas
    elif input == "DOWN":
        return (x, y + 1)  # On descend (Y augmente)
    
    # Si aucune direction valide n'est donnée
    else:
        pass  # Ne fait rien 

    # On retourne les coordonnées actuelles si rien n'a changé
    return (x, y)













def draw_snake(x, y, width=10, height=10):
    for j in range(height):
        for i in range(width):
            if i == x and j == y:
                print("*", end="")
            else:
                print(".", end="")
        print()

def main():
    snake_coords = [9, 10]
    print("#" * 10)
    draw_snake(snake_coords[0], snake_coords[1])
    print("#" * 10)

main()