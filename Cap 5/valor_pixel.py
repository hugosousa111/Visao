import	cv2
imagem	=	cv2.imread("frutas.jpeg")
valorPixel	=	imagem[150,150]
print(valorPixel)

#lendo so um canal
valorPixel	=	imagem[150,150,1]
print(valorPixel)