def caesar_cipher_encryption(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  # Cek apakah karakter adalah huruf
            # Menentukan apakah huruf tersebut kapital atau tidak
            start = ord('A') if char.isupper() else ord('a')
            # Geser huruf sesuai dengan pergeseran (shift)
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text += encrypted_char
        else:
            # Jika karakter bukan huruf (misal spasi), langsung tambahkan ke hasil
            encrypted_text += char
            
    return encrypted_text

# Kunci yang diberikan
key = "RISMA"
shift = 3

# Enkripsi kunci "RISMA"
encrypted_key = caesar_cipher_encryption(key, shift)
print(f"Kunci Enkripsi: {encrypted_key}")
