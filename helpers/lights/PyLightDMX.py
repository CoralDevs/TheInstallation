import serial
import time
import numpy as np
import warnings


class PyLightDMXWarning(UserWarning):
    pass


class PyLightDMX:
    def __init__(self, port='COM3', max_channels=512, refresh_rate=20):
        self.serial_connection = serial.Serial(port, baudrate=250000, bytesize=8, stopbits=2)

        self.max_channels = max_channels
        self.data = np.zeros([self.max_channels + 1], dtype='uint8')
        self.frame_delay = 1 / (refresh_rate / 1000)

        #  Timing description: https://www.freestylersupport.com/wiki/dmx_basics:dmx_timing
        self.Break_us = 88.0
        self.MAB_us = 8.0

    def set_refresh_rate(self, refresh_rate):
        self.frame_delay = 1 / (refresh_rate / 1000)

    def set_data(self, channel, value):
        self.data[channel] = value

    def set_data_list(self, data_list):
        try:
            for channel, value in data_list:
                self.set_data(channel, value)
        except Exception as e:
            warnings.warn(f'{e}. List must contain tuples of (id, data)!', PyLightDMXWarning, stacklevel=2)

    def send(self):
        self.serial_connection.break_condition = True
        time.sleep(self.Break_us / 1000000.0)

        self.serial_connection.break_condition = False
        time.sleep(self.MAB_us / 1000000.0)

        self.serial_connection.write(bytearray(self.data))

        time.sleep(self.frame_delay / 1000.0)  # between 0 - 1 sec

    def send_zeros(self):
        self.data = np.zeros([self.max_channels + 1], dtype='uint8')
        self.send()

    def set_rgb(self, channels, values, brightness=100):
        # If given a single value, return a list of 3 channels:
        if isinstance(channels, int):
            channels = list(range(channels, channels + 3))  # E.g. if given 2, assign [2, 3, 4]
        elif not isinstance(channels, list) or not len(channels) == 3:
            warnings.warn(
                "You are passing an invalid channel parameter. It should be an integer or list of 3 integers.",
                PyLightDMXWarning, stacklevel=2)
            return

        # Check if values is a list of 3 integers between 0 and 255. Else set values to [0, 0, 0]
        if not (isinstance(values, list) and len(values) == 3 and all(
                isinstance(x, int) and 0 <= x <= 255 for x in values)):
            values = [0, 0, 0]

        # Adjust values based on brightness parameter
        values = [int(value * brightness / 100) for value in values]

        for channel, value in zip(channels, values):
            self.set_data(channel, value)

    def __del__(self):
        self.serial_connection.close()
        print('PyLightDMX: Closed serial connection')
