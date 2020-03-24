# Traçando um Sketch (esboço) de um vídeo a partir da webcam

# Execute: python cap05-08-sketch.py

# Imports
import cv2
import numpy as np

# Função para gerar o Sketch
def sketch(image):
    # Converte para Grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplica Guassian Blur para suavizar a imagem
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    # Extrai as bordas
    canny_edges = cv2.Canny(img_gray_blur, 10, 90)
    
    # Binarização e inversão da imagem
    ret, mask = cv2.threshold(canny_edges, 100, 355, cv2.THRESH_BINARY_INV)
    return mask


# Inicializa a webcam e cap é o objeto fornecido pelo VideoCapture. 
# Ele contém um booleano indicando se ele foi bem sucedido (ret) Ele também contém as imagens coletadas da webcam (frame).
cap = cv2.VideoCapture(0)

# Loop
while True:
    ret, frame = cap.read()
    cv2.imshow('Live Sketcher', sketch(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# Release da camera e fecha as janelas
cap.release()
cv2.destroyAllWindows()     