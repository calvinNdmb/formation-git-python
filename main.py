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












def newCoords(x,y,input):# Déterminer les nouvelles coordonées

    return (x,y)
    pass

def detect_press():# Détecter l'appuie d'une touche
    return input
    pass       


def main():
    pass