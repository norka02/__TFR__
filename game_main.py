import time

# todo delete unused libraries
import pygame
import sys
from algorythm.Tre import Tre
from algorythm.Ancestors import Ancestors
from utils import detect_stat_dyn_collide
from game.game_parameters import GameParameters as gp
from game.cars import PlayerCar, ComputerCar


class Game:
    """Modulacja z funkcjami pygame -> dużo miesza bo razem z załadowaniem obrazka długi ciąg się robi"""

    alg_speed = 10
    alg_rotation = 10

    @staticmethod
    def draw_static(window, images: list):
        window.fill((29, 130, 34))
        for image, position in images:
            window.blit(image, position)

    @staticmethod
    def draw_static_algo2(window, images: list, timer, generation_counter):
        """draw_static_algo2 -> draws board (track and satatic fragments) for play_algo_v2"""
        window.fill((29, 130, 34))
        for image, position in images:
            window.blit(image, position)
        font = pygame.font.Font("freesansbold.ttf", 32)
        data_text = font.render("__DATA__", True, "white")
        gp.GAME_WINDOW.blit(data_text, (1050, 320))
        time_counter = font.render("Time  ->  " + str(round(time.time() - timer, 3)), True, "white")
        gp.GAME_WINDOW.blit(time_counter, (1000, 360))
        generation_counter = font.render("Count  ->  " + str(generation_counter), True, "white")
        gp.GAME_WINDOW.blit(generation_counter, (1000, 400))
        usage = font.render("__USAGE__", True, "white")
        gp.GAME_WINDOW.blit(usage, (1050, 500))
        how_to_exit = font.render("Press TAB to exit", True, "white")
        gp.GAME_WINDOW.blit(how_to_exit, (1000, 540))

    @staticmethod
    def draw_static_algo1(window, images: list, timer):
        """draw_static_algo1 -> draws board (track and satatic fragments) for play_algo"""
        window.fill((29, 130, 34))
        for image, position in images:
            window.blit(image, position)
        font = pygame.font.Font("freesansbold.ttf", 32)
        data_text = font.render("__DATA__", True, "white")
        gp.GAME_WINDOW.blit(data_text, (1050, 360))
        time_counter = font.render("Time  ->  " + str(round(time.time() - timer, 3)), True, "white")
        gp.GAME_WINDOW.blit(time_counter, (1000, 400))
        usage = font.render("__USAGE__", True, "white")
        gp.GAME_WINDOW.blit(usage, (1050, 500))
        how_to_exit = font.render("Press TAB to exit", True, "white")
        gp.GAME_WINDOW.blit(how_to_exit, (1000, 540))

    @staticmethod
    def draw_static_solo(window, images: list, timer):
        """draw_static_solo -> draws board (track and static fragments) for play_solo"""
        window.fill((29, 130, 34))
        for image, position in images:
            window.blit(image, position)
        font = pygame.font.Font("freesansbold.ttf", 32)
        data_text = font.render("__DATA__", True, "white")
        gp.GAME_WINDOW.blit(data_text, (1050, 320))
        if timer == 0:
            time_counter = font.render("Time  ->  " + str(timer), True, "white")
        else:
            time_counter = font.render("Time  ->  " + str(round(time.time() - timer, 3)), True, "white")
        gp.GAME_WINDOW.blit(time_counter, (1000, 360))
        usage = font.render("__USAGE__", True, "white")
        gp.GAME_WINDOW.blit(usage, (1050, 560))
        how_to_start = font.render("Press SPACE to start game", True, "white")
        gp.GAME_WINDOW.blit(how_to_start, (950, 600))
        how_to_exit = font.render("Press TAB to exit", True, "white")
        gp.GAME_WINDOW.blit(how_to_exit, (950, 640))

    @staticmethod
    def draw_static_info(window, images: list, time=None):
        """draw_static_info -> draws information how to start new game after pressing TAB or corssing the finish line
        and how to exit it"""
        window.fill((29, 130, 34))
        for image, position in images:
            window.blit(image, position)
        font = pygame.font.Font("freesansbold.ttf", 32)
        if time is not None:
            text = font.render(f"Your time: {round(time, 3)}", True, "white")
            gp.GAME_WINDOW.blit(text, (100, 640))
        text = font.render("To start game press ENTER", True, "white")
        gp.GAME_WINDOW.blit(text, (100, 670))
        text = font.render("To exit game press ESC", True, "white")
        gp.GAME_WINDOW.blit(text, (100, 700))

    @staticmethod
    def draw_dynamic(window, all_cars):
        for car in all_cars:
            car.draw_rotated_car(window)
            car.control()
            car.collision(gp.RACE_TRACK_BORDER_MASK)
        pygame.display.update()

    @staticmethod
    def exiting_game_algo(run, which_algo=1):
        while run:
            Game.draw_static_info(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES_WIN_ALGO)
            pygame.display.update()
            Game.exit_game()
            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN] and which_algo == 1:
                Game.play_algo()
            elif key[pygame.K_RETURN] and which_algo == 2:
                Game.play_algo_v2()
            elif key[pygame.K_ESCAPE]:
                return False

    @staticmethod
    def play_algo():
        """play_algo -> first algorithm that overcomes the track by itself"""
        run = True
        FPS = 300  # klatki na sekunde
        timer = pygame.time.Clock()  # tworzenie instancji zegara
        cars2 = []
        cars2.append(
            ComputerCar(rotation_vel=Game.alg_rotation, start_pos_y=380 - 50, start_pos_x=750,
                        max_velocity=Game.alg_speed)
        )
        tre = Tre(1)
        stime = time.time()

        while run:
            timer.tick(FPS)
            all_cars = cars2
            Game.draw_static_algo1(
                window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES, timer=stime
            )
            Game.draw_dynamic(window=gp.GAME_WINDOW, all_cars=all_cars)
            # key = pygame.key.get_pressed()
            # if key[pygame.K_c]:
            #     player_cars.append(PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200))
            #     time.sleep(0.5)
            cars2 = tre.next_step(cars2)
            if len(cars2) < 1000:
                cars2.append(
                    ComputerCar(rotation_vel=Game.alg_rotation, start_pos_y=380 - 50, start_pos_x=750,
                                max_velocity=Game.alg_speed)
                )
            key = pygame.key.get_pressed()
            if key[pygame.K_TAB]:
                tre.save_path_to_file_pickle()
                run = Game.exiting_game_algo(run)

            Game.exit_game()

    @staticmethod
    def exit_game():
        """exit_game -> function which defines exiting the game"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    @staticmethod
    def play_solo():
        """play_solo -> main loop function for driving a car and trying to cross the finish line. Defines static
        and dynamic parameters of the solo game"""

        """Frames per second"""
        FPS = 60
        """Creating clock instance"""
        timer = pygame.time.Clock()
        """Creating player car instance"""
        player_car = [PlayerCar(rotation_vel=1, start_pos_y=380 - 50, start_pos_x=750, max_velocity=0)]

        "Starting game and timer parameters"
        stime = 0
        start_game = False
        run = True

        """Main loop where the game is running"""
        while run:
            timer.tick(FPS)
            Game.draw_static_solo(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES, timer=stime)
            Game.draw_dynamic(window=gp.GAME_WINDOW, all_cars=player_car)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                start_game = True
                stime = time.time()

            if start_game:
                player_car[0].max_velocity = 1
                player_car[0].control()
                car_pos = (player_car[0].x_cord, player_car[0].y_cord)
                finish_pos = (gp.FINISH_X_CORD, gp.FINISH_Y_CORD)
                collision_with_meta = detect_stat_dyn_collide(gp.FINISH_LINE, player_car[0].IMG, car_pos, finish_pos)
                etime = time.time()
                if collision_with_meta and (etime - stime) > 2.0:
                    while run:
                        Game.draw_static_info(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES_WIN, time=etime - stime)
                        pygame.display.update()
                        Game.exit_game()
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_RETURN]:
                            Game.play_solo()
                        elif keys[pygame.K_ESCAPE]:
                            run = False
                if player_car[0].collide is not None or keys[pygame.K_TAB]:
                    """This conditional statement defines what is doing when car collides band"""
                    while run:
                        Game.draw_static_info(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES_DEAD)
                        pygame.display.update()
                        Game.exit_game()
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_RETURN]:
                            Game.play_solo()
                        elif keys[pygame.K_ESCAPE]:
                            run = False

            Game.exit_game()

    @staticmethod
    def play_algo_v2():
        """play_algo_v2 -> second algorithm that overcomes the track by itself"""
        ancestors = Ancestors()

        run = True
        FPS = 60  # klatki na sekunde
        timer = pygame.time.Clock()  # tworzenie instancji zegara

        cars2 = []

        for i in range(1000):
            car = ComputerCar(rotation_vel=Game.alg_rotation, start_pos_y=380 - 50, start_pos_x=750,
                              max_velocity=Game.alg_speed)
            cars2.append(car)

        time_counter = time.time()
        generation_counter = 1

        while run:
            timer.tick(FPS)
            all_cars = cars2
            Game.draw_static_algo2(
                window=gp.GAME_WINDOW,
                images=gp.IMAGES_AND_SIZES,
                timer=time_counter,
                generation_counter=generation_counter,
            )
            Game.draw_dynamic(window=gp.GAME_WINDOW, all_cars=all_cars)
            # key = pygame.key.get_pressed()
            # if key[pygame.K_c]:
            #     player_cars.append(PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200))
            #     time.sleep(0.5)
            cars2 = ancestors.next_step(cars2)
            if len(cars2) == 0:
                for i in range(500):
                    cars2.append(
                        ComputerCar(
                            rotation_vel=Game.alg_rotation, start_pos_y=380 - 50, start_pos_x=750,
                            max_velocity=Game.alg_speed
                        )
                    )
                # print(ancestors.set_of_sets_all)
                ancestors.reduce_sets()
                ancestors.who_to_follow(cars2)
                generation_counter += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # ants.show_matrix()
                    pygame.quit()
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_TAB]:
                ancestors.save_path_file_pickle()
                run = Game.exiting_game_algo(run, which_algo=2)
