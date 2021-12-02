import sys, subprocess
from portReader import PortReader

class MicroPythoUploader:
    def __init__(self) -> None:
        esptool_ver = subprocess.getstatusoutput('esptool.py version')[1]
        print(esptool_ver)

    @staticmethod
    def createWindow() -> None:
        import PySimpleGUI as psg
        portReader = PortReader()
        connecterd_ports = portReader.serial_ports()
        
        psg.theme('Dark Blue 3')
        layout = [
          [psg.Text('Connected Ports')],
          [psg.Listbox(values=(connecterd_ports), size=(30, 3))],
          [psg.OK(), psg.Cancel()]
          ]

        window = psg.Window('Get filename example', layout)
        event, values = window.read()

        window.close()

    def uploadFiles(self) -> None:
        pass


test = MicroPythoUploader()
test.createWindow()
