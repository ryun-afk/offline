import cv2 as cv
import os

from windowcapture import WindowCapture
from matchtemplate import MatchTemplate

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize the WindowCapture class
wincap = WindowCapture('Mabinogi')
# initialize templates
test = MatchTemplate('images/test.jpg')

while(True):
    # press 'q' with the output window focused for 1 ms to exit.
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    # for processing
    original_image = wincap.update_screenshot()
    points = test.find_image(original_image)


    # for debugging/performance
    wincap.draw_points(image = original_image, points = points, )
    wincap.show_image(name = 'marked', img = original_image)
    
    wincap.print_fps()

print('Done.')

