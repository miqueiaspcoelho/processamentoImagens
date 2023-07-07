import cv2
import numpy as np

#leitura da imagem
img = cv2.imread('./images/A_blue_eye.jpg')
#mudando os dimensões
img = cv2.resize(img,(0,0), fx=0.3,fy=0.3)

img_blue = (img[:,:,0]) #canal azul
img_green = (img[:,:,1]) #canal verde
img_red = (img[:,:,2]) #canal vermelho

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #imagem em escala de cinza
width, height = img_red.shape #dimensões da imagens (linha, coluna)

img_bin = img_red.copy() #copiando a imagem, para depois substituir os valores dos pixels em posições especificas

#faz a binarização
pixel =0
for i in range(width):
    for j in range(height):
        pixel = img_red[i][j]
        if pixel > 95:
            img_bin[i][j] = 255
        else:
            img_bin[i][j] = 0

#Guardar os extremos da limiarização, para desenhar o círculo
positionsX=[]
positionsY=[]

#crescimento por região
element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1,1))
img_bin = cv2.erode(img_bin,element)

#Filtro para retirar ruídos
img_bin = cv2.medianBlur(img_bin,9)

#detecção de bordas
img_bin = cv2.Canny(img_bin,100,200)

#Percorrendo a imagem binarizada
for i in range(width):
    for j in range(height):
        pixel = img_red[i][j]
        if pixel == 0:
            positionsX.append(i)
            positionsY.append(j)

#definição de uma cor
color = (0,255,255)

#fazendo os círculos
cv2.circle(img, (positionsY[0],positionsX[0]), 70, color)
cv2.circle(img, (positionsY[0],positionsX[0]), 20, color)

#Exibição das imagens
result = np.hstack((img_blue,img_green,img_red))
cv2.imshow('Canais Separados',result)
cv2.imshow('Segmentado', img_bin)
cv2.imshow('Resultado', img)
cv2.waitKey(0)