import cv2

#leitura da imagem
img = cv2.imread('./images/lana.png')
cv2.imshow('imagem',img)
cv2.waitKey(0)
