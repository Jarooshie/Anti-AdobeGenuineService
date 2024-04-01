import wmi

c = wmi.WMI()

listener = c.Win32_Process.watch_for("creation")

PROCESS_NAME = 'AdobeGCClient.exe'

for process in c.Win32_Process(name=PROCESS_NAME):
    result = process.Terminate()
    if result == 0:
        print(f"Process {PROCESS_NAME} terminated successfully.")
    else:
        print(f"Failed to terminate {PROCESS_NAME}.")

while True:
    new_process = listener()

    new_process.Terminate() if new_process.Caption == PROCESS_NAME else None