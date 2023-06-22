from helpers.lights.PyLightArduino import PyLightArduino
import helpers.lights.PortFinder as port_finder
import time
import colorsys

if __name__ == '__main__':
    port = port_finder.find_serial_number("757353033313517152D1")
    arduino = PyLightArduino(port)  # Replace with the correct serial port

    duration = 5  # Duration of the rainbow loop in seconds
    start_time = time.time()

    while time.time() - start_time < duration:
        elapsed_time = time.time() - start_time
        hue = int(elapsed_time / duration * 360) % 360

        # Convert HSV to RGB
        rgb = colorsys.hsv_to_rgb(hue / 360, 1.0, 1.0)
        r, g, b = [int(val * 255) for val in rgb]

        arduino.set_light_color(1, r, g, b)

    arduino.close()
