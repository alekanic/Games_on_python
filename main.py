from map import Map
import time
import os

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 25
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
field.generate_forests(3, 8)
field.generate_rivers(8)

# то, какой кадр отрисовывается
tick = 1
while True:
    os.system("clear")
    print("TICK" + str(tick))
    field.print_map()
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
