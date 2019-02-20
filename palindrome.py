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
#letters = ""

#def palindrome(text):
  #  """Test to see if the text is a palindrome."""

    #letters = text.split(" ")
    #print("letters" + str(letters))
#only keeps letters

def palindrome_recursive(text):
    """In order to see if the text you recevied was a palindrom run it so that you call the function everytime you evaluate a letter in the string."""
    letters = only_letters(text)
    #print("lettters" + str(letters))
#makes all letters lower_case
    letter = letters.lower()
    #print("letter" + str(letter))
#simple
#creates string for letters
    #letter_left_to_right = letter[:]
    #print("letter_left_to_right" + letter_left_to_right)
#creates string for letters in reverse
    #letter_reverse = letter[::-1]
    #print("letter_reverse" + letter_reverse)
#compare letter_left_to_right and letter_reverse to see if they are a palindrome or not
    #if letter_left_to_right == letter_reverse:
     #   print("this is a palindrome")
    #else:
    #    print("this is not a palindrome")


# iterative version
# run a for loop so that it starts by going through every letter in letters.Find the length of the string and then find the range of the length so it sets a limit on how many times it is repeated. NOTE you only have to got through half of the string before you are able to tell if it is a palindrome.
    #for idx in range(len(letter)//2):
#then get it to test if the first letter and last letter are the same, and then repeat it for all the ones from there. If they are not the same then it is not a palindrome so it is false. Return false so that it stops running.
       # if letter[idx] != letter[-(idx+1)]:

          #  return False
       # else: 
            #return True
#call it to be printed at the end
#if palindrome(text):
 #   print("this is a palindrome")
#else:
  #  print("this is not a palindrome")

#recursive version
#you have to set bases that you know to be true so that the function knows when to stop and when to keep going.
#one base for this is that we want this to run until the lenght of letter is one because when it gets down to the last letter it will know if it is a palindrome or not, because it has passed all the ones before it.
    if len(letter) <= 1:
        return True
#now if it passes that when go to the next thing we know to be true or is a base.
#the value of the first(0) and last (-1) have to be equal. So ask it to run that until they are not equal. If they are not equal then it is false.
    if letter[0] != letter[-1]:
        return False
#now we want to run the function for the range of all idx so you start at 1 and go to -1 because we already know that if letter[0] and letter[-1] are true then they are palindrome. So we got up to the next numbers which start with 1 and go until -1, becuase -1 and 0 already ran
    return palindrome_recursive(letter[1:-1])
#then you have to give the output
#call the function
if palindrome_recursive(text):
    print("this is a palindrome")
else:
    print("this is not a palindrome")