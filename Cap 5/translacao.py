import cv2
import numpy as np

imagemo = cv2.imread("frutas.jpeg")

[totalLinhas,totalColunas] = imagemo.shape[:2]

matriz = np.float32([[1, 0, 100], [0, 1, 100]])
imagemDeslocada = cv2.warpAffine(imagemo, matriz, (totalColunas, totalLinhas))

cv2.imshow("Resultado", imagemDeslocada)

cv2.waitKey(0)
cv2.destroyAllWindows()