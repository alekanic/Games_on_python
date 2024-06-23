from utilis import randbool
from utilis import randcell
from utilis import randneighbour

# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-центр

CELL_TYPES = "🟩🌲🌊🚑🏣"
class Map:

    def generate_rivers(self, l):
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randneighbour(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bound(rx2, ry2):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def generate_forests(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def print_map(self):
        print("⬛️" * (self.w + 2))
        for row in self.cells:
            print("⬛", end='')
            for cell in row:
                if cell >= 0 and cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end='')
                # if cell == 0:
                #     print("🟩", end='')
                # elif cell == 1:
                #     print("🌲", end='')
                # elif cell == 2:
                #     print("🌊", end='')
                # elif cell == 3:
                #     print("🚑", end='')
                # elif cell == 4:
                #     print("🏣", end='')
            print("⬛️")
        print("⬛️" * (self.w + 2))

    def check_bound(self, x, y):
        if x < 0 or y < 0 or x > self.h or y > self.w:
            return False
        return True

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for i in range(h)]

tmp = Map(20, 10)
tmp.generate_forests(3, 8)
tmp.generate_rivers(8)
tmp.print_map()