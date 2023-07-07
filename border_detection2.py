import cv2
import numpy as np

#faz a binarização invertida
def bin_inv(img, limiar):
    img_bin = img.copy()
    width, height = img.shape
    for i in range(width):
        for j in range(height):
            if img_gray[i][j] > limiar:
                img_bin[i][j] = 0
            else:
                img_bin[i][j] = 255
    return img_bin

#leitura da imagem
img = cv2.imread('./images/A_blue_eye.jpg')

#mudando os dimensões
img = cv2.resize(img,(0,0), fx=0.3,fy=0.3)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #imagem em escala de cinza
img_gray = cv2.GaussianBlur(img_gray, (19, 19),0)#removendo ruídos

#encontrar pupila
limiar_pupila = 50
img_bin_pupila = bin_inv(img_gray, limiar_pupila)
img_canny_pupila = cv2.Canny(img_bin_pupila, 0,255)
contours_pupila, heirarchies_pupila = cv2.findContours(img_canny_pupila, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours_pupila = max(contours_pupila, key=cv2.contourArea)
cv2.drawContours(img, contours_pupila, -1, (255, 0, 0), 3)

#encontrar iris
limiar_iris = 130
img_bin_iris = bin_inv(img_gray, limiar_iris)
img_canny_iris = cv2.Canny(img_bin_iris, 0,255)
contours_iris, heirarchies_iris = cv2.findContours(img_canny_iris, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours_iris = max(contours_iris, key=cv2.contourArea)
cv2.drawContours(img, contours_iris, -1, (0, 255, 0), 3)

#exibindo imagens
result1=np.hstack((img_bin_pupila,img_bin_iris))
result2=np.hstack((img_canny_pupila,img_canny_iris))
result = np.vstack((result1,result2))
cv2.imshow('Pupila x Iris - binarizadas - Pupila x Iris - contornos', result)
cv2.imshow('Segmentado', img)

cv2.waitKey(0)