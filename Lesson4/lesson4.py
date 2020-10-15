def return_winner():
    new_file = open('test.txt', 'r+')

    for line in new_file.readlines():
        print(line[:-2])
        command, score = line.split(' ')

        team1, team2 = command.split(':')
        goals, goals2 = score.split(':')

        if int(goals) == int(goals2):
            print(f'Draw betweem: {team1} and {team2}.')
        elif int(goals) > int(goals2):
            print(f'Winner is: {team1}!')
        else:
            print(f'Winner is: {team2}!')

        print('\n')

    new_file.close()
#new_file.write('\nAbdysh-Ata:DynamoRF 1000:0')

def add_score():
    new_file = open('test.txt', 'a')
    score = input('Enter commands and their scores: ')
    new_file.write('\n'+score)
    new_file.close()


def main():
    while True:
          print('Choose option')
          print('1) Add new score: ')
          print('2) List all scores and their winners: ')
          print('3) Stop program')
          choice = int(input('Enter your choice: '))

          if choice == 1:
              add_score()
          elif choice == 2:
            return_winner()
          elif choice == 3:
              break
          else:
            print('Error no such choice! ')

main()
