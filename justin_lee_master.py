team_name = 'Justin Lee'
strategy_name = 'spiteful_cc/slavemaster'
strategy_description = 'Plays spiteful_cc strategy until it identifies a slave, then switches to slavemaster strategy.'

slaveIdentifier  = ['c', 'c', 'b', 'b', 'c', 'c', 'c', 'c']
masterIdentifier = ['c', 'c', 'c', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c']

def move(my_history, their_history, my_score, their_score):
  isOpponentSlave = False
  if len(their_history) >= len(slaveIdentifier):
    isOpponentSlave = True
    for x in range(len(slaveIdentifier)):
      if not their_history[x] == slaveIdentifier[x]:
        isOpponentSlave = False
  if isOpponentSlave == True:
    if len(my_history) < len(masterIdentifier):
      return masterIdentifier[len(my_history)]
    else:
      return 'b'
  else:
    if len(my_history) <= 1:
      return 'c'
    else:
      if 'b' in their_history:
        return 'b'
      else:
        return 'c'