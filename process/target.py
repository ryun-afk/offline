import cv2 as cv
import numpy as np
import random

class Target:

    #properties
    target = None
    w = 0
    h = 0
    locations = []
    marker_color = (0,0,0)

    # constructor
    def __init__(self,image_path):
        self.target = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
        self.w = self.target.shape[1]
        self.h = self.target.shape[0]
        self.marker_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # find target image and return (x,y)points
    def find_locations(self, template = None, threshold=0.9):

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, 
        # TM_CCORR, TM_CCORR_NORMED,
        # TM_SQDIFF, TM_SQDIFF_NORMED
        method = cv.TM_CCOEFF_NORMED

        # returns points where target was found in template
        result = cv.matchTemplate(template, self.target, method)
        matches = np.where(result >= threshold)
        points = list(zip(*matches[::-1]))

        points = [(x + int(self.w/2), y + int(self.h/2)) for x, y in points]

        self.locations = points
    
    def mark_locations(self, template = None):
        img = template
        
        marker_type = cv.MARKER_CROSS
        marker_size = self.w
        if self.w < self.h:
            marker_size = self.h

        for (x, y) in self.locations:
            cv.drawMarker(img, (x, y),
                          color = self.marker_color, 
                          markerType = marker_type, 
                          markerSize = marker_size, 
                          thickness = 5)

        return img
        

        
        



