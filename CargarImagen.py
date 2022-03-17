import numpy as np
import cv2 as cv
img = cv.imread('imagen.jpg')

print('filas:',img.shape[0] )
print('columnas:',img.shape[1] )
print('canales:',img.shape[2] )


cv.imshow('imagen',img) #muestra la imagen en una nueva ventana


cv.waitKey(0)
