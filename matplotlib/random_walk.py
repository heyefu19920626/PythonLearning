from random import choice


class RandomWalk():

    def __init__(self,num_points=5000):

        self.num_points = num_points

        self.x_values = []
        self.y_values = []

        self.x_value = 0
        self.y_value = 0

    def fill_walk(self):

        while self.num_points > 0:

            x_value = self.get_value()
            y_value = self.get_value()

            if x_value == 0 and y_value == 0:
                continue

            self.x_value += x_value
            self.y_value += y_value

            self.x_values.append(self.x_value)
            self.y_values.append(self.y_value)

            self.num_points -= 1

    def get_value(self):

        dircection = choice([-1,1])
        distance = choice([0,1,2,3,4])

        return dircection * distance
