import math
import random
import numpy
import utils


class Ants:
    def __init__(self, size):
        self.size = []
        self.size.append(utils.position_fix(size[0]))
        self.size.append(utils.position_fix(size[1]))
        print(self.size)
        self.matrix = [[1 for x in range(self.size[0])] for y in range(self.size[1])]
        self.scent_strength = 1.2
        # print(self.matrix)
        # self.scents_of_death = []

    def decide(self, car_position_x, car_position_y, car_rotation):
        rotation_matrix = [
            [math.cos(math.radians(car_rotation)), -math.sin(math.radians(car_rotation))],
            [math.sin(math.radians(car_rotation)), math.cos(math.radians(car_rotation))],
        ]

        sens_half_width = 2
        sens_length = 1
        left_points = []
        right_points = []
        # straight_points = []
        for y in range(sens_length):
            # straight_points.append([0, y + 1])
            for x in range(sens_half_width):
                # print([-x - 1, y + 1])
                # print([x + 1, y + 1])
                left_points.append(numpy.matmul([-x - 1, y + 2], rotation_matrix))
                right_points.append(numpy.matmul([x + 1, y + 2], rotation_matrix))
        # print(len(left_points))
        # print(len(right_points))
        # print(left_points[0])
        # left_points = numpy.multiply(left_points, rotation_matrix)
        # right_points = numpy.multiply(right_points, rotation_matrix)
        for point in range(len(left_points)):
            # print(int(numpy.round(left_points[point][0] + car_position_y, 0)))
            left_points[point] = [
                int(numpy.round(left_points[point][0] + car_position_x, 0)),
                int(numpy.round(left_points[point][1] + car_position_y, 0)),
            ]
        for point in range(len(right_points)):
            right_points[point] = [
                int(numpy.round(right_points[point][0] + car_position_x, 0)),
                int(numpy.round(right_points[point][1] + car_position_y, 0)),
            ]
        # for point in range(len(straight_points)):
        #     straight_points[point] = [int(numpy.round(straight_points[point][0] + car_position_x, 0)),
        #                               int(numpy.round(straight_points[point][1] + car_position_y, 0))]
        weight_left = 1
        weight_right = 1
        # weight_straight = 1
        for i in range(len(left_points)):
            weight_left += self.matrix[left_points[i][0]][left_points[i][1]]
        for i in range(len(right_points)):
            weight_right += self.matrix[right_points[i][0]][right_points[i][1]]
        # for i in range(len(straight_points)):
        #     weight_straight += self.matrix[straight_points[i][0]][straight_points[i][1]]

        decision = random.choices([-1, 1], [weight_left ** 2, weight_right ** 2], k=1)
        # print(weight_left)
        # print(weight_right)
        # print(decision)
        # print(car_position_x)
        # print(car_position_y)
        # print(left_points)
        # print(right_points)
        return decision[0]

    def next_step(self, cars):
        carsnew = []
        for car in cars:
            if car.colide:
                # print(car.colide)
                max_delete = 50
                for cords in car.scent_of_death:
                    self.matrix[cords[0]][cords[1]] /= self.scent_strength
            else:
                # car.turn = round(random.uniform(-1, 1))
                # car.turn = random.choice([-1, 1])
                car.turn = self.decide(
                    utils.position_fix(car.x_cord), utils.position_fix(car.y_cord), car.angle
                )
                # car.turn = self.get_decision(car.path)
                # car.path.append(car.turn)
                carsnew.append(car)
                x = utils.position_fix(car.x_cord)
                y = utils.position_fix(car.y_cord)
                car.scent_of_death.append([x, y])
                print(car.scent_of_death)
                self.matrix[x][y] *= self.scent_strength

                if self.matrix[x][y] > 1.2 ** 200:
                    print(":<")
                    for i in range(self.size[0]):
                        for j in range(self.size[1]):
                            if self.matrix[i][j] > 100:
                                self.matrix[i][j] -= 100

        return carsnew

    def show_matrix(self):
        with open("matrix.txt", "w") as f:
            for row in self.matrix:
                countTmp = 0
                for ttmp in row:
                    countTmp += ttmp
                # print(countTmp)
                f.write(" ".join(str(x) for x in row) + "\n")
