import cv2 as cv
import numpy as np

class MatchTemplate:

    #properties
    template = None
    w = 0
    h = 0

    # constructor
    def __init__(self,template_path):
        self.template = self.read_image_path(template_path)
        self.w = self.template.shape[1]
        self.h = self.template.shape[0]

    # read image path and filter
    def read_image_path(self, image_path = None):
        image = cv.imread(image_path, cv.IMREAD_UNCHANGED)
        return image
    
    # find target image and return (x,y)points
    def find_image(self, target = None, threshold=0.5):

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, 
        # TM_CCORR, TM_CCORR_NORMED,
        # TM_SQDIFF, TM_SQDIFF_NORMED
        method = cv.TM_CCOEFF_NORMED
        result = cv.matchTemplate(target, self.template, method)

        matches = np.where(result >= threshold)
        points = list(zip(*matches[::-1]))
        adjusted_points = [(x + int(self.w/2), y + int(self.h/2)) for x, y in points]
        return adjusted_points