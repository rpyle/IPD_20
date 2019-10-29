team_name = 'Hinesly'
strategy_name = 'Collude 1st, then collude if other player has colluded more times than betrayed.'
strategy_description = 'Collude on 1st round, then collude only if the other player has colluded more times than betrayed.'
    
def move(my_history, their_history, my_score, their_score):
  if len(their_history) == 0 or len(my_history) == 0:
    return 'c'
  else:
    c_count = 0
    b_count = 0
    for item in their_history:
      if item == 'c':
        c_count += 1
      else:
        b_count += 1
    if c_count >= b_count:
      return 'c'
    else:
      return 'b'
  
  

