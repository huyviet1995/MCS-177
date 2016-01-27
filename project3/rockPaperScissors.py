# str, str -> void
def RPSgame(player1, player2):
    """Prints outcome of one round of the rock, paper, scissors game.
       This function uses the function isLegal and beats, which you
       have to write"""
    if not (isLegal(player1) and isLegal(player2)):
        print("Both players must select from rock, paper, or scissors")
    elif beats(player1, player2):
        print("Player 1 wins")
    elif beats(player2, player1):
        print("Player 2 wins")
    else:
        print("It's a tie")

#string -> boolean
def isLegal(weapon):
    """Take the weapon that the player chooses as input, return true if
       the weapon is 'rock','paper' or 'scissors', else return false"""
    if (weapon=='rock') or (weapon=='paper') or (weapon=='scissors'):
        return True
    else:
        return False

#string,string -> boolean
def beats(weapon1,weapon2):
    """ take the weapon that the first player and the second player chooses
        and return True if the first player beats the second player, else
        return False"""
    if (weapon1=='rock' and weapon2=='scissors') or (weapon1=='scissors' and weapon2=='paper') or (weapon1=='paper' and weapon2=='rock'):
        return True
    else:
        return False
