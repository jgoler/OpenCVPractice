import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('Park', img)

cv.waitKey(0)