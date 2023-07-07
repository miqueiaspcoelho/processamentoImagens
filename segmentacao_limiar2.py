import cv2
import numpy as np

#fonte: https://offsouza.medium.com/segmentando-objetos-pela-cor-opencv-487d5181b473
#leitura da imagem e conversão para HSV
#min H = 0, min S = 219, min V = 87; max H = 179, max S = 255, max V = 162 (obtido por meio do código get_color.py)
#min H = 0, min S = 36, min V = 132; max H = 179, max S = 178, max V = 222
#min H = 0, min S = 149, min V = 145; max H = 179, max S = 195, max V = 203
#min H = 0, min S = 63, min V = 125; max H = 179, max S = 218, max V = 186
#leitura da imagem
#img = cv2.imread('./images/teste1.jpg')
img = cv2.imread('./images/teste4.jpg')
img = cv2.resize(img,(0,0), fx=0.5,fy=0.5)

#conversão para HSV, melhor para trabalhar na segmentação de cores
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#suavizando ruídos
blur = cv2.medianBlur(hsv ,7)

#definição do range, ou seja, tudo que vai ser considerado a cor a ser segmentada
#obtemos com o código get_color.py
#lower = np.array([0,219,87])
#upper = np.array([179,255,162])

lower = np.array([0,149,145])
upper = np.array([179,195,203])

#função de binarização
mask = cv2.inRange(blur, lower, upper)

#segmentando apenas a cor desejada (funciona como a remoção de algo não selecionado, igual ferramentas que tem no photoshop)
#estamos dando um merge na imagem com ela propria, porém, aplicando uma máscara
res = cv2.bitwise_and(img,img, mask= mask)            

#guarda extremos da imagem binarizada
positionsX =[]
positionsY =[]
width, heigth = mask.shape
for i in range(width):
    for j in range(heigth):
        if (mask[i][j]) == 255:
            positionsX.append(i)
            positionsY.append(j)

#extremos da imagem binarizada
a = max(positionsX)
b = min(positionsX)
c = max(positionsY)
d = min(positionsY)

#coordenadas das linhas horizontal e vertical
line_up_x = int(abs(d+c)/2)
line_up_y = b

line_down_y = a
line_down_x = line_up_x

line_left_x= d
line_left_y= int(abs(a+b)/2)

line_right_x = c
line_right_y = line_left_y

#retangulo
cv2.rectangle(img,(d,b),(c,a),(0,255,255),2)

#linhas
cv2.line(img, (line_up_x, line_up_y), (line_down_x, line_down_y), (0,0,0), 2)
cv2.line(img, (line_left_x, line_left_y), (line_right_x, line_right_y), (0,0,0), 2)

#exibe resultados
cv2.imshow('Mascara Utilizada',mask)
cv2.imshow('Original X Segmentacao', np.hstack([img,res]))
cv2.waitKey(0)