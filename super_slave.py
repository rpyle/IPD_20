####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'mendoza_slave'
strategy_name = 'Super Slave'
strategy_description = 'If I recognize my master, I collude. Otherwise, I betray.'

def move(my_history, their_history, my_score, their_score):
    '''
    Returns 'c' or 'b' for collude or betray.
    '''

    # This player always colludes if it recognizes that its my slave. Otherwise, it betrays.
    if len(my_history) == 0:
        return 'l'
    if ' ' in their_history:
        return 'c'
    else:
        return 'b'
