import random
import copy


##Make a deck from which cards will be drawn
deck =  [2] * 4 + [3] * 4 + [4] * 4 + [5] * 4 + [6] * 4 + [7] * 4 + [8] * 4  + [9] * 4 + [10] * 16 + ['A'] * 4 


##Assign a sum to the hand, handle "A" value accordingly
def assign_a_value(hand):
    ## To assign value of "A" we sort the cards and see if we want to assign 1 or 11
    hand.sort(key = lambda item: ([str,int].index(type(item)), item) , reverse = True) ## All "A" are in the end
    
    sum_of_hand = 0
    for i in hand:
        if i != 'A':
           sum_of_hand += i
        else: 
            if sum_of_hand + 11 >21: 
                sum_of_hand += 1 ##Assign "A" as 1 to avoid Bust condition
            else:
                sum_of_hand += 11 ##Maximize as +11 to get closest and lesser/equal value to 21
    return sum_of_hand

## Function to draw a card and calculate sum
def hit_chosen(hand, deck):
    select_index = random.randint(0, len(deck)-1)
    card_selected = deck.pop(select_index)
    hand.append(card_selected)

    if  'A' in  hand:
        hitter_hand_test = copy.deepcopy(hand)
        sum_of_hitter_cards = assign_a_value(hitter_hand_test) ## Calculate sum 
    else:
        sum_of_hitter_cards = sum(hand)
    return sum_of_hitter_cards


##Intially both dealer and player have empty hand
player_hand = []
dealer_hand =  []
## Dealing initial cards of length 2 each

##for player
##  the player is dealt first

while len(player_hand) != 2:
    select_index = random.randint(0, len(deck)-1)
    card_selected = deck.pop(select_index)
    player_hand.append(card_selected)

##for dealer
while len(dealer_hand) != 2:
    select_index = random.randint(0, len(deck)-1)
    card_selected = deck.pop(select_index)
    dealer_hand.append(card_selected)



## Show initial cards and score!!
## for player
##choose to deal with A or not

sum_of_player_cards = 0
if  'A' in  player_hand:
    player_hand_test = copy.deepcopy(player_hand)
    sum_of_player_cards = assign_a_value(player_hand_test)
else:
    sum_of_player_cards = sum(player_hand)

##Display Initial cards, hide 1st card of dealer
print(f"Player has: {player_hand} = {sum_of_player_cards}")
print(f"Dealer has: ? {dealer_hand[1:]} = ?") 

##Ask player if they want to Hit or Stand?
while(sum_of_player_cards < 21):
    hit_or_stand = input("Would you like to (H)it or (S)tand?")
    
    if hit_or_stand == 'H':
        sum_of_player_cards = hit_chosen(player_hand, deck)
        ##hit and calculate updated sum
        if sum_of_player_cards > 21:
            print(f"Player busts {player_hand} with {sum_of_player_cards}") ##bust for player if player card sum >21
            print("Dealer wins")
            exit()
        if sum_of_player_cards == 21: ## perfect score for player when sum on card =21
            
            print(f"Player Scored {str(sum_of_player_cards)}  with  {player_hand}" )
            print("Player Wins!")
            print("Blackjack!")
            exit()

        ##else if still sum on player card <21 
        ## summarize status before prompting user to hit or stand
        print(f"Player has: {player_hand} = {sum_of_player_cards}") 
        print(f"Dealer has: ? {dealer_hand[1:]} = ?") 

    elif hit_or_stand == 'S': ##if user prompts on standing
        print(f"Player stands with: {player_hand} = {sum_of_player_cards}")
        break
    else: ##incase erroneous input given by user
        print("Please choose valid option")

##dealer deals their cards :
sum_of_dealer_cards =  assign_a_value(dealer_hand)
while(sum_of_dealer_cards <17): ##dealer hits until sum on dealer card <17
    
    print(f"Dealer has: {dealer_hand} = {sum_of_dealer_cards}")
    print("Dealer hits")
    sum_of_dealer_cards = hit_chosen(dealer_hand, deck)
    ##if upon hitting the dealer gets sum > 21 it is bust condition for dealer, then player wins
    if(sum_of_dealer_cards > 21):
        print(f"Dealer busts {dealer_hand} with {sum_of_dealer_cards}")
        print("Player wins")
        exit()

    
##dealer stands after score >= 17
print(f"Dealer has: {dealer_hand} = {sum_of_dealer_cards}")
print("Dealer stands")

##when both have chosen to stand the one with highest sum wins
if(sum_of_dealer_cards > sum_of_player_cards):
    print("Dealer Wins")
    print(f"{dealer_hand} = {sum_of_dealer_cards} to Player's {player_hand} = {sum_of_player_cards}")
elif(sum_of_dealer_cards < sum_of_player_cards):
    print("Player Wins")
    print(f"{player_hand} = {sum_of_player_cards} to Dealer's  {dealer_hand} = {sum_of_dealer_cards}")
else:
    print("Tied")



