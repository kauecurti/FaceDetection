# Tirando fotos pela webcam - Este é um template genérico para captura de fotos pela webcam do seu computador

# O script vai solicitar ao usuário um identificador e então vai tirar um foto com a webcam.
# Você deve pressionar a tecla q 15 vezes para capturar 15 fotos. Aumente o valor da variável numeroAmostras se precisar de mais fotos.
# Essas fotos podem ser usadas para o treinamento de um classificador.

# Execute o script assim: python cap05-05-tirando_fotos_webcam_template.py

# Imports
import cv2
  
# Classificador
classificador = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

# Abre a webcam para captura. Se tiver mais de uma webcam, mude o valor para 1, 2, etc...para especificar o número da webcam.
camera = cv2.VideoCapture(0)

# Contador
amostra = 1

# Número de amostras capturadas
numeroAmostras = 15

# Solicita ao usuário um id para identificar as fotos de maneira única.
# As fotos serão capturadas todas no mesmo tamanho.
id_user = input("Digite seu identificador de usuário (qualquer número entre 1 e 15: ")
largura, altura = 220, 220
print("Capturando Faces...")

# Captura das faces nas fotos
while (True):
	conectado, imagem = camera.read()
	imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
	facesDetectadas = classificador.detectMultiScale (imagemCinza, scaleFactor = 1.6, minSize = (80, 80))

	for (x, y, l, a) in facesDetectadas:
		cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

		# Pressione a tecla q 15 vezes para capturar 15 faces. O script vai encerar automaticamente após 15 execuções.
		# Altere o valor da variável numeroAmostras para capturar mais fotos.
		if cv2.waitKey(1) & 0xFF == ord('q'):
			imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))

			# A face é capturada e a imagem gravada em disco no diretório fotos.
			cv2.imwrite("fotos/pessoa." + str(id_user) + "." + str(amostra) + ".jpg", imagemFace)
			print("[foto " + str(amostra) + " capturada com sucesso]")
			amostra += 1

	cv2.imshow("Face", imagem)
	#cv2.waitKey(0)

	if (amostra >= numeroAmostras + 1):
		break

print("Faces Capturadas com Sucesso!")
camera.release()
cv2.destroyAllWindows()




