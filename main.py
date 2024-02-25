import cv2 as cv
import os
import time

from threading import Thread

from util.keyboard import KeyboardCapture
from util.window import WindowCapture
from util.debug import Debug

from process.targetimage import TargetImage


os.chdir(os.path.dirname(os.path.abspath(__file__)))
test = TargetImage('images/test.jpg')


game = WindowCapture('Mabinogi')
keyboard = KeyboardCapture()
debug = Debug()


while(True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    Thread(game.update_screen())
    Thread(keyboard.record_keyboard())

    #points = test.image_locations(canvas = game.image)
    debug.show_image(img = game.image)
    debug.print_fps()

    

print('Done.')