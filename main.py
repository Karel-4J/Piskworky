# coding=utf-8
winner = 0

history = []
cord_x = []
cord_y = []

print ("Make a move! (Write coordinates x,y)")

while winner == 0:
    makeMove = input()
    history.append(makeMove)

    if len(makeMove) == 2:
        cord_x.append(makeMove[0])
        cord_y.append(makeMove[1])
    else:
        print("Write coordinates x,y (example: 0,0)")
    print (cord_y)
    # Vytvořit pole

    # Checknout ho





