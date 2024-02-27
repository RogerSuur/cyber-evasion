import time
from cryptography.fernet import Fernet

def generate_key():
    """Generate and return a symmetric encryption key."""
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    """Encrypt the specified file."""
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    """Decrypt the specified file."""
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def increase_file_size(file_path, increase_by):
    """Increase file size by appending null bytes."""
    with open(file_path, 'ab') as file:
        file.write(b'\0' * increase_by)

def main():
    file_path = 'path_to_target_program.exe'
    key = generate_key()
    
    encrypt_file(file_path, key)
    
    increase_file_size(file_path, 101*1024*1024)
    
    example_int = 0
    for _ in range(100001):
        example_int += 1
    
    start_time = time.time()
    time.sleep(101) 
    if time.time() - start_time >= 101:
        decrypt_file(file_path, key)
    else:
        print("101 seconds have not elapsed.")

if __name__ == "__main__":
    main()
