# Read encrypted flag
encrypted = "picoCTF{w1{1wq8cFF:7Rkr}"

decrypted = ""

for i in range(len(encrypted)):
    char = encrypted[i]
    
    if i < 8:
        # First 8 chars: unchanged
        decrypted += char
    elif 8 <= i <= 22:
        # Reverse the transformation
        if i % 2 == 0:
            # Even: was +5, reverse with -5
            decrypted += chr(ord(char) - 5)
        else:
            # Odd: was -2, reverse with +2
            decrypted += chr(ord(char) + 2)
    else:
        # After index 22: unchanged
        decrypted += char

print("FLAG:", decrypted)
