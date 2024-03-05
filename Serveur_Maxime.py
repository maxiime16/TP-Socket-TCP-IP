# Maxime DEVILLEPOIX
# https://pbs.twimg.com/ext_tw_video_thumb/1270816460072517635/pu/img/5CikunWIYoEewo4i.jpg

import socket
import datetime

# Initialisation du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Détermination du port en fonction de l'âge
port = 50000 + 25
while True:
    try:
        server_socket.bind(('localhost', port))
        break
    except OSError:
        port += 100

# Activation du mode écoute
server_socket.listen(1)

print("Le serveur est en écoute sur le port", port)

# Accepter une connexion
conn, addr = server_socket.accept()
print("Connexion établie avec", addr)

# Réception et renvoi du message au client
while True:
    data = conn.recv(1024)
    if not data:
        print("Le client a fermé la connexion.")
        break
    message = data.decode()
    print("Message reçu du client :", message)
    if message == "date":
        # Obtenir la date et l'heure actuelle
        current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Date et heure actuelles :", current_date_time)
        # Envoyer la date au client
        conn.sendall(current_date_time.encode())
    elif message == "je sui a laeropor bisouuuu je manvol":
        print("Le client a fermé la connexion.")
        break
    else:
        # Réponse par défaut si le message n'est pas reconnu
        response = message + "\nJe suis là !"
        conn.sendall(response.encode())

# Fermeture de la connexion
conn.close()
