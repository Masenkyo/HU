import json
import random

def CreateDeck():
    with open("cards.json", "r") as cards:
        data = json.load(cards)

    deck = []
    for suit in data["suits"]:
        for rank in data["ranks"]:
            deck.append({
                "rank": rank["name"],
                "suit": suit,
                "value": rank["value"]
            })
    return deck

def CalculateHand(hand):
    value = 0
    aces = 0

    for card in hand:
        if card["rank"] == "ace":
            aces += 1
            value += 11
        else:
            value += card["value"]

    while value > 21 and aces > 0:
        value -= 10
        aces -= 1

    return value

def BlackJack():
    remainingCards = CreateDeck()
    random.shuffle(remainingCards)

    playerHand = [remainingCards.pop(), remainingCards.pop()]
    dealerHand = [remainingCards.pop(), remainingCards.pop()]

    print(f"dealers second card: {dealerHand[1]["rank"]}")

    while True:
        handValue = CalculateHand(playerHand)
        print(f"Your hand: {[c["rank"] for c in playerHand]} | Score: {handValue}")
        if handValue > 21:
            break

        action = input("(H)it or (s)tand: ").lower()
        match action:
            case "h":
                playerHand.append(remainingCards.pop())
            case "s":
                break

    if handValue <= 21:
        print("\n--- dealers Turn ---")
        while True:
            dealerValue = CalculateHand(dealerHand)
            if dealerValue >= 17:
                break

            dealerHand.append(remainingCards.pop())

        print(f"dealer hits: {[c["rank"] for c in dealerHand]} | Score: {dealerValue}")
        if dealerValue > 21:
            return print("dealer bust, you won!!!")
        elif handValue > dealerValue:
            return print("you won!!!")
        elif handValue == dealerValue:
            return print("it's a tie, push!")
        else:
            return print("you lost...")
    else:
        return print("you bust")

if __name__ == "__main__":
    BlackJack()