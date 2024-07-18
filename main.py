import clouds
from map import Map
from clouds import Clouds
import time # библиотека чтобы вызвать time.sleep()
import os # для очистки консоли
from helicopter import Helicopter as Helico
from pynput import keyboard
import json

# объявляем константы
TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
CLOUDS_UPDATE = 200
MAP_W, MAP_H = 20, 10
tick = 1

field = Map(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)

MOVES = {"w": (-1, 0), "d": (0, 1), "s": (1, 0), "a": (0, -1)}
# f - save, g - recover

def process_key(key):
    global helico, tick, clouds, field
    c = key.char.lower()
    # обработка движений вертолета
    if c in MOVES.keys():
        dx = MOVES[c][0]
        dy = MOVES[c][1]
        helico.move(dx, dy)
    # сохранение игры
    if c == 'f':
        data = {"helicopter": helico.export_data(),
                "clouds": clouds.export_data(),
                "field": field.export_data(),
                "data": tick}
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    # загрузка игры
    if c == 'g':
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            helico.import_data(data["helicopter"])
            tick = data["tick"] or 1
            field.import_data(data["field"])
            clouds.import_data(data["clouds"])

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key,)
listener.start()

while True:
    os.system("clear") #cls
    field.process_helicopter(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    print("TICK" + str(tick))  # отрисовываем номер кадра, который сейчас отрисовыватеся
    tick += 1
    time.sleep(TICK_SLEEP) # ограничение частоты отрисовки кадров
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires(helico)
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update_clouds()
