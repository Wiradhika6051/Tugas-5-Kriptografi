import bcrypt
import base64
import os

def gensalt(rounds=None, prefix=None):
    rounds = rounds if rounds is not None else 12
    prefix = prefix if prefix is not None else b"2b"
    
    if prefix not in [b"2a", b"2b"]:
        raise ValueError("Supported prefixes are b'2a' or b'2b'")
    
    if not (4 <= rounds <= 31):
        raise ValueError("Invalid rounds")
    
    # Generate 16 random bytes for the salt
    salt = os.urandom(16)
    
    # Encode the salt using base64
    encoded_salt = base64.b64encode(salt).decode('utf-8')
    
    # Construct the salt string
    salt_str = f"${prefix.decode('utf-8')}${rounds:02}${encoded_salt}"
    
    return salt_str

# Example usage:
salt = gensalt(rounds=12, prefix=b"2b")
print(salt)
