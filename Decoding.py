encoded = input("Enter encoded message: ")
decoded = ""

i = 0
j = 0

while i < len(encoded):
    if j % 2 == 0:
        decoded += chr(ord(encoded[i]) - 17)
        i += 1
    else:
        num = ""
        while encoded[i] != "z":
            num += encoded[i]
            i += 1

        ascii_val = round((int(num) - 1650) ** (1/3))
        decoded += chr(ascii_val)
        i += 1  

    j += 1

print(decoded)
