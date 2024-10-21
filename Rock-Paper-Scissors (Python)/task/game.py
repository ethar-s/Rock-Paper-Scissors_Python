# Write your code here
import random

def win(computer_choice1,name):
    add_score(name)
    print("Well done. The computer chose {} and failed".format(computer_choice1))

def draw(computer_choice1,name):
    add_score1(name)
    print("There is a draw ({})".format(computer_choice1))

def lose(computer_choice1, name):
    print('Sorry, but the computer chose {}'.format(computer_choice1))

def return_score(name):
    names_scores = open('rating.txt', 'r')
    for name_score in names_scores:
        name_score = name_score.split()
        global player_score
        print(name_score[0])

        if name_score[0] == name:
            player_score += int(name_score[1])
            names_scores.close()
            break
    names_scores.close()

def  add_score(name):
            global player_score
            player_score += 100


def add_score1(name):
    global player_score
    player_score += 50


def info(name):
    return_score(player_name)
    print(player_score)


player_score = 0

answer = input('Enter your name: ').strip()
player_name = answer
game_choice = ['scissors', 'rock', 'paper']
print('Hello, {}'.format(answer))
answer = input()
print("Okay, let's start")
answerers = 0
while  answer != '!exit':
    if (answer == '' or answerers == 1) and  answer != '!exit' and answer != '!rating':
        answerers = 1
        computer_choice = random.choice(game_choice)
        if answer == 'scissors':
            if computer_choice == 'paper':
                win(computer_choice, player_name)
            elif computer_choice == 'scissors':
                draw(computer_choice, player_name)
            elif computer_choice == 'rock':
                lose(computer_choice, player_name)
        elif answer == 'rock':
            if computer_choice == 'paper':
                lose(computer_choice, player_name)
            elif computer_choice == 'scissors':
                win(computer_choice, player_name)
            elif computer_choice == 'rock':
                draw(computer_choice, player_name)
        elif answer == 'paper':
            if computer_choice == 'paper':
                draw(computer_choice, player_name)
            elif computer_choice == 'scissors':
                lose(computer_choice, player_name)
            elif computer_choice == 'rock':
                win(computer_choice, player_name)
        elif answer == '!exit':
            pass
        elif answer == player_name:
            pass
        else:
            print('Invalid input')
    elif answer == '!rating':
        info(player_name)
    elif len(answer) > 0:
        index = 0
        game_choice = answer.split(",")
        computer_choice = random.choice(game_choice)
        game_choice_middile_nummer = int(round(len(game_choice) / 2 ))
        losing_list = []
        wining_list = []
        for i in range(len(game_choice)) :
            if computer_choice == game_choice[i]:
                index = i
        if index < game_choice_middile_nummer:
            losing_list = computer_choice[:index -1:-1 ] + computer_choice[index + game_choice_middile_nummer + 1:]
            wining_list = computer_choice[index + 1 : game_choice_middile_nummer + index ]
        elif index > game_choice_middile_nummer:
            losing_list = computer_choice[index - game_choice_middile_nummer: index ]
            wining_list = computer_choice[index + 1:] + computer_choice[-index-game_choice_middile_nummer-1::-1 ]
        if answer == computer_choice:
            draw(computer_choice,player_name)
        elif answer in losing_list:
            lose(computer_choice, player_name)
        elif answer in wining_list:
            win(computer_choice, player_name)

    answer = input()
print('Bye!')


