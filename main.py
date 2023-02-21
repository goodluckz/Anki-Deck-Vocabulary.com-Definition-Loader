from vocab_api import Word
import codecs

if __name__ == "__main__":
    with open("wordlist.txt") as f:
        l = f.read().splitlines()
    res = []
    # print(l)
    for word in l:
        print(word)
        meaning = Word(word)
        if meaning.as_dict()['short_desc'] != []:
            res.append(meaning.as_dict())
    print(res, file=codecs.open('word_meaning.txt', 'w', 'utf-8'))