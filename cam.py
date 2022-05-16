import cv2
import sockets
import pickle


#abre a webcam
cap = cv2.VideoCapture(0)

#verifica se a webcam foi aberta
if not cap.isOpened():
    raise IOError('Problema ao acessar a WebCam')

while True:
    #pega o frame e altera o tamanho
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    #Abre uma Janela e abre o frame
    cv2.imshow('Input', frame)
    #pega a tecla digitada (esc = sai do while)
    c = cv2.waitKey(1)
    if c == 27:
        break
#libera a camera e fecha as janelas
cap.release()
cv2.destroyAllWindows()
