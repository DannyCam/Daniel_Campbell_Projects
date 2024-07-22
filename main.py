import random
from art import logo
from replit import clear

#1: Import play_blackjack() method
#2: Create and use a finite "set" of cards to play from
#2a: deal both player and dealer cards before asking for user input
#2b: find out whether player or dealer hand is dealt first
#2c: find out if player and dealer use separate decks
#3: Replace numbers with ascii art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand, hand_total):
  """Calculates the score of the current hand, then returns the number associated with the total of the hand. \nInput the name of the hand followed by the total you would like to calculate or recalculate."""
  hand_total = 0
  for something in hand:
      hand_total += something
  return hand_total


def draw(number):
  """Randomly 'picks' any number of cards from the list of cards.\nInput the number of cards you would like to draw."""
  card_given = []
  for pulls in range(0, number): 
    card_given.append(cards[random.randint(0, 12)])
  return card_given


# def compare(p_hand, d_hand):
#   """Compares two hands to see which is the winning hand.\nInput player's hand followed by dealer's hand to run."""
#   if p_hand == d_hand:

# if player_hand_total == dealer_hand_total:
#      return print("Tie")
#     elif player_hand_total > dealer_hand_total:
#       return print("You Win!")
#     else:
#       return print("You Lose")

def bust(hand):
  """Decides whether a hand is a bust and returns 21, 'bust', or 'no_bust' as strings.\nThis also inludes changing an ace from 11 to 1 if the hand exceeds 21.\nInput the name of the hand you want to test."""
  hand_total = 0
  
  for cards in hand:
    hand_total += cards

  if hand_total == 21:
    return 21
  elif hand_total < 21:
    return "no_bust"
  elif hand_total > 21:
    if 11 in hand:
      #change ace from 11 to 1
      for ace in hand:
        if ace == 11:
          # find the position
          ace_position = hand.index(11)
          # remove 11
          hand.pop(ace_position)
          # put 1 where the 11 was
          hand.insert(ace_position, 1)
          return "no_bust"
    else:
      return "bust"

# p_hand means player hand
# d_hand means dealer hand
# def compare(p_hand, d_hand):

def play_blackjack():
    """Plays the blackjack game. No input necessary."""
    #################################################################################
    # Drawing phase #
    player_hand = draw(2)
    player_hand_total = 0
    player_hand_total = calculate_score(player_hand, player_hand_total)
    # Dealer is referring to the "computer"
    dealer_hand = draw(2)
    dealer_hand_total = 0
    dealer_hand_total = calculate_score(dealer_hand, dealer_hand_total)

    # Add conditional statement so ace is either 11 or 1
    print(f"\nYour hand is below and your total is {player_hand_total}.\n{player_hand}")
    print(f"The dealer draws {dealer_hand[0]}.")


    ##################################################################################
    # Check and compare for user Blackjack #
    if player_hand_total == 21:
      if dealer_hand_total == 21:
        return print(f"Tie\nDealer's hand is {dealer_hand}")
      else:
        return print(f"You win!\nDealer's hand is {dealer_hand}")


    ##################################################################################
    # Player draw phase #

    answer = input("Would you like to draw? y/n: ").lower()
    drawing = True

    while drawing == True:
      if answer == "y":
        new_card = draw(1)[0]
        player_hand.append(new_card)
        bust_check = bust(player_hand)
        player_hand_total = calculate_score(player_hand, player_hand_total)
        #change conditional statements to bust
        if bust_check == 21:
          print(f"\nYou draw {new_card} and your total is {player_hand_total}.\nThat's 21! {player_hand}\n")
          drawing = False
        elif bust_check == "no_bust":
          print(f"\nYou draw {new_card} and your total is {player_hand_total}.\n{player_hand}\n")
          answer = input("Would you like to draw? y/n: ").lower()
        elif bust_check == "bust":
          return print(f"\nYou draw {new_card} and your total is {player_hand_total}.\nYou bust. {player_hand}\n")
          # drawing = False
      elif answer == "n":
        drawing = False
      else:
        answer = input("Would you like to draw? y/n: ").lower()


    ##################################################################################
    # Dealer draw phase #
    print(f"\nThe dealer's hand is {dealer_hand} and their total is {dealer_hand_total}.")

    if dealer_hand_total == 21:
      print("You Lose")
    while dealer_hand_total < 17:
      new_card = draw(1)[0]
      dealer_hand.append(new_card)

      bust_check = bust(dealer_hand)
      dealer_hand_total = calculate_score(dealer_hand, dealer_hand_total)
      if bust_check == 21:
          print(f"The dealer draws {new_card} and their total is {dealer_hand_total}.\nThat's 21! {dealer_hand}\n")
      elif bust_check == "no_bust":
          new_card = draw(1)[0]
          print(f"The dealer draws {new_card} and their total is {dealer_hand_total}.\n{dealer_hand}\n")
      elif bust_check == "bust":
          return print(f"The dealer draws {new_card} and their total is {dealer_hand_total}.\nDealer bust. {dealer_hand}\nYou Win!\n")


    ##################################################################################
    # Comparison phase #
    if player_hand_total == dealer_hand_total:
     return print("Tie")
    elif player_hand_total > dealer_hand_total:
      return print("You Win!")
    else:
      return print("You Lose")


###############################################################################
print(f"Welcome to Blackjack\n{logo}")
answer = input("Enter 'y' to play! ").lower()
if answer == "y":
  playing = True
else:
  playing = False
while playing == True:
  play_blackjack()
  more_games = input("Would you like to keep playing? Type y/n: ").lower()
  if more_games == "y":
    clear()
    print(logo)
  else:
    playing = False

# compare() function so this is a little easier to look at