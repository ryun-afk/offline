import cv2 as cv
import os

from threading import Thread

from capture.keyboard import KeyboardCapture
from capture.window import WindowCapture
from process.targetimage import TargetImage
from debug import Debug

os.chdir(os.path.dirname(os.path.abspath(__file__)))
test = TargetImage('img/test.jpg')


game = WindowCapture('Mabinogi')
keyboard = KeyboardCapture()
debug = Debug()

while(True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    Thread(game.update_screen())
    Thread(keyboard.record_keyboard())

    debug.mark_image(image = game.image, points = test.find_in(game.image))
    debug.show_image(img = game.image)
    debug.print_fps()

    

print('Done.')