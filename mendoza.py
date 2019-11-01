####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random
import os.path
import prisoners_dilemma
from prisoners_dilemma import *

team_name = 'Mendoza'
strategy_name = 'The Thief'
strategy_description = '''
Your code is mine! Will find the best strategy by running its own tournament, take that code and run it. It will also give itself a successful advantage with the most efficient slave.'''

game_flag = 0
best_strat_index = 0

def gather_intel():
    global game_flag
    global best_strat_index
    list_test = []
    my_modules = modules[:]
    if mendoza in my_modules:
        my_modules.remove(mendoza)
    scores, moves = prisoners_dilemma.play_tournament(my_modules)
    epic_list = scores[:]
    for index in range(len(my_modules)):
        list_test.append(sum(scores[index]))
    max_score = max(list_test)
    best_strat_index = list_test.index(max_score)
    if best_strat_index >= modules.index(mendoza):
        best_strat_index += 1
    game_flag = 1

def move(my_history, their_history, my_score, their_score):
    '''
    Returns 'c' or 'b' for collude or betray.
    '''

    if ' ' in their_history:
        if not(' ' in my_history):
            return 'l'
    if ' ' in their_history and ' ' in my_history:
        return 'b'

    global game_flag
    if game_flag == 0:
        gather_intel()

    return modules[best_strat_index].move(my_history, their_history, my_score, their_score)