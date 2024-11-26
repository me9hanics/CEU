from pathlib import Path
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

PROJECT_FOLDER = Path(__file__).parent
CEU_PUBLIC_KEY_PATH = PROJECT_FOLDER / "ceu_key.pub"  # Public key
with open(CEU_PUBLIC_KEY_PATH, "r", encoding="utf8") as key_file:
    ceu_public_key = RSA.import_key(key_file.read())

# Encrypt message
message = "Hi, I am Student 12345"
short_secret_message = message.encode("utf-8")
public_key_cipher = PKCS1_OAEP.new(ceu_public_key)
encrypted_message = public_key_cipher.encrypt(short_secret_message)

# Save encrypted message
ENCRYPTED_MESSAGE_FILE = PROJECT_FOLDER / "encrypted_message.bin"
with open(ENCRYPTED_MESSAGE_FILE, "wb") as f:
    f.write(encrypted_message)