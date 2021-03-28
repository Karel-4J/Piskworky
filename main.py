# coding=utf-8
# input fungus jen v 2.7

def check_winner(moves_like_jagger):

    for n in moves_like_jagger:
        count = 1
        for x_check in range(1, 6, 1):
            temp = (n[0] + x_check, n[1])
            if temp in moves_like_jagger:
                count += 1
            else:
                break
        if count == 5:
            return True
        count = 1
        for diagonal_plus_check in range(1, 6, 1):
            temp = (n[0] + diagonal_plus_check, n[1] + diagonal_plus_check)
            if temp in moves_like_jagger:
                count += 1
            else:
                break
        if count == 5:
            return True
        count = 1
        for y_check in range(1, 6, 1):
            temp = (n[0], n[1] + y_check)
            if temp in moves_like_jagger:
                count += 1
            else:
                break
        if count == 5:
            return True
        count = 1
        for diagonal_minus_check in range(1, 6, 1):
            temp = (n[0] + diagonal_minus_check, n[1] - diagonal_minus_check)
            if temp in moves_like_jagger:
                count += 1
            else:
                break
        if count == 5:
            return True


winner = False
message = ""
turn = 0
max_y = 0
min_y = 0
max_x = 0
min_x = 0
podvody = False

# dick_pole = {
#                 "player_1": [(-1, 1), (-2, 2), (-3, 3), (-4, 4)],
#                 "player_2": []
#             }

dick_pole = {
    "player_1": [],
    "player_2": []
}

print("Make a move! (Write coordinates x,y)")

while not winner:

    makeMove = input()
    if len(makeMove) == 2:

        for i in dick_pole["player_2"]:
            if makeMove == i:
                print("Ty podvodníku!")
                podvody = True
                break
        for i in dick_pole["player_1"]:
            if makeMove == i:
                print("Ty podvodníku!")
                podvody = True
                break
        if podvody:
            podvody = False
            continue
        if makeMove[0] >= max_x - 3:
            max_x = makeMove[0] + 3
        if makeMove[0] <= min_x + 2:
            min_x = makeMove[0] - 2
        if makeMove[1] >= max_y - 3:
            max_y = makeMove[1] + 3
        if makeMove[1] <= min_y + 2:
            min_y = makeMove[1] - 2

        turn += 1
        print("turn: " + str(turn))

        if turn % 2 == 1:
            dick_pole["player_1"].append(makeMove)
            winner = check_winner(dick_pole["player_1"])
            message = "1"
        else:
            dick_pole["player_2"].append(makeMove)
            winner = check_winner(dick_pole["player_2"])
            message = "2"
    else:
        print("Write coordinates x,y (example: 0,0)")

    pole = ""
    for ii in range(min_y, max_y, 1):
        if ii < 0:
            col = str(ii) + "|"
        else:
            col = " " + str(ii) + "|"

        for i in range(min_x, max_x, 1):
            if ii == min_y:
                if i < 0:
                    col = col + str(i) + " |"
                else:
                    col = col + " " + str(i) + " |"
            else:
                if (i, ii) in dick_pole["player_1"]:
                    col = col + " x |"
                elif (i, ii) in dick_pole["player_2"]:
                    col = col + " o |"
                else:
                    col = col + "   |"
        lang = max_x-min_x+1
        pole = pole + col + "\n " + lang * "-+--" + "\n"
    print(pole)
else:
    print("Winner is player " + message + "!")
