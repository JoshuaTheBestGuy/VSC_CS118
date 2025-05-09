"""
This program will simulate a game of blackjack. The game will record your high score, and store it in a separate file. 
Author: Joshua Hendrickson, alone and unafraid.
Dates: 03/29/2025 -> 03/30/2025
"""

from random import randint
from bj_functions import hit

user_money = 500
asked = False

while True: 
    deck = {1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4}
    user_deck_values = {"A":11, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10}
    dealer_deck_values = {"A":11, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10}
    user_cards = []
    user_value = 0
    dealer_cards = []
    dealer_value = 0
    hand1 = []
    hand1_deck_values = {"A":11, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10}
    hand1_bet = 0
    hand1_value = 0
    hand1_bust = False
    hand2 = []
    hand2_deck_values = {"A":11, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10}
    hand2_bet = 0
    hand2_value = 0
    hand2_bust = False
    user_bust = False
    dealer_bust = False
    last_card = None
    blackjack = False
    dealer_changed = False
    user_changed = False
    hand1_changed = False
    hand2_changed = False
    can_split = False
    did_split = False
    finished_hand1 = False
    finished_hand2 = False
    done_hitting_hand1 = False
    done_hitting_hand2 = False
    done_hitting = False
    high_score_balance = False
    hit_again = False
    dealer_done = False
    
    with open("Personal_Projects/blackjackhighscore.txt", "r+") as file:
        high_score = file.read()
        high_score = int(high_score)
    if asked == False and high_score > user_money:
        high_score_balance = input(f"\nWelcome to blackjack! Your current balance is '{user_money}'. Would you like to start with your high score balance of '{high_score}'? Yes or No: ")
        high_score_balance = high_score_balance.lower()
        while True:
            if high_score_balance == "no":
                break
            elif high_score_balance == "yes":
                break
            else:
                print(f"Your action of '{high_score_balance}' is not a valid action.")
                high_score_balance = input(f"\nWelcome to blackjack! Your current balance is '{user_money}'. Would you like to start with your high score balance of '{high_score}'? Yes or No: ")
                high_score_balance = high_score_balance.lower()
        asked = True
    else:
        print(f"\nWelcome to blackjack! Your current balance is '{user_money}'.")
    while True:
        if high_score_balance == "yes":
            user_money = high_score
            print(f"Your new balance is '{user_money}'.")
            break
        else:
            break
    if user_money == 0:
        print("You went bankrupt.... get out of my casino.")
        exit()
    bet = input(f"Please place your bet, or 'q' to exit the casino: ")
    while True:
        if blackjack == True:
            break
        if bet == "q":
            with open("Personal_Projects/blackjackhighscore.txt", "r+") as file:
                high_score = file.read()
                high_score = int(high_score)
            if user_money > high_score:
                with open("Personal_Projects/blackjackhighscore.txt", "w+") as file:
                    if user_money > high_score:
                        file.write(str(user_money))
                        print(f"Congrats! You have a new high score of {user_money}! Keep gambling!")
            if user_money == 0:
                print("You went bankrupt.... get out of my casino.")
            exit()
            # record high score
            break
        else:
            if str(bet).isnumeric == True:
                bet = int(bet)
                continue
            elif str(bet).isnumeric() == False:
                print(f"Your bet of '{bet}' dollars is not a valid bet. Please place a bet above '1'.")
                bet = input("Please place your bet, or 'q' to exit the casino: ")
            elif str(bet) == "0":
                print(f"Your bet of '{bet}' dollars is not a valid bet. Please place a bet above '1'.")
                bet = input("Please place your bet, or 'q' to exit the casino: ")
            elif int(bet) > user_money:
                print(f"Your bet of '{bet}' dollars exceeds your total balance of '{user_money}' dollars. Please place a bet below this. ")
                bet = input("Please place your bet, or 'q' to exit the casino: ")
            else:
                print(f"Your bet of '{bet}' dollars has been placed! Good luck!")
                bet = int(bet)
                user_money -= bet
                break


    deck, user_cards, last_card, user_value, user_deck_values = hit(deck, user_cards, user_value, user_deck_values, 2)
    deck, dealer_cards, last_card, dealer_value, dealer_deck_values = hit(deck, dealer_cards, dealer_value, dealer_deck_values, 2)

    if user_value == 21:
        blackjack = True
    if blackjack == True:
        print(f"You got {user_cards}, with a value of '{user_value}'. That's a blackjack, congrats!")
        user_money += bet * 3
    if blackjack == False:
        print(f"You begin this round with {user_cards}, with a value of '{user_value}'. The dealer's top card is {dealer_cards[-1]}.")
        if user_cards[0] == user_cards[-1] and user_money > (bet * 2):
            print(f"Split is available because you have two of the same cards!")
            can_split = True
        action = input("Would you like to stand, hit, double-down, or split?: ")
        action = action.lower()

        while True:
            if action == "stand":
                print(f"You chose to stand. Good luck!")
                print(f"The dealer has {dealer_cards} with a value of '{dealer_value}'.")
                while True:
                    if dealer_value > 21:
                        dealer_deck_values["A"] = 1
                        if dealer_changed == False:
                            if "A" in dealer_cards:
                                dealer_value -= 10
                                dealer_changed = True
                        if dealer_value > 21:
                            break
                    if dealer_value >= 17:
                        print("The dealer must stand, good luck!")
                        break
                    else:
                        deck, dealer_cards, last_card, dealer_value, dealer_deck_values = hit(deck, dealer_cards, dealer_value, dealer_deck_values, 1)
                    print(f"The dealer got a {last_card}, for a total value of '{dealer_value}'.")
                break
            elif action == "hit" or hit_again == True:
                while user_bust == False and done_hitting == False:
                    print(f"You chose to hit. Good luck!")
                    if user_value > 21:
                        user_deck_values["A"] = 1
                        if user_changed == False:
                            if "A" in user_cards:
                                user_value -= 10
                                user_changed = True
                        if user_value > 21:
                            print(f"You went over '21' and busted with a value of '{user_value}'.")
                            break
                    elif user_value == 21:
                        print(f"You hit '21', good luck!")
                        break
                    else:
                        deck, user_cards, last_card, user_value, user_deck_values = hit(deck, user_cards, user_value, user_deck_values, 1)
                        if user_value > 21:
                            user_deck_values["A"] = 1
                            if user_changed == False:
                                if "A" in user_cards:
                                    user_value -= 10
                                    user_changed = True
                            if user_value > 21:
                                user_bust = True
                        print(f"You got a {last_card}, the values of your cards is '{user_value}'.")
                        if user_value < 21:
                            user_bust = False
                        elif user_value > 21:
                            user_bust = True
                            break
                        elif user_value == 21:
                            break
                        hit_again = input("Would you like to hit again? Yes or No: ")
                        hit_again = hit_again.lower()
                        while True:
                            if hit_again == "no":
                                hit_again = False
                                done_hitting = True
                                break
                            elif hit_again == "yes":
                                hit_again = True
                                done_hitting = False
                                break
                            else:
                                print(f"Your action of '{hit_again}' is not a valid action.")
                                hit_again = input("Would you like to hit again? Yes or No: ")
                                hit_again = hit_again.lower()
                        if done_hitting == True and hit_again == False:
                            while dealer_done == False:
                                print(f"The dealer has {dealer_cards} with a value of '{dealer_value}'.")
                                while dealer_done == False:
                                    if dealer_value > 21:
                                        dealer_deck_values["A"] = 1
                                        if dealer_changed == False:
                                            if "A" in dealer_cards:
                                                dealer_value -= 10
                                                dealer_changed = True
                                        if dealer_value > 21:
                                            print(f"The dealer busted!")
                                            dealer_bust = True
                                            break
                                    if dealer_value >= 17 and dealer_bust == False:
                                        print("The dealer must stand, good luck!")
                                        dealer_done = True
                                        break
                                    elif dealer_value == 21:
                                        print("The dealer must stand, good luck!")
                                        dealer_done = True
                                        break
                                    deck, dealer_cards, last_card, dealer_value, dealer_deck_values = hit(deck, dealer_cards, dealer_value, dealer_deck_values, 1)
                                    print(f"The dealer got a '{last_card}', for a total value of '{dealer_value}'.")
                                break    
                            break
                        break
                    break
                break
            elif action == "double-down":
                print("You have chosen to double-down. Your bet will be doubled, and you will only receive one card.")
                user_money -= bet
                bet *= 2
                deck, user_cards, last_card, user_value, user_deck_values = hit(deck, user_cards, user_value, user_deck_values, 1)
                print(f"You got a {last_card}, the values of your cards is '{user_value}'.")
                if user_value < 21:
                    user_bust = False
                elif user_value > 21:
                    user_bust = True
                    break
                elif user_value == 21:
                    break
                print(f"The dealer has {dealer_cards} with a value of '{dealer_value}'.")
                while True:
                    if dealer_value > 21:
                        dealer_deck_values["A"] = 1
                        if dealer_changed == False:
                            if "A" in dealer_cards:
                                dealer_value -= 10
                                dealer_changed = True
                        if dealer_value > 21:
                            break
                    if dealer_value >= 17:
                        print("The dealer must stand, good luck!")
                        break
                    else:
                        deck, dealer_cards, last_card, dealer_value, dealer_deck_values = hit(deck, dealer_cards, dealer_value, dealer_deck_values, 1)
                    print(f"The dealer got a '{last_card}', for a total value of '{dealer_value}'.")
                break
            elif action == "split" and can_split == True:
                print(f"You chose to split {user_cards}.")
                did_split = True
                hand1.append(user_cards[0])
                hand2.append(user_cards[-1])
                hand1_value = user_value // 2
                hand2_value = user_value // 2
                user_money -= bet
                hand1_bet = bet
                hand2_bet = bet
                print(f"Let's start with your first card of {hand1}, with a value of '{hand1_value}'. Time for your first card....")
                deck, hand1, last_card, hand1_value, hand1_deck_values = hit(deck, hand1, hand1_value, hand1_deck_values, 1)
                if hand1_value > 21:
                    hand1_deck_values["A"] = 1
                    if hand1_changed == False:
                        if "A" in hand1:
                            hand1_value -= 10
                            hand1_changed = True
                    if hand1_value > 21:
                        hand1_bust = True
                print(f"You got a {last_card}, the values of your cards is '{hand1_value}'.")
                if hand1_value < 21:
                    hand1_bust = False
                elif hand1_value > 21:
                    hand1_bust = True
                    break
                elif hand1_value == 21:
                    break
                hit_again = input("Would you like to hit again? Yes or No: ")
                hit_again = hit_again.lower()
                while True:
                    if hit_again == "no":
                        done_hitting_hand1 = True
                        break
                    elif hit_again == "yes":
                        done_hitting_hand1 = False
                        break
                    else:
                        print(f"Your action of '{hit_again}' is not a valid action.")
                        hit_again = input("Would you like to hit again? Yes or No: ")
                        hit_again = hit_again.lower()
                while hand1_bust == False and done_hitting_hand1 == False:
                    deck, hand1, last_card, hand1_value, hand1_deck_values = hit(deck, hand1, hand1_value, hand1_deck_values, 1)
                    if hand1_value > 21:
                        hand1_deck_values["A"] = 1
                        if hand1_changed == False:
                            if "A" in hand1:
                                hand1_value -= 10
                                hand1_changed = True
                        if hand1_value > 21:
                            hand1_bust = True
                            print(f"You got a '{last_card}', the values of your cards is '{hand1_value}'.")
                            break
                    print(f"You got a '{last_card}', the values of your cards is '{hand1_value}'.")
                    if hand1_value < 21:
                        hand1_bust = False
                    elif hand1_value > 21:
                        hand1_bust = True
                        break
                    elif hand1_value == 21:
                        break
                    hit_again = input("Would you like to hit again? Yes or No: ")
                    hit_again = hit_again.lower()
                    while True:
                        if hit_again == "no":
                            done_hitting_hand1 = True
                            break
                        elif hit_again == "yes":
                            done_hitting_hand1 = False
                            break
                        else:
                            print(f"Your action of '{hit_again}' is not a valid action.")
                            hit_again = input("Would you like to hit again? Yes or No: ")
                            hit_again = hit_again.lower()
                print(f"\nTime for your next hand, with a value of '{hand2_value}'.")
                deck, hand2, last_card, hand2_value, hand2_deck_values = hit(deck, hand2, hand2_value, hand2_deck_values, 1)
                if hand2_value > 21:
                    hand2_deck_values["A"] = 1
                    if hand2_changed == False:
                        if "A" in hand2:
                            hand2_value -= 10
                            hand2_changed = True
                    if hand2_value > 21:
                        hand2_bust = True
                print(f"You got a {last_card}, the values of your cards is '{hand2_value}'.")
                if hand2_value < 21:
                    hand2_bust = False
                elif hand2_value > 21:
                    hand2_bust = True
                    break
                elif hand2_value == 21:
                    break
                hit_again = input("Would you like to hit again? Yes or No: ")
                hit_again = hit_again.lower()
                while True:
                    if hit_again == "no":
                        done_hitting_hand2 = True
                        hit_again = False
                        break
                    elif hit_again == "yes":
                        done_hitting_hand2 = False
                        hit_again = True
                        break
                    else:
                        print(f"Your action of '{hit_again}' is not a valid action.")
                        hit_again = input("Would you like to hit again? Yes or No: ")
                        hit_again = hit_again.lower()
                while hand2_bust == False and done_hitting_hand2 == False:
                    deck, hand2, last_card, hand2_value, hand2_deck_values = hit(deck, hand2, hand2_value, hand2_deck_values, 1)
                    if hand2_value > 21:
                        hand2_deck_values["A"] = 1
                        if hand2_changed == False:
                            if "A" in hand2:
                                hand2_value -= 10
                                hand2_changed = True
                        if hand2_value > 21:
                            hand2_bust = True
                            print(f"You got a '{last_card}', the values of your cards is '{hand2_value}'.")
                            break
                    print(f"You got a '{last_card}', the values of your cards is '{hand2_value}'.")
                    if hand2_value < 21:
                        hand2_bust = False
                    elif hand2_value > 21:
                        hand2_bust = True
                        break
                    elif hand2_value == 21:
                        break
                    hit_again = input("Would you like to hit again? Yes or No: ")
                    hit_again = hit_again.lower()
                    while True:
                        if hit_again == "no":
                            done_hitting_hand2 = True
                            hit_again = False
                            break
                        elif hit_again == "yes":
                            done_hitting_hand2 = False
                            hit_again = True
                            break
                        else:
                            print(f"Your action of '{hit_again}' is not a valid action.")
                            hit_again = input("Would you like to hit again? Yes or No: ")
                            hit_again = hit_again.lower()
                while hit_again == False and done_hitting_hand2 == True and done_hitting_hand1 == True:
                            print(f"The dealer has '{dealer_cards}' with a value of '{dealer_value}'.")
                            while True:
                                if dealer_value > 21:
                                    dealer_deck_values["A"] = 1
                                    if dealer_changed == False:
                                        if "A" in dealer_cards:
                                            dealer_value -= 10
                                            dealer_changed = True
                                    if dealer_value > 21:
                                        print("The dealer busted!")
                                        break
                                elif dealer_value >= 17:
                                    print("The dealer must stand, good luck!")
                                    break
                                if hit_again == False:
                                    deck, dealer_cards, last_card, dealer_value, dealer_deck_values = hit(deck, dealer_cards, dealer_value, dealer_deck_values, 1)
                                    print(f"The dealer got a '{last_card}', for a total value of '{dealer_value}'.")
                            break
                break
            else:
                print(f"Your action of '{action}' is not a valid action.")
                action = input("Would you like to stand, hit, double-down, or split?: ")
                action = action.lower()
        if dealer_value > 21 and did_split == False:
            print(f"\nYou won! You had a value of '{user_value}' and the dealer had a value of '{dealer_value}'.")
            user_money += bet * 2
        elif user_value > 21 and did_split == False:
            print(f"\nYou lost! You had a value of '{user_value}' and the dealer had a value of '{dealer_value}'.")
        elif user_value == dealer_value and did_split == False:
            print(f"\nYou tied with the dealer! You had a value of '{user_value}' and the dealer had a value of '{dealer_value}'.")
            user_money += bet
        elif user_value > dealer_value and did_split == False:
            print(f"\nYou won! You had a value of '{user_value}' and the dealer had a value of '{dealer_value}'.")
            user_money += bet * 2
        elif user_value < dealer_value and did_split == False:
            print(f"\nYou lost! You had a value of '{user_value}' and the dealer had a value of '{dealer_value}'.")

        if dealer_value > 21 and did_split == True:
            if hand1_bust == False:
                print(f"\nYou won your first hand! You had a value of '{hand1_value}' and the dealer had a value of '{dealer_value}'.")
                user_money += hand1_bet * 2
                finished_hand1 = True
            if hand2_bust == False:
                print(f"\nYou won your second hand! You had a value of '{hand2_value}' and the dealer had a value of '{dealer_value}'.")
                user_money += hand2_bet * 2
                finished_hand2 = True
        if hand1_bust == True and did_split == True and finished_hand1 == False:
            print(f"\nYou lost your first hand! You had a value of '{hand1_value}' and the dealer had a value of '{dealer_value}'.")
            finished_hand1 = True
        if hand2_bust == True and did_split == True and finished_hand2 == False:
            print(f"\nYou lost your second hand! You had a value of '{hand2_value}' and the dealer had a value of '{dealer_value}'.")
            finished_hand2 = True
        if hand1_value == dealer_value and did_split == True and finished_hand1 == False:
            print(f"\nYou tied with the dealer on your first hand! You had a value of '{hand1_value}' and the dealer had a value of '{dealer_value}'.")
            user_money += bet
            finished_hand1 = True
        if hand2_value == dealer_value and did_split == True and finished_hand2 == False:
            print(f"\nYou tied with the dealer on your second hand! You had a value of '{hand2_value}' and the dealer had a value of '{dealer_value}'.")
            user_money += bet
            finished_hand2 = True
        if hand1_value > dealer_value and did_split == True and finished_hand1 == False:
            print(f"\nYou won your first hand! You had a value of '{hand1_value}' and the dealer had a value of '{dealer_value}'.")
            user_money += bet * 2
            finished_hand1 = True
        if hand2_value > dealer_value and did_split == True and finished_hand2 == False:
            print(f"\nYou won your second hand! You had a value of '{hand2_value}' and the dealer had a value of '{dealer_value}'.")
            user_money += bet * 2
            finished_hand2 = True
        if hand1_value < dealer_value and did_split == True and finished_hand1 == False:
            print(f"\nYou lost your first hand! You had a value of '{hand1_value}' and the dealer had a value of '{dealer_value}'.")
            finished_hand1 = True
        if hand2_value < dealer_value and did_split == True and finished_hand2 == False:
            print(f"\nYou lost your second hand! You had a value of '{hand2_value}' and the dealer had a value of '{dealer_value}'.")
            finished_hand2 = True