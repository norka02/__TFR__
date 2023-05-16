import pygame

"""
                        ___Utils module___ 
    This module defines uniq functions which are used in other modules
"""


def resize_img(img, modulation):
    """resize_img() -> This function resizing an input image to fit it to other images in program"""
    size_width = round(img.get_width() * modulation, 0)
    size_high = round(img.get_height() * modulation, 0)
    return pygame.transform.scale(img, (size_width, size_high))


def blit_rotate_center(surf, image, top_left, angle):
    """blit_rotate_center -> obraca obraz względem zadanego kąta, następnie pobiera prostokąt obrazu (obiekt rect) i
    ustawia środek prostokąta obrócnego obrazu na środek prostokąta orginalnego obrazu z podanym górnym lewym rogiem
    (topleft -> po to aby obraz został w miejscu na ekranie gdzie był stary obraz, inaczej byłby on automatycznie
    w automatyczne współrzędne (0,0)). Na koniec rysowany jest obraz na powierzchni ekranu (surf).
    """
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    surf.blit(rotated_image, new_rect)
    return rotated_image


def position_fix(cord):
    scale = 2  # zrobic globalna zmienna (ale to potem)
    cord = int(cord / scale)
    return cord


def detect_stat_dyn_collide(static_img, dynamic_img, dynamic_pos, static_pos):
    """detect_stat_dyn_collide() -> This function checks collisions between static and dynamic objects"""
    static_rect = static_img.get_rect(topleft=static_pos)
    dynamic_rect = dynamic_img.get_rect(topleft=dynamic_pos)
    if dynamic_rect.colliderect(static_rect):
        return True
    return False
