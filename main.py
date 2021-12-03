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
        devices = portReader.serial_ports_info()
        print(devices)
        
        psg.theme('Dark Blue 3')
        layout = [
          [psg.Text('Connected Ports')],
          [psg.InputCombo(values=(devices), size=(32, 5))],
          [psg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='left')],
          [psg.InputText(), psg.FileBrowse()],
          [psg.OK(), psg.Cancel()]
          ]
        window = psg.Window('Micropython Uploader', layout)
        event, values = window.read()

        window.close()

    def uploadFiles(self) -> None:
        pass


test = MicroPythoUploader()
test.createWindow()
