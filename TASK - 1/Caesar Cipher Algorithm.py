def caesar_cipher(message, shift_key, encrypt=True):
    result = ""
    
    if not encrypt:
        shift_key = -shift_key
    
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - ascii_offset + shift_key) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
    
    return result

def main():
    print("Caesar Cipher Program Task 1")
    choice = input("Do you want to E(Encrypt) or D(Decrypt)? ").strip().lower()
    
    if choice not in ("e", "d"):
        print("Invalid choice! Please enter 'E' for encryption or 'D' for decryption.")
        return
    
    message = input("Enter your message: ")
    shift_key = int(input("Enter the shift value (integer): "))
    
    encrypt = choice == "e"
    result = caesar_cipher(message, shift_key, encrypt)  
    
    action = "Encrypted" if encrypt else "Decrypted"
    print(f"{action} Message: {result}")

if __name__ == "__main__":
    main()
print("TASK has been executed successfully")
