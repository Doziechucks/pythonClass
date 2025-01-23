sentence = "Hello, World"

def encrypt_text(sentence):
    word = ""
    for letter in sentence:
        if letter.isalpha() != True:
            word += letter
        else:
            man = ord(letter)
            if 64 < man < 91:
                gamma = man + 13
                if (gamma > 90):
                    alpha = gamma - 90
                    beta = alpha + 64
                    word += chr(beta)
                else:
                    word += chr(gamma)
            elif 96 < man < 123:
                gamma = man + 13
                if gamma > 122:
                    alpha = gamma - 122
                    beta = alpha + 96
                    word += chr(beta)
                else:
                    word += chr(gamma)
    return word
print(encrypt_text(sentence))

