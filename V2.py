word_dict = {}

for word in my_lyrics:
    Alle_Wörter = word.capitalize()
    if Alle_Wörter in word_dict:
        word_dict[Alle_Wörter] = word_dict[Alle_Wörter] + 1
    elif Alle_Wörter not in word_dict:
        word_dict[Alle_Wörter] = 1

for pair in sorted(word_dict.items(), key=lambda colum:colum[1]):
    print(pair)
