# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-центр

CELL_TYPES = "🟩🌲🌊🚑🏣"
class Map:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for i in range(h)]

    #def generate_rivers(self):

    #def generate_forests(self):

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
        else:
            return True

tmp = Map(10, 10)
tmp.cells[1][1] = 1
tmp.cells[2][2] = 2
tmp.print_map()