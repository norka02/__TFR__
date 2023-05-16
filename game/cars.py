import pygame
import math
from game.game_parameters import GameParameters as gp
from utils import blit_rotate_center


class AbstractCar:
    """Fields and methods which are uniq to all cars"""

    """An image of a car"""
    IMG = ""

    def __init__(self, rotation_vel, start_pos_x, start_pos_y, max_velocity):
        """Defines fields of an abstract car"""
        self.x_cord = start_pos_x
        self.y_cord = start_pos_y
        self.pos_top_left = (self.x_cord, self.y_cord)
        self.image = self.IMG
        self.velocity = 0
        self.max_velocity = max_velocity
        self.rotation_vel = rotation_vel
        self.angle = 84
        self.current_image = None
        self.collide = None
        self.scent_of_death = []
        self.path = []
        self.follow_path = []
        self.jump = 0.1
        self.follow_ancestor_path = True

    """Methods which are responsible for moving and rotating car objects. In pygame coordinate system, an angle of
     zero degrees corresponds to the orientation of the object along the x-axis, with the "top" of the object pointing
     up the screen (in opposite direction to growing y-axis values)"""
    """If car want to go left the angle has to decrease, if right the angle has to increase"""
    def rotate(self, left=False, right=False):
        """rotate() -> This function defines rotation of a car"""
        if left:
            self.angle += self.rotation_vel
        if right:
            self.angle -= self.rotation_vel

    """The zero angle is along the y-axis, because of that the trigonometric functions are opposite compared to 
    situation if the zero angle was along the x-axis"""
    def move(self):
        """move() -> This function defines how any car moves"""
        radians = math.radians(self.angle)
        x_move = self.max_velocity * math.sin(radians)
        y_move = self.max_velocity * math.cos(radians)
        self.x_cord -= x_move
        self.y_cord -= y_move

    def draw_rotated_car(self, window):
        """draw_rotated_car() -> This function draws rotated car"""
        self.current_image = blit_rotate_center(
            surf=window, image=self.image, top_left=(self.x_cord, self.y_cord), angle=self.angle
        )

    def collision(self, track_mask, x=0, y=0):
        """collision() -> This function checks collisions with band"""
        offset = int(self.x_cord), int(self.y_cord)
        car_mask = pygame.mask.from_surface(self.current_image)
        self.collide = track_mask.overlap(car_mask, offset)
        return self.collide


class ComputerCar(AbstractCar):
    """This class defines fields and methods which defines computer car"""
    IMG = gp.CAR_IMG

    def __init__(self, rotation_vel, start_pos_x, start_pos_y, max_velocity):
        """Defines fields of a computer car"""
        super().__init__(rotation_vel, start_pos_x, start_pos_y, max_velocity)
        self.turn = 0

    def control(self):
        """control() -> This function defines how computer control a car"""
        if self.turn == 0:
            pass
        elif self.turn == 1:
            super().rotate(right=True)
        elif self.turn == -1:
            super().rotate(left=True)
        super().move()

    def set_turn(self, turn):
        """set_turn() -> This function sets turn from genetic algorithm"""
        self.turn = turn


class PlayerCar(AbstractCar):
    """This class defines fields and methods which defines player car"""
    IMG = gp.CAR_IM4G

    def __init__(self, rotation_vel, start_pos_x, start_pos_y, max_velocity):
        """Defines fields of a player car"""
        super().__init__(rotation_vel, start_pos_x, start_pos_y, max_velocity)

    def control(self):
        """control() -> This function defines how to control a player car"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            super().rotate(left=True)
        if keys[pygame.K_d]:
            super().rotate(right=True)
        super().move()
