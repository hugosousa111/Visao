import	cv2
imgOriginal	=	cv2.imread("estacionamento.jpeg")
imgTratada	=	cv2.bilateralFilter(imgOriginal,	9,	75,	75)
                           #imagem, filtro, sigma color e space
#sigma menor q 10 num faz nada
#sigma maior q 150 faz de mais

# maior o color maior sera a mistura das cores vizinhas
#maior o space,	maior sera a influencia do filtro nos pixels vizinhos

cv2.imshow("Original",	imgOriginal)
cv2.imshow("Tratada",	imgTratada)
cv2.waitKey(0)
cv2.destroyAllWindows()