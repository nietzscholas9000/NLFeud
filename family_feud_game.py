# family_feud_game.py
#
# Nicholas Johnson
#
# Runs a family feud style game in the terminal.
# See readme.txt for more detailed description/instructions
#

import csv
from nltk.corpus import wordnet as wn


# run tests that will check for corrupted data?


def synonyms_list(word):
    """returns a list of every synonym for the input word in the WordNet corpus"""
    # does not generate plurals, so there might be false negatives when comparisons are run
    # future consideration: analyzing expected word sense to more properly match synonyms

    syn_list = []
    for ss in wn.synsets(word):
        # print(ss.name(), ss.lemma_names())
        syn_list.append(ss.lemma_names())
    # print(syn_list)

    # flatten lists of synonyms into single list for comparison
    flat_syn_list = flatten_list(syn_list)

    # make each word lowercase and remove '-' and '_'
    flat_syn_list = [element.lower() for element in flat_syn_list]
    flat_syn_list = [element.replace('-', ' ') for element in flat_syn_list]
    flat_syn_list = [element.replace('_', ' ') for element in flat_syn_list]

    # print(flat_syn_list)
    return flat_syn_list


def flatten_list(lis):
    flat = []
    for sub in lis:
        for word in sub:
            flat.append(word)
    return flat


def grabq(filename):
    """ reads in CSV specified .csv file and uses a
    dictionary comprehension to format data
    and create a list of dictionaries (returns this list"""
    with open(filename, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        fdata = []
        for row in reader:
            # create new dictionary, formatted with lower case answers free of unnecessary punctuation
            # changes to consider:  .replace('"', '')
            new_dict = {k: v.lower().replace('/', ' ').replace('-', ' ') for k, v in row.items()}
            # consider another dict comp to remove plurals and things like 'a'
            fdata.append(new_dict)

        return fdata


def main():
    print('''There are several csv files of questions/answers that may be used in this game.

    The included files you may choose from are: 
    three_ans.csv, four_ans.csv, five_ans.csv, six_ans.csv, seven_ans.csv, or fast_money.csv

    Ideally there will be two teams of users, that will take turns playing.
    But one may continue to choose the same team and see how many points they can get for correct answers.
    ''')

    # uncomment the next line to choose your file by usr input
    # data_choice = input('Enter a file name: ')

    data_choice = "seven_ans.csv"
    csv_file = grabq(data_choice)
    game_round(csv_file)


# consider renaming function something more general, such as game_rounds(), gameplay(), etc.
# adding an optional variable with a default value to input variables to optionally choose q-number?
# or do this inside of the function?
def game_round(dict_list):
    """ runs game round, including user interaction and question comparison """

    team_one_points = 0
    team_two_points = 0

    for row in dict_list:

        # setup game/round variables...
        print()
        print()
        question = row['Question']
        print('Is this a good question?\t\t', question)
        skipq = input('\n\tEnter "y" if you would like to skip this question, or any other key to continue...\n')

        if (skipq != 'y') and (skipq != 'Y'):
            team = input("\nwho's turn is it? team 1 or 2: \n")  # throws error if a number is not entered
            print('\n \n')
            answers = 0  # number of answers left on the board
            if 'Answer 7' in row:
                answers = 7
            elif 'Answer 6' in row:
                answers = 6
            elif 'Answer 5' in row:
                answers = 5
            elif 'Answer 4' in row:
                answers = 4
            elif 'Answer 3' in row:
                answers = 3
            numq = answers

            steal = False
            strikes = []
            round_points = 0

            # checks each answer by a team, adding pts or a strike
            # until other team steals or no Q's left

            already_guessed = []  # keep track of guesses on the board
            while (strikes != ['x', 'x', 'x']) and (answers != 0):
                print(question)
                guess = input("\n\twhat's your guess?\n")
                print()
                # generate symnonyms of guess to compare to answers
                guess_options = synonyms_list(guess)
                guess_options.insert(0, guess)

                print(guess_options, 'are the synonyms of', guess)

                # if you guessed this or something too similar already, try again

                flat_guess = flatten_list(already_guessed)
                # print(flat_guess, 'flat, already_guessed list')
                while guess in flat_guess:
                    guess = input("\nThat answer is already on the board, try something else...\n")
                    guess_options = synonyms_list(guess)
                    guess_options.insert(0, guess)

                # print(already_guessed, 'already guessed before answer comparison')

                # if set(row.get('Answer 7', '')).intersection(guess_options):
                if row.get('Answer 7', '') in guess_options:
                    print('correct!')
                    answers -= 1
                    round_points += int(row.get('#7'))
                    already_guessed.append(guess_options)
                elif row.get('Answer 6', '') in guess_options:              # default return of empty string
                    print('correct!')
                    answers -= 1                                                # in case there's no column
                    round_points += int(row.get('#6'))
                    already_guessed.append(guess_options)
                elif row.get('Answer 5', '') in guess_options:
                    print('correct!')
                    answers -= 1
                    round_points += int(row.get('#5'))
                    already_guessed.append(guess_options)
                elif row.get('Answer 4', '') in guess_options:
                    print('correct!')
                    answers -= 1
                    round_points += int(row.get('#4'))
                    already_guessed.append(guess_options)
                elif row.get('Answer 3', '') in guess_options:
                    print('correct!')
                    answers -= 1
                    round_points += int(row.get('#3'))
                    already_guessed.append(guess_options)
                elif row.get('Answer 2', '') in guess_options:
                    print('correct!')
                    answers -= 1
                    round_points += int(row.get('#2'))
                    already_guessed.append(guess_options)
                elif row.get('Answer 1', '') in guess_options:
                    print('correct!')
                    answers -= 1
                    round_points += int(row.get('#1'))
                    already_guessed.append(guess_options)
                else:
                    strikes.append('x')
                    already_guessed.append(guess_options)
                    print()
                    print('Sorry that answer is not on the board.')
                    print()
                # print(already_guessed, 'already_guessed after comparison')
                # how to account for answers being entered more than once?

                print()
                print('strikes: ', strikes)
                print('you now have', round_points, 'points')
                print('answers left', answers)
                print()

            #  game/round state after checking question
            if strikes == ['x', 'x', 'x']:
                steal = True
                print("The other team gets a chance to steal!\n")
            elif (int(team) == 1) and (answers == 0):  # points not being added
                team_one_points += round_points
            elif (int(team) == 2) and (answers == 0):
                team_two_points += round_points

            if steal:
                print("\nHere's your chance to steal...\n")
                print(question)
                # stolen = False

                guess = input("\n\twhat's your guess?\n")

                # generate symnonyms of guess to compare to answers
                guess_options = synonyms_list(guess)
                guess_options.insert(0, guess)  # this may be redundant

                # re-try if already guessed
                flat_guess = flatten_list(already_guessed)
                while guess in flat_guess:
                    guess = input("\nThat answer is already on the board, try something else...\n")
                    guess_options = synonyms_list(guess)

                if row.get('Answer 7', '') in guess_options:
                    print('correct!')
                    round_points += int(row.get('#7'))
                    already_guessed.append(guess_options)
                elif row.get('Answer 6', '') in guess_options:  # default return of empty string
                    print('correct!')
                    round_points += int(row.get('#6'))
                    already_guessed.append(guess_options)
                elif row.get('Answer 5', '') in guess_options:
                    print('correct!')
                    round_points += int(row.get('#5'))
                    already_guessed.append(guess_options)
                elif row.get('Answer 4', '') in guess_options:
                    print('correct!')
                    round_points += int(row.get('#4'))
                    already_guessed.append(guess_options)
                elif row.get('Answer 3', '') in guess_options:
                    print('correct!')
                    round_points += int(row.get('#3'))
                    already_guessed.append(guess_options)
                elif row.get('Answer 2', '') in guess_options:
                    print('correct!')
                    round_points += int(row.get('#2'))
                    already_guessed.append(guess_options)
                elif row.get('Answer 1', '') in guess_options:
                    print('correct!')
                    round_points += int(row.get('#1'))
                    already_guessed.append(guess_options)
                else:
                    steal = False
                    strikes.append('x')
                    already_guessed.append(guess_options)
                    print()
                    print('Sorry that answer is not on the board.')
                    print()

                # steal points from other teams answers..
                # does this always steal pts, regardless if correct?
                if int(team) == 1 and (steal is True):
                    team_two_points += round_points
                elif int(team) == 2 and (steal is True):
                    team_one_points += round_points

            # print("Let's look at the answers on the board.")
            print("Let's look at the answers on the board.")
            print('question')
            for i in range(1, numq + 1):
                k = 'Answer {}'.format(i)
                v = '#{}'.format(i)
                print("Answer {} is".format(i), row.get(k), "\t\t", row.get(v), "points")

            print()
            print('team one pts: ', team_one_points)
            print('team two pts: ', team_two_points)
            print()
            if team_two_points > team_one_points:
                print('team 2 wins the round!')
            else:
                print('team 1 wins the round!')

            # ask user whether to continue or not
            next_question = input('Next question? (enter y or n)')
            if (next_question == 'n') or (next_question == 'N'):
                break  # break outside of for loop and stop questions
                # pass
            else:
                continue
        elif (skipq == 'y') or (skipq == 'Y'):
            pass  # move to next question

    # after questions are done, output the winning team & their points
    if team_two_points > team_one_points:
        print('team 2 wins the game with', team_two_points, 'points!')
    else:
        print('team 1 wins the game with', team_one_points, 'points!')


main()
