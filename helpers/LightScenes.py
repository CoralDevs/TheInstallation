from helpers.lights.PyLightDMX import *
import helpers.lights.PortFinder as port_finder
import time


class LightScenes():
    def __init__(self):
        self.dmx_port = port_finder.find_serial_number("VEGLIH5YA")
        self.dmx = PyLightDMX(self.dmx_port, refresh_rate=60)
        self.relative_uv_brightness = 1
        self.relative_rgb_brightness = 0.5
        self.percentages = [50, 50, 50]
        self.fake_uv_color = [95, 0, 255]
        # self.fake_uv_color = [0, 85, 255]

    def update_data(self, percentages):
        self.percentages = percentages

    def coral_1(self, percentage):
        self.dmx.set_zones(1, [255, 255, 255, 255], 100 - (percentage * self.relative_uv_brightness))  # UV
        self.dmx.set_rgb(8, self.fake_uv_color, percentage * self.relative_rgb_brightness)  # RGB
        self.dmx.set_rgb(11, self.fake_uv_color, percentage * self.relative_rgb_brightness)  # RGB

    def coral_2(self, percentage):
        self.dmx.set_zones(14, [255, 255, 255, 255], 100 - (percentage * self.relative_uv_brightness))  # UV
        self.dmx.set_rgb(21, self.fake_uv_color, percentage * self.relative_rgb_brightness)  # RGB

    def coral_3(self, percentage):
        self.dmx.set_zones(24, [255, 255, 255, 255], 100 - (percentage * self.relative_uv_brightness))  # UV
        self.dmx.set_rgb(31, self.fake_uv_color, percentage * self.relative_rgb_brightness)  # RGB

    def send(self):
        self.dmx.send()

    def loop2(self):
        delay = 1 / 60
        self.coral_1(self.percentages[0])
        self.coral_2(self.percentages[1])
        self.coral_3(self.percentages[2])
        self.dmx.send()
        # print(self.percentages)
        time.sleep(delay)

    def loop(self):
        pass

    def breathe_demo(self, duration=1):
        if duration <= 0 or duration > 10:
            print(f"LightScenes: Illegal speed value {duration}")
            return

        step = int(10 / duration)  # Inverse scaling for the step value

        for percentage in range(100, -1, -step):  # Decreasing range from 100 to 0
            self.coral_1(percentage)
            # print("Percentage:", percentage)
            self.dmx.send()

        for percentage in range(0, 100, step):  # Increasing range from 0 to 100
            self.coral_1(percentage)
            # print("Percentage:", percentage)
            self.dmx.send()