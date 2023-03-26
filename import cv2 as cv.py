import cv2 as cv
img = cv.imread("user.png")
cv.imshow('mra',img)
cv.waitKey(0)
cv.destroyAllWindows()
