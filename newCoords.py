def newCoords(x, y, direction):  # Déterminer les nouvelles coordonnées
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    return (x, y)