import world
import agent
import time

running = True
midp = world.mapx.shape[0] // 2
ag = agent.Agent(midp, midp)

while running:
    (x, y) = ag.heuristic_move(world.mapx)
    if not world.edit_tile(x, y, 2):
        running = False
        break
    world.print_map()
    ag.time_alive += 1
    time.sleep(5)


print("Program End <> | Agent time alive: {}", ag.time_alive)
