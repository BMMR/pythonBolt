import time

import cv2
import numpy as np
from flask import Flask, send_file
import os
import threading
import subprocess
from server import *
from control_android import *


# Funtions related to viewer software
def start_program():
    # code to be executed in thread 2
    print("Hello from start!")
    start()

################# Part dedicated to view image
def start():
    # Load the template and source images
    template = cv2.imread('image/target.png')
    source = cv2.imread('image/original.png')

    # Convert the images to grayscale
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    source_gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)

    # Find the location of the template in the source image
    result = cv2.matchTemplate(source_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Get the coordinates of the maximum value in the result
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the maximum value is above a certain threshold
    if max_val > 0.8:
        # If it is, draw a rectangle around the template in the source image
        h, w = template.shape[:2]
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(source, top_left, bottom_right, (0, 0, 255), 2)

    # coordinator of target
    print('top')
    print(top_left)

    print('bottom_right')
    print(bottom_right)

    # Display the source image with the rectangle drawn on it
    cv2.imwrite('image/save.png', source)


################# Control android
# Move the cursor to the specified coordinates
def move_cursor(x, y):
    run_adb_command(f"shell input tap {x} {y}")


def run_adb_command(command):
    adb_path = "platform-tools/adb"  # Replace this with the path to the ADB executable on your device
    full_command = f"{adb_path} {command}"
    output = os.popen(full_command).read()
    print(output)

################# Starting threads
def starting_threads():
    # create thread 1
    thread_1 = threading.Thread(target=start_server)

    # create thread 2
    thread_2 = threading.Thread(target=start_program)

    # start thread 1
    thread_1.start()

    # start thread 2
    thread_2.start()

################# Main Menu
if __name__ == '__main__':
    device = '19173cd4'  # Xiaomi phone

    variable=1


    if variable==1:
        #start_server()
        #time.sleep(4)
        #connect(device)
        #click_touch("200","300")
        end_server(device)


    else:
        print("Starting_threads")
        starting_threads()





