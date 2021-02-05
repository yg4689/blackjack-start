############### Blackjack Project #####################
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

##################### Hints #####################


from art import logo
from replit import clear
import random

# select a random card
def deal_card(cards):
  return random.choice(cards)

#calculate_score() that takes a List of cards as input 
#and returns the score.check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 .If the score is already over 21, remove the 11 and replace it with a 1.
def calculate_score(listnum):
  total= sum(listnum)
  flag=False
  if 11 in listnum:
    flag=True
  if len(listnum)==2 and total==21:
    if flag==True:
      return 0
  if total>21 and flag==True:
    listnum.remove(11)
    listnum.append(1)
  return total
  
#compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score,computer_score):
  if user_score==computer_score:
    return "IT'S A DRAW!"
  elif computer_score==0:
    return "USER LOSES!"
  elif user_score==0:
    return "USER WINS!"
  elif user_score>21:
    return "USER LOSES!"
  elif computer_score>21:
    return "COMPUTER LOSES!"
  else:
    if user_score>computer_score:
      return "USER WINS!"
    return "COMPUTER WINS!"
  
def play_game():
  print(logo)
  cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_cards = []
  computer_cards = []
  user_cards.append(deal_card(cards))
  user_cards.append(deal_card(cards))
  computer_cards.append(deal_card(cards))
  computer_cards.append(deal_card(cards))
  run=1
  while run==1:
    print(user_cards,"=",calculate_score(user_cards))
    print(computer_cards,"=",calculate_score(computer_cards))
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    #If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    if user_score==0 or computer_score==0 or user_score==21:
      print("GAME OVER!")
      break
    else:
      user_input=input("Enter 'Y' if you need another card or Enter 'N' to stop")

    if user_input=="Y":
      user_cards.append(deal_card(cards))
      run=1
    else:
      run=0
  #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card(cards))
    computer_score = calculate_score(computer_cards)
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score:{computer_score}")
  print(compare(user_score, computer_score))

  #Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack 
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()


