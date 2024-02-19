import cv2 as cv
import os

from windowcapture import WindowCapture
from matchtemplate import MatchTemplate

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize the WindowCapture class
wincap = WindowCapture('Mabinogi')
potion = MatchTemplate('test.png')

while(True):
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    # processing
    wincap.update_screenshot()

    # for debugging/performance
    wincap.print_fps()

print('Done.')

