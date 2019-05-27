import cv2

imagem = cv2.imread("folha-binaria.bmp", 0)
# 0 eh pra ler em tons de cinza
totalPixelsPreto = 0
totalPixelsBranco = 0

[linha,coluna] = imagem.shape
# linha, colunas e cores

print(linha)
print(coluna)
print(linha * coluna)

for x in range(0, linha):
  for y in range(0, coluna):
    if imagem[x,y] == 255:
      totalPixelsBranco += 1
    else:
      totalPixelsPreto += 1

print(totalPixelsBranco)
print(totalPixelsPreto)
print(totalPixelsBranco + totalPixelsPreto)