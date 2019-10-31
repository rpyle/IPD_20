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
from prisoners_dilemma import modules
from itertools import permutations
import mendoza

team_name = 'Mendoza'
strategy_name = 'Future Vision'
strategy_description = '''\
I can see the future.'''

response_list = []
c_count = 0
b_count = 0

perfect_list = []
possible_outputs = ['c','b']
gameAmount = 0
fake_game_flag = 0
list_test = []
all_possible_list = []
for i in range(0,200):
  all_possible_list.append('c')
  all_possible_list.append('d')

master_list = permutations(all_possible_list, 50)

def gather_intel(game_number):
  global fake_game_flag
  global possible_outputs
  global master_list
  global list_test
  global my_own_code
  perfect_list = []
  enemy_code = modules[game_number]
  fake_game_flag = 1
  best_score = -1000
  for list_pos in master_list:
    list_test = list_pos[:]
    answer = game_iterative_rounds(mendoza, enemy_code)
    if answer > best_score:
      perfect_list = list_test[:]
      best_score = answer(0)
  for value in perfect_list[:]:
    perfect_list.append(value)
  fake_game_flag = 0


def game_iterative_rounds(player1, player2):
    '''
    Plays a random number of rounds (between 100 and 200 rounds)
    of the iterative prisoners' dilemma between two strategies.
    player1 and player2 are modules.
    Returns 4-tuple, for example ('cc', 'bb', -200, 600)
    but with much longer strings
    '''
    number_of_rounds = 50
    moves1 = ''
    moves2 = ''
    score1 = 0
    score2 = 0
    for round in range(number_of_rounds):
        score1, score2, moves1, moves2 = game_round(player1, player2, score1, score2, moves1, moves2)
    return score1

def game_round(player1, player2, score1, score2, moves1, moves2):
    '''
    Calls the move() function from each module which return
    'c' or 'b' for collude or betray for each player.
    The history is provided in a string, e.g. 'ccb' indicates the player
    colluded in the first two rounds and betrayed in the most recent round.
    Returns a 2-tuple with score1 and score2 incremented by this round
    '''

    RELEASE = 0 # (R, "reward" in literature) when both players collude
    TREAT = 100 # (T, "temptation" in literature) when you betray your partner
    SEVERE_PUNISHMENT = -500 # (S, "sucker" in literature) when your partner betrays you
    PUNISHMENT = -250 # (P) when both players betray each other

    # Keep T > R > P > S to be a Prisoner's Dilemma
    # Keep 2R > T + S to be an Iterative Prisoner's Dilemma

    ERROR = -250

    # Get the two players' actions and remember them.
    action1 = player1.move(moves1, moves2, score1, score2)
    action2 = player2.move(moves2, moves1, score2, score1)
    if (type(action1) != str) or (len(action1) != 1):
        action1=' '
    if (type(action2) != str) or (len(action2) != 1):
        action2=' '

    # Change scores based upon player actions.
    actions = action1 + action2
    if actions == 'cc':
        # Both players collude; get reward.
        score1 += RELEASE
        score2 += RELEASE
    elif actions == 'cb':
        # Player 1 colludes, player 2 betrays; get severe, treat.
        score1 += SEVERE_PUNISHMENT
        score2 += TREAT
    elif actions == 'bc':
        # Player 1 betrays, player 2 colludes; get treat, severe.
        score1 += TREAT
        score2 += SEVERE_PUNISHMENT
    elif actions == 'bb':
        # Both players betray; get punishment.
        score1 += PUNISHMENT
        score2 += PUNISHMENT
    else:
        # Both players get the "error score" if someone's code returns an improper action.
        score1 += ERROR
        score2 += ERROR

    # Append the actions to the previous histories.
    if action1 in 'bc':
        moves1 += action1
    else:
        moves1 += ' '
    if action2 in 'bc':
        moves2 += action2
    else:
        moves2 += ' '

    # Return scores incremented by this round's results.
    return (score1, score2, moves1, moves2)

def play_ball((my_history, their_history, my_score, their_score)):
  global gameAmount
  global fake_game_flag
  global list_test
  if len(my_history) == 0:
    gameAmount += 1
  if fake_game_flag == 1:
    return list_test[len(my_history)]
  else:
    return perfect_list[len(my_history)]

def create_list():
  global response_list
  global c_count
  global b_count
  response_list = []
  c_count = 0
  b_count = 0
  for i in range(20):
    response_list.append('c')
    c_count += 1
    response_list.append('b')
    b_count += 1
  for i in range(20):
    response_list.append('c')
    c_count += 1

def botStrat(my_history, their_history, my_score, their_score):
  global response_list
  global c_count
  global b_count

  if len(my_history)==0: # It's the first round; create the list.
    create_list()
  else:
    recent_round_them = their_history[-1]
    recent_round_me = my_history[-1]

    if recent_round_me == 'c' and recent_round_them == 'b':
      if c_count >= 4:
        response_list.remove('c')
        response_list.remove('c')
        response_list.remove('c')
        c_count -= 3

    if recent_round_me == 'b' and recent_round_them == 'b':
      if b_count >= 2:
        response_list.append('b')
        b_count += 1

    if recent_round_me == 'c' and recent_round_them == 'c':
      if c_count >= 2:
        response_list.append('c')
        c_count += 1

    if recent_round_me == 'b' and recent_round_them == 'c':
      if b_count >= 3:
        response_list.append('b')
        response_list.append('b')
        b_count -= 2

  length = len(response_list) - 1
  random_choice = response_list[random.randint(1,length)]
  return random_choice

def copy_cat(my_history, their_history, my_score, their_score):
  if len(my_history)==0: # It's the first round; create the list.
    return 'c'
  else:
    return their_history[-1]

def move(my_history, their_history, my_score, their_score):
  '''
  Returns 'c' or 'b' for collude or betray.
  '''
  global gameAmount
  global fake_game_flag
  if fake_game_flag == 0:
    gather_intel(gameAmount)
  #return botStrat(my_history, their_history, my_score, their_score)
  #return copy_cat(my_history, their_history, my_score, their_score)
  return play_ball((my_history, their_history, my_score, their_score))