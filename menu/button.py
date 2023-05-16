import pygame


class Button:
    def __init__(self, txt, pos, screen, font):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (230, 40))  # WIDTH/3
        self.screen = screen
        self.font = font

    def draw(self):
        """draw() -> draws button with text inside"""
        pygame.draw.rect(self.screen, "light gray", self.button, 0, 5)
        pygame.draw.rect(self.screen, "dark gray", [self.pos[0], self.pos[1], 230, 40], 5, 5)
        text2 = self.font.render(self.text, True, "black")
        if len(self.text) > 10:
            self.screen.blit(text2, (self.pos[0] + 20, self.pos[1] + 7))
        else:
            self.screen.blit(text2, (self.pos[0] + 100 - len(self.text) * 10, self.pos[1] + 7))

    def check_clicked(self):
        """check_clicked() -> checks if the button has been clicked"""
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False
