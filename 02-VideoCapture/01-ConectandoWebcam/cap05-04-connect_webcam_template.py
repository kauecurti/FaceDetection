# Conectando a webcam - Este é um template genérico para captura de vídeos pela webcam do seu computador
# Execute uma das duas opções: 

# Com um arquivo de vídeo como parâmetro: python cap05-04-connect_webcam_template.py --video videos/video1.mp4
# Sem um arquivo de vídeo como parâmetro (a detecção será feita a partir da webcam no seu computador): python cap05-04-connect_webcam_template.py

# Imports
import argparse
import imutils
import cv2
 
# Argumento
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="Caminho (opcional) para o vídeo")
args = vars(ap.parse_args())
 
# Se um caminho de vídeo não foi fornecido, usamos a referência para a webcam
if not args.get("video", False):
	camera = cv2.VideoCapture(0)  # Caso você tenha mais de uma webcam, altere o valor que indica sua webcam: 1, 2, etc...
 
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
 
	# Mostra o frame na nossa tela
	cv2.imshow("Frame", imutils.resize(frame, width=600))
	key = cv2.waitKey(1) & 0xFF
 
	# Se a tecla 'q' for pressionada, interrompe o loop e para a execução do script
	if key == ord("q"):
		break
 
# Limpa a câmera e fecha a janela
camera.release()
cv2.destroyAllWindows()



