import random

if __name__ == '__main__':

    scores_win = 0
    scores_lose = 0
    MAX_ATTEMPTS = 8
    commands = ["play", "results", "exit"]

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list_answers = ['python', 'java', 'swift', 'javascript']

    input_command = ""

    while input_command not in commands:
        input_command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

    while input_command != "exit":

        if input_command == "play":

            user_letters = set()
            r_num = random.randint(0, len(list_answers) - 1)
            correct_ans = list_answers[r_num]
            print(correct_ans)
            correct_letters = set(correct_ans)

            str_hidden = ("-" * len(correct_ans))
            lst_hidden = list(str_hidden)

            attempts = MAX_ATTEMPTS
            print("H A N G M A N", "# 8 attempts")
            print()

            while attempts > 0:

                print("".join(lst_hidden))

                user_letter = input("Input a letter:")
                user_letter = user_letter.replace(">", "")
                user_letter = user_letter.replace(" ", "")

                if len(user_letter) > 1 or user_letter == "":
                    print(f"Please, input a single letter. # {attempts} attempts")
                    print()
                    continue

                if user_letter.islower() != 1 or user_letter not in alphabet:
                    print("Please, enter a lowercase letter from the English alphabet.")
                    print()
                    continue

                if user_letter in user_letters:
                    print(f"You've already guessed this letter. # {attempts} attempts")
                    print()
                    continue

                if user_letter in correct_letters:
                    if user_letter not in lst_hidden:
                        res = [elem for elem in range(len(correct_ans)) if correct_ans.startswith(user_letter, elem)]
                        for elem in res:
                            lst_hidden[elem] = user_letter
                        print()
                    else:
                        print(f"You've already guessed this letter. # {attempts} attempts")
                        print()
                else:
                    attempts -= 1
                    print(f"That letter doesn't appear in the word.  # {attempts} attempts")
                    print()

                user_letters.add(user_letter)


                if "".join(lst_hidden).count("-") == 0 and attempts > 0:
                    print(f"You guessed the word {correct_ans}!")
                    print("You survived!")
                    scores_win += 1
                    input_command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
                    break
            else:
                scores_lose += 1
                print("You lost!")
                input_command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

        elif input_command == "results":
            print(f"You won: {scores_win} times.")
            print(f"You lose: {scores_lose} times.")
            input_command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

        else:
            input_command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
