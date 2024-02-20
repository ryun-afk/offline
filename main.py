import cv2 as cv
import os
import debug

from windowcapture import WindowCapture
from targetimage import MatchTemplate

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize the WindowCapture class
capture = WindowCapture('Mabinogi')
# initialize templates
test = MatchTemplate('images/test.jpg')

while(True):
    # press 'q' with the output window focused for 1 ms to exit.
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    # for processing
    capture.update_screen()

    original = capture.image
    points = test.find_image(original)


    # for debug
    debug.mark_image(original,points)
    debug.show_image('original', original)
    

print('Done.')

