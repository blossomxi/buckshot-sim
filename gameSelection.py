import coinFlip
class gameSelection:
    def chooseOption(option):
        #TODO: Allow user to use string aswell
        print("How do you want to play?\n 1.) Co-op\n 2.) AI\n Please choose with 1 or 2")
        option = int(input())
        if option == 1:
            coinFlip.headsOrTails(input)
            print('Going into game now...')
        elif option == 2:
            coinFlip.headsOrTails(input)
            print('Going into game now...')
        elif option != 1 or option !=2:
            print('Error, Please choose 1 or 2.')