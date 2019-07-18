print("Welcome to 'Rock Paper Scissor Game' ")
print("                 By-  Maaz Mohammed")
print("                      BT18GCS105")
print("                      Section-III")
print()
print()
print()
count_1 = 0
count_2 = 0
count_3 = 0
print("Type H to see the rule of games")
print("Type E to exit the game")
print("else press any key to start the game")
a = input()
if a == 'H' or a == 'h':
    print("Following are the rules of the game")
    print(" 1) If player 1 plays scissor and player 2 plays paper then player 1 wins the round")
    print(" 2) If player 1 plays paper and player 2 plays rock then player 1 wins the round")
    print(" 3) If player 1 plays rock and player 2 plays scissor then player 1 wins the round")
    print(" 4) If both the players plays same thing then there will be a draw")
    print(" 5) There are five rounds in this game the player which win majority of cases win the game")
    print(" 6) If no. of rounds won by the players are equal then game is draw")
    print()
    print()
    print("Type E to exit or any key to play the game")
    q = input()
    if q == 'E' or q == 'e':
        print("Have a nice day")
        exit()
    else:
        print("LETS PLAY THE GAME")
        print("Press any key to continue")
        z = input()
        player_1 = input("Please enter name of player 1  ")
        player_2 = input("Please enter name of player 2  ")
        print("# Type S for scissor")
        print("# Type R for rock")
        print("# Type P for paper")
        for i in range(1, 6):
            print("Round ", i)
            b = input("Player one throws   ")
            c = input("Player two throws   ")
            if b == c :
                if b == 'S' or b == 's' or b == 'r' or b == 'R' or b == 'p' or b == 'P' :
                    count_3 += 1
                    print("draw")
                else:
                    print("Wrong key is pressed")
                    exit()
            elif (b == 's' or b == 'S') and (c == 'p' or c == 'P'):
                count_1 += 1
                print(player_1, "wins the round")
            elif (b == 'p' or b == 'P') and (c == 's' or c == 'S'):
                count_2 += 1
                print(player_2, "wins the round")
            elif (b == 'p' or b == 'P') and (c == 'r' or c == 'R'):
                count_1 += 1
                print(player_1, "wins the round")
            elif (b == 'r' or b == 'R') and (c == 'p' or c == 'P'):
                count_2 += 1
                print(player_2, "wins the round")
            elif (b == 'r' or b == 'R') and (C == 's' or c == 'S'):
                count_1 += 1
                print(player_1, "wins the round")
            elif (b == 's' or b == 'S') and (c == 'r' or c == 'R'):
                count_2 += 1
                print(player_2, "wins the round")
            else:
                print("wrong key pressed...")
                exit()
        if count_1 > count_2:
            print(player_1, " Wins the game")
        elif count_1 < count_2:
            print(player_2, " Wins the game")
        else:
            print("Draw, No one wins the game")
        print("\n")
        print("\n")
        print("\n")
        print("type Y if you want to see game statics")
        print("Else type any key to exit ")
        x = input()
        if x == 'y' or x == 'Y':
            print("Welcome to Game statics")
            print("No. of times ", player_1, " won the round is ", count_1)
            print("No. of times ", player_2, " won the round is ", count_2)
            print("No. of times there was a draw: ", count_3)
            print("Result of the game is :")
            if count_1 > count_2:
                print(player_1, " Wins the game")
            elif count_1 < count_2:
                print(player_2, " Wins the game")
            else:
                print("Draw, No one wins the game")
            print("Type any key to exit")
            exit()
        else:
            print("Have a nice day")
            exit()
elif a == 'E' or a == 'e':
    print("Have a nice day")
    exit()
else:
    print("LETS PLAY THE GAME")
    print("Press any key to continue")
    z = input()
    player_1 = input("Please enter name of player 1  ")
    player_2 = input("Please enter name of player 2  ") 
    print("# Type S for scissor")
    print("# Type R for rock")
    print("# Type P for paper")
    for i in range(1, 6):
        print("Round ", i)
        b = input("Player one throws   ")
        c = input("Player two throws   ")
        if b == c :
            if b == 'S' or b == 's' or b == 'r' or b == 'R' or b == 'p' or b == 'P' :
                count_3 += 1
                print("draw")
            else:
                print("Wrong key is pressed")
                exit()
        elif (b == 's' or b == 'S') and (c == 'p' or c == 'P'):
            count_1 += 1
            print(player_1, "wins the round")
        elif (b == 'p' or b == 'P') and (c == 's' or c == 'S'):
            count_2 += 1
            print(player_2, "wins the round")
        elif (b == 'p' or b == 'P') and (c == 'r' or c == 'R'):
            count_1 += 1
            print(player_1, "wins the round")
        elif (b == 'r' or b == 'R') and (c == 'p' or c == 'P'):
            count_2 += 1
            print(player_2, "wins the round")
        elif (b == 'r' or b == 'R') and (C == 's' or c == 'S'):
            count_1 += 1
            print(player_1, "wins the round")
        elif (b == 's' or b == 'S') and (c == 'r' or c == 'R'):
            count_2 += 1
            print(player_2, "wins the round")
        else:
            print("wrong key pressed...")
            exit()
    if count_1 > count_2:
        print(player_1, " Wins the game")
    elif count_1 < count_2:
        print(player_2, " Wins the game")
    else:
        print("Draw, No one wins the game")
    print("\n")
    print("\n")
    print("\n")
    print("type Y if you want to see game statics")
    print("Else type any key to exit ")
    x = input()
    if x == 'y' or x == 'Y':
        print("Welcome to Game statics")
        print("No. of times ", player_1, " won the round is ", count_1)
        print("No. of times ", player_2, " won the round is ", count_2)
        print("No. of times there was a draw: ", count_3)
        print("Result of the game is :")
        if count_1 > count_2:
            print(player_1, " Wins the game")
        elif count_1 < count_2:
            print(player_2, " Wins the game")
        else:
            print("Draw, No one wins the game")
        print("Type any key to exit")
        exit()
    else:
        print("Have a nice day")
        exit()
