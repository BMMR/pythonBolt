################# Part dedicated to view image
import cv2


def start_read_process(original,target):
    # Load the template and source images

    #original='image/original.png'
    #target='image/target.png'

    template = cv2.imread(target)
    source = cv2.imread(original)

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
