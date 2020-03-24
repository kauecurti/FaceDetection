# Pesquisando uma imagem dentro de outra imagem

# Execute: python cap05-09-encontrando_imagens.py

import cv2
import numpy as np

# Carrega a inagem e converte para Grayscale
image = cv2.imread('images/WaldoBeach.jpg')
cv2.imshow('Onde está Waldo?', image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Carrega a imagem que queremos buscar na outra imagem
template = cv2.imread('images/waldo.jpg',0)

# Faz o match
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Cria a Bounding Box
top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv2.rectangle(image, top_left, bottom_right, (0,0,255), 5)

# Mostra a imagem
cv2.imshow('Onde está Waldo?', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


