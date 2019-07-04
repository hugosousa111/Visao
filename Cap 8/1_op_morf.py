import cv2
import numpy as np

#retangular,elipse e cruz.
print(cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)))
print(cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
print(cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)))

#criando um elemento estruturante
elementoEstruturante = np.matrix([
[0, 0, 1, 0, 0],
[0, 1, 1, 1, 0],
[1, 1, 1, 1, 1],
[0, 1, 1, 1, 0],
[0, 0, 1, 0, 0]
], np.uint8)

