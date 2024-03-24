import pyautogui
import time

def get_pixel_color(x, y):
    """
    Obtient la couleur d'un pixel spécifique sur l'écran.

    Args:
        x (int): La coordonnée x du pixel.
        y (int): La coordonnée y du pixel.

    Returns:
        color (tuple): Un tuple contenant les valeurs RGB du pixel.
    """
    # Capturer la couleur du pixel spécifié
    color = pyautogui.pixel(x, y)
    return color

if __name__ == "__main__":
    # Couleur à détecter
    target_color = (255, 57, 57)

    while True:
        # Coordonnée y du pixel à scanner
        y_pixel = 591  # Maintenant c'est la hauteur

        # Variable pour suivre l'état du pixel rouge
        red_pixel_found = False

        # Parcourir les pixels de 100 à 2000 en incréments de 100 pour les coordonnées x
        for x_pixel in range(445, 1920, 10):  # Maintenant c'est la largeur
            # Obtenir la couleur du pixel spécifié
            pixel_color = get_pixel_color(x_pixel, y_pixel)

            # Vérifier si la couleur du pixel correspond à la couleur cible
            if pixel_color == target_color:
                print(f"La couleur du pixel ({x_pixel}, {y_pixel}) est : {pixel_color}")
                if not red_pixel_found:
                    red_pixel_found = True
            else:
                red_pixel_found = False

            # Vérifier continuellement si la couleur du pixel change
            while red_pixel_found:
                new_color = get_pixel_color(x_pixel, y_pixel)
                if new_color != target_color:
                    # Si la couleur change, effectuer un espace pendant 1/18e de seconde
                    pyautogui.keyDown('space')
                    time.sleep(0.5)  # Attendre 0.5 seconde avant d'appuyer sur click droit
                    pyautogui.keyUp('space')

                    # Appuyer sur le bouton droit de la souris
                    pyautogui.rightClick()
                    red_pixel_found = False
                    break  # Sortir de la boucle while si la couleur change

        # Attendre 0.3 seconde avant de recommencer la boucle
        time.sleep(0.3)  