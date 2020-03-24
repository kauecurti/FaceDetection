# Classe para deteção dos olhos

# Imports
import cv2

class EyeTracker:
	def __init__(self, faceCascadePath, eyeCascadePath):
		# Carrega o detector de faces e olhos
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
		self.eyeCascade = cv2.CascadeClassifier(eyeCascadePath)

	def track(self, image):
		# Detecta faces na imagem e inicializa a lista de retângulos que contém as faces e os olhos
		faceRects = self.faceCascade.detectMultiScale(image, scaleFactor = 1.2, minNeighbors = 9, minSize = (40, 40), flags = cv2.CASCADE_SCALE_IMAGE)
		rects = []

		# Loop pelas faces detectadas
		for (fX, fY, fW, fH) in faceRects:
			# Extrai o ROI do rosto e atualiza a lista de faces detectadas
			faceROI = image[fY:fY + fH, fX:fX + fW]
			rects.append((fX, fY, fX + fW, fY + fH))
			
			# Detecta os olhos nas faces
			eyeRects = self.eyeCascade.detectMultiScale(faceROI, scaleFactor = 1.6, minNeighbors = 18, minSize = (20, 20), flags = cv2.CASCADE_SCALE_IMAGE)

			# Loop pelos olhos detectados
			for (eX, eY, eW, eH) in eyeRects:
				# Atualiza s lista de olhos detectados
				rects.append(
					(fX + eX, fY + eY, fX + eX + eW, fY + eY + eH))

		# Retorna os retângulos que representam as caixas ao redor dos rostos e dos olhos
		return rects