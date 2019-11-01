team_name = 'Robert'
strategy_name = 'Fine until betrayal or 100th round, then I want to win.'
strategy_description = '''\
Betray if betrayed and lower score.
If I haven't been betrayed yet, I'll betray starting with the 100th round.
'''
def move(my_history, their_history, my_score, their_score):
   
    # If the other player has betrayed or this is the last half of the game,
 if 'b' in their_history or len(their_history) > 100:
   if their_score >= my_score:
    return 'b'
   else:
     return 'c'  
 else:
   return 'c'  
