# Importar los modulos
import cv2
from cvzone.HandTrackingModule import HandDetector


# Inicializar detector de manos con alta confianza y máximo 2 manos
detector = HandDetector(detectionCon=0.8, maxHands=2)


# Abrir cámara (0 = cámara integrada)
video = cv2.VideoCapture(0)

# Se verifica si la cámara se abrió correctamente
if not video.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: No se pudo leer el frame de la cámara.")
        break

    # Detectar las manos y se obtiene la imagen con las anotaciones
    hands, img = detector.findHands(frame)

    # Se muestra la imagen con las manos detectadas
    cv2.imshow("Frame", img)

    # Se espera 1ms y se desea cerrar el programa se presionan 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Se libera la cámara y cerrar ventanas
video.release()
cv2.destroyAllWindows()