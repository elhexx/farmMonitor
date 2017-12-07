from serial import Serial
import serial.tools.list_ports


class ArduinoSerial():
    def __init__(self):
        self.serial_connection = Serial()
        self.is_connected = False
        self.port = self.auto_get_port()


    def auto_get_port(self):
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            port = str(p).split(' ')[0]
            try:
                with Serial(port, 9600, timeout=1) as ser:
                    ser.close()
                    return port
            except:
                return None

    def get_all_vals(self):
        with Serial(self.port, 9600, timeout=1) as ser:
            val = None
            while not val:
                ser.write('4'.encode())
                ser.flush()
                val = ser.readline()
            return val



    def close(self):
        if self.is_connected:
            self.serial_connection.close()
            self.is_connected = False
