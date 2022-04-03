import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# Paint the image a certain color
#blank[200:300, 300:400] = 0, 0, 255
#cv.imshow('Green', blank)

cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2),
             (0, 255, 0),
             thickness=cv.FILLED)
cv.imshow('Rectangle', blank)
