import cv2 as cv
import numpy as np

class MatchTemplate:

    #properties
    template = None
    w = 0
    h = 0

    def __init__(self,template_path):
        self.template = self.read_image_path(template_path)

        cv.imshow('Computer Vision', self.template)
        self.w = self.template.shape[1]
        self.h = self.template.shape[0]

    # read image path and filter
    def read_image_path(self, image_path = None):
        image = cv.imread(image_path, cv.IMREAD_UNCHANGED)
        return image
    
    # find target image and return (x,y)points
    def find_image(self, target_image, threshold=0.5, debug_mode=None):

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        method = cv.TM_CCOEFF_NORMED
        result = cv.matchTemplate(self.original_image, target_image, method)

        # Get the all the positions from the match result that exceed our threshold
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        #print(locations)

        # You'll notice a lot of overlapping rectangles get drawn. We can eliminate those redundant
        # locations by using groupRectangles().
        # First we need to create the list of [x, y, w, h] rectangles
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), target_w, target_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)
        # Apply group rectangles.
        # The groupThreshold parameter should usually be 1. If you put it at 0 then no grouping is
        # done. If you put it at 2 then an object needs at least 3 overlapping rectangles to appear
        # in the result. I've set eps to 0.5, which is:
        # "Relative difference between sides of the rectangles to merge them into a group."
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

        points = []
        if len(rectangles):
            # Loop over all the rectangles
            for (x, y, w, h) in rectangles:
                # Save the points
                points.append((center_x, center_y))

                if debug_mode == 'rectangles':
                    # Determine the box position
                    top_left = (x, y)
                    bottom_right = (x + w, y + h)
                    line_color = (0, 255, 0)
                    line_type = cv.LINE_4
                    # Draw the box
                    cv.rectangle(self.original_image, 
                                 top_left, bottom_right, 
                                 color=line_color, lineType=line_type, 
                                 thickness=2)
                elif debug_mode == 'points':
                    # Determine the center position
                    center_x = x + int(w/2)
                    center_y = y + int(h/2)
                    marker_color = (255, 0, 255)
                    marker_type = cv.MARKER_CROSS
                    # Draw the center point
                    cv.drawMarker(self.original_image, 
                                  (center_x, center_y), 
                                  color=marker_color, markerType=marker_type, 
                                  markerSize=40, thickness=2)
        return points