import numpy
import utils


class Agent:

    def __init__(self, x, y, floodfill):
        self.x = x
        self.y = y
        self.floodfill = floodfill
        self.time_alive = 0
        self.dir = "UP"
        self.alive = True

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

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

        # print(
        # f"Space: | UP {up_dist} | DOWN {down_dist} | LEFT {left_dist} | RIGHT {right_dist}")

        if (self.floodfill):
            ff_weight = 1
            up_space, down_space, left_space, right_space = self.floodfill_heuristic_move(
                map_state)

            up_dist += up_dist / ff_weight * up_space
            down_dist += down_dist / ff_weight * down_space
            left_dist += left_dist / ff_weight * left_space
            right_dist += right_dist / ff_weight * right_space

        max_dist = max(up_dist, down_dist, left_dist, right_dist)

        if (max_dist == up_dist):
            self.move_up()
            self.dir = "UP"
        elif (max_dist == down_dist):
            self.move_down()
            self.dir = "DOWN"
        elif (max_dist == left_dist):
            self.move_left()
            self.dir = "LEFT"
        elif (max_dist == right_dist):
            self.move_right()
            self.dir = "RIGHT"

        return (self.x, self.y)

    def scan_direction(self, dx, dy, map_state):
        dist = 0
        (x, y) = self.x, self.y
        # NumPy arrays go by row, column -> y, x
        while (map_state[y+dy, x+dx] == 0):
            x += dx
            y += dy
            dist += 1

        return dist

    def floodfill_heuristic_move(self, map_state):
        if map_state[self.y + 1, self.x + 1] != 0 \
                or map_state[self.y + 1, self.x - 1] != 0 \
            or map_state[self.y - 1, self.x + 1] != 0 \
                or map_state[self.y - 1, self.x - 1] != 0:
            space_up = utils.floodfill(map_state, self.x, self.y - 1)
            space_down = utils.floodfill(map_state, self.x, self.y + 1)
            space_left = utils.floodfill(map_state, self.x - 1, self.y)
            space_right = utils.floodfill(map_state, self.x + 1, self.y)

            return (space_up, space_down, space_left, space_right)
        return 0, 0, 0, 0
