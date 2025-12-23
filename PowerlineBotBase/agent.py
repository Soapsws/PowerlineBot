import numpy


class Agent:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.time_alive = 0
        self.dir = "UP"
        self.alive = True

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def heuristic_move(self, map_state):
        up_cost = 1000000 if self.dir == "DOWN" else 0
        down_cost = 1000000 if self.dir == "UP" else 0
        left_cost = 1000000 if self.dir == "RIGHT" else 0
        right_cost = 1000000 if self.dir == "LEFT" else 0

        dist = 0
        for i in range(self.y, -1, -1):
            if map_state[self.x, i] != 0:
                up_cost += 1000 / (dist + 1)
            dist += 1
        dist = 0
        for i in range(self.y, map_state.shape[0]):
            if map_state[self.x, i] != 0:
                down_cost += 1000 / (dist + 1)
            dist += 1
        dist = 0
        for i in range(self.x, -1, -1):
            dist = 0
            if map_state[i, self.y] != 0:
                left_cost += 1000 / (dist + 1)
            dist += 1
        dist = 0
        for i in range(self.x, map_state.shape[0]):
            dist = 0
            if map_state[i, self.y] != 0:
                right_cost += 1000 / (dist + 1)
            dist += 1

        min_cost = min(up_cost, down_cost, left_cost, right_cost)
        if (min_cost) == up_cost:
            self.move_up()
            self.dir = "UP"
        elif (min_cost) == down_cost:
            self.move_down()
            self.dir = "DOWN"
        elif (min_cost) == left_cost:
            self.move_left()
            self.dir = "LEFT"
        else:
            self.move_right()
            self.dir = "RIGHT"
