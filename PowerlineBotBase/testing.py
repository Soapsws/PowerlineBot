import world
import agent
import time
import utils

midp = world.mapx.shape[0] // 2


def standard_test(iterations, obstacles, floodfill):
    avg = 0.0
    for i in range(iterations):
        print("iteration ", i)
        running = True
        ag = agent.Agent(midp, midp, floodfill)
        utils.generate_obstacles(obstacles, world.mapx, ag)
        while running:
            (prev_x, prev_y) = ag.x, ag.y
            (x, y) = ag.heuristic_move(world.mapx)
            if not world.edit_tile(x, y, 2):
                running = False
                break
            world.mapx[prev_y, prev_x] = 2
            ag.time_alive += 1
        avg += ag.time_alive
        world.reset()
    avg //= iterations
    print("Program End <> | Agent average time alive:", avg)


def single_test(obstacles, floodfill):
    running = True
    ag = agent.Agent(midp, midp, floodfill)
    utils.generate_obstacles(obstacles, world.mapx, ag)
    while running:
        utils.clear_terminal()
        (prev_x, prev_y) = ag.x, ag.y
        (x, y) = ag.heuristic_move(world.mapx)
        if not world.edit_tile(x, y, 88):  # use big value for more spaced out map
            running = False
            break
        world.mapx[prev_y, prev_x] = 2
        world.print_map()
        ag.time_alive += 1
        world.reset()
    print("Program End <> | Agent time alive:", ag.time_alive)
