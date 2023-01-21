################# Part dedicated to view image
import cv2
import numpy as np

def selected_speed_read_image(select_target,fast_speed,slow_speed):

    # Ajusting speed of reading
    if select_target == "image/targets/tag_open_sc.png":  # process should be slowest
        set_speed = slow_speed  # Lower speed because of first loading
    if select_target == "image/targets/tag_enter_id_deploy.png":
        set_speed = slow_speed  # Lower speed because of first loading
    else:
        set_speed = fast_speed  # Higher speed to process the code of phone (not related with the internet connection)

    return set_speed


def selected_modes_of_working(select_mode):
    # code to be executed in thread
    if (select_mode == 1):
        target_open_scooter = ['image/targets/tag_enter_id.png', 'image/targets/tag_open_sc.png',
                               'image/targets/tag_return.png']
        target_exec = target_open_scooter

    if select_mode == 2:
        target_open_batt_scooter = ['image/targets/tag_enter_id.png', 'image/targets/tag_open_sc.png',
                                    'image/targets/tag_3_dots.png', 'image/targets/tag_replace_batt.png',
                                    'image/targets/tag_return.png']
        target_exec = target_open_batt_scooter

    if select_mode == 3:
        target_deploy_scooter = ['image/targets/tag_scan_deploy.png', 'image/targets/tag_enter_id_deploy.png',
                                    'image/targets/tag_start_deploy.png', 'image/targets/tag_dismiss_deploy.png',
                                    'image/targets/tag_close_deploy.png']
        target_exec = target_deploy_scooter


    return target_exec


def start_read_process(original,target,thresold):

    # Load the template and source images
    source = cv2.imread(original) #image from screen of the phone
    template = cv2.imread(target) # image that is the target

    try:
        # Convert the images to grayscale
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        source_gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
        # Find the location of the template in the source image
        result = cv2.matchTemplate(source_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        # Get the coordinates of the maximum value in the result
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print("max_val"+str(max_val))

        # Check if the maximum value is above a certain threshold
        if max_val > thresold:
            # If it is, draw a rectangle around the template in the source image
            h, w = template.shape[:2]
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(source, top_left, bottom_right, (0, 0, 255), 2)

        # Display the source image with the rectangle drawn on it
        cv2.imwrite('image/save.png', source)
    except:
        print("Error: Image dont read")

    try:
        # Point calculation of center
        top_leftF, bottom_rightF=calculation_point(top_left, bottom_right)
        print(top_leftF + bottom_rightF)
    except:
        print("Dont_found_the_target")
        top_leftF="0" # if dont find nothing
        bottom_rightF="0" # if dont find nothing

    return top_leftF, bottom_rightF

def calculation_point(top_left, bottom_right):
    pointX0= top_left[0] # Point X0
    pointX1= bottom_right[0] # point X1

    pointY0= top_left[1] # point Y1
    pointY1= bottom_right[1] # point Y2

    pointXF = int((pointX0+ pointX1)/2) # point X Final
    pointYF = int((pointY0+ pointY1)/2) # point X Final

    return str(pointXF),str(pointYF)



