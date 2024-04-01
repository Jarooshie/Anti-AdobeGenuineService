import psutil
import wmi

c = wmi.WMI()

listener = c.Win32_Process.watch_for("creation")

PROCESS_NAME = 'AdobeGCClient.exe'

for proc in psutil.process_iter():
    proc.kill() if proc.name() == PROCESS_NAME else None
        
while True:
    new_process = listener()

    new_process.Terminate() if new_process.Caption == PROCESS_NAME else None