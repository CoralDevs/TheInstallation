from helpers.LightScenes import LightScenes
from helpers.dataset import DatasetHandler
import time
import threading


def light_scene_thread_function(this_light_scene):
    while True:
        # this_light_scene.breathe_demo(duration=3)
        this_light_scene.loop()


light_scene = LightScenes()
dataset_handler = DatasetHandler()
light_scene_thread = threading.Thread(target=light_scene_thread_function, args=(light_scene,))
light_scene_thread.start()

for year in range(1987, 2024):
    data_for_year = dataset_handler.get_data(year)
    light_scene.update_data(data_for_year)
    print(f"Year: {year} -> {data_for_year[1]}%")
    time.sleep(0.25)