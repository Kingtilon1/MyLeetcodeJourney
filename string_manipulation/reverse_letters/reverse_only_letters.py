def reverse_only_letters(s):
    symbols = {}
    letters = []

    for index, char in enumerate(s):
        if char.isalpha():
            letters.append(char)
        else:
            symbols[index] = char

    letters.reverse()

    result = []
    letter_index = 0

    for i in range(len(s)):
        if i in symbols:
            result.append(symbols[i])
        else:
            result.append(letters[letter_index])
            letter_index += 1

    return ''.join(result)

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
