## Coding logic for blackjack


## Language Used : 
Python
## version
python 3.7

Libraries used
1. random 
2. copy



##Intial State :
1. Deck of 52 cards
2. Empty hand for Player
3. Empty hand for Dealer



##Assumptions 
1. The player is dealt card first


## Additional Condition checking not mentioned in the problem statement
1. The player and dealer is tied if both stand at 21
2. When player/ dealer bust, only sum is given in message. Eg. if player is busted, the error message as per problem statement is 
"Player busts with 25"
Instead I added which cards they had when they were busted. I changed it to :
"Player busts [10,10,5] with 25"
3. Message displayed if irrelevant prompt (other than H/S) is added by user


##What I did well on this project
1. Code is readable and easy to follow
2. Tried my best to cover all cases possible, including tie condition
3. Comprehensive commenting

## Tradeoffs I encountered while programming and how you resolved them
1. In the question the dealer's last card is hidden (when drawing 2 cards)
Eg in case the dealer card were ['A', 9]
as per question 9 should have been hidded. But to ease appending process and calculating, I have hidden the first card in the dealer's hand,
ie Dealer's hidden card is 'A' 
in the above example


## What I would improve on this project given more time
1. Individually show K, Q, J they all appear as 10 while drawing card
2. I would make the code more modular
3. I think there are some extra condition for summing up the cards with and without "A", those I would have removed
4. Written test cases

## What manual tests you ran on the code
1. Ensured "A" calculation was running correctly : 

player_hand = ['A', 'A'] should yield sum  = 12
player_hand = [8, 'A', 7] yields value as 16 and not 26

2. Checked the code flow in case of HIT/STAND by player:
player is hit when H is prompted
player final is calculated when S is prompted
multiple H work for player and sum is updated

3. Checked the code flow in case of HIT/STAND by dealer:
dealer hits until sum < 17
stands >= 17














