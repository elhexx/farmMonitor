from serial import Serial


class ArduinoSerial():
    def __init__(self):
        self.serial_connection = Serial()
        self.is_connected = False

    def get_temp(self):

        with Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
            val = None
            while not val:
                ser.write('1'.encode())
                ser.flush()
                val = ser.readline()
            return val


    def get_Humd(self):
        with Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
            val = None
            while not val:
                ser.write('2'.encode())
                ser.flush()
                val = ser.readline()
            return val


    def close(self):
        if self.is_connected:
            self.serial_connection.close()
            self.is_connected = False