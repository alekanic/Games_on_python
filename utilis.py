from random import randint as rand

def randbool(r, mxr):
    tmp = rand(0, mxr)
    return (tmp <= r)

def randcell(w, h):
    tw = rand(0, w - 1)
    th = rand(0, h - 1)
    return (th, tw)

def randneighbour(x, y):
    tmp = rand(0, 3)
    # 0 - наверх, 1 - направо, 2 - вниз, 3 - налево
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dx, dy = moves[tmp][0], moves[tmp][1]
    return (x + dx, y + dy)