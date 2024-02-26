import cv2 as cv
import os

from threading import Thread

from util.keyboard import Keyboard
from util.window import Window

from process.processimage import ProcessImage

os.chdir(os.path.dirname(os.path.abspath(__file__)))
test = ProcessImage('images/test.jpg')
raccoon = ProcessImage('images/raccoon.png')

game = Window('Mabinogi')
keyboard = Keyboard()
    

while(True):
    # find better way to end loop
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    Thread(game.update_screen())
    Thread(keyboard.record_keyboard())

    test.find_locations(game.image_original)
    test.debug(game.image_original)

    game.debug()
    game.print_fps()


print('Done.')


