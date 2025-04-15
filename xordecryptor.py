def decrypt(encrypted_text, key):
    decrypted_text = ""
    
    for i in range(len(encrypted_text)):
        decrypted_text += chr((ord(encrypted_text[i]) - ord(key[i % len(key)]) + 256) % 256)

    return decrypted_text

encrypted = input("Enter the encrypted string: ")
key = input("Enter the decryption key: ")

result = decrypt(encrypted, key)
print("Decrypted message:", result)