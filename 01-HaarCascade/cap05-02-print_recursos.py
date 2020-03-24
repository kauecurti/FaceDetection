# Imprime os recursos extraídos das imagens
# Execute: python cap05-02-print_recursos.py --image images/people1.jpg

# Imports
import argparse
import cv2

# Argumentos
ap = argparse.ArgumentParser()
# ap.add_argument("-f", "--face", required=True, help="Caminho para o cascade")
ap.add_argument("-i", "--image", required=True, help="Caminho para a imagem")
args = vars(ap.parse_args())

# Carrega a imagem e converte para Grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Criando o detector de faces
detector = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

# Detectando as faces
facesDetectadas = detector.detectMultiScale(gray, scaleFactor=1.08, minNeighbors=9, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
print ("\nEncontrada(s) %d face(s)" % (len(facesDetectadas)))
print("\nRecursos detectados: ")
print(facesDetectadas)
print("\n")

# Loop pelas faces e desenha um retângulo. As coordenadas definem onde o retângulo será desenhado, 
# sendo que x e y são as coordenadas e w e h são largura e altura
for (x, y, w, h) in facesDetectadas:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Print
cv2.imshow("Faces", image)
cv2.waitKey(0)








