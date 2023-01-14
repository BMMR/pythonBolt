import subprocess
import time

# Start server abd
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

#take screen shot
def screen_shot(sleep_time):
    time.sleep(sleep_time)
    #This path my need to change in other computers change
    working_path="C:\\Users\Bruno\Desktop\projetos em curso\Bolt\pythonBolt\image"
    # Capture the screen of the device and save the image to a file on the SD card
    subprocess.run(["platform-tools/adb", "shell", "screencap", "-p", "/sdcard/screenshot.png"])
    # Copy the screenshot file from the device to the current directory on the computer
    subprocess.run(["platform-tools/adb", "pull", "/sdcard/screenshot.png", working_path])

# Disconnect from the device
def end_server(device):
    subprocess.run(['platform-tools/adb', 'disconnect', device])

# Select the screen point
def select_and_insert_text(x,y):
    # Tap on the point (100, 200) on the screen
    subprocess.run(['platform-tools/adb', 'shell', 'input', 'touchscreen', 'tap', x, y])

# Insert text in screen
def insert_text(col):
    # Type the text "Hello World"
    # Subprocess to run
    subprocess.run(['platform-tools/adb', 'shell', 'input', 'text', col])




