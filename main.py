from helpers.LightScenes import LightScenes
import time
import threading


def light_scene_thread_function(this_light_scene):
    while True:
        this_light_scene.breathe_demo(duration=3)
        # this_light_scene.loop()


light_scene = LightScenes()
light_scene_thread = threading.Thread(target=light_scene_thread_function, args=(light_scene,))
light_scene_thread.start()
time.sleep(1)
light_scene.update_data([10, 10, 10])
