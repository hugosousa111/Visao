import	cv2
imgOriginal	=	cv2.imread("mulher.jpeg")
imgTratada	=	cv2.GaussianBlur(imgOriginal,	(3,3),	5) #sigma
cv2.imshow("Original",	imgOriginal)
cv2.imshow("Tratada",	imgTratada)
cv2.waitKey(0)
cv2.destroyAllWindows()