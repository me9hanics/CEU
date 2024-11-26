from pathlib import Path
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

PROJECT_FOLDER = Path(__file__).parent.parent
CEU_PRIVATE_KEY_PATH = PROJECT_FOLDER / "ceu_key"  # Private key
ENCRYPTED_MESSAGE_FILE = PROJECT_FOLDER / "encrypted_message.bin"

with open(CEU_PRIVATE_KEY_PATH, "r", encoding="utf8") as key_file:
    ceu_private_key = RSA.import_key(key_file.read())

# Get message
with open(ENCRYPTED_MESSAGE_FILE, "rb") as f:
    encrypted_message_from_file = f.read()

private_key_cipher = PKCS1_OAEP.new(ceu_private_key)
decrypted_message = private_key_cipher.decrypt(encrypted_message_from_file)
print(f"Decrypted message: {decrypted_message.decode('utf-8')}")