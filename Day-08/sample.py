alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


word = ""
ls_text = []
position = -1
for letter in range(len(text)) :
    for l in alphabet :
        position += 1
        if text[letter] == l :
            word == alphabet[position + shift]
            ls_text.append(word)
print(ls_text)