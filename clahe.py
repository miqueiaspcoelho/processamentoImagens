#fonte: https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
#algoritmo de equalização otimizado, retirado da documentação do opencv
import numpy as np
import cv2 as cv
img = cv.imread('./images/hist_img.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
# create a CLAHE object (Arguments are optional).
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv.imshow('clahe_2.jpg',cl1)
cv.waitKey(0)