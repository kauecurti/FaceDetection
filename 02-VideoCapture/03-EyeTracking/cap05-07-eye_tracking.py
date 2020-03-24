# Eye Tracking

# Execute:

# Para Eye Tracking em um arquivo de vídeo:
# python cap05-07-eye_tracking.py --face cascades/haarcascade_frontalface_default.xml --eye cascades/haarcascade_eye.xml --video videos/video2.mov

# Para Eye Tracking a partir da webcam:
# python cap05-07-eye_tracking.py --face cascades/haarcascade_frontalface_default.xml --eye cascades/haarcascade_eye.xml

# Imports
import imutils
import argparse
import cv2
from eyetracker import EyeTracker

# Argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required = True, help = "Caminho para o face cascade")
ap.add_argument("-e", "--eye", required = True, help = "Caminho para o eye cascade")
ap.add_argument("-v", "--video", help = "Caminho para o arquivo de vídeo (opcional)")
args = vars(ap.parse_args())

# Cria o EyeTracker
et = EyeTracker(args["face"], args["eye"])

# Se um caminho de vídeo não foi fornecido, usa a webcam
if not args.get("video", False):
	camera = cv2.VideoCapture(0)

# Ou então carrega o vídeo fornecido
else:
	camera = cv2.VideoCapture(args["video"])

# Loop
while True:
	# Obtém o frame
	(grabbed, frame) = camera.read()

	# Se estivermos vendo um vídeo e não pegarmos um frame, chegamos ao final do vídeo
	if args.get("video") and not grabbed:
		break

	# Resize do frame e conversão para grayscale
	frame = imutils.resize(frame, width = 800)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detecta faces e olhos nos frames
	rects = et.track(gray)

	# Desliza as caixas sobre as faces e desenha os retângulos
	for rect in rects:
		cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)

	# Mostra os olhos e o rosto rastreados
	cv2.imshow("Tracking", frame)

	# Se a tecla 'q' for pressionada, interrompe o loop
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# Limpa a câmera e fecha qualquer janela aberta
camera.release()
cv2.destroyAllWindows()

