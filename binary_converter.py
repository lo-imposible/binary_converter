# [::-1] reverses string to simplify calculating
userNum = (input("Input a binary number (between 1-8 characters): "))[::-1]
value = 0

# checks lengths of input to make sure it is below 8 characters
if len(userNum) > 8 or len(userNum) < 1:
    print("You have not entered a correct length for a binary number (1-8)")
else:
    # checks validity for characters equal to binary digits 
    valid = True
    for i in userNum:
        if i != '1' and i != '0':
            valid = False
            print("Not a valid binary input.")
            break
    # if valid binary string calculate decimal value 
    if valid:
        for i in range(len(userNum)):
            digit = userNum[i]
            if digit == '1':
                value = value + pow(2, i)
        print(f"The decimal value of the number is {value}")