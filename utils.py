# Creating a class named Utils
class Utils:
    # Function that reverses the number
    def Reversed(number):
        # Converting the number to string
        numAsStr = str(number)
        # Function does not run if input is not an integer
        if(numAsStr.isdigit() == False):
            return -1
        # Reversing the number using slicing
        reversedNumber = numAsStr[::-1]
        print("The reverse of the number " + numAsStr + " is " + reversedNumber + ".")
        # Returning the reversed number back in integer form
        return (int(reversedNumber))

    # Function that converts decimal number into binary and octal
    def Formatter(number):
        #Function does not run if input is not an integer
        if(str(number).isdigit() == False):
            return -1
        print("The value of " + str(number) + " is:")
        print(str(bin(number)) + " in binary.")
        print(str(oct(number)) + " in octal.")
        # Returning the binary and octal formats of the number
        return (bin(number), oct(number))

