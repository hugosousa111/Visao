import cv2
import numpy as np

imagemo = cv2.imread("frutas.jpeg",0)

[totalLinhas,totalColunas] = imagemo.shape

matriz = cv2.getRotationMatrix2D((totalColunas / 2, totalLinhas / 2), 90, 1)
imagemRotacionada = cv2.warpAffine(imagemo, matriz, (totalColunas, totalLinhas))

cv2.imshow("Resultado", imagemRotacionada)

cv2.waitKey(0)
cv2.destroyAllWindows()