def atbash(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr(ord('z') - (ord(char) - ord('a'))))
        elif 'A' <= char <= 'Z':
            result.append(chr(ord('Z') - (ord(char) - ord('A'))))
        else:
            result.append(char)
    return ''.join(result)


if __name__ == "__main__":
    encrypted = "krxlXGU{zgyzhs_xizxp_xz00558y}"
    decrypted = atbash(encrypted)

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
