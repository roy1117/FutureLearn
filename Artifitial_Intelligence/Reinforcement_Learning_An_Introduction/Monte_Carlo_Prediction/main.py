from prettytable import PrettyTable
import numpy as np
import random
import time
import copy
DECK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class GameHandler:
    def __init__(self, display_option=False, auto_play=True, delay=0, update_value_function=False):
        self.update_value_function = update_value_function
        self.delay = delay
        self.agent = Agent()
        self.display_option = display_option
        self.auto_play = auto_play
        self.game_display = PrettyTable()
        self.game_display.field_names = ["Index", "Dealer Cards", "Player Cards"]
        # state = [dealer face up card, player sum, usable ace]
        self.state = np.zeros(2)
        # result = [player win, dealer win]
        self.result = np.zeros(3)
        self.dealer_cards = []
        self.player_cards = []
        self.state_trace = []

    def start_game(self, number_of_plays):
        for i in range(number_of_plays):
            # resetting the game
            result = 0
            self.state_trace = []
            players_turn = True
            dealers_turn = False
            game_end = False
            self.state = np.zeros(2)
            self.dealer_cards = []
            self.player_cards = []
            self.game_display.clear_rows()
            self.initiate_game()
            # Player turn
            while players_turn:
                # black jack case
                summation = self.get_summation(self.player_cards)
                if summation == 21:
                    print("Player reached 21, Dealer's turn")
                    players_turn = False
                    dealers_turn = True
                    break

                if not self.auto_play:
                    action = input("which action? 1.hit 2.stand")
                else:
                    action = self.agent.get_action(self.state)
                    pass

                if action == "1":
                    choice = self.random_distribute()
                    self.player_cards.append(choice)
                    summation = self.get_summation(self.player_cards)
                    # Save the state
                    if summation <= 20:
                        self.state[1] = summation
                        state = copy.deepcopy(self.state)
                        self.state_trace.append(state)

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
                    result = -1
                    players_turn = False
                    dealers_turn = True
                    game_end = True

            while dealers_turn and not game_end:
                summation = self.get_summation(self.dealer_cards)
                if self.display_option:
                    self.game_display.add_row(["hidden card", self.dealer_cards[1], "X"])
                    self.game_display.add_row(["Sum", summation, "X"])
                    print(self.game_display)
                while summation < 17:
                    choice = self.random_distribute()
                    self.dealer_cards.append(choice)
                    summation = self.get_summation(self.dealer_cards)
                    if self.display_option:
                        self.game_display.add_row(["dealer's hit", choice, "X"])
                        self.game_display.add_row(["Sum", summation, "X"])
                        print(self.game_display)
                if summation > 21:
                    print('dealer burst')
                    self.result[0] += 1
                    result = 1
                elif summation == self.get_summation(self.player_cards):
                    # draw
                    self.result[2] += 1
                    print('the game draw')
                    result = 0
                elif summation > self.get_summation(self.player_cards):
                    # dealer win
                    self.result[1] += 1
                    result = -1
                    print('dealer won the game')
                else:
                    # player win
                    self.result[0] += 1
                    result = 1
                    print('player won the game')
                game_end = True
                dealers_turn = False
            print('---------------game end------------------')
            print(self.result)
            if self.update_value_function:
                self.agent.value_function_update(self.state_trace, result)
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
        summation = self.get_summation(self.player_cards)
        # Save the state
        if summation <= 20:
            self.state[1] = summation
            state = copy.deepcopy(self.state)
            self.state_trace.append(state)
        if self.display_option:
            self.game_display.add_row(["initial 1", self.dealer_cards[0], self.player_cards[0]])
            self.game_display.add_row(["initial 2", "Unknown", self.player_cards[1]])
            self.game_display.add_row(["initial Sum", "Unknown", self.get_summation(self.player_cards)])
            print(self.game_display)

    def get_summation(self, cards_deck):
        summation = 0
        for card in cards_deck:
            # check usable ace
            if card == 1:
                if summation <= 10:
                    card = 11
                else:
                    card = 1
            summation += card
        return summation


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
        self.policy = np.full((10, 17), 0.5)
        # A policy that sticks only when the summation is 20
        self.policy[:, 16] = 0
        self.value_function = np.zeros((10, 17))
        self.visit_count = np.zeros((10, 17))

    def get_action(self, state):
        dealer_card = int(state[0] - 1)
        player_sum = int(state[1] - 4)
        probability = self.policy[dealer_card][player_sum]
        action = random.choices(["1", "2"], [probability, 1 - probability])
        return action[0]

    def value_function_update(self, state_trace, result):
        for state in state_trace:
            dealer_card = int(state[0] - 1)
            player_sum = int(state[1] - 4)
            visited_count = self.visit_count[dealer_card][player_sum]
            # previous average
            prev_avg = self.value_function[dealer_card][player_sum]
            # new average
            new_avg = ((visited_count * prev_avg) + result) / (visited_count + 1)
            # value function update
            self.value_function[dealer_card][player_sum] = new_avg
            # visited count update
            self.visit_count[dealer_card][player_sum] += 1

    def get_value_function(self):
        return self.value_function


if __name__ == '__main__':
    handler = GameHandler(display_option=False, auto_play=True, delay=0, update_value_function=True)
    handler.start_game(50000)
    print(handler.get_value_function())
    # print(simulator.test_random_distribute(100000))
