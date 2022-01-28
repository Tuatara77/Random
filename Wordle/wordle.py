import random

with open("5-letter-words.txt", "r") as words:
    wordslist = words.readlines()
for f in range(len(wordslist)):
    wordslist[f] = wordslist[f][:5]

word = list(random.choice(wordslist))

guesscount = 1
wordguess = list(input(f"Guess {guesscount}: "))
while wordguess != word and guesscount < 5:

    for f in range(len(wordguess)):
        if wordguess[f] == word[f]:
            print(f"{wordguess[f]} is in the correct spot")
        elif wordguess[f] in word:
            print(f"{wordguess[f]} is right but in the wrong place")
    
    guesscount += 1
    wordguess = list(input(f"Guess {guesscount}: "))

if wordguess == word:
    wordslist.remove(word)
    with open("5-letter-words.txt", "w") as words:
        for f in wordslist:
            words.write(f"{f}\n")
else:
    word = "".join(word)
    print(f"The word was {word}")
    with open("5-letter-words.txt", "w") as words:
        for f in wordslist:
            words.write(f"{f}\n")
