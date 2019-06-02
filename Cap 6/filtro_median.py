import	cv2
imgOriginal	=	cv2.imread("mulher_pimenta.jpeg")
imgTratada	=	cv2.medianBlur(imgOriginal,	5)
cv2.imshow("Original",	imgOriginal)
cv2.imshow("Tratada",	imgTratada)
cv2.waitKey(0)
cv2.destroyAllWindows()
