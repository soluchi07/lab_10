import string
import sys

def shiftChar(char, n):
    if ord(char) <= (90 - n) :
        result = chr(ord(char) + n)
    else:
        result = chr(ord(char) + n -26)
    return result

def main():
    letters = string.ascii_uppercase
    message = sys.stdin.read().upper()
    n = int(sys.argv[1])
    encrypted = ""
    for char in message:
        if char in letters:
            encrypted += shiftChar(char, n)
    
    for i in range(len(encrypted)):
        if i % 50 == 49:
            print(encrypted[i], end = "\n")
        elif i % 5 == 4 :
            print(encrypted[i], end = " ")
        else:
            print(encrypted[i], end="")
        

if __name__ == "__main__":
    main()