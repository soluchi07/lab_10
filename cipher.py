import string
import sys

#define function for shifting characters using the key n
def shiftChar(char, n):
    if ord(char) <= (90 - n) :
        result = chr(ord(char) + n)
    else:
        result = chr(ord(char) + n -26)
    return result

#define main function
def main():
    #define string of uppercase letters
    letters = string.ascii_uppercase

    #store stdin in uppercase as message
    message = sys.stdin.read().upper()

    #take the second argument as the encryption key
    n = int(sys.argv[1])

    #initialise empty string for encrypted message
    encrypted = ""

    #iterate through message, shift if character if it's in the alphabet and add it to the encrypted string
    for char in message:
        if char in letters:
            encrypted += shiftChar(char, n)

    #iterate through new encrypted string to print characters out in 10 blocks of 5
    for i in range(len(encrypted)):
        if i % 50 == 49:
            print(encrypted[i], end = "\n")
        elif i % 5 == 4 :
            print(encrypted[i], end = " ")
        else:
            print(encrypted[i], end="")
        
#call main function
if __name__ == "__main__":
    main()
