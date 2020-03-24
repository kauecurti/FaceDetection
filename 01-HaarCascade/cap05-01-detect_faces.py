# Deteção de Faces
# Execute: python cap05-01-detect_faces.py --face cascades/haarcascade_frontalface_default.xml --image images/valley1.jpg

# Imports
import argparse
import cv2

# Argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="Caminho para o cascade")
ap.add_argument("-i", "--image", required=True, help="Caminho para a imagem")
args = vars(ap.parse_args())

# Carrega a imagem e converte para Grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Criando o detector de faces
detector = cv2.CascadeClassifier(args["face"])

# Detecção de Faces

# scaleFactor: quanto o tamanho da imagem é reduzido em cada escala de imagem. Esse valor é usado para criar a pirâmide de escala. 
# Para detectar rostos em escalas múltiplas na imagem (algumas faces podem estar mais próximas do primeiro plano e, portanto, maiores, 
# outras faces podem ser menores e em segundo plano, assim, por isso o uso de diferentes escalas). Um valor de 1,05 indica que estamos reduzindo 
# o tamanho da imagem em 5% em cada nível na pirâmide.
# Redimensiona um rosto maior para um menor. Mais lento se o valor for menor.

# minNeighbors: quantos vizinhos cada janela deve ter para que a área na janela seja considerada um rosto. 
# O classificador em cascata detectará várias janelas em torno de um rosto. Este parâmetro controla quantos retângulos (vizinhos) 
# precisam ser detectados para que a janela seja rotulada como um rosto.
# Valores altos: Menos detecções, porém apresenta maior qualidade

# minSize: uma tupla de largura e altura (em pixels) indicando o tamanho mínimo da janela. 
# Caixas menores do que este tamanho são ignoradas. É uma boa ideia começar com (30, 30) e ajustar a partir daí.

faceRects = detector.detectMultiScale(gray, scaleFactor=1.08, minNeighbors=8, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
print ("Encontrada(s) %d face(s)" % (len(faceRects)))

# Loop pelas faces e desenha um retângulo
for (x, y, w, h) in faceRects:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Print
cv2.imshow("Faces", image)
cv2.waitKey(0)




