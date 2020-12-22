import time
start = time.time()
with open('dayTwentyTwoInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

playerOneNotDone = True
playerOneCards = []
playerTwoCards = []
for line in content:
    if line.isdigit():
        if playerOneNotDone:
            playerOneCards.append(int(line))
        else:
            playerTwoCards.append(int(line))
    elif line == '':
        playerOneNotDone = False


def play_combat_simple(player_one_cards, player_two_cards):
    while len(player_one_cards) > 0 and len(player_two_cards) > 0:
        player_one_card = player_one_cards.pop(0)
        player_two_card = player_two_cards.pop(0)
        if player_one_card > player_two_card:
            player_one_cards.append(player_one_card)
            player_one_cards.append(player_two_card)
        else:
            player_two_cards.append(player_two_card)
            player_two_cards.append(player_one_card)


playerOneCardsPart2 = playerOneCards[:]
playerTwoCardsPart2 = playerTwoCards[:]

play_combat_simple(playerOneCards, playerTwoCards)
winner = playerOneCards if len(playerOneCards) > 0 else playerTwoCards
valueOfHand = 0
valueCurrentCard = len(winner)
for card in winner:
    valueOfHand += valueCurrentCard * card
    valueCurrentCard -= 1

print('part one:', valueOfHand)


# returns true if player one wins
def play_combat_recursive(player_one_cards, player_two_cards):
    history = []
    while len(player_one_cards) > 0 and len(player_two_cards) > 0:
        if [player_one_cards, player_two_cards] in history:
            return True
        else:
            history.append([player_one_cards[:], player_two_cards[:]])

        player_one_card = player_one_cards.pop(0)
        player_two_card = player_two_cards.pop(0)

        if len(player_one_cards) >= player_one_card and len(player_two_cards) >= player_two_card:
            player_one_won_round = play_combat_recursive(
                                        player_one_cards[0:player_one_card],
                                        player_two_cards[0:player_two_card])
        else:
            player_one_won_round = player_one_card > player_two_card

        if player_one_won_round:
            player_one_cards.append(player_one_card)
            player_one_cards.append(player_two_card)
        else:
            player_two_cards.append(player_two_card)
            player_two_cards.append(player_one_card)

    return len(player_one_cards) > 0


playerOneWon = play_combat_recursive(playerOneCardsPart2, playerTwoCardsPart2)

winnerPart2 = playerOneCardsPart2 if playerOneWon else playerTwoCardsPart2
valueOfHand = 0
valueCurrentCard = len(winnerPart2)
for card in winnerPart2:
    valueOfHand += valueCurrentCard * card
    valueCurrentCard -= 1

print('part 2:', valueOfHand)
print('It took', time.time()-start, 'seconds.')
