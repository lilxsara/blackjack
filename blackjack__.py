import random
print("WELCOME TO BLACKJACK! ENJOY!")
player_chips = float(input("Buy chips: "))

def deck():
    hand = []
    for i in range(2):
        if sum(hand) >= 11:
            hand.append(random.randint(1,10))
        else:
            hand.append(random.randint(2,11))
    return hand

def play_again(player_balance):
    again = str(input("\nDo you want to play again? [Y/N]: ")).lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        game()
    else:
        print("\nBalance: $", player_balance)
        print("Bye!Thank you for playing!")
        exit()

def hit(hand):
    if sum(hand) >= 11:
        hand.append(random.randint(1, 10))
    else:
        hand.append(random.randint(2, 11))
    return hand

def dealer_hit(dealer_hand):
    while sum(dealer_hand) < 17:
        hit(dealer_hand)
    print("\nDealer has", str(sum(dealer_hand)), "with", dealer_hand)

def blackjack(dealer_hand,player_hand,player_balance,player_bet):
    if sum(player_hand) == 21:
        print("You got a blackjack\n")
        player_balance += player_bet + (player_bet * 1.5)
        play_again(player_balance)
    elif sum(dealer_hand) == 21:
        print("Dealer got a blackjack!\n")
        player_balance -= player_bet
        play_again(player_balance)
    return player_chips

def score(dealer_hand,player_hand,player_bet):
    global player_chips
    if sum(dealer_hand) > 21:
        player_chips += player_bet
        print("Dealer has busted")
    elif sum(player_hand) > 21:
        player_chips -= player_bet
        print("You busted with " + str(sum(player_hand)))
    elif (sum(player_hand) > sum(dealer_hand)) and (sum(player_hand) <= 21):
        player_chips += player_bet
        print("You won with " + str(sum(player_hand)))
    elif (sum(player_hand) < sum(dealer_hand)) and sum(dealer_hand) <= 21:
        player_chips -= player_bet
        print("You lose with " + str(sum(player_hand)))
    elif sum(player_hand) == sum(dealer_hand):
        print("Pushed")

def score_split(dealer_hand,player_hand1,player_hand2,player_bet):
    global player_chips
    if sum(dealer_hand) > 21:
        player_chips += player_bet*2
        print("Dealer has busted. You won!")
    #Checking either each hand or both > or < or == with dealer's hand
    if (sum(player_hand1) > sum(dealer_hand) or sum(player_hand2) > sum(dealer_hand)) and (sum(player_hand1) <= 21 or sum(player_hand2) <= 21):
        if (sum(player_hand1) > sum(dealer_hand) and sum(player_hand2) > sum(dealer_hand)) and (sum(player_hand1) <= 21 and sum(player_hand2) <= 21):
            player_chips += player_bet * 2
            print("You won with " + str(sum(player_hand1)) + " from first hand and " + str(sum(player_hand2)) + " from second hand.")
        elif (sum(player_hand1) > sum(dealer_hand)) and sum(player_hand1) <= 21:
            player_chips += player_bet
            print("You won with " + str(sum(player_hand1)) + " from first hand.")
        elif (sum(player_hand2) > sum(dealer_hand)) and sum(player_hand2) <= 21:
            player_chips += player_bet
            print("You won with " + str(sum(player_hand2)) + " from second hand.")
    if (sum(player_hand1) == sum(dealer_hand) or sum(player_hand2) == sum(dealer_hand)) and (sum(dealer_hand) <= 21):
        if sum(player_hand1) == sum(dealer_hand) and sum(player_hand2) == sum(dealer_hand):
            print("Both hands are pushed")
        elif sum(player_hand1) == sum(dealer_hand):
            print("Pushed with first hand")
        elif sum(player_hand2) == sum(dealer_hand):
            print("Pushed with second hand")
    if (sum(player_hand1) < sum(dealer_hand) or sum(player_hand2) < sum(dealer_hand)) and sum(dealer_hand) <= 21:
        if sum(player_hand1) < sum(dealer_hand) and sum(player_hand2) < sum(dealer_hand):
            player_chips -= player_bet*2
            print("You lose for both hands")
        elif sum(player_hand1) < sum(dealer_hand):
            player_chips -= player_bet
            print("You lose with " + str(sum(player_hand1)) + " from first hand")
        elif sum(player_hand2) < sum(dealer_hand):
            player_chips -= player_bet
            print("You lose with " + str(sum(player_hand2)) + " from second hand")

def insurance(dealer_hand,player_bet):
    global player_chips
    action = str(input("\nDo you want to buy insurance?[Y/N]: ")).lower()
    if action == "y" or action == "yes":
        player_insurance = float(input("Please put your insurance bet[max = half of the bet]: $"))
        if player_insurance <= player_bet/2 and player_chips - player_insurance != 0:
            if sum(dealer_hand) == 21:
                player_chips += player_insurance*2
                player_chips -= player_bet
                print("\nYou won! Dealer got a blackjack!")
                play_again(player_chips)
            elif sum(dealer_hand) < 21:
                player_chips -= player_insurance
                print("\nDealer doesnt have a blackjack! All your insurance bets are gone!")
        else:
            print("\nYour chips is insufficient to buy the insurance. Sorry!")
            insurance(dealer_hand, player_bet)
    else:
        if sum(dealer_hand) == 21:
            print("\nYou lose your bet! Dealer has blackjack!")
            player_chips -= player_bet
            play_again(player_chips)
        else:
            print("\nDealer doesnt have blackjack")

def game():
    global player_chips
    print("\nBalance: $", player_chips)
    if player_chips != 0:
        bet = float(input("Please put your bet: "))
        if bet <= player_chips:
            dealer_hand = deck()
            if len(dealer_hand) == 2:
                if dealer_hand[1] == 1:
                    dealer_hand[1] = 11
                if dealer_hand[0] == 11 and dealer_hand[1] == 11:
                    dealer_hand[1] = 1
                print("\nDealer shows", dealer_hand[1])

            player_hand = deck()
            print("You have", str(sum(player_hand)), "with", player_hand)
            blackjack(dealer_hand, player_hand, player_chips, bet)
            player_hand1 = [player_hand[0], ]
            player_hand2 = [player_hand[1], ]

            if (dealer_hand[1] == 11 and sum(player_hand) < 21): #Checking for insurance condition
                insurance(dealer_hand, bet)

            while sum(player_hand) <= 21:
                if (player_hand[0] == player_hand[1] and len(player_hand) < 3) and player_chips >= bet*2:
                    if len(player_hand1) >= 2 and len(player_hand2) >= 2:
                        if sum(player_hand1) > 21 and sum(player_hand2) > 21:
                            print("\nYour both hands are busted!")
                            break
                        action = str(input("\nHit[H1/[H2] to hit each hand or Stand[S] for both hands: ")).lower()
                    else:
                        action = str(input("\nHit[H] or Stand[S] or Double Down[D] or Split[P]: ")).lower()
                elif len(player_hand) < 3 and player_chips >= bet*2:
                    action = str(input("\nHit[H] or Stand[S] or Double Down[D]: ")).lower()
                else: action = str(input("\nHit[H] or Stand[S]: ")).lower()

                if action == "p": #Split action
                    while len(player_hand1) < 2 and len(player_hand2) < 2:
                        hit(player_hand1)
                        hit(player_hand2)
                    print("First hand:", player_hand1, "with " + str(sum(player_hand1)))
                    print("Second hand:", player_hand2, "with " + str(sum(player_hand2)))
                    continue
                elif action == "h" or (action == "h1" or action == "h2"): #Hit action
                    if len(player_hand1) >= 2 and len(player_hand2) >= 2: #hit for split card
                        if action == "h1" and sum(player_hand1) > 21:
                            print("Your first hand is busted")
                        elif action == "h2" and sum(player_hand2) > 21:
                            print("Your second hand is busted")
                        elif action == "h1":
                            hit(player_hand1)
                            print("First hand:", player_hand1, "with " + str(sum(player_hand1)))
                            if sum(player_hand1) > 21:
                                player_chips -= bet
                                print("You busted with " + str(sum(player_hand1)))
                        elif action == "h2":
                            hit(player_hand2)
                            print("Second hand:", player_hand2, "with " + str(sum(player_hand2)))
                            if sum(player_hand2) > 21:
                                player_chips -= bet
                                print("You busted with " + str(sum(player_hand2)))
                        continue
                    else: #normal hit
                        hit(player_hand)
                        print("You have", str(sum(player_hand)), "with", player_hand)
                        if sum(player_hand) > 21:
                            player_chips -= bet
                            print("You busted")
                            break
                    continue
                elif action == "d": #Double Down action
                    bet *= 2
                    hit(player_hand)
                    print("You have", str(sum(player_hand)), "with", player_hand)
                    if sum(player_hand) > 21:
                        player_chips -= bet
                        print("You busted")
                        break
                    else:
                        dealer_hit(dealer_hand)
                        score(dealer_hand, player_hand, bet)
                        break
                elif action == "s": #Stand action
                    if len(player_hand1) >= 2 and len(player_hand2) >= 2: #stand for split card
                        dealer_hit(dealer_hand)
                        score_split(dealer_hand, player_hand1, player_hand2, bet)
                        break
                    else: #normal stand
                        print("Stood on ", str(sum(player_hand)))
                        dealer_hit(dealer_hand)
                        score(dealer_hand, player_hand, bet)
                        break
        else:
            print("You have insufficient chips to put the bet. Try again\n")
            game()
    else:
        print("\nYou have 0 chip. Sorry, game over!")
        exit()
    play_again(player_chips)
game()