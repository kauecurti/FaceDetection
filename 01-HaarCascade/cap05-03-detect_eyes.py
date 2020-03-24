# Deteção de Olhos
# Execute: python cap05-03-detect_eyes.py --image images/people1.jpg

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

# Cria um detector de olhos
detectorOlhos = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

# Detectando 
olhosDetectados = detectorOlhos.detectMultiScale(gray)

# Loop pelos olhos detectados e extrai as informações sobre os olhos
# Coordenadas: x e y
# Largura e altura: l e a
for (x, y, l, a) in olhosDetectados:

	# Obtém a imagem original
    imagem = cv2.rectangle(image, (x, y), (x + l, y + a), (0, 0, 255), 2)

    # Coleta a região dos olhos
    regiao = imagem[y:y + a, x:x + l]

    # Converte a região dos olhos para Grayscale
    # Os classificadores requerem as imagens em escala de cinza
    regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)

    # Detecta os olhos
    olhosDetectados = detectorOlhos.detectMultiScale(regiaoCinzaOlho, scaleFactor=1.1, minNeighbors=9)
    print(olhosDetectados)
    
    # Desenha os retângulos em torno dos olhos detectados
    for (ox, oy, ol, oa) in olhosDetectados:
        cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (255, 0, 255), 2)

# Print
cv2.imshow("Olhos", image)
cv2.waitKey(0)




