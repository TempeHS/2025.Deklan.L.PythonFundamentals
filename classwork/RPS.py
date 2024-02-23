def main():
    playerchoice(input())
    generate_random

def playerchoice(rps):
    match rps:
        case 'rock':
            if generate_random == "paper":
                print('lose')
            elif generate_random == "rock":
                print('draw')
            else:
                print('win')
        case 'paper':
            if generate_random == 'scissors':
                print('lose')
            elif generate_random == "paper":
                print('draw')
            else:
                print('win')
        case 'scissors':
            if generate_random == "rock":
                print('lose')
            if generate_random == "scissors":
                print('draw')
            else:
                print('win')

def generate_random():

main()