import pygame


def resize_img(img, modulation):
    size_width = round(img.get_width() * modulation, 0)
    size_high = round(img.get_height() * modulation, 0)
    return pygame.transform.scale(img, (size_width, size_high))


def rotate_obj(window, image, angle, width, high):
    rotated_img = pygame.transform.rotate(image, angle)
    new_rect = rotated_img.get_rect()
    window.blit(rotated_img, new_rect.topleft)


# sprawdzić rotozoom
def blit_rotate_center(surf, image, top_left, angle):
    # Obraca obraz względem jego kąta
    rotated_image = pygame.transform.rotate(image, angle)
    # Pobiera prostokąt obrazu i ustawia środek prostokąta obróconego obrazu
    # na środek prostokąta oryginalnego obrazu z podanym górnym lewym rogiem (topleft), topleft aby obraz został w miejscu na ekranie
    # bez topleft by obraz zwracany był w automatyczne współrzędne 0,0 a chcemy we współrzędne starego obrazu
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    # Rysuje obrócony obraz na powierzchni 'surf'
    surf.blit(rotated_image, new_rect)  # domyślnie topleft
