import re
import serial


class tools():
    def __init__(self, baudrate: int, port: int, data_regex = re.compile(r'-?\d+')):
        self.port = port
        self.baudrate = baudrate
        self.regex = data_regex
        
    def connect(self) -> serial.Serial:
        status = True
        try:
            connection = serial.Serial(self.baudrate, self.port)
        except serial.SerialException:
            status = False
        return (status, connection)
    
    @classmethod
    def get_raw(cls, connection: serial.Serial)->str:
        return connection.readline().decode().strip()
    
    def get(self, connection: serial.Serial)->str:
        return self.regex.findall(tools.get_raw(connection))
    
    def send(self, message, connection: serial.SerialBase):
        connection.writelines(message)
