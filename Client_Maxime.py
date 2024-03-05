import socket
import tkinter as tk
import threading

# Fonction pour passer à l'étape suivante (saisie du message)
def next_step():
    name = name_entry.get()
    if name:
        client_socket.sendall(("Serveur es-tu là, tu vas bien, je m’appelle {} ?".format(name)).encode())
        name_entry.config(state='disabled')
        next_button.config(state='disabled')
        message_label.pack()
        message_entry.pack()
        send_button.pack()

# Fonction pour envoyer le message au serveur
def send_message():
    message = message_entry.get()
    if message:
        client_socket.sendall(message.encode())
        if message == "je sui a laeropor bisouuuu je manvol":
            client_socket.close()
            root.destroy()
        if root.winfo_exists():  # Vérifier si la fenêtre principale existe encore
            message_entry.delete(0, tk.END)

# Fonction pour recevoir et afficher les messages du serveur
def receive_message():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            response = data.decode()
            message_box.insert(tk.END, "Réponse du serveur : " + response + "\n")
        except OSError as e:
            print("Erreur de réception de données :", e)
            break

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Client")

# Configuration du socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 50025)
client_socket.connect(server_address)

# Création des widgets pour l'étape 1 (saisie du prénom)
name_label = tk.Label(root, text="Prénom :")
name_label.pack()

name_entry = tk.Entry(root, width=50)
name_entry.pack()

next_button = tk.Button(root, text="Suivant", command=next_step)
next_button.pack()

# Création des widgets pour l'étape 2 (saisie du message)
message_label = tk.Label(root, text="Message :")

message_entry = tk.Entry(root, width=50)

send_button = tk.Button(root, text="Envoyer", command=send_message)

message_box = tk.Text(root, height=10, width=50)
message_box.pack()

# Démarrer un thread pour recevoir les messages du serveur
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

# Boucle principale de l'interface graphique
root.mainloop()
