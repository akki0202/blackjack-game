############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
boom=0
want_toplay = input("Do you want to play BlackJack? 'y' or 'n' ")
if want_toplay == 'y':
    from art import logo
    print(logo)
    comp_card = random.choice(deck)
    comp_card2 = random.choice(deck)
    complist=[comp_card,comp_card2]
    print(f"The computer's card is: {comp_card}")
    your_card1 = random.choice(deck)
    your_card2 = random.choice(deck)
    list = [your_card1]
    list.append(your_card2)
    sum = 0
    for a in list:
        sum = sum + a
    print(f"Your set of cards is: {list} , curent score {sum}")
    again = input("Type 'y' to get another card 'n' to pass: ")
    while again == 'y':
        your_card3 = random.choice(deck)
        list.append(your_card3)
        sum=0
        for a in list:
            sum = sum + a
        print(f"Your set of cards is: {list}, curent score {sum}")
        print(f"The computer's card is: {comp_card}")
        
        if sum>21:
          again='n'
          print("You went over: You Lose!")
          boom = 1
          #boom used because of unintentinal activation of line 57-63
        else:
          again = input("Type 'y' to get another card 'n' to pass: ")  
    if again=='n' and boom!= 1 :
       print(f"Your final hand {list}, your score: {sum}")
       print(f"Computer's final hand {complist}, computer's score: {comp_card+comp_card2}")
       if sum > (comp_card+comp_card2) and sum<=21:
         print("You win! 😁")
       elif sum < (comp_card+comp_card2) and sum<21:
         print("You lose! (❁´◡`❁)")  
       elif sum == (comp_card+comp_card2):
         print("Draw! 💦")

#############################COMPLETED THIS PROJECT WITHOUT USING ANY HINTS😎🤏#################################