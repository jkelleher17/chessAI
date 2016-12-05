import random
import time
from moves import all_moves
##########################################################

#board
state = []
#turn count
turnN = int
#turn color
turnC = ''
#move made array
mLog = []
#hit log
mPlog = []
#number of the moves made
mlCounter = -1
#Undo flag
mlFlag = 0
#p transition to q
PtoQlog = []
#timelimit
timelimit = 0
timecounter = 0
timecache = 0


class ChessGame(object):

    def __init__(self):
        self.state = list('kqbnrppppp..........PPPPPRNBQK')
        self.turnN = 1
        self.turnC = 'W'
        self.mLog = []
        self.mPlog = []
        self.mlCounter = -1
        self.mlFlag = 0
        self.PtoQlog = []
        self.timelimit = 0
        self.timecounter = 0
        self.timecache = 0

    def chess_reset(self):
        self.__init__()

    def chess_boardGet(self):
        strOut = ''
        strOut += str(self.turnN)
        strOut += ' '
        strOut += self.turnC
        strOut += '\n'
        strOut += ''.join(self.state[0:5]) + '\n'
        strOut += ''.join(self.state[5:10]) + '\n'
        strOut += ''.join(self.state[10:15]) + '\n'
        strOut += ''.join(self.state[15:20]) + '\n'
        strOut += ''.join(self.state[20:25]) + '\n'
        strOut += ''.join(self.state[25:30]) + '\n'
        return strOut

    def chess_boardSet(self, strIn):
        mLog = []
        mPlog = []
        mlCounter = -1
        mlFlag = 0
        PtoQlog = []
        strIn = str(strIn)
        turnn, self.turnC, self.state[0:5], self.state[5:10], self.state[10:15], self.state[15:20], self.state[20:25], self.state[25:30] = list(strIn.split())
        self.turnN = int(turnn)

    def chess_winner(self):
        if not 'k' in self.state:
            return 'W'
        elif not 'K' in self.state:
            return 'B'
        elif self.turnN > 40:
            return '='
        return '?'

    def chess_isValid(self, intX, intY):
        if intX < 0:
            return False

        elif intX > 4:
            return False

        if intY < 0:
            return False

        elif intY > 5:
            return False

        return True

    def chess_isEnemy(self, strPiece):
        return not self.chess_isNothing(strPiece) and not self.chess_isOwn(strPiece)
 
    def chess_isOwn(self,strPiece):
        if self.chess_isNothing(strPiece):
            return False
        return (strPiece.isupper() and self.turnC == "W") or (strPiece.islower() and self.turnC == "B")

    def chess_isNothing(self, strPiece):
        return strPiece == '.'

    def eval(self, state, turnC):
        values = {
            'k': 100, 
            'q': 50, 
            'b': 20,
            'r': 10,
            'n': 5,
            'p': 1
            }

        points = 0

        for space in state:
            if space == '.':
                continue

            if (space.isupper() and turnC == 'W') or (space.islower() and turnC == 'B'):
                points += values[space.lower()]
            else:
                points -= values[space.lower()]
        return points

    def chess_eval(self):
        return self.eval(self.state, self.turnC)
        
    def chess_moves(self):
        return all_moves(self.state, self.chess_isEnemy,self.chess_isOwn,self.chess_isNothing, self.turnC)

    def chess_move(self, strIn):
        column = ['a', 'b', 'c', 'd', 'e']
        c = 0
   
        #separate the start and end position
        start, end = list(strIn.split('-'))

        #find the column for the start position
        while column[c] != start[0]:
            c += 1

        #calculate the position in the array
        Oposition =29 - (5 * (int(start[1]) - 1) + (4 - c))

        #Check to make sure '.' is not selected
        if self.chess_isNothing(self.state[Oposition]):
            return False

        #Check to make sure it is our own piece
        if str(self.state[Oposition]).isupper() and turnC == 'B' and self.mlFlag == 0:
            return False

        if self.chess_isEnemy(self.state[Oposition]) and self.mlFlag == 0:
            return False

        #save the value of the selected peice
        piece = self.state[Oposition]

        #replace the start position with '.'
        self.state[Oposition] = '.'

        # find the column for the end position
        c = 0
        while column[c] != end[0]:
            c += 1

        # calculate the position in the array
        position = 29 - (5 * (int(end[1]) - 1) + (4 - c))

        if self.mlFlag == 0:
            self.mLog.append(str(strIn))
            self.mlCounter += 1
            self.mPlog.append(str(self.state[position]))

            #Check to see if replacement with queen is needed
            if position < 5 and piece == 'P':
                self.state[position] = 'Q'
                PtoQlog.append(self.mlCounter)
            elif position > 24 and piece == 'p':
                self.state[position] = 'q'
                self.PtoQlog.append(self.mlCounter)
            else:
                self.state[position] = piece
            
        else:
            # Check to see if replacement with queen is needed
            self.state[position] = piece
            self.state[Oposition] = mPlog[self.mlCounter]

            # Check to see if replacement with pawn is needed
            length = len(PtoQlog)
            for i in range(0, length):
                if self.mlCounter == PtoQlog[i]:
                    if piece.islower():
                        self.state[position] = 'p'
                        del PtoQlog[i]
                    elif piece.isupper():
                        self.state[position] = 'P'
                        del PtoQlog[i]

            self.mlFlag = 0
            self.mLog.pop()
            self.mPlog.pop()
            self.mlCounter -= 1

        if self.turnC == 'W':
            self.turnC = 'B'
        else:
            self.turnC = 'W'
            self.turnN += 1

    def sim_move(self, strIn, state, turnC):
        column = ['a', 'b', 'c', 'd', 'e']
        c = 0
   
        #separate the start and end position
        start, end = list(strIn.split('-'))

        #find the column for the start position
        while column[c] != start[0]:
            c += 1

        #calculate the position in the array
        Oposition =29 - (5 * (int(start[1]) - 1) + (4 - c))

        #Check to make sure '.' is not selected
        if self.chess_isNothing(state[Oposition]):
            return False

        #Check to make sure it is our own piece
        if str(state[Oposition]).isupper() and turnC == 'B' and self.mlFlag == 0:
            return False

        if self.chess_isEnemy(self.state[Oposition]) and self.mlFlag == 0:
            return False

        #save the value of the selected peice
        piece = state[Oposition]

        #replace the start position with '.'
        state[Oposition] = '.'

        # find the column for the end position
        c = 0
        while column[c] != end[0]:
            c += 1

        # calculate the position in the array
        position = 29 - (5 * (int(end[1]) - 1) + (4 - c))

        if self.mlFlag == 0:
            # self.mLog.append(str(strIn))
            # self.mlCounter += 1
            # self.mPlog.append(str(self.state[position]))

            #Check to see if replacement with queen is needed
            if position < 5 and piece == 'P':
                sstate[position] = 'Q'
                # PtoQlog.append(self.mlCounter)
            elif position > 24 and piece == 'p':
                state[position] = 'q'
                # self.PtoQlog.append(self.mlCounter)
            else:
                state[position] = piece
            
        else:
            print
            # # Check to see if replacement with queen is needed
            # state[position] = piece
            # state[Oposition] = mPlog[self.mlCounter]

            # # Check to see if replacement with pawn is needed
            # length = len(PtoQlog)
            # for i in range(0, length):
            #     if self.mlCounter == PtoQlog[i]:
            #         if piece.islower():
            #             state[position] = 'p'
            #             del PtoQlog[i]
            #         elif piece.isupper():
            #             state[position] = 'P'
            #             del PtoQlog[i]

        if turnC == 'W':
            turnC = 'B'
        else:
            turnC = 'W'
        
        return state, turnC




    def chess_movesShuffled(self):
        movelist = self.chess_moves()
        random.shuffle(movelist)
        return movelist

    def chess_moveRandom(self):
        movelist = self.chess_movesShuffled()
        self.chess_move(movelist[0])
        return movelist[0]

    def chess_movesEvaluated(self):
        # with reference to the state of the game, determine the possible moves and sort them in order of an increasing evaluation score before returning them - note that you can call the chess_moves() function in here

        movelist = self.chess_movesShuffled()

        score = []
        newlist = []

        for move in movelist:
            self.chess_move(move)
            score.append(self.chess_eval())
            self.chess_undo()

        length = len(score)

        for i in range(0, length):
            value = min(score)
            index = score.index(value)
            newlist.append(movelist[index])

            del score[index]
            del movelist[index]

        return newlist


    def chess_moveGreedy(self):
        # perform a greedy move and return it - one example output is given below - note that you can call the chess_movesEvaluated() function as well as the chess_move() function in here
        movelist = self.chess_movesEvaluated()
        self.chess_move(movelist[0])
        return movelist[0]

    def chess_moveNegamax(self,intDepth, intDuration):
        # perform a negamax move and return it - one example output is given below - note that you can call the the other functions in here
        return self.chess_moveGreed()

    def chess_moveAlphabeta(self,intDepth, intDuration):
        # perform a alphabeta move and return it - one example output is given below - note that you can call the the other functions in here
        return self.chess_moveGreedy()

 
    def chess_undo(self):
        # undo the last move and update the state of the game / your internal variables accordingly - note that you need to maintain an internal variable that keeps track of the previous history for this
        if self.mlCounter > -1:
            self.mlFlag = 1

            start, end = list(self.mLog[self.mlCounter].split('-'))
            end = end.strip('\n')
            strOut = end + '-' + start
            self.chess_move(strOut)


