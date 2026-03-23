import msvcrt

ACTIONS = {
    'z': 'up',
    'q': 'left',
    's': 'down',
    'd': 'right',
}


def detect_press():
    """Attend une touche et renvoie la direction correspondante, ou None."""
    key = msvcrt.getch()

    if key == b'\x1b':  # Echap
        return 'quit'
    elif key in (b'\xe0', b'\x00'):  # Touche spéciale (flèches, F1...) — on ignore
        msvcrt.getch()  # consomme le 2e octet
        return None
    else:
        ch = key.decode('utf-8', errors='replace').lower()
        if ch in ACTIONS:
            return ACTIONS[ch]
        return None
