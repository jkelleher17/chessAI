def all_moves(state, chess_isEnemy,chess_isOwn,chess_isNothing, turnC):
    # with reference to the state of the game and return the possible moves - one example is given below - note that a move has exactly 6 characters

    strOut = []
    letters = ['a', 'b', 'c', 'd', 'e']
    n = 0

    while n < 30:
        if chess_isOwn(state[n]):
            row = 6 - (n / 5)
            column = n % 5
            start = letters[column] + str(row)

            #possible moves for pawns
            if state[n] == 'P' or state[n] == 'p':
                if turnC == 'W':
                    if chess_isNothing(state[n - 5]):
                        end = letters[column] + str(row + 1)
                        strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[n - 4]) and (n - 4) % 5 == column + 1:
                        end = letters[column + 1] + str(row + 1)
                        strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[n - 6]) and (n - 6) % 5 == column - 1:
                        end = letters[column - 1] + str(row + 1)
                        strOut.append(start + '-' + end + '\n')
                elif turnC == 'B':
                    if chess_isNothing(state[n + 5]):
                        end = letters[column] + str(row - 1)
                        strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[n + 4]) and (n + 4) % 5 == column - 1:
                        end = letters[column - 1] + str(row - 1)
                        strOut.append(start + '-' + end + '\n')
                    if n + 6 < 30 and chess_isEnemy(state[n + 6]) and (n + 6) % 5 == column + 1:
                        end = letters[column + 1] + str(row - 1)
                        strOut.append(start + '-' + end + '\n')

            #possible moves for rook
            elif state[n] == 'R' or state[n] == 'r':
                #Move to right
                a = column + 1
                m = n + 1
                while a < 5 and not chess_isOwn(state[m]):
                    end = letters[a] + str(row)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[m]):
                        a = 5
                    a += 1
                    m += 1
                #move to left
                a = column - 1
                m = n - 1
                while a > -1 and not chess_isOwn(state[m]):
                    end = letters[a] +str(row)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[m]):
                        a = 0
                    m -= 1
                    a -= 1
                a = row + 1
                m = n - 5
                #move up
                while a < 7 and not chess_isOwn(state[m]):
                    end = letters[column] + str(a)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[m]):
                        a = 7
                    a += 1
                    m -= 5
                a = row - 1
                m = n + 5
                # move down
                while a > 0 and not chess_isOwn(state[m]):
                    end  = letters[column] + str(a)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[m]):
                         a = 0
                    a -= 1
                    m += 5

            #possible moves for knight
            elif state[n] == 'N' or state[n] == 'n':
                r = row
                a = 0
                m = n
                while a < 2:
                    #move up left and right
                    if not chess_isOwn(state[m - 11]) and r + 2 < 7 and -1 < column - 1 + (a * 2) < 5:
                        end = letters[column - 1 + (a * 2)] + str(r + 2)
                        strOut.append(start + '-' + end + '\n')
                    #move down left and right
                    if m < 21 and not chess_isOwn(state[m + 9]) and 0 < r - 2 and -1 < column - 1 + (a * 2) < 5:
                        end = letters[column - 1 + (a * 2)] + str(r - 2)
                        strOut.append(start + '-' + end + '\n')
                    #move left and right up
                    if not chess_isOwn(state[n - 7 + (a * 4)]) and r + 1 < 7 and -1 < column - 2 + (a * 4) < 5:
                        end = letters[column - 2 + (a * 4)] + str(r + 1)
                        strOut.append(start + '-' + end + '\n')
                    #move left and right down
                    if n + 7 - (a * 4) < 30 and not chess_isOwn(state[n + 7 - (a * 4)]) and 0 < r - 1 and -1 < column + 2 - (a * 4) < 5:
                        end = letters[column + 2 - (a * 4)] + str(r - 1)
                        strOut.append(start + '-' + end + '\n')
                    a += 1
                    m += 2

            #possible moves for king
            elif state[n] == 'K' or state[n] == 'k':
                a = -1
                while a < 2:
                    # move left up and down
                    if column - 1 > -1 and 0 < row + a < 7 and not chess_isOwn(state[n - 1 - (a * 5)]):
                        end = letters[column - 1] + str(row + a)
                        strOut.append(start + '-' + end + '\n')
                    #move right up and down
                    if column + 1 < 5 and 0 < row + a < 7 and not chess_isOwn(state[n + 1 - (a * 5)]):
                            end = letters[column + 1] + str(row + a)
                            strOut.append(start + '-' + end + '\n')
                    #move up and down
                    if 0 < row + a < 7 and not a == 0 and not chess_isOwn(state[n - (a * 5)]):
                            end = letters[column] + str(row + a)
                            strOut.append(start + '-' + end + '\n')
                    a += 1

            #possible moves for Bishop
            elif state[n] == 'B' or state[n] == 'b':
                a = -1
                while a < 2:
                    # move left up and down
                    if column - 1 > -1 and 0 < row + a < 7 and not chess_isOwn(state[n - 1 - (a * 5)]):
                        if a == 0:
                            if not chess_isEnemy(state[n - 1 - (a * 5)]):
                                end = letters[column - 1] + str(row + a)
                                strOut.append(start + '-' + end + '\n')
                        else:
                            end = letters[column - 1] + str(row + a)
                            strOut.append(start + '-' + end + '\n')
                        # move cross
                        m = n - 2 - (a * 10)
                        while not a == 0 and chess_isNothing(state[m + 1 + (a * 5)]) and -1 < m < 30 and m % 5 < column:
                            if not chess_isOwn(state[m]) and 6 - (m / 5) > 0:
                                end = letters[m % 5] + str(6 - (m / 5))
                                strOut.append(start + '-' + end + '\n')
                            if chess_isEnemy(state[m]):
                                m == 0
                            m = m - 1 - (a * 5)
                    # move right up and down
                    if column + 1 < 5 and 0 < row + a < 7 and not chess_isOwn(state[n + 1 - (a * 5)]):
                        if a == 0:
                            if not chess_isEnemy(state[n + 1 - (a * 5)]):
                                end = letters[column + 1] + str(row + a)
                                strOut.append(start + '-' + end + '\n')
                        else:
                            end = letters[column + 1] + str(row + a)
                            strOut.append(start + '-' + end + '\n')
                        #move cross
                        m = n + 2 - (a * 10)
                        while not a == 0 and chess_isNothing(state[m - 1 + (a * 5)]) and m < 30 and m % 5 > column:
                            if not chess_isOwn(state[m]) and 6 - (m / 5) < 7 :
                                end = letters[m % 5] + str(6 - (m / 5))
                                strOut.append(start + '-' + end + '\n')
                            if chess_isEnemy(state[m]):
                                m == 100
                            m = m + 1 - (a * 5)
                    # move up and down
                    if 0 < row + a < 7 and not a == 0 and chess_isNothing(state[n - (a * 5)]):
                        end = letters[column] + str(row + a)
                        strOut.append(start + '-' + end + '\n')
                    a += 1

            # possible moves for Queen
            elif state[n] == 'Q' or state[n] == 'q':
                a = -1
                while a < 2:
                    # move left up and down
                    if column - 1 > -1 and 0 < row + a < 7 and not chess_isOwn(state[n - 1 - (a * 5)]):
                        end = letters[column - 1] + str(row + a)
                        strOut.append(start + '-' + end + '\n')
                        # move cross
                        m = n - 2 - (a * 10)
                        while not a == 0 and chess_isNothing(state[m + 1 + (a * 5)]) and -1 < m < 30 and m % 5 < column:
                            if not chess_isOwn(state[m]) and 6 - (m / 5) > 0:
                                end = letters[m % 5] + str(6 - (m / 5))
                                strOut.append(start + '-' + end + '\n')
                            if chess_isEnemy(state[m]):
                                m == 0
                            m = m - 1 - (a * 5)
                        m = n - 2
                        #Move left all the way
                        while a == 0 and chess_isNothing(state[m + 1]) and -1 < m and m % 5 < column:
                            if not chess_isOwn(state[m]):
                                end = letters[m % 5] + str(row)
                                strOut.append(start + '-' + end + '\n')
                            if chess_isEnemy(state[m]):
                                m == 0
                            m -= 1
                    # move right up and down
                    if  column + 1 < 5 and 0 < row + a < 7 and not chess_isOwn(state[n + 1 - (a * 5)]):
                        end = letters[column + 1] + str(row + a)
                        strOut.append(start + '-' + end + '\n')
                        #move cross
                        m = n + 2 - (a * 10)
                        while not a == 0 and chess_isNothing(state[m - 1 + (a * 5)]) and m < 30 and m % 5 > column:
                            if not chess_isOwn(state[m]) and 6 - (m / 5) < 7:
                                end = letters[m % 5] + str(6 - (m / 5))
                                strOut.append(start + '-' + end + '\n')
                            if chess_isEnemy(state[m]):
                                m == 100
                            m = m + 1 - (a * 5)
                        m = n + 2
                        #move right all the way
                        while a == 0 and chess_isNothing(state[m - 1]) and m < 30 and m % 5 > column:
                            if not chess_isOwn(state[m]):
                                end = letters[m % 5] + str(6 - (n / 5))
                                strOut.append(start + '-' + end + '\n')
                            if chess_isEnemy(state[m]):
                                m == 30
                            m += 1
                    a += 1
                a = row + 1
                m = n - 5
                # move up
                while a < 7 and not chess_isOwn(state[m]):
                    end = letters[column] + str(a)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[m]):
                        a = 7
                    a += 1
                    m -= 5
                a = row - 1
                m = n + 5
                # move down
                while a > 0 and not chess_isOwn(state[m]):
                    end = letters[column] + str(a)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[m]):
                        a = 0
                    a -= 1
                    m += 5
        n += 1
    return strOut

