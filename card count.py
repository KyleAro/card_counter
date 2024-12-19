import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

def deal_card():
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_count(card, count):
    if card in [2, 3, 4, 5, 6]:
        count += 1
    elif card in [10, 11]:
        count -= 1
    return count

def simulate_game():
    count = 0
    player_cards = []
    
    # Deal initial two cards
    for _ in range(2):
        card = deal_card()
        count = calculate_count(card, count)
        player_cards.append(card)
    
    print("Player cards:", player_cards)
    print("Current count:", count)
    
    # Simulate player actions
    while True:
        action = input("Enter 'h' to hit or 's' to stand: ")
        
        if action == 'h':
            card = deal_card()
            count = calculate_count(card, count)
            player_cards.append(card)
            print("Player cards:", player_cards)
            print("Current count:", count)
            
            if sum(player_cards) > 21:
                print("Bust! You lose.")
                break
        elif action == 's':
            print("Player stands.")
            break
    
    # Simulate dealer's actions
    dealer_cards = []
    while sum(dealer_cards) < 17:
        card = deal_card()
        dealer_cards.append(card)
    
    print("Dealer cards:", dealer_cards)
    
    # Determine the result
    if sum(dealer_cards) > 21:
        print("Dealer busts! You win.")
    elif sum(dealer_cards) > sum(player_cards):
        print("Dealer wins.")
    elif sum(dealer_cards) < sum(player_cards):
        print("You win!")
    else:
        print("It's a tie!")

# Loop for playing multiple rounds
while True:
    simulate_game()
    
    play_again = input("Do you want to play again? (y/n) ")
    if play_again != 'y':
        break
