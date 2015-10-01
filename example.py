# This is a comment, the computer ignores this
# it is only to explain to other coders (programmers)
# what is going on in the program code

# Creating variables (places to store values) is always the sam:
# Give the variable a name and then give the variable an initial value

# Initialise a variable by naming it "numberOne" and giving it a default value of 0
numberOne = 0

# Initialise a variable by naming it "numberTwo" and giving it a default value of 0
numberTwo = 0

# Initialise a variable by naming it "result" and giving it a default value of 0
result = 0

# Now we use the input function to ask the user for two numbers to multiply
# Remember:     input("Question to be printed to the user")

# ask for number one
numberOne = input("Please enter number one   ")

# We print out what the user typed in to infrom the user that the program read the input
print("Thank you, you typed in ", numberOne)

# Ask for number two
numberTwo= input("Please enter number two   ")

# We print out what the user typed in to infrom the user that the program read the input
print("Thank you, you typed in ", numberTwo)

# As the input() function is always returning (producing) a String (Word) value, we now need
# to convert the String-values stored in numberOne and umberTwo to "int" values (whole numbers)
# as we can only multiply whole numbers (for now)

# we convert by suing the int() function that converts strings to integers (words to whole numbers)
numberOne = int(numberOne)
numberTwo = int(numberTwo)

# now we can multiply the two numbers and assign the result to the result variable
result = numberOne * numberTwo

# And finally we print out the result to the user
print("The rsult of your muliplication is =",result)

# If you want to ask for a name (or word, sentence) you can just use input()
# without conversion to numbers

# So we create the variable usernmae and assign it the value from the Input 
username = input("Oh by the way, what is your name? ")

# Then we can use it to type a message to the user
print("Oh well, thank you",username,"for using this program")
