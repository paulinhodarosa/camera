import cv2
import socket
import pickle

port = 8084

#abre a webcam
cap = cv2.VideoCapture(0)

#verifica se a webcam foi aberta
if not cap.isOpened():
    raise IOError('Problema ao acessar a WebCam')

#objeto socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#associa o socket a uma porta
server.bind(('0.0.0.0', porta))
server.listen()

while True:
    print(f'*** Servidor aguardando porta {porta} ***')
    #Aguarda conexoes
    conn, addr = server.accept()
    print(f' == Conexão Recebida de {addr} ==')


    #Obtem e altera o tamanho
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)

    #empacota o frame
    dados = pickle.dumps(frame)

    #envia o pacote com o frame
    conn.send(dados)

    #fecha conexao
    conn.close()
    print('== Cliente Desconectado ==')
   
#     #Abre uma Janela e abre o frame
#     cv2.imshow('Input', frame)
#     #pega a tecla digitada (esc = sai do while)
#     c = cv2.waitKey(1)
#     if c == 27:
#         break
# #libera a camera e fecha as janelas
# cap.release()
# cv2.destroyAllWindows()
