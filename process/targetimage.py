import cv2 as cv
import numpy as np


class TargetImage:

    #properties
    image = None
    w = 0
    h = 0

    # constructor
    def __init__(self,image_path):
        self.template = cv.imread(image_path, cv.IMREAD_UNCHANGED)

        self.w = self.template.shape[1]
        self.h = self.template.shape[0]
    
    # find target image and return (x,y)points
    def find_in(self, canvas = None, threshold=0.5):

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, 
        # TM_CCORR, TM_CCORR_NORMED,
        # TM_SQDIFF, TM_SQDIFF_NORMED
        method = cv.TM_CCOEFF_NORMED
        result = cv.matchTemplate(canvas, self.template, method)

        matches = np.where(result >= threshold)
        points = list(zip(*matches[::-1]))
        adjusted_points = [(x + int(self.w/2), y + int(self.h/2)) for x, y in points]
        return adjusted_points