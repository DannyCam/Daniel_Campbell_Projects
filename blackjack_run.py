def play_blackjack():
    """Plays the blackjack game. No input necessary."""
    #################################################################################
    # Drawing phase #
    player_hand = [11,8]
    player_hand_total = 0
    calculate_score(player_hand, player_hand_total)
    # Dealer is referring to the "computer"
    dealer_hand = draw(2)
    dealer_hand_total = 0
    calculate_score(dealer_hand, dealer_hand_total)

    # Add conditional statement so ace is either 11 or 1
    print(f"\nYour hand is below and your total is {player_hand_total}.\n{player_hand}")
    print(f"The dealer draws {dealer_hand[0]}.")


    ##################################################################################
    # Check for user Blackjack #
    if player_hand_total == 21:
      if dealer_hand_total == 21:
        return print(f"Tie\nDealer hand is {dealer_hand}")
      else:
        return print(f"You win!\nDealer hand is {dealer_hand}")


    ##################################################################################
    # Player draw phase #

    answer = input("Would you like to draw? y/n: ").lower()
    drawing = True

    while drawing == True:
      if answer == "y":
        new_card = draw(1)[0]
        player_hand.append(new_card)
        bust_check = bust(player_hand)
        for something in player_hand:
              player_hand_total += something
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
      # dealer_hand_total += new_card
      if bust_check == 21:
          print(f"The dealer draw {new_card} and their total is {dealer_hand_total}.\nThat's 21! {dealer_hand}\n")
      elif bust_check == "no_bust":
          new_card = draw(1)[0]
          print(f"The dealer draw {new_card} and their total is {dealer_hand_total}.\n{dealer_hand}\n")
      elif bust_check == "bust":
          return print(f"The dealer draw {new_card} and their total is {dealer_hand_total}.\nDealer bust. {dealer_hand}\nYou Win!\n")


    ##################################################################################
    # Comparison phase #
    if player_hand_total == dealer_hand_total:
     return print("Tie")
    elif player_hand_total > dealer_hand_total:
      return print("You Win!")
    else:
      return print("You Lose")