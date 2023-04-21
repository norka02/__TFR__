import pygame
import os
from utils import resize_img


class GameParameters:
    """Ta klasa służy jako pojemnik na stałe parametry gry"""

    RACE_TRACK_PATH = os.path.join("images", "racetrack1.png")
    RACE_TRACK_BORDER_PATH = os.path.join("images", "racetrack-borders.png")
    CAR_PATH = os.path.join("images", "carYellow.png")

    RACE_TRACK_BORDER = resize_img(pygame.image.load(RACE_TRACK_BORDER_PATH), 1.1)
    RACE_TRACK_IMG = resize_img(pygame.image.load(RACE_TRACK_PATH), 1.1)
    CAR_IMG = resize_img(pygame.image.load(CAR_PATH), 0.04)
    RACE_TRACK_BORDER_MASK = pygame.mask.from_surface(RACE_TRACK_BORDER)

    WIDTH, HIGH = RACE_TRACK_IMG.get_width(), RACE_TRACK_IMG.get_height()
    GAME_WINDOW = pygame.display.set_mode((WIDTH, HIGH))

    IMG_CORD_X = 0
    IMG_CORD_Y = 0
    IMAGES_AND_SIZES = [(RACE_TRACK_IMG, (IMG_CORD_X, IMG_CORD_Y))]
