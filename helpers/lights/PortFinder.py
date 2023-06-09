import serial.tools.list_ports
import warnings


class PortFinder(UserWarning):
    pass


def print_device_info_list():
    available_ports = list(serial.tools.list_ports.comports())
    if not available_ports:
        print("PortFinder: No COM ports available.")
    else:
        for port in available_ports:
            print(f"Device: {port.device}")
            print(f"Name: {port.name}")
            print(f"Description: {port.description}")
            print(f"Hardware ID: {port.hwid}")
            print(f"Manufacturer: {port.manufacturer}")
            print(f"Product: {port.product}")
            print(f"Serial Number: {port.serial_number}")
            print()


def find_serial_number(serial_no):
    available_ports = list(serial.tools.list_ports.comports())
    if not available_ports:
        warnings.warn("No COM ports available.", PortFinder, stacklevel=2)
        return -1
    else:
        for port in available_ports:
            if port.serial_number == serial_no:
                print(f"PortFinder: Device {serial_no} found in port {port.device}")
                return port.device
    warnings.warn(f"Device with Serial No. {serial_no} not found!", PortFinder, stacklevel=2)
    return -1
