import time

import cv2
import numpy as np
from flask import Flask, send_file
import os
import threading
import subprocess
from server import *
from control_android import *
from image_read import *


# Funtions related to viewer software
def start_program():
    # code to be executed in thread 2
    print("Hello from start!")
    original='image/original.png'
    target='image/target.png'
    start_read_process(original, target)


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

    variable=0

    if variable==1:
        #start_server()
        #time.sleep(4)
        #connect(device)
        #click_touch("200","300")
        end_server(device)
    else:
        print("Starting_threads")
        starting_threads()





