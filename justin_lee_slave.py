team_name = 'Justin Lee'
strategy_name = 'j_slave'
strategy_description = 'Identifies slavemaster and feeds them.'

slaveIdentifier  = ['c', 'c', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']
masterIdentifier = ['c', 'c', 'c', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c']

def move(my_history, their_history, my_score, their_score):
  if len(my_history) < len(slaveIdentifier):
    return slaveIdentifier[len(my_history)]
  isOpponentMaster = True
  for x in range(len(masterIdentifier)):
    if not their_history[x] == masterIdentifier[x]:
      isOpponentMaster = False
  if isOpponentMaster == True:
    return 'c'
  else:
    return 'b'