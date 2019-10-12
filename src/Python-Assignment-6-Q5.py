import random

# Question 5
print("Question 5.")

# Part A
def generate_password(username):
    # Print the prefix before displaying password
    print("Generated password: ", end="")
    # For loop replace vowels with numbers and prints consecutively
    new_string = ""

    for i in range(len(username)):
        if username[i:i].lower() == "e":
            new_string += "1"
        elif ((username[i] == "u") or (username[i] == "U")):
            new_string += "2"
        elif ((username[i] == "i") or (username[i] == "I")):
            new_string += "3"
        elif ((username[i] == "o") or (username[i] == "O")):
            new_string += "4"
        elif ((username[i] == "a") or (username[i] == "A")):
            new_string += "5"
        # If no vowel, simply prints letter and continues
        else:
            new_string += username[i]
    # Adds a random digit onto the end of generated password
    new_string += str(random.randint(0,9))

    return new_string[:]

# Part B
while True:
    username = input("Enter username (type QUIT to quit): ")
    # Calls upon function
    password = generate_password(username)
    print(password)
    # Exits loop
    if (username == "QUIT"):
        break

