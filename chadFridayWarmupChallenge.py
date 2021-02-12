#!/usr/bin/python3

# imports always go at the top of your code


def game_decision_dontbuy():
    print("")
    print("DON'T BUY IT!")
    return

def game_decision_thinkdecide():
    print("")
    print("THINK ABOUT IT ...")
    return

def game_decision_buybuybuy():
    print("")
    print("BUY BUY BUY!")
    return

def game_decision_getbacktowork():
    print("")
    print("STOP GOOFING AROUND ... GET BACK TO WORK!")
    return

def main():

    # Should I buy That Game on STEAM

    print("Should I Buy That Game on STEAM?")
    print("=============================")

    firstQuestion = "yes"
    while firstQuestion != "q": 
        firstQuestion = input("Is the game ON SALE (yes/no)? ").lower()
        
        if firstQuestion == "yes":
            secondQuestion = input("Is it more than 75% off (yes/no)? ").lower()

            if secondQuestion == "yes":
                print ("Next Question")
                break
            elif firstQuestion == "no":
                game_decision_dontbuy()
                break
            else:
                game_decision_getbacktowork() 
                break

        elif firstQuestion == "no":
            game_decision_dontbuy()
        else:
            game_decision_getbacktowork() 
            break
               
if __name__ == "__main__":
    main()
