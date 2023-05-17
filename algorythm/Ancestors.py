import pickle
import random



class Ancestors:
    def __init__(self):
        self.set_of_sets_all = []
        self.set_of_sets = []

        self.max_sets = 50  # zad22 ustawic to i base_unfollow_probability tak zeby w 20 cyklach dojechac do lewej na dole
        self.base_unfollow_probability = 4 / 5  # always less than 1

    def next_step(self, cars):
        """foreach car in cars if car colides we delete it else decision funcion is called"""
        cars_new = []
        for car in cars:
            if car.collide:
                if car.path:
                    self.set_of_sets_all.append(car.path)
            else:
                self.decide(car)  # sets car turn
                car.path.append(car.turn)
                car.jump = car.jump / self.base_unfollow_probability  # zad11 to tez wtedy trzeba zmienic
                cars_new.append(car)
        return cars_new

    def decide(self, car):
        """decides if car will folow its path or start acting randomly
        chance to abandon path increases with distance traveled"""
        if len(car.path) < len(car.follow_path) and car.follow_ancestor_path:
            if random.choices([0, 1], [car.jump, 1 - car.jump], k=1)[0]:
                car.turn = car.follow_path[len(car.path)]
            else:
                car.follow_ancestor_path = False
                car.turn = random.choice([-1, 1])
        else:
            car.turn = random.choice([-1, 1])

    def reduce_sets(self):
        """reduces number of paths that can be followed
        only longest paths are saved"""
        self.set_of_sets = sorted(self.set_of_sets_all, key=len, reverse=True)[
                           0: self.max_sets
                           ].copy()
        self.set_of_sets_all = []

    def who_to_follow(self, cars):
        """car is assigned with random path to follow"""
        print("======================")
        for tmp_set in self.set_of_sets:
            print(len(tmp_set), "  ", tmp_set)
        for car in cars:
            car.follow_path = random.choice(self.set_of_sets)
            # car.follow_path = [0]
            car.jump = self.base_unfollow_probability ** len(car.follow_path)  #  zad11 np jako zadanie mozna to do napisania dac

    def save_path(self):
        """returns longest path from set of paths that can be followed by car"""
        if not self.set_of_sets:
            print("cant save path")
        else:
            path = sorted(self.set_of_sets, key=len, reverse=True)[0]
            print("PATH: ")
            print(path)
            return path

    def save_path_file_pickle(self):
        """saves path to binary file"""
        path = self.save_path()
        with open("Ancestors_path.pkl", "wb") as f:
            pickle.dump(path, f)
