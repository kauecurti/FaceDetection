# Face Swapping

# Execute: python cap05-10-face_swapping.py

# Imports
import cv2
import sys

# Classificador
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

# Carrega imagem e converte para Grayscale
img = cv2.imread('images/obama.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecta as faces
faces = face_cascade.detectMultiScale(gray, 1.1, 8)

# Imprime o comprimento das matrizes
if len(faces) != 2:
	sys.exit('Por favor insira uma imagem com EXATAMENTE 2 rostos!')

# Coordenadas das fotos
x1, y1, w1, h1 = faces[0]
x2, y2, w2, h2 = faces[1]

# Faces
face1 = img[y1:y1+h1, x1:x1+w1]
face2 = img[y2:y2+h2, x2:x2+w2]

# Resize
face1 = cv2.resize(face1, (w2, h2))
face2 = cv2.resize(face2, (w1, h1))

# Face 1
img[y1:y1+h1, x1:x1+w1] = face2

# Face 2 
img[y2:y2+h2, x2:x2+w2] = face1

# Print
cv2.imshow('Swap', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


