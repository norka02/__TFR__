import pygame
import random

import game_main as gmf
from menu.button import Button
from game_main import Game


class MainMenu:
    pygame.init()
    FPS = 60

    def __init__(self):
        self.WIDTH = 1400
        self.HEIGHT = 820   #860
        self.timer = pygame.time.Clock()
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption("Menus TFR")
        self.want_go_to_main_menu = False
        self.font = pygame.font.Font("freesansbold.ttf", 24)
        self.bg = pygame.transform.scale(
            pygame.image.load("images/autaRace.jpg"), (self.WIDTH, self.HEIGHT)
        )
        self.ball = pygame.transform.scale(pygame.image.load("images/tfrBallLogo.png"), (150, 150))
        self.background = pygame.transform.scale(
            pygame.image.load("images/CarsOldOne.webp"), (self.WIDTH, self.HEIGHT)
        )
        self.zlom = pygame.transform.scale(
            pygame.image.load("images/zygzzlom.jpg"), (self.WIDTH, self.HEIGHT)
        )
        self.menu_command = 0
        self.option_command = -1

    def draw_menu_screen(self, command=-1):
        """draw_menu_screen is function that generates whole view of main manu (buttons, words, background picture)"""
        self.screen.blit(self.bg, (0, 0))
        move_menu_height = 220
        pygame.draw.rect(self.screen, "black", [50, 100+move_menu_height, 300, 300])
        pygame.draw.rect(self.screen, "green", [50, 100+move_menu_height, 300, 300], 5)
        pygame.draw.rect(self.screen, "white", [70, 120+move_menu_height, 260, 40], 0, 5)
        pygame.draw.rect(self.screen, "gray", [70, 120+move_menu_height, 260, 40], 5, 5)
        txt = self.font.render("Menus!", True, "black")
        self.screen.blit(txt, (135, 127+move_menu_height))
        menu = Button("Exit Menu", (85, 350+move_menu_height), self.screen, self.font)
        menu.draw()
        play_button = Button("Play", (85, 180+move_menu_height), self.screen, self.font)
        play_button.draw()
        options_button = Button("Options", (85, 240+move_menu_height), self.screen, self.font)
        options_button.draw()
        random_button = Button("Randomize", (85, 300+move_menu_height), self.screen, self.font)
        random_button.draw()
        if menu.check_clicked():
            command = 0
        if play_button.check_clicked():
            command = 1
        if options_button.check_clicked():
            command = 2
        if random_button.check_clicked():
            command = 3
        return command

    def draw_preload_screen(self):
        """draw_preload_screen is the opening screen of the program"""
        menu_btn = Button(
            "Main Menu", (self.WIDTH / 2 - 75, self.HEIGHT - 100), self.screen, self.font
        )
        menu_btn.draw()
        self.screen.blit(self.ball, (200, 670))
        if menu_btn.check_clicked():
            self.menu_command = -1

    def which_game_option_choosen(self):
        """which_game_option_choosen -> function used to inform our user which game option is currently choosen"""
        if self.option_command == 1:
            return "SOLO"
        elif self.option_command == 2:
            return "ALGO 1"
        elif self.option_command == 3:
            return "ALGO 2"

    def draw_options_screen(self, command=-1):
        """draw_options_screen -> creates option screen, which you can open by clicking at the
        'options' button at the main_menu screen"""
        self.screen.blit(self.zlom, (0, 0))
        pygame.draw.rect(self.screen, "black", [50, 100, 300, 300])
        pygame.draw.rect(self.screen, "green", [50, 100, 300, 300], 5)
        pygame.draw.rect(self.screen, "white", [70, 120, 260, 40], 0, 5)
        pygame.draw.rect(self.screen, "gray", [70, 120, 260, 40], 5, 5)
        txt = self.font.render("Options!", True, "black")
        self.screen.blit(txt, (135, 127))
        # menu exit button
        exit_button = Button("Exit Options", (85, 350), self.screen, self.font)
        exit_button.draw()
        solo_button = Button("Solo Game", (85, 180), self.screen, self.font)
        solo_button.draw()
        algo1_button = Button("Algorithm no. 1", (85, 240), self.screen, self.font)
        algo1_button.draw()
        algo2_button = Button("Algorithm no.2", (85, 300), self.screen, self.font)
        algo2_button.draw()
        if exit_button.check_clicked():
            command = 0
            self.menu_command = -1
        elif solo_button.check_clicked():
            self.option_command = 1
        elif algo1_button.check_clicked():
            self.option_command = 2
        elif algo2_button.check_clicked():
            self.option_command = 3
        return command

    def menus(self):
        """menus - is main loop function that contains all operations that you can change or set before starting solo
        game or algorithm"""
        run = True

        while run:
            self.screen.blit(self.background, (0, 0))
            self.timer.tick(MainMenu.FPS)
            print(f"menu_command: {self.menu_command}")
            print(f"option_command: {self.option_command}")
            if self.menu_command == 0:
                self.draw_preload_screen()
            elif self.menu_command == -1:
                self.menu_command = self.draw_menu_screen()
                if self.menu_command != -1:
                    self.want_go_to_main_menu = False
            elif self.menu_command > 0:
                self.draw_preload_screen()
                self.text = self.font.render("Randomized Game Option  ->  " + str(self.which_game_option_choosen()), True, "white")
                self.screen.blit(self.text, (150, 100))

                if self.menu_command == 2:
                    exit_command = self.draw_options_screen()
                    pygame.display.flip()
                    self.text = self.font.render(
                        "Choosen Game Option  ->  " + str(self.which_game_option_choosen()), True, "black"
                    )
                    self.screen.blit(self.text, (900, 750))
                    if exit_command == 0:
                        self.menu_command = -1
                        pygame.display.flip()

                if self.menu_command == 1 and self.option_command == 1:
                    pygame.display.flip()
                    game = gmf.Game()
                    game.play_solo()
                    #run = False
                    self.menu_command = 0
                elif self.menu_command == 1 and self.option_command == 2:
                    pygame.display.flip()
                    game = gmf.Game()
                    game.play_algo()
                    #run = False
                    self.menu_command = 0
                elif self.menu_command == 1 and self.option_command == 3:
                    pygame.display.flip()
                    game = gmf.Game()
                    game.play_algo_v2()
                    #run = False
                    self.menu_command = 0

                if self.menu_command == 3:
                    self.option_command = random.randint(1, 3)
                    self.menu_command = 10

            key = pygame.key.get_pressed()
            if key[pygame.K_TAB]:
                run = False

            Game.exit_game()
            pygame.display.flip()
