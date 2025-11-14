def decrypt(ciphertext):
    for key in range(1, 26):
        decrypted_text = ""
        for char in ciphertext:
            if 'a' <= char <= 'z':
                shifted_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
                decrypted_text += shifted_char
            elif 'A' <= char <= 'Z':
                shifted_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
                decrypted_text += shifted_char
            else:
                decrypted_text += char
        print(f"{key}: {decrypted_text}")
def calculate(n):
    result = decrypt(n)
    return result
length ="Itnsl dtzw mtrjbtwp nx lwjfy bfd yt qjfws fsi rjrtwnej. Uqjfxj knsi ymj pjdbtwi tk ymnx jshwduynts yt knsnxm ktzwym jcjwhnxj"
calculate(length)