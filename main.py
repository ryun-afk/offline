import cv2 as cv
import os

from windowcapture import WindowCapture
from targetimage import TargetImage
from debug import Debug

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

mabi = WindowCapture('Mabinogi')
test = TargetImage('images/test.jpg')
debug = Debug()

while(True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    # for processing
    mabi.update_screen()
    original = mabi.image
    points = test.found_in(original)

    # for debug
    debug.mark_image(original, points)
    debug.show_image('original', original)
    debug.print_fps()
    

print('Done.')

