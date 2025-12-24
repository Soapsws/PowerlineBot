import world
import agent
import time

running = True
midp = world.mapx.shape[0] // 2
ag = agent.Agent(midp, midp)

while running:
    (prev_x, prev_y) = ag.x, ag.y
    (x, y) = ag.heuristic_move(world.mapx)
    if not world.edit_tile(x, y, 8):
        running = False
        break
    world.mapx[prev_y, prev_x] = 2

    world.print_map()
    ag.time_alive += 1
    # time.sleep(5)


print("Program End <> | Agent time alive: {}", ag.time_alive)

# To-Do:
# (1) Make head distinguishable for easier debugging [ done -> 8 ]
# (2) Add static obstacles
