from random import choice


class RandomWalk():

    def __init__(self,num_points=5000):

        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.num_points:

            x_value = self.get_value()
            y_value = self.get_value()

            if x_value == 0 and y_value == 0:
                continue

            self.x_values.append(self.x_values[-1] + x_value)
            self.y_values.append(self.y_values[-1] + y_value)

    def get_value(self):

        dircection = choice([-1,1])
        distance = choice([0,1,2,3,4])

        return dircection * distance
