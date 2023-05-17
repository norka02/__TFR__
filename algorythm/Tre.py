import os
import pickle
import random

class Tre:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.strength_path = 15 #zad33 ustawic wzor na wyliczanie tego w zaleznosci od ilosci samochodzikow

    def load_old_tree(self):
        if os.path.exists("tre_left.pkl") and os.path.exists("tre_right.pkl"):
            with open("tre_left.pkl", 'rb') as file:
                self.left = pickle.load(file)
            with open("tre_right.pkl", 'rb') as file:
                self.right = pickle.load(file)
        else:
            print("nope")

    def next_step(self, cars):
        """next_step -> for every object (car) in list of objects (cars) we are checking if it collides with any
        barrier, if so we delete the car's path, if not we perform get_deciosion() function and expand our path data
        """
        cars_new = []
        for car in cars:
            if car.collide:
                # print(car.colide)
                self.purge_path(car.path)
            else:
                decision = self.get_decision(car.path.copy())
                car.turn = decision
                car.path.append(decision)
                cars_new.append(car)
        return cars_new

    def function(self):
        """function -> adding elements to the Tre, if there is None, if they exist - draws decision (if next step would
        be right or left), on this data extends path strength"""
        if self.left is None:
            self.left = Tre(1)
        if self.right is None:
            self.right = Tre(1)
        decision = random.choices([-1, 1], [self.left.data, self.right.data], k=1)[0]
        # print(self.left.data)
        # print(self.right.data)
        if decision == -1:
            self.left.data += self.strength_path  # zad33 o ut czeba wzora zapodać
        elif decision == 1:
            self.right.data += self.strength_path  # zad33 i tu tez oczywiscie jakby co
        return decision


    def get_decision(self, path):
        """get_decision() -> recursively traverses the Tre to find best option (probability), going left or right"""
        # # print(path)
        # try:
        #     next_node = path.pop(0)
        # except:
        #     next_node = 0
        #     print("oops")
        #
        if len(path) == 0:
            return self.function()
        else:
            next_node = path.pop(0)
            if next_node == -1:
                return self.left.get_decision(path)
            elif next_node == 1:
                return self.right.get_decision(path)

    def purge_path(self, path):
        """purge_path() -> deletes paths of dead ants"""
        if len(path) == 0:
            self.data -= 1
        else:
            next_node = path.pop(0)
            if next_node == -1:
                self.left.purge_path(path)
                self.data -= self.strength_path  # zad33 tu tez tylko ze operacja przeciwna jak widac byl plus a jest minus
            elif next_node == 1:
                self.right.purge_path(path)
                self.data -= self.strength_path  # zad33 i tu

    def save_path(self):
        if self.left is None or self.right is None:
            tmp = []
            return tmp
        elif self.left.data == self.right.data:
            tmp = []
            return tmp
        else:
            if self.left.data > self.right.data:
                curnent_val = -1
                tmp_list = self.left.save_path()
                tmp_list.append(curnent_val)
                return tmp_list
            if self.left.data < self.right.data:
                curnent_val = 1
                tmp_list = self.right.save_path()
                tmp_list.append(curnent_val)
                return tmp_list

    def save_path_to_file(self):
        path = self.save_path()
        path.reverse()

        # open a file for writing
        with open("tre_path.txt", "w") as f:
            # write the list to the file
            for item in path:
                f.write(str(item) + "\n")

    def save_path_to_file_pickle(self):
        path = self.save_path()
        path.reverse()
        with open("tre_path.pkl", "wb") as f:
            pickle.dump(path, f)
    def save_tree(self):
        with open("tre_left.pkl", "wb") as f:
            pickle.dump(self.left, f)
        with open("tre_right.pkl", "wb") as f:
            pickle.dump(self.right, f)
