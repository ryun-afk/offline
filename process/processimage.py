import cv2 as cv
import numpy as np

class ProcessImage:

    #properties
    image_original = None
    w = 0
    h = 0
    locations = []

    # constructor
    def __init__(self,image_path):
        self.image_original = cv.imread(image_path, cv.IMREAD_UNCHANGED)
        self.w = self.image_original.shape[1]
        self.h = self.image_original.shape[0]
    
    # find target image and return (x,y)points
    def find_locations(self, template = None, threshold=0.9):

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, 
        # TM_CCORR, TM_CCORR_NORMED,
        # TM_SQDIFF, TM_SQDIFF_NORMED
        method = cv.TM_CCOEFF_NORMED
        target = self.image_original.astype(template.dtype)
        result = cv.matchTemplate(template, target, method)

        matches = np.where(result >= threshold)
        points = list(zip(*matches[::-1]))
        
        self.points = [(x + int(self.w/2), y + int(self.h/2)) for x, y in points]
    
    def debug(self, template = None, marker_color = (0, 255, 0), name = 'searching',resize_factor = .4):
        img = template
        marker_type = cv.MARKER_CROSS

        for (x, y) in self.points:
            # Draw the center point
            cv.drawMarker(img, (x, y), color = marker_color, markerType = marker_type, markerSize=20, thickness=1)

        cv.imshow('search', cv.resize(img, (0, 0), fx=resize_factor, fy=resize_factor))
        

        
        



