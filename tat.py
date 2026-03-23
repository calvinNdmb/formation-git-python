def newCoords(x, y, input_dir):
    # Si le joueur appuie à droite
    if input_dir == "RIGHT": # input_dir = la direction chois
        return (x + 1, y)  # On avance de 1 sur l'axe X
    
    # Si le joueur appuie à gauche
    elif input_dir == "LEFT":
        return (x - 1, y)  # On recule de 1 sur l'axe X
    
    # Si le joueur appuie en haut
    elif input_dir == "UP":
        return (x, y - 1)  # On monte (Y diminue)
    
    # Si le joueur appuie en bas
    elif input_dir == "DOWN":
        return (x, y + 1)  # On descend (Y augmente)
    
    # Si aucune direction valide n'est donnée
    else:
        return (x, y)  # On retourne les coordonnées actuelles
#!===================================================================
#!===================================================================

def detect_press():
    # Demande à l'utilisateur une direction
    input_user = input("Direction (UP, DOWN, LEFT, RIGHT) : ")
    # Convertit en majuscule pour éviter les erreurs
    input_user = input_user.upper()
    return input_user


#!===================================================================
#!===================================================================

def draw_snake(x, y, width=10, height=10):
    for j in range(height):
        for i in range(width):
            if i == x and j == y:
                print("*", end="")
            else:
                print(".", end="")
        print()

def main():
    # Coordonnées initiales du serpent
    x, y = 5, 5
    largeur, hauteur = 10, 10
    
    print("=== JEU DU SERPENT ===")
    print("Utilisez UP, DOWN, LEFT, RIGHT pour vous déplacer")
    print("Tapez 'QUIT' pour quitter\n")
    
    while True:
        # Affiche la grille
        print("#" * (largeur + 2))
        draw_snake(x, y, largeur, hauteur)
        print("#" * (largeur + 2))
        
        # Demande la direction
        direction = detect_press()
        
        # Option pour quitter
        if direction == "QUIT":
            print("Au revoir !")
            break
        
        # Calcule les nouvelles coordonnées
        nouveau_x, nouveau_y = newCoords(x, y, direction)
        
        # Vérifie si le serpent reste dans les limites
        if 0 <= nouveau_x < largeur and 0 <= nouveau_y < hauteur:    # Cette condition vérifie si le serpent reste dans la grille
                                                                     # 0 <= nouveau_x < largeur : Vérifie que X n'est pas négatif ET inférieur à la largeur
                                                                     # 0 <= nouveau_y < hauteur : Vérifie que Y n'est pas négatif ET inférieur à la hauteur
            x, y = nouveau_x, nouveau_y                           # Si les nouvelles coordonnées sont valides, on les applique

        else:                                                        # Si le mouvement est invalide (en dehors de la grille)
                                                                     # On affiche un message d'erreur pour prévenir le joueur
                                                                     # Le serpent reste à sa position précédente (on ne change pas x et y)
            print("❌ Mouvement impossible ! Vous êtes sorti de la grille.") 
            print(f"Limites : 0-{largeur-1} pour X, 0-{hauteur-1} pour Y")    # Affiche les limites exactes (de 0 à largeur-1 pour X, de 0 à hauteur-1 pour Y)
        
        print()   # Affiche une ligne vide pour séparer les tours de jeu et améliorer la lisibilité

if __name__ == "__main__":   # Affiche une ligne vide pour séparer les tours de jeu et améliorer la lisibilité
    main()