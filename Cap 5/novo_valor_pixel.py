import	cv2
imagem	=	cv2.imread("frutas.jpeg")
print	imagem[150,150]
imagem[150,150]	=	[255,255,255]	
print(imagem[150,150])

cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()