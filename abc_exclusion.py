def unique(strings):
    word = []
    for string1 in strings:
        for string2 in strings:
            if string1 == string2:
                continue

            return word + [string1]

print(unique("aabbcc"))
