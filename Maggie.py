team_name = 'Maggie'
strategy_name = 'strat'
strategy_description = 'return \'\', \' \', or int 4'

import random

def move(my_history, their_history, my_score, their_score):
   if 'b' in their_history[-15:]: # If the other player has betrayed within last 15 rounds, 
        return 'b'               
    else:
        if random.random()<0.10:
          return 'b' 
        else:
            return 'c'         
    