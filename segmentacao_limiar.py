import cv2
import numpy as np

#leitura da imagem
img = cv2.imread('./images/WhiteHorse.jpg')

#filtro para remoção de ruídos
img_blur = cv2.blur(img,(2,2))

#imagem em escala de cinza
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

#copia para depois substituição dos pixels
img_seg = img_gray.copy()

width, height = img_gray.shape #dimensões da imagens 
threshold = 170 #limiar para segmentação
pixel_value=0 #valor do pixel, usado para calculo do histograma
positionsX =[] #guarda extremos da segmentação em X
positionsY =[] #guarda extremos da segmentação em X

#binarização
for i in range(width):
    for j in range(height):
        pixel_value = img_gray[i][j]
        if pixel_value > threshold:
            img_seg[i][j] = 255
            positionsX.append(i)
            positionsY.append(j)
        else:
            img_seg[i][j] = 0

#obtendo máximos e mínimos para depois desenhar o retangulo ao redor da imagem
a = max(positionsX)
b = min(positionsX)
c = max(positionsY)
d = min(positionsY)

#retangulo
cv2.rectangle(img,(d,b),(c,a),(255,255,255),2)

#exibindo os resultados
result = np.hstack((cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),img_seg))
cv2.imshow('Antes X Depois',result)
cv2.waitKey(0)
