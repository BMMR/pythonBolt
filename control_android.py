import subprocess

# Start the ADB server
def start_server():
    subprocess.run(["platform-tools/adb", "start-server"])

# Connect to the device
def connect(device):
    subprocess.run(['platform-tools/adb', 'connect', device])

# Click at the coordinates (100, 200)
def click_touch(x,y):
    subprocess.run(["platform-tools/adb", "shell", "input", "tap", x, y])

# Send a touch event to the device
def swipe_touch(x,y,x2,y2):
    subprocess.run(['platform-tools/adb', 'shell', 'input', 'touchscreen', 'swipe', x, y, x2, y2], check=True)

# Disconnect from the device
def end_server(device):
    subprocess.run(['platform-tools/adb', 'disconnect', device])