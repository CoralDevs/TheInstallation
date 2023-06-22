import serial
import time


class PyLightArduino:
    def __init__(self, port, baudrate=9600):
        self.ser = serial.Serial(port, baudrate)
        print("PyLightArduino: Waiting 2s for serial communication")
        time.sleep(2)  # Wait for the Arduino to establish serial connection

    def set_light_color(self, light_number, r, g, b):
        if light_number not in [1, 2, 3]:
            raise ValueError("Invalid light number. Only 1, 2, or 3 are allowed.")

        # Format the command as 'L<light_number><rrr><ggg><bbb>'
        command = 'L{}{:03d}{:03d}{:03d}'.format(light_number, r, g, b)

        # Send the command to the Arduino
        self.ser.write((command + "\n").encode())

        time.sleep(0.02)

        print(command)

    def close(self):
        self.ser.close()
