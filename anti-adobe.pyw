import psutil
import wmi

c = wmi.WMI()

listener = c.Win32_Process.watch_for("creation")

PROCESS_NAME = 'AdobeGCClient.exe'

for proc in psutil.process_iter():
    if proc.name() == PROCESS_NAME:
        proc.kill()
        
while True:
    new_process = listener()
    for proc in psutil.process_iter():
        if proc.name() == PROCESS_NAME:
            proc.kill()

    print(f"New process started: {new_process.Caption}, PID: {new_process.ProcessId}")
    
