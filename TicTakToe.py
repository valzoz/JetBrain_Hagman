if __name__ == '__main__':

    DASH = []

    print(9 * "-")
    for i in range(0, 3):
        DASH.append(list(3 * " "))
        print("| " + " ".join(DASH[i]) + " |")
    print(9 * "-")

    lst_field = DASH
    X_turn = True

    while True:

        incorrect = True
        while incorrect:
            user_X = input("Enter the coordinates:").split()
            if len(user_X) != 2:
                print("You should enter numbers!")
            elif user_X[0].isdigit() == 0 or user_X[1].isdigit() == 0:
                print("You should enter numbers!")
            elif int(user_X[0]) > 3 or int(user_X[0]) < 1:
                print("Coordinates should be from 1 to 3!")
            elif int(user_X[1]) > 3 or int(user_X[1]) < 1:
                print("Coordinates should be from 1 to 3!")
            elif lst_field[int(user_X[0]) - 1][int(user_X[1]) - 1] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                incorrect = False

        if X_turn:
            lst_field[int(user_X[0]) - 1][int(user_X[1]) - 1] = "X"
            X_turn = False
        else:
            lst_field[int(user_X[0]) - 1][int(user_X[1]) - 1] = "O"
            X_turn = True

        lst_field_col = tuple(zip(*lst_field[::-1]))

        print(9 * "-")
        for i in range(0, 3):
            print("| " + " ".join(lst_field[i]) + " |")
        print(9 * "-")

        arr_temp = []
        for i in range(0, 3):
            arr_temp.append("".join(lst_field[i]))

        num_O = 0
        num_X = 0
        for elem in "".join(arr_temp):
            if elem == "X":
                num_X += 1
            elif elem == "O":
                num_O += 1

        if abs(num_O - num_X) > 1:
            print("Impossible")
            break
        elif "".join(lst_field[0]).count("X") == 3 and "".join(lst_field[1]).count("O") == 3 and num_O + num_X < 9:
            print("Impossible")
            break
        elif "".join(lst_field[1]).count("X") == 3 and "".join(lst_field[2]).count("O") == 3 and num_O + num_X < 9:
            print("Impossible")
            break
        elif "".join(lst_field[0]).count("X") == 3 and "".join(lst_field[2]).count("O") == 3 and num_O + num_X < 9:
            print("Impossible")
            break
        elif "".join(lst_field[0]).count("O") == 3 and "".join(lst_field[2]).count("X") == 3 and num_O + num_X < 9:
            print("Impossible")
            break
        elif "".join(lst_field[0]).count("O") == 3 and "".join(lst_field[1]).count("X") == 3 and num_O + num_X < 9:
            print("Impossible")
            break
        elif "".join(lst_field_col[0]).count("X") == 3 and "".join(lst_field_col[1]).count(
                "O") == 3 and num_O + num_X < 9:
            print("Impossible")
            break
        elif "".join(lst_field_col[1]).count("X") == 3 and "".join(lst_field_col[2]).count(
                "O") == 3 and num_O + num_X < 9:
            print("Impossible")
            break
        elif "".join(lst_field_col[0]).count("X") == 3 and "".join(lst_field_col[2]).count(
                "O") == 3 and num_O + num_X < 9:
            print("Impossible")
            break
        elif "".join(lst_field_col[0]).count("O") == 3 and "".join(lst_field_col[2]).count(
                "X") == 3 and num_O + num_X < 9:
            print("Impossible")
            break
        elif "".join(lst_field_col[0]).count("O") == 3 and "".join(lst_field_col[1]).count(
                "X") == 3 and num_O + num_X < 9:
            print("Impossible")
        elif "".join(lst_field[0]).count("X") == 3 or "".join(lst_field[1]).count("X") == 3 or "".join(
                lst_field[2]).count("X") == 3:
            print("X wins")
            break
        elif "".join(lst_field[0]).count("O") == 3 or "".join(lst_field[1]).count("O") == 3 or "".join(
                lst_field[2]).count("O") == 3:
            print("O wins")
            break
        elif "".join(lst_field_col[0]).count("X") == 3 or "".join(lst_field_col[1]).count("X") == 3 or "".join(
                lst_field_col[2]).count("X") == 3:
            print("X wins")
            break
        elif "".join(lst_field_col[0]).count("O") == 3 or "".join(lst_field_col[1]).count("O") == 3 or "".join(
                lst_field_col[2]).count("O") == 3:
            print("O wins")
            break
        elif "".join([lst_field[i][i] for i in range(len(lst_field))]).count("X") == 3 or "".join(
                [lst_field[i][2 - i] for i in range(len(lst_field))]).count("X") == 3:
            print("X wins")
            break
        elif [lst_field[i][i] for i in range(len(lst_field))].count("O") == 3 or [lst_field[2 - i][i] for i in
                                                                                  range(len(lst_field))].count(
                "O") == 3:
            print("O wins")
            break
        elif num_O + num_X < 9:
            continue
        elif num_O + num_X == 9:
            print("Draw")
            break

