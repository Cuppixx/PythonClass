"""17+4 card game"""
import random


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4


def deal_card():
    """Function to deal a card"""
    return random.choice(deck)


def calculate_score(hand):
    """Function to calculate the total score"""
    score = sum(hand)
    aces = hand.count(11)
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score


def display_hand(player_hand, dealer_hand, reveal_dealer=False):
    """Function to display hand and score"""
    print(f"Your hand: {player_hand} (Score: {calculate_score(player_hand)})")
    if reveal_dealer:
        print(f"Dealer's hand: {dealer_hand} (Score: {calculate_score(dealer_hand)})")
    else:
        print(f"Dealer's hand: [{dealer_hand[0]}, ?]")


def play_game():
    """Game logic"""
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        display_hand(player_hand, dealer_hand)
        if calculate_score(player_hand) == 21:
            print("Blackjack! You win!")
            game_over = True
        elif calculate_score(player_hand) > 21:
            print("You busted! Dealer wins.")
            game_over = True
        else:
            action = input("Do you want to 'hit' or 'stand'? ").lower()
            if action == "hit":
                player_hand.append(deal_card())
            elif action == "stand":
                game_over = True

    if calculate_score(player_hand) <= 21:
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deal_card())
        display_hand(player_hand, dealer_hand, reveal_dealer=True)

        if calculate_score(dealer_hand) > 21:
            print("Dealer busted! You win.")
        elif calculate_score(dealer_hand) > calculate_score(player_hand):
            print("Dealer wins.")
        elif calculate_score(dealer_hand) < calculate_score(player_hand):
            print("You win!")
        else:
            print("It's a tie!")


play_game()
