import random 

def play():
    user = input("What's choice,rock for 'r' paper for 'p' scissor for 's': ")
    computer = random.choice(['r','s','p'])

    if user==computer:
        return 'It\'s tie'
    if is_win(user,computer):
        return "You Won"
    return "you lost"

def is_win(player,opponent):
    #r>s s>p p>r
    if (player == 'r' and opponent =='s') or (player == 's' and opponent =='p') or (player == 'p' and opponent =='r'):
        return True


print(play())
