# functions that you need but will call further down.
    # clear text so all that is left is letters
def only_letters(text):
    """ take out all characters that are not lower case letters"""
    #keep these things
    get_all_letters = "abcdefghijklmnopqrstuvwxyz"
    get_all_letters += get_all_letters.upper()
    #set up a loop that goes to each character to see if it is a letter. If is it not a letter get ride of it. If it is a letter keep it.
    #create a new sequence
    all_case_letters = ""
    #write a for statement to loop through all the characters
    for character in text:
        #call the above sequence to determine if the text has those letters in it
        if character in get_all_letters:
            #then what should it do, it should add that character to all_case_letters sequence
            all_case_letters += character
            #now return the seequence for lower_case_letters
    return all_case_letters

# get text
text = str(input(
    "Hello User! Please write some text. I will tell you if it is a palindrome. Write text here: "))
#remove spaces
letters = text.split(" ")
print("letters" + str(letters))
#only keeps letters
letter = only_letters(text)
print("lettters" + str(letter))
#makes all letters lower_case
letter = letter.lower()
print("letter" + str(letter))
#creates string for letters
letter_left_to_right = letter[:]
print("letter_left_to_right" + letter_left_to_right)
#creates string for letters in reverse
letter_reverse = letter[::-1]
print("letter_reverse" + letter_reverse)
#compare letter_left_to_right and letter_reverse to see if they are a palindrome or not
if letter_left_to_right == letter_reverse:
        print("this is a palindrome")
else:
        print("this is not a palindrome")