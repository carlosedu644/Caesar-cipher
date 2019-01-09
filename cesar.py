# Python program to encoding and decrypt Caesar Cipher


def alphabet_map():
    alpha = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
             'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
             'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ' ': 27}
    return alpha


def alphabet(phrase):
    return alphabet_map()[phrase]


def inv_alphabet_map(phrase):
    inv_map = {v: k for k, v in alphabet_map().items()}
    return inv_map[phrase]


def main():
    print("1 - Encoding")
    print("2 - Decoding")
    menu = int(input("> "))
    phrase = input("Phrase > ")
    shift = int(input("Shift> "))
    list_phrase = list(phrase)

    # Encoding
    if menu == 1:
        for i in range(0, len(list_phrase)):

            if abs(alphabet(list_phrase[i]) + shift) < 26:
                print(inv_alphabet_map(abs(alphabet(list_phrase[i]) + shift)))
            else:
                print(inv_alphabet_map(abs(alphabet(list_phrase[i]) + shift - 26)))
    # Decoding
    elif menu == 2:
        for i in range(0, len(list_phrase)):

            if alphabet(list_phrase[i]) - shift < 0:
                print(inv_alphabet_map(alphabet(list_phrase[i]) - shift + 26))
            else:
                print(inv_alphabet_map(alphabet(list_phrase[i]) - shift))


main()
