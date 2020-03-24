# Detectando Faces em Vídeos

# Para detectar faces em arquivos de vídeo, exeucte: python cap05-06-detect_faces_video.py --video videos/video1.mp4
# Para detectar faces em ao vivo em sua webcam, exeucte: python cap05-06-detect_faces_video.py 

# Imports
import argparse
import imutils
import cv2

# Argumentos
ap = argparse.ArgumentParser()
#ap.add_argument("-f", "--face", required=True, help="Caminho para o arquivo Haar")
ap.add_argument("-v", "--video", help="Caminho para o arquivo de vídeo (opcional)")
args = vars(ap.parse_args())

# Criando o classificador
detector = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

# Se um caminho de vídeo não foi fornecido, usamos a referência para a webcam
if not args.get("video", False):
	camera = cv2.VideoCapture(0) # Caso você tenha mais de uma webcam, altere o valor que indica sua webcam: 1, 2, etc...

# Caso contrário, usamos a referência ao arquivo de vídeo
else:
	camera = cv2.VideoCapture(args["video"])

# Navegamos pelos frames do vídeo enquanto não for pressionada a tecla "q" no seu teclado
while True:
	# Obtém o frame corrente
	(grabbed, frame) = camera.read()

	# Se estivermos vendo um vídeo e não pegarmos um frame, chegamos ao final do vídeo
	if args.get("video") and not grabbed:
		break

	# Resize do frame, conversão para grayscale e detecção de faces no frame 
	frame = imutils.resize(frame, width=570)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faceRects = detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

	# Loop pelas faces e desenho dos retângulos
	for (x, y, w, h) in faceRects:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

	# Mostra o frame na nossa tela
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# Se a tecla 'q' for pressionada, interrompe o loop e para a execução do script
	if key == ord("q"):
		break

# Limpa a câmera e fecha a janela
camera.release()
cv2.destroyAllWindows()

