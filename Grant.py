team_name = 'Grant'
strategy_name = 'Forgive25'
strategy_description = 'If betrayed in the last twentyfive moves betray'

def move(my_history, their_history, my_score, their_score):

  if len(their_history)==0:
    return 'c'

  elif len(their_history) <25 and 'b' in their_history:
    return 'b'
  elif 'b' in their_history[-25:]:
    return 'b'
  else:
    return 'c'