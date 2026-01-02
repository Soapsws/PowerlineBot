import random
import os
from collections import deque
import heapq
import math


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def generate_obstacles(num_blocks, map_state, agent):
    placed = 0
    while placed < num_blocks:
        x = random.randint(0, map_state.shape[1] - 1)
        y = random.randint(0, map_state.shape[0] - 1)
        if (map_state[y, x] == 1 or (x, y) == (agent.x, agent.y)):
            continue
        map_state[y, x] = 1
        placed += 1


def floodfill(map_state, x, y):
    q = deque()
    s = set()

    min_x = math.inf
    max_x = 0
    min_y = math.inf
    max_y = 0

    q.append((x, y))
    s.add((x, y))

    space = 0
    while q:
        # right pop - default pop() - makes it DFS, not BFS
        (temp_x, temp_y) = q.popleft()

        min_x = min(min_x, temp_x)
        max_x = max(max_x, temp_x)
        min_y = min(min_y, temp_y)
        max_y = max(max_y, temp_y)

        if upd_ff(temp_x + 1, temp_y, s, q, map_state):
            space += 1
        if upd_ff(temp_x - 1, temp_y, s, q, map_state):
            space += 1
        if upd_ff(temp_x, temp_y + 1, s, q, map_state):
            space += 1
        if upd_ff(temp_x, temp_y - 1, s, q, map_state):
            space += 1

    length = max_x - min_x
    height = max_y - min_y

    if length == 0 or height == 0:
        bonus_top = 0
    else:
        bonus_top = (min(length, height) / max(length, height)) * space / 2

    return space + bonus_top


def upd_ff(x, y, s, q, map_state):
    if x >= map_state.shape[1] or x < 0 or y >= map_state.shape[0] or y < 0:
        return False
    if not (x, y) in s and map_state[y, x] == 0:
        q.append((x, y))
        s.add((x, y))
        return True
    return False


def pathfind(nodes, edges, start, end, heuristic):
    # h = 0 -> simple dijkstra
    pq = []
    cost = [math.inf] * len(nodes)
    prev = [None] * len(nodes)
    cost[start] = 0
    heapq.heappush(pq, (cost[start], start))

    while (pq):
        cost_curr, curr = heapq.heappop(pq)
        if curr == end:  # only works cus priority queue
            break
        if cost_curr > cost[curr]:  # outdated value skip
            continue
        for cost_n, n in edges[curr]:
            # cost_path <=> g(n) | heuristic[n] <=> h[n]
            cost_path = cost_curr + cost_n
            if cost_path < cost[n]:
                prev[n] = curr
                # not storing h, this is simply g
                cost[n] = cost_path
                # heuristic is ONLY used for priority
                heapq.heappush(pq, (cost_path + heuristic[n], n))

    return cost, prev
