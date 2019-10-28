team_name = 'Justin Lee'
strategy_name = 'spiteful_cc'
strategy_description = 'For the first two rounds, always collude. If the enemy ever betrays after those two collusions, always betray from that point.'

slaveIdentifier = ['c', 'c', 'b', 'c', 'b', 'c']

def move(my_history, their_history, my_score, their_score):
  isOpponentSlave = False
  if len(their_history) >= len(slaveIdentifier):
    isOpponentSlave = True
    for x in range(len(slaveIdentifier)):
      if not their_history[x] == slaveIdentifier[x]:
        isOpponentSlave = False
  
  