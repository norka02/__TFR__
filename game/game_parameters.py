import pygame
import os
from utils import resize_img


class GameParameters:
    """This class defines the static game parameters"""

    """Creating system paths to images"""
    RACE_TRACK_PATH = os.path.join("images", "racetrack1.png")
    #RACE_TRACK_BORDER_PATH = os.path.join("images", "racetrack-borders.png")
    RACE_TRACK_BORDER_TRIM_PATH = os.path.join("images", "racetrack-borders_TRIM.png")
    CAR_PATH = os.path.join("images", "carYellow.png")
    CAR_PATH2 = os.path.join("images", "car2.png")
    RACE_END_DEAD_PATH = os.path.join("images", "McQueen_DEAD_ZĄB.jpg")
    FINISH_LINE_PATH = os.path.join("images", "finish_line.jpg")
    RACE_END_FINISH_WIN_PATH = os.path.join("images", "winningFinishLineCross.jpg")
    RACE_END_FINISH_WIN_ALGO_PATH = os.path.join("images", "winning.jpg")

    """Loading images to program and resizing images to fit them on screen"""
    #RACE_TRACK_BORDER = resize_img(pygame.image.load(RACE_TRACK_BORDER_PATH), 1.1)
    RACE_TRACK_BORDER_TRIM = resize_img(pygame.image.load(RACE_TRACK_BORDER_TRIM_PATH), 1.1)
    RACE_TRACK_IMG = resize_img(pygame.image.load(RACE_TRACK_PATH), 1.1)
    CAR_IMG = resize_img(pygame.image.load(CAR_PATH), 0.04)
    CAR_IM4G = resize_img(pygame.image.load(CAR_PATH2), 0.04)
    #RACE_TRACK_BORDER_MASK = pygame.mask.from_surface(RACE_TRACK_BORDER)
    RACE_TRACK_BORDER_MASK = pygame.mask.from_surface(RACE_TRACK_BORDER_TRIM)   #_TRIM
    RACE_END_DEAD = resize_img(pygame.image.load(RACE_END_DEAD_PATH), 1.3)  #1.2
    RACE_END_WIN = resize_img(pygame.image.load(RACE_END_FINISH_WIN_PATH), 1)     #1.1
    RACE_END_WIN_ALGO = resize_img(pygame.image.load(RACE_END_FINISH_WIN_ALGO_PATH), 2.4)   #2.2
    FINISH_LINE = pygame.transform.rotate(resize_img(pygame.image.load(FINISH_LINE_PATH), 0.07), 90)
    FINISH_MASK = pygame.mask.from_surface(FINISH_LINE)
    WIDTH, HIGH = RACE_TRACK_IMG.get_width(), RACE_TRACK_IMG.get_height()
    GAME_WINDOW = pygame.display.set_mode((WIDTH, HIGH))

    """Setting static cords to objects on screen and adding them to lists that are displayed on the in-game screen"""
    FITTING = -50
    IMG_CORD_X = 0
    IMG_CORD_Y = 0 + FITTING
    FINISH_X_CORD = 700
    FINISH_Y_CORD = 365 + FITTING
    FINISH_POS = (FINISH_X_CORD, FINISH_Y_CORD)
    IMAGES_AND_SIZES = [(RACE_TRACK_IMG, (IMG_CORD_X, IMG_CORD_Y)), (FINISH_LINE, (FINISH_X_CORD, FINISH_Y_CORD))]
    IMAGES_AND_SIZES_DEAD = [(RACE_END_DEAD, (IMG_CORD_X, IMG_CORD_Y))]
    IMAGES_AND_SIZES_WIN = [(RACE_END_WIN, (IMG_CORD_X, IMG_CORD_Y))]
    IMAGES_AND_SIZES_WIN_ALGO = [(RACE_END_WIN_ALGO, (IMG_CORD_X, IMG_CORD_Y))]
    # RACE_TRACK_BORDER_MASK = [(RACE_TRACK_BORDER_MASK, (IMG_CORD_X, IMG_CORD_Y))]

    # FONT = pygame.font.Font('freesansbold.ttf', 24)

    # todo -> próba przesunięcia trasy zakończona fiaskiem (zmienne z 'TRIM') -
    #  wywala błąd przy algo 2 przy random.choice() (set czy jakoś tak), a przy algo 1 puszcza ale się chyba od razu
    #  colliduje z obramówką trasy -> to check odkomentuj wszystkie TRIM oraz FITTING w powyższym kodzie oraz patrz
    #  linia 86/87 w module game_main.py (car.collision())

