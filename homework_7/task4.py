def key_occur(str):
    count = dict()
    words = str.split()

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count

str_1 = input('Enter a sentence ')
print(key_occur(str_1))