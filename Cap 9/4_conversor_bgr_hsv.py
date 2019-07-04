import cv2
import numpy as np
verdeRGB = np.uint8([[[0,255,0]]])
verdeHSV = cv2.cvtColor(verdeRGB, cv2.COLOR_BGR2HSV)
print verdeHSV

#verde
# Limite inferior:
# 60 - 20 = 40
tomClaro = np.array([40 100 100])
# Limite superior:
# 60 + 20 = 80
tomEscuro = np.array([80 255 255])