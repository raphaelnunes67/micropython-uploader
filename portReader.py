import sys, glob, serial
from serial.tools import list_ports

class PortReader:
  
    def __init__(self) -> None:
        pass
      
    @staticmethod
    def serial_ports() -> list:
        """ Lists serial port names
            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        
        for port in list_ports.comports():
            print(port.manufacturer)
            print(port.device)
        
        return result
    
    @staticmethod
    def serial_ports_info() -> list:
        devices = []
        for port in list_ports.comports():
            # print(port.manufacturer)
            # print(port.device)
          
            device = str(port.device) + " - " + str(port.manufacturer)
            devices.append(device)
            
        return devices

if __name__ == '__main__':
    print(PortReader.serial_ports_info())
