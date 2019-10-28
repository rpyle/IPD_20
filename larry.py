team_name = 'Larry'
strategy_name = 'No idea man'
strategy_description = 'Always lose by 4 points or so'

def move(my_history, their_history, my_score, their_score):
  total = 0
  doom = 0
  if len(my_history) > 150:
    return 'b'
  if len(my_history) < 2:
    return 'c'
  for i in their_history:
    if i == 'c':
      total += 1
      if total > 2:
        return 'c'
    if i == 'b':
      total = 0
      doom -= 1
      if doom < -2:
        return 'b'
  if 'b' in their_history[-2:]:
    return 'b'
  else:
    return 'c'
