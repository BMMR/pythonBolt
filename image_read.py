################# Part dedicated to view image
import cv2
import numpy as np


def read_process_version2(original,target):
    # Load the input image and the template image
    input_image = cv2.imread(original)
    template_image = cv2.imread(target)

    # Convert the images to grayscale
    input_image_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    template_image_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(input_image_gray, template_image_gray, cv2.TM_CCOEFF_NORMED)

    # Check if the template image appears in the input image
    threshold = 0.8
    loc = np.where(result >= threshold)

    if len(loc[0]) > 0:
        # Template image was found, draw a bounding box around it
        for pt in zip(*loc[::-1]):
            cv2.rectangle(input_image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    # Show the output image
    cv2.imshow('Output', input_image)
    cv2.waitKey(0)



def start_read_process(original,target):
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

        # Check if the maximum value is above a certain threshold
        if max_val > 0.8:
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



