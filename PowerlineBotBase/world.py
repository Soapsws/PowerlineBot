import numpy as np

mapx = np.zeros((16, 16))
for i in range(mapx.shape[0]):
    mapx[0, i] = 1
    mapx[mapx.shape[0] - 1, i] = 1
    mapx[i, 0] = 1
    mapx[i, mapx.shape[0] - 1] = 1


def print_map():
    print(mapx)


def edit_tile(x, y, new_val):
    if check_collision(mapx[x, y]):
        return False
    mapx[x, y] = new_val
    return True


def check_collision(existing_val):
    if existing_val == 1 or existing_val == 2:
        return True
    return False
