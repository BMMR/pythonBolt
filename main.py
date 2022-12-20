import threading
from server import *
from control_android import *
from image_read import *


# Funtions related to viewer software
def start_program():
    # code to be executed in thread 2
    print("Hello from start!")
    original='image/screenshot.png'
    target='image/tag_gmail.png'
    top_left, bottom_right=start_read_process(original, target)

    print("top_left")
    print(top_left)

    print("bottom_right")
    print(bottom_right)


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
        start_server()
        #time.sleep(4)
        #screen_shot()
        #connect(device)
        #click_touch("200","300")
        #end_server(device)
    else:
        print("Starting_threads")
        starting_threads()





