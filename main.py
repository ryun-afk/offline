import cv2 as cv
import os

from threading import Thread

from utility.keyboard import Keyboard
from utility.window import Window

from process.target import Target

os.chdir(os.path.dirname(os.path.abspath(__file__)))
test = Target('images/test.jpg')
raccoon = Target('images/raccoon.png')

game = Window('Mabinogi')
keyboard = Keyboard()
    
running = True

while(running):

    game.update_screen()
    Thread(keyboard.record_keyboard())

    # use grayscale to search faster
    debug_screen = game.image_grayscale
    test.find_locations(debug_screen)
    raccoon.find_locations(debug_screen)

    # set up to mark image for display
    debug_screen = game.image_original
    debug_screen = test.mark_locations(template=debug_screen)
    debug_screen = raccoon.mark_locations(template=debug_screen)
    game.debug(image = debug_screen)
    game.print_fps()
    
    # need better way to end loop
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


print('Done.')


