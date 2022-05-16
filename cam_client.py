import cv2
import socket
import pickle

#porta e endereço do servidor
porta = 8084
dest = '192.168.246.66'
while True:
    #objeto socket
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #conecta ao servidor
    print(f'-- Conectando a {dest} --')
    cliente.connect((dest, porta))

    #recebe os dados do servidor
    data = []
    while True:
        pacote = cliente.recv(4096)
        if not pacote: break
        data.append(pacote)

    #desempacota o frame recebido
    frame = pickle.loads(b"".join(data))

    cliente.close()


    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break
cv2.destroyAllWindows()