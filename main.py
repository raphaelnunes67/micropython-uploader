import sys
import subprocess
from portReader import PortReader
import requests


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
        psg.theme('Default')
        frame_firmware_layout = [
            [psg.InputText(size=(53, 1)), psg.FileBrowse(button_text="...", button_color="#306998",
                file_types=(('dfu', '*.dfu'), ('bin', '*.bin')))],
            [psg.Text(size=(18,1)), psg.Button('Upload Firmware', button_color="#306998")]
        ]
        
        frame_script_layout = [
            [psg.InputText(size=(53, 1)), psg.FileBrowse(button_text="...", button_color="#306998")],
            [psg.Text(size=(18,1)), psg.Button('Upload Files', button_color="#306998")]
        ]
        
        layout = [

            [psg.Frame('New Firmware Path', frame_firmware_layout)],
            [psg.Frame('Upload Files', frame_script_layout)],

            [psg.Text('New Firmware Path', size=(20, 1),
                      auto_size_text=False, justification='left')],
            [psg.InputText(size=(53, 1)), psg.FileBrowse()],
            [psg.Text('Connected Ports')],
            [psg.InputCombo(values=(devices), size=(32, 5)),
             psg.Button('Erase Flash')],
            [psg.Multiline(
                default_text='This is the default Text should you decide not to type anything', size=(60, 10))],
            [psg.Text('', size=(20, 1)), psg.Button('EXIT')]
        ]
        window = psg.Window('Micropython Uploader', layout)
        event, values = window.read()

        window.close()

    def uploadFiles(self) -> None:
        pass


test = MicroPythoUploader()
test.createWindow()