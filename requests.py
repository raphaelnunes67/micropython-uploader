import requests


url = 'https://micropython.org/resources/firmware/esp32c3-20210902-v1.17.bin'
r = requests.get(url, allow_redirects=True)

open('esp32c3-20210902-v1.17.bin', 'wb').write(r.content)