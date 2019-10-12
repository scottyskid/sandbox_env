



def is_selfdescriptive(number):
    digits = [int(d) for d in str(number)]
    for n in range(len(digits)):
        num_of_digits = 0
        for digit in digits:
            if digit == n:
                num_of_digits += 1
        if num_of_digits != digits[n]:
            return False

    return True

def update_number(number):
    digits = [int(d) for d in str(number)]
    new = ""
    for n in range(len(digits)):
        num_of_digits = 0
        for digit in digits:
            if digit == n:
                num_of_digits += 1
        new += str(num_of_digits)
    return new



if __name__ == "__main__":
    number = "999999999"
    found = False
    
    for i in range(100):
        print(number)
        if is_selfdescriptive(number):
            found = True
            break
        else:
            number = update_number(number)
    print(found)
        
