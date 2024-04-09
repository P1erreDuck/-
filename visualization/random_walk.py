from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    """    def fill_walk(self):
            while len(self.x_values) < self.num_points:
                x_direction = choice([1, -1])
                x_distance = choice(range(1, 4))
                x_step = x_direction * x_distance
                y_direction = choice([1, -1])
                y_distance = choice(range(1, 4))
                y_step = y_direction * y_distance
                if x_step == 0 and y_step == 0:
                    continue
                x = self.x_values[-1] + x_step
                y = self.y_values[-1] + y_step
                self.x_values.append(x)
                self.y_values.append(y)"""

    def get_step(self, direction, distance):
        """direction = (choice([1, -1]
        distance = choice(range(1, 4))
        вывел в параметры"""
        step = direction * distance
        return step

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step(1, choice(range(1, 8)))
            y_step = self.get_step(choice([1, -1]), choice(range(1, 4)))
            if x_step == 0 and y_step == 0:
                continue
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)