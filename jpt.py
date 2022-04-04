import random   #This is necessary to randomly generate word from the list


# read words from the list and keep them in one line
with open("word_list.txt") as f:
    word_list = f.read().splitlines()

# It picks a random word from the list
rgnum = random.randint(0, len(word_list)-1)
pick_word = word_list[rgnum]

# Convert word into ******. 
hash_word = ('*' * (len(pick_word))) 

# This function is used to guess the words
def predict(letter, word, star):
    seen = False # It checks if the letter exist in the word. 
    if letter in word:
        seen = True
        for i in range(0, len(word)): # It replaces the stars with the found letters
            if word[i] == letter:
                star = star[0:i] + letter + star[i+1:len(star)]
    return (seen, star)


print(hash_word) # Let's initiate the game

lives = 6 # Maximum of 6 attempts allowed.
while(lives > 0):
    guessed_letter = input("Please enter your next guess: ")

    letter_found, hash_word = predict(guessed_letter, pick_word, hash_word)

    if not letter_found:
        lives -= 1                                                      #if a letter is not found, decrease lives by 1
        if lives == 0:                                                  #when lives is zero, the game is lost
            print("\nyou lose. \nThe secret word was " + pick_word)
            break
        else:                                                           #otherwise, display no of lives remaining
            print("\nletter not found; %d attempts remaining." % lives)
            print(hash_word)                                            #print hashed words   
    else:
        if "*" not in hash_word:                                        #once the *s are finished, you've won
            print("\ncongratulations you win")
            break
        else:
            print("\nletter found; %d attempts remaining." % lives)     #otherwise display no of lives remaining
            print(hash_word)                                            #print hashed word