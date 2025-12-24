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
        up_dist = - \
            1 if self.dir == "DOWN" else self.scan_direction(0, -1, map_state)
        down_dist = - \
            1 if self.dir == "UP" else self.scan_direction(0, 1, map_state)
        left_dist = - \
            1 if self.dir == "RIGHT" else self.scan_direction(-1, 0, map_state)
        right_dist = - \
            1 if self.dir == "LEFT" else self.scan_direction(1, 0, map_state)

        max_dist = max(up_dist, down_dist, left_dist, right_dist)
        print("Space: | UP {} | DOWN {} | LEFT {} | RIGHT {}",
              up_dist, down_dist, left_dist, right_dist)

        if (max_dist == up_dist):
            self.move_up()
        elif (max_dist == down_dist):
            self.move_down()
        elif (max_dist == left_dist):
            self.move_left()
        elif (max_dist == right_dist):
            self.move_right()

        return (self.x, self.y)

    def scan_direction(self, dx, dy, map_state):
        dist = 0
        (x, y) = self.x, self.y
        while (map_state[x+dx, y+dy] == 0):
            x += dx
            y += dy
            dist += 1

        return dist
