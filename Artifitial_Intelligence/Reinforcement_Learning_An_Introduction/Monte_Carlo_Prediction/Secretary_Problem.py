import random
import copy
import numpy as np
from prettytable import PrettyTable

NUMBER_OF_CANDIDATES = 14
SCALE = 15
CENTER_MIN = 50
CENTER_MAX = 100
GAMMA = 0.2

class SecretaryGame():
    def __init__(self, print_result=False, print_summary=False, auto_play=False, exploring=True):
        self.print_summary = print_summary
        self.print_result = print_result
        self.auto_play = auto_play
        self.agent = Agent(exploring=exploring)
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

    def summary(self, win_count, lose_count, number_of_iterations, number_of_hiring, number_of_answer):
        if not self.print_summary:
            return
        else:
            self.game_summary.clear_rows()
            self.game_summary.add_row([number_of_iterations, win_count, lose_count])
            for i in range(len(number_of_hiring)):
                self.game_summary.add_row(['hire {0}'.format(i), int(number_of_hiring[i]), ''])
            for i in range(len(number_of_answer)):
                self.game_summary.add_row(['answer was {0}'.format(i), int(number_of_answer[i]), ''])
            print(self.game_summary)
            print(self.agent.policy)

    def play_game(self, number_of_iterations):
        win_count = 0
        lose_count = 0
        number_of_hiring = np.zeros(NUMBER_OF_CANDIDATES)
        number_of_answer = np.zeros(NUMBER_OF_CANDIDATES)
        for i in range(number_of_iterations):
            # Start of a episode of game
            self.agent.start_episode()
            is_best = 1
            action = 0
            centre = np.random.randint(CENTER_MIN, CENTER_MAX)
            candidates = np.random.normal(loc=centre, scale=SCALE, size=NUMBER_OF_CANDIDATES)
            # set default choice as the last one in case the play skips everything
            choice = len(candidates) - 1
            trace = []
            best_value = candidates[0]
            for i in range(len(candidates)):
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
                        action = self.agent.get_action(policy=self.agent.policy, choice_index=i, is_best=is_best)
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
            # end of an episode
            self.agent.end_episode()
            self.agent.update_action_value_function(trace=trace, result=result)
            self.result(choice=choice, candidates=candidates, result=result, answer=answer)
        self.summary(win_count, lose_count, number_of_iterations, number_of_hiring, number_of_answer)


class Agent():
    def __init__(self, exploring):
        self.exploring = exploring
        self.explored = False
        # Initializing policy -> 0.5, and action value function -> 0
        # We don't consider the last choice. At last we have to pick anyway
        self.policy = np.full((2, NUMBER_OF_CANDIDATES - 1), 0.5)
        self.action_value = np.zeros((2, NUMBER_OF_CANDIDATES, 2))
        self.visited_count = np.zeros((2, NUMBER_OF_CANDIDATES, 2))

    def start_episode(self):
        pass

    def end_episode(self):
        self.explored = False

    def update_action_value_function(self, trace, result):
        for choice_index, is_best, action in trace:
            visited_count = self.visited_count[is_best][choice_index][action]
            prev_avg = self.action_value[is_best][choice_index][action]
            new_avg = ((visited_count * prev_avg) + result) / (visited_count + 1)
            self.action_value[is_best][choice_index][action] = new_avg
            self.visited_count[is_best][choice_index][action] += 1

    def update_policy(self):
        for j in range(2):
            for i in range(NUMBER_OF_CANDIDATES - 1):
                # Hiring is stronger
                if self.action_value[j][i][0] > self.action_value[j][i][1]:
                    # 0 is 100% of hiring.
                    self.policy[j][i] = 0
                else:
                    # skipping is stronger
                    # 1 is 100% of skipping
                    self.policy[j][i] = 1

    def get_action(self, policy, choice_index, is_best):
        # Explore Exploit
        result = random.choices(['Explore', 'Exploit'], [GAMMA, 1 - GAMMA])[0]
        if result == 'Explore' and self.exploring and not self.explored:
            action = self.get_stochastic_aciton(0.5)
            self.explored = True
        else:
            action = self.get_stochastic_aciton(policy[is_best][choice_index])
        return action

    def test_get_action(self, policy, number_of_iteration):
        summary = np.zeros((2, NUMBER_OF_CANDIDATES, 2))
        for index in range(number_of_iteration):
            for i in range(len(summary)):
                for j in range(len(summary[i])):
                    action = self.get_action(policy, choice_index=j, is_best=i)
                    summary[i][j][action] += 1
        return summary

    def get_stochastic_aciton(self, probability):
        # 0 hire 1 skip
        action = random.choices([0, 1], [1 - probability, probability])
        return action[0]

    def test_get_stochastic_aciton(self, number_of_iterations, probability):
        hiring = 0
        skipping = 0
        for i in range(number_of_iterations):
            result = self.get_stochastic_aciton(probability)
            if result == 0:
                hiring += 1
            else:
                skipping += 1
        return number_of_iterations, hiring, skipping

    def set_policy(self, n_skip):
        self.policy = np.full((2, NUMBER_OF_CANDIDATES - 1), 1)
        self.policy[1][n_skip:] = 0


if __name__ == '__main__':
    game = SecretaryGame(print_result=False, print_summary=False, auto_play=True, exploring=True)

    # # Test get_stochastic_aciton function
    # number_of_iterations, hiring, skipping = game.agent.test_get_stochastic_aciton(1000, 0)
    # print(number_of_iterations, hiring, skipping)

    # # Test get_action function
    # policy = [[1, 1, 1, 1], [0, 0, 0, 0]]
    # summary = game.agent.test_get_action(policy=policy, number_of_iteration=1000)
    # print(summary)

    for j in range(10):
        for i in range(500):
            game.play_game(number_of_iterations=100)
            game.agent.update_policy()
        print(game.agent.policy)
        print(game.agent.visited_count)
        print(game.agent.action_value)
        game.agent.visited_count = np.zeros((2, NUMBER_OF_CANDIDATES, 2))

    # # Test optimal policy
    # game.agent.set_policy(n_skip=5)
    # game.play_game(number_of_iterations=10000)

    print('Finish')



