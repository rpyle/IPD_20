from random import *
team_name = 'Grant'
strategy_name = 'Copy 5'
strategy_description = ''
    
def move(my_history, their_history, my_score, their_score):

  if len(their_history)==0:
    return 'c'

  elif len(their_history) <25:
    return their_history[-1]

  elif 'b' in their_history[-25:]:
    return 'b'

  else:
    return 'c'