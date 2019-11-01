import random
def stinky(length):
    return (("bruh \n" * (length ** length)))

team_name = 'Larry'
strategy_name = 'death with a twist %s' % (stinky(10))
strategy_description = 'death but if the score is over 150 then betray'

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
  else:
    return 'c'


 
