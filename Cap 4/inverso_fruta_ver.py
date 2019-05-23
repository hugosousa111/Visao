import cv2
# Carregando imagem RGB e segmentando canais
imagem = cv2.imread("frutas.jpg")
azul, verde, vermelho = cv2.split(imagem)

# Combinando os três canais em uma única imagem
imagem = cv2.merge((azul, verde, vermelho))
cv2.imshow("Imagem1", imagem)


imagem = cv2.merge((verde,azul, vermelho))
cv2.imshow("Imagem2", imagem)

imagem = cv2.merge((vermelho, azul, verde))
cv2.imshow("Imagem3", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()
