team_name = 'Larry'
strategy_name = 'Gradual'
strategy_description = 'Always lose by 4 points or so'

def move(my_history, their_history, my_score, their_score):
  
  betrayals = 0
  counted = 0
  if len(my_history) < 2:
   return 'c'
  for i in their_history:
    if i == 'b':
      betrayals += 1

  if len(my_history) >= 100:
    return 'b'

  for i in reversed(my_history):
    if i == 'b':
      counted += 1
    else:
      break
  
  if betrayals - counted >= 1:
    print betrayals
    print counted
    print "betraying because betrayals higher than counted"
    return 'b'
  else:
    print "collude"
    return 'c'

    
  