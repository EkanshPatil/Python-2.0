import random

wordlist = ["snowman","santa","elf","rudholf","christmas","newyear","maggi","northpole","present","christmastree"]
 

def jumble(word):
    wordlist = list(word)
    random.shuffle(wordlist)
    return "".join(wordlist)

def get_hint(word):
    return "The first letter of the word is: {}".format(word[0].upper())

def play():
    global wordlist
    score = 0
    rounds = int(input("How many rounds do you want to play? "))
    print("Welcome to the jumble word game!")
    
    for i in range(rounds):
        word = random.choice(wordlist)
        jumbleword = jumble(word)
        print("Round {}".format(i))
        print("Jumbled word is: {}".format(jumbleword))

        hint = input("Do you want a hint (yes/no) ").lower()
        if hint  == "yes":
            print(get_hint(word))

        guess = input("Guess the original word! ").lower()

        while not guess.isalpha():
            print("PLEASE ENTER A VALID WORD USING !ENGLISH! DO NOT ENTER OTHER CHARACTERS OR NUMBERS ONLY ENTER LETTERS!")
            guess = input("Guess the original word! ").lower()
 
        if guess == word:
            print("Congratulations you guessed the correct word!")
            score+=1

        else:
            print("WRONG the correct word is {}".format(word))    

    print("Game finished! your final score is: {}/{}".format(score,rounds))

play()