import cv2 as cv
from time import time


class Debug:
    # properties
    loop_time = 0

    # constructor
    def __init__(self):
        self.loop_time = time()

    # print FPS
    def print_fps(self):
        print('FPS {}'.format(1 / (time() - self.loop_time)))
        self.loop_time = time()

    # display computer vision for debugging
    def show_image(self, name = 'Computer Vision',img = None, resize_factor = .4):
        image = cv.resize(img, (0, 0), fx=resize_factor, fy=resize_factor)
        cv.imshow(name, image)

    # draw points
    def mark_image(self, image = None, points = (0,0), marker_color = (0, 255, 0)):
        img = image
        marker_type = cv.MARKER_CROSS

        for (x, y) in points:
            # Draw the center point
            cv.drawMarker(img, (x, y), color = marker_color, markerType = marker_type, markerSize=20, thickness=1)

        return img