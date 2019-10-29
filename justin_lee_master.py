team_name = 'Justin Lee'
strategy_name = 'spiteful_cc/slavemaster'
strategy_description = 'Plays spiteful_cc strategy until it identifies a slave, then switches to slavemaster strategy. Identifies its own slaves and also tricks opposing players slaves into feeding self.'

slaveIdentifier  = ['c', 'c', 'b', 'b', 'c', 'c', 'c']
masterIdentifier = ['c', 'c', 'c', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c']
devinSlaveIdentifier  = ['c', 'b', 'b', 'b', 'b', 'c']
devinMasterIdentifier = ['c', 'c', 'b', 'b', 'b', 'b', 'c', 'b', 'c']

def move(my_history, their_history, my_score, their_score):
  isOpponentSlave = False
  if len(their_history) >= len(slaveIdentifier):
    isOpponentSlave = True
    for x in range(len(slaveIdentifier)):
      if not their_history[x] == slaveIdentifier[x]:
        isOpponentSlave = False
  isOpponentDevinSlave = False
  if len(their_history) >= len(devinSlaveIdentifier):
    isOpponentDevinSlave = True
    for x in range(len(devinSlaveIdentifier)):
      if not their_history[x] == devinSlaveIdentifier[x]:
        isOpponentDevinSlave = False
  if isOpponentDevinSlave == True:
    if len(my_history) < len(devinMasterIdentifier):
      return devinMasterIdentifier[len(my_history)]
    else:
      return 'b'
  elif isOpponentSlave == True:
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