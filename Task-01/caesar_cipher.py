def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

# 👇 User Input
msg = input("Enter your message: ")
shift_val = int(input("Enter shift value: "))

enc = encrypt(msg, shift_val)
print(f"Encrypted: {enc}")

dec = decrypt(enc, shift_val)
print(f"Decrypted: {dec}")
