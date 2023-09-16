from prettytable import PrettyTable
import numpy as np
import random
import time

DECK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class GameHandler:
    def __init__(self, display_option=False, auto_play=True, delay=0):
        self.delay = delay
        self.agent = Agent()
        self.display_option = display_option
        self.auto_play = auto_play
        self.game_display = PrettyTable()
        self.game_display.field_names = ["Index", "Dealer Cards", "Player Cards"]
        # state = [dealer face up card, player sum, usable ace]
        self.state = np.zeros(3)
        # result = [player win, dealer win, draw]
        self.result = np.zeros(3)
        self.dealer_cards = []
        self.player_cards = []

    def start_game(self, number_of_plays):
        for i in range(number_of_plays):
            # resetting the game
            players_turn = True
            dealers_turn = False
            game_end = False
            self.state = np.zeros(3)
            self.dealer_cards = []
            self.player_cards = []
            self.game_display.clear_rows()
            self.initiate_game()
            # Player turn
            while players_turn:
                if not self.auto_play:
                    action = input("which action? 1.hit 2.stand")
                else:
                    action = self.agent.get_action(self.state)
                    pass

                if action == "1":
                    choice = self.random_distribute()
                    self.player_cards.append(choice)
                    summation = sum(self.player_cards)
                    # Save the state
                    self.state[1] = summation

                    if self.display_option:
                        self.game_display.add_row(["player hit", "X", choice])
                        self.game_display.add_row(["Sum", "X", summation])
                        print(self.game_display)
                else:
                    print("Player stands, Dealer's turn")
                    players_turn = False
                    dealers_turn = True
                    break
                if summation == 21:
                    print("Player reached 21, Dealer's turn")
                    players_turn = False
                    dealers_turn = True
                    break
                elif summation > 21:
                    print("Player burst, player lost")
                    self.result[1] += 1
                    players_turn = False
                    dealers_turn = True
                    game_end = True

            while dealers_turn and not game_end:
                summation = sum(self.dealer_cards)
                if self.display_option:
                    self.game_display.add_row(["hidden card", self.dealer_cards[1], "X"])
                    self.game_display.add_row(["Sum", summation, "X"])
                    print(self.game_display)
                while summation < 17:
                    choice = self.random_distribute()
                    self.dealer_cards.append(choice)
                    summation = sum(self.dealer_cards)
                    if self.display_option:
                        self.game_display.add_row(["dealer's hit", choice, "X"])
                        self.game_display.add_row(["Sum", summation, "X"])
                        print(self.game_display)
                if summation > 21:
                    print('dealer burst')
                    self.result[0] += 1
                elif summation == sum(self.player_cards):
                    # draw
                    self.result[2] += 1
                    print('the game draw')
                elif summation > sum(self.player_cards):
                    # dealer win
                    self.result[1] += 1
                    print('dealer won the game')
                else:
                    # player win
                    self.result[0] += 1
                    print('player won the game')
                game_end = True
                dealers_turn = False
            print('---------------game end------------------')
            print(self.result)
            time.sleep(self.delay)

    def initiate_game(self):
        # distribute a card to dealer
        # face up the card
        choice = self.random_distribute()
        self.dealer_cards.append(choice)
        # Save the state
        self.state[0] = choice

        # distribute a card to player
        # face up the card
        choice = self.random_distribute()
        self.player_cards.append(choice)

        # distribute a card to dealer
        # face down the card
        choice = self.random_distribute()
        self.dealer_cards.append(choice)

        # distribute a card to player
        # face up the card
        choice = self.random_distribute()
        self.player_cards.append(choice)
        # Save the state
        self.state[1] = sum(self.player_cards)

        if self.display_option:
            self.game_display.add_row(["initial 1", self.dealer_cards[0], self.player_cards[0]])
            self.game_display.add_row(["initial 2", "Unknown", self.player_cards[1]])
            self.game_display.add_row(["initial Sum", "Unknown", sum(self.player_cards)])
            print(self.game_display)

    def random_distribute(self):
        choice = random.choice(DECK)
        return choice

    def test_random_distribute(self, iteration):
        summary = np.zeros(11)
        for i in range(iteration):
            choice = self.random_distribute()
            summary[choice] += 1
        return summary

    def get_state(self):
        return self.state

class Agent:
    def __init__(self):
        # policy = [dealer card, player card summation, usable ace]
        # TODO
        self.policy = np.full((10, 20, 2), 0.5)

    def get_action(self, state):
        dealer_card = int(state[0] - 1)
        player_sum = int(state[1] - 2)
        usable_ace = int(state[2])
        probability = self.policy[dealer_card][player_sum][usable_ace]
        action = random.choices(["1", "2"], [probability, 1-probability])
        return action[0]

if __name__ == '__main__':
    handler = GameHandler(display_option=True, auto_play=True, delay=0)
    handler.start_game(10)
    # print(simulator.test_random_distribute(100000))

