import random
import copy
import numpy as np
from prettytable import PrettyTable

NUMBER_OF_CANDIDATES = 5
SCALE = 15
CENTER_MIN = 50
CENTER_MAX = 100


class SecretaryGame():
    def __init__(self, print_result=False, auto_play=False):
        self.print_result = print_result
        self.auto_play = auto_play
        self.agent = Agent()
        self.game_summary = PrettyTable()
        self.game_summary.field_names = ['Total number of games', 'Win count', 'Lose count']


    def result(self, choice, candidates, result, answer):
        if not self.print_result:
            return
        else:
            print('---------Result---------------------')
            print('Your choice was {0}'.format(choice))
            if result:
                print('You got it right!!')
            else:
                print('Sorry, the answer was {0}'.format(answer))
            print('------Candidates was like blow------')
            print(candidates)

    def print_summary(self, win_count, lose_count, number_of_iterations, number_of_hiring, number_of_answer):
        self.game_summary.add_row([number_of_iterations, win_count, lose_count])
        for i in range(len(number_of_hiring)):
            self.game_summary.add_row(['hire {0}'.format(i), int(number_of_hiring[i]), ''])
        for i in range(len(number_of_answer)):
            self.game_summary.add_row(['answer was {0}'.format(i), int(number_of_answer[i]), ''])
        print(self.game_summary)

    def play_game(self, number_of_iterations):
        win_count = 0
        lose_count = 0
        number_of_hiring = np.zeros(NUMBER_OF_CANDIDATES)
        number_of_answer = np.zeros(NUMBER_OF_CANDIDATES)
        for i in range(number_of_iterations):
            # Start of a episode of game
            is_best = 1
            action = 0
            centre = np.random.randint(CENTER_MIN, CENTER_MAX)
            candidates = np.random.normal(loc=centre, scale=SCALE, size=NUMBER_OF_CANDIDATES)
            # set default choice as the last one in case the play skips everything
            choice = len(candidates) - 1
            trace = []
            best_value = candidates[0]
            for i in range(len(candidates)):
                print(candidates[i])
                if candidates[i] >= best_value:
                    is_best = 1
                    best_value = candidates[i]
                else:
                    is_best = 0
                if not self.auto_play:
                    action = int(input('please select your action 0. Hire 1. Skip'))
                else:
                    if i == len(candidates) - 1:
                        action = 0
                    else:
                        action = self.agent.get_action(choice_index=i, is_best=is_best)
                if not i == len(candidates) - 1:
                    trace.append([i, is_best, action])

                if action == 0 or i == len(candidates) - 1:
                    choice = i
                    answer = np.argmax(candidates)
                    if choice == answer:
                        result = True
                        win_count += 1
                    else:
                        result = False
                        lose_count += 1
                    number_of_hiring[choice] += 1
                    number_of_answer[answer] += 1
                    break
            self.agent.update_action_value_function(trace=trace, result=result)
            self.result(choice=choice, candidates=candidates, result=result, answer=answer)
        self.print_summary(win_count, lose_count, number_of_iterations, number_of_hiring, number_of_answer)


class Agent():
    def __init__(self):
        # Initializing policy -> 0.5, and action value function -> 0
        # We don't consider the last choice. At last we have to pick anyway
        self.policy = [[0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5]]
        self.action_value = [[[0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0]]]
        self.visited_count = [[0, 0, 0, 0], [0, 0, 0, 0]]

    def update_action_value_function(self, trace, result):
        for choice_index, is_best, action in trace:
            visited_count = self.visited_count[is_best][choice_index]
            prev_avg = self.action_value[is_best][choice_index][action]
            new_avg = ((visited_count * prev_avg) + result) / (visited_count + 1)
            self.action_value[is_best][choice_index][action] = new_avg
            self.visited_count[is_best][choice_index] += 1
            # self.update_policy()

    def update_policy(self):
        for j in range(2):
            for i in range(NUMBER_OF_CANDIDATES - 1):
                # Hiring is stronger
                if self.action_value[j][i][0] >= self.action_value[j][i][1]:
                    self.policy[j][i] = 0
                else:
                    # skipping is stronger
                    self.policy[j][i] = 1



    def get_action(self, choice_index, is_best):
        action = self.get_stochastic_aciton(self.policy[is_best][choice_index])
        return action

    def get_stochastic_aciton(self, probability):
        # 0 hire 1 skip
        action = random.choices([0, 1], [probability, 1 - probability])
        return action[0]

if __name__ == '__main__':
    game = SecretaryGame(print_result=False, auto_play=True)
    game.play_game(number_of_iterations=10000)
    print('Finish')


