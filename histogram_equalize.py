#imports
import cv2
import numpy as np

#leitura da imagem
img = cv2.imread('./images/hist_img.jpg') #imagem original
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #imagem em escala de cinza
img_equalize = img_gray.copy() #imagem que será equalizada

#variáveis
width, height = img_gray.shape #dimensões da imagens 
H = [0] * 256 #histograma
equalize_values = [] #valores equalizados de histograma
frequency = 0 #frequencia
frequency_sum = 0 #frequencia acumulada
qt_pixels = width * height #quantidade de pixels
pixel_value=0 #valor do pixel, usado para calculo do histograma
max_value = 255 #valores vão de 0 a 255

#histograma
for i in range(width):
    for j in range(height):
        pixel_value = img_gray[i][j]
        H[pixel_value] +=1

#histograma acumulado
for value in H:
    frequency = value / qt_pixels
    frequency_sum += frequency #acumulado
    equalize_values.append(round(frequency_sum * max_value))

#imagem equalizada
pixel_to_replace =0
for i in range(width):
    for j in range(height):
        pixel_to_replace = img_gray[i][j]
        img_equalize[i][j] = equalize_values[pixel_to_replace]
result = np.hstack((img_gray,img_equalize))

#imagens
cv2.imshow('Original', img)
cv2.imshow('Antes X Depois', result)
cv2.waitKey(0)
