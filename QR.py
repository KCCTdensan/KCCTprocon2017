import os
import subprocess
def read_QR():
    print("ZBarを起動しています...")
    with os.popen("zbarcam.exe --raw") as f:
        print(f.read())