import cv2
import numpy as np

def findClickPositions(needleImgPath, haystackImg, threshold=0.8, debug_mode=None):

    needleImg = cv2.imread(needleImgPath, cv2.IMREAD_UNCHANGED)

    needle_w = needleImg.shape[1]
    needle_h = needleImg.shape[0]

    method = cv2.TM_CCOEFF_NORMED
    result = cv2.matchTemplate(haystackImg, needleImg, method)

    locations = np.where(result >= threshold)
    location = list(zip(*locations[::-1]))

    if(len(location) !=  0):
        return True



    # rectangles = []
    # if locations[0].size > 0:
    #     for loc in locations:
    #         rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]

    #         rectangles.append(rect)
    #         rectangles.append(rect)

    # else:
    #     print("No matches found.")

    # rectangles, weights = cv2.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

    # points = []
    # if len(rectangles):
    #     line_color = (0, 255, 0)
    #     line_type = cv2.LINE_4
    #     marker_color = (255, 0, 255)
    #     marker_type = cv2.MARKER_CROSS

    #     for (x, y, w, h) in rectangles:
    #         center_x = x + int(w/2)
    #         center_y = y + int(h/2)
    #         points.append((center_x, center_y))

    #         if debug_mode == 'rectangles':
    #             top_left = (x, y)
    #             bottom_right = (x + w, y + h)

    #             cv2.rectangle(haystackImg, top_left, bottom_right, color=line_color, lineType=line_type, thickness=2)
    #         elif debug_mode == 'points':
    #             cv2.drawMarker(haystackImg, (center_x, center_y), color=marker_color, markerType=marker_type, markerSize=40, thickness=2)
        
    # if debug_mode:
    #     cv2.imshow('Matches', haystackImg)

        
