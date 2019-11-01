####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Cole Hunter'
strategy_name = 'Win At All Costs'
strategy_description = 'If my socre is greater than their score then always betray. If they have betrayed me before then always betray. If it is before round 50, I have not been betrayed, and my score is equal to or less than their score then collude. If none of this is true then I will do whatever my opponet did two turns ago.'
    
def move(my_history, their_history, my_score, their_score):
  if my_score > their_score:
    return 'b'
  for i in their_history:
    if i == 'b':
      return 'b'
  if len(my_history) < 50:
    return 'c'
  elif their_history[-2] == 'c':
    return 'c'
  elif their_history[-2] == 'b':
    return 'b'
