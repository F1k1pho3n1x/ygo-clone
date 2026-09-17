from random import choice
from typing import ClassVar

from Card import Card, Card_ExtraMonster
from Effect import CardEvent

# GLOBAL GAME SETTINGS (GENERAL)


###########

class Player:
    PlayerName: str
    LifePoints: int
    IsTurn: bool
    NormalSummonUsed: bool

    LingeringEffects: list[CardEvent]

    Deck: list[Card] = []
    ExtraDeck: list[Card_ExtraMonster]
    Hand: list[Card]
    Graveyard: list[Card]
    BanishedZone: list[Card]

    def __init__(self, PlayerName):
        self.PlayerName = PlayerName
        self.LifePoints = DuelEngine.STARTING_LIFE_POINTS

    def DrawCard(self):
        if len(self.Deck) > 0:
            current_card = self.Deck.pop()
            self.Hand.append(current_card)
        else:
            self.GameOverNotify()
            pass

    def ShuffleDeck(self):
        copy_deck = []
        #deck_size = len(self.Deck)
        deck_size = 30
        numbers = [x for x in range(deck_size)]
        selected_numbers = []
        print(numbers)
        for i in range(deck_size):
            chosen_number = choice(numbers)
            selected_numbers.append(chosen_number)
            numbers.remove(chosen_number)
        print(numbers)
        print(selected_numbers)
        # Replace this logic to apply to cards, use the same IDs for shuffling, just on cards
        card1 = selected_numbers[0]
        for i in range(deck_size):
            card2 = selected_numbers[card1]
            selected_numbers[card1] = card1
            card1 = card2
        print(selected_numbers)

    def IncreaseLifePoints(self, amount):
        self.LifePoints += amount

    def DecreaseLifePoints(self, amount):
        self.LifePoints -= amount
        if self.LifePoints <= 0:
            self.GameOverNotify()

    def GameOverNotify(self):
        pass


class DuelEngine:

    # DUEL SPECIFIC SETTINGS (CURRENT DUEL SETUP)

    STARTING_LIFE_POINTS: ClassVar[int] = 6000
    STARTING_HAND_SIZE: ClassVar[int] = 4
    DRAW_CARDS_PER_TURN: ClassVar[int] = 1
    NORMAL_SUMMONS_PER_TURN: ClassVar[int] = 1


    ############

    Hand_Player: list[Card]
    Hand_Opponent: list[Card]

    def __init__(self):
        player = Player("Player")
        opponent = Player("Opponent")

        first_player = DuelEngine.DecideFirstPlayer(player, opponent)

        for i in range(DuelEngine.STARTING_HAND_SIZE):
            player.DrawCard()
            opponent.DrawCard()


        while True:
            pass


    def PlayTurn(self):
        pass

    @staticmethod
    def DecideFirstPlayer(self, player1, player2):
        player1_pick = "ROCK"
        player2_pick = "SCISSORS"
        # play Rock Paper Scissors
        if player1_pick == "ROCK" and player2_pick == "SCISSORS" \
            or player1_pick == "SCISSORS" and player2_pick == "PAPER" \
            or player1_pick == "PAPER" and player2_pick == "ROCK":
            return player1
        elif player2_pick == "ROCK" and player2_pick == "SCISSORS" \
            or player2_pick == "SCISSORS" and player2_pick == "PAPER" \
            or player2_pick == "PAPER" and player2_pick == "ROCK":
            return player2

        # TIED, Re-run
        return DuelEngine.DecideFirstPlayer(player1, player2)



p = Player()
p.ShuffleDeck()