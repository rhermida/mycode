#!/usr/bin/python3

# imports always go at the top of your code


def main():

    # Ask user for height and width inputs

    charHeight = int(input("Please enter how high you want the display to be: "))
#     charWidht = int(input("Please enter how wide you want the display to be: "))
    charWidht = 5

    tempCounter = 1 
    for x in range(charHeight):

        while tempCounter < charWidht:
            print("*", end=" ")

        tempCounter += 1
        print ("")
        print ("")

if __name__ == "__main__":
    main()
