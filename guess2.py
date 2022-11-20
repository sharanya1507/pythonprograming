counter = 0
secret_word ="doraemon"
while counter < 11:
    word = input("enter the secret word")
    counter = counter + 1
    if word == secret_word:
        print("you guessed is right")
        break
    elif word =="d":
        print("you guessed the 1st letter")
    elif word =="o":
        print("you guessed the 2nd letter")
    elif word =="r":
        print("you guessed the 3rd letter")
    elif word =="a":
        print("you guessed the 4th letter")
    elif word =="e":
        print("you guessed the 5th letter")
    elif word =="m":
        print("you guessed the 6th letter")
    elif word =="o":
        print("you guessed the 7th letter")
    elif word =="n":
        print("you guessed the 8th letter")
else:
    print("better luck next time")
