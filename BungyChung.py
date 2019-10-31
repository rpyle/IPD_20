####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Justin Taing'
strategy_name = 'Stop Snitching'
strategy_description = 'Start out with a betray, if they betray you, switch to always betray'

def move(my_history, their_history, my_score, their_score):
  if len(my_history) == 0:
    return 'c'
  elif len(my_history) < 3:
    return 'b'
  elif their_history[-1] or their_history[-2] == 'c':
    return 'b'
  else:
    return their_history[-1]

