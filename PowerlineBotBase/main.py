import world
import agent
import time
import utils

running = True
midp = world.mapx.shape[0] // 2
ag = agent.Agent(midp, midp)

utils.generate_obstacles(20, world.mapx, ag)

while running:
    utils.clear_terminal()  # CLEARS TERMINAL
    (prev_x, prev_y) = ag.x, ag.y
    (x, y) = ag.heuristic_move(world.mapx)
    if not world.edit_tile(x, y, 88):  # use big value for more spaced out map
        running = False
        break
    world.mapx[prev_y, prev_x] = 2

    world.print_map()
    ag.time_alive += 1

    time.sleep(0.1)

print("Program End <> | Agent time alive:", ag.time_alive)

# To-Do:
# (1) Finish floodfill heuristic move logic (done with iteration 1)
# (2) Play around some more
