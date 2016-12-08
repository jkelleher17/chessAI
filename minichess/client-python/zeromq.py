import json

##########################################################

import zmq # pip install pyzmq

from collections import Counter

import random
##########################################################

zeromq_boolRunning = False

##########################################################
# c = ChessGame()


class OpeningBookCalculator(object):

    def __init__(self, alpha, discount, epsilon=0.5):
        self.alpha = alpha
        self.discount = discount
        self.q_val = Counter()
        self.epsilon = epsilon
        self.state = ()

    def q_value(self, action):
        # print self.state
        if (self.state, action) in self.q_val:
            return self.q_val[(self.state, action)]
        return 0

    def computeValueFromQValues(self, reward):
        reward = -1*reward
        for x in xrange(4):
            reward = -1*reward
            state = tuple(list(self.state[:x]))
            action = list(self.state)[x]
            if (state,action) in self.q_val:
                self.q_val[(state, action)] = self.q_val[(state, action)] +  self.alpha*(reward - self.q_val[(state, action)])
            else:
                self.q_val[(state, action)] = self.alpha*reward

    def computeActionFromQValues(self):
        move = None
        if len(self.state) < 3:
            max_score = -float("inf")
            max_move = None
            if random.random() < self.epsilon:
                for move in chess_movesEvaluated():
                    if self.q_value(move) > max_score:
                        max_score = self.q_value(move)
                        max_move  = move
            else:
                max_move = chess_movesEvaluated()[0] 
            chess_move(max_move)
            move = max_move
        else:
            move =  chess_moveAlphabeta(3,200000)
        self.state = tuple(list(self.state) + [move])
        return move


def zeromq_start():
    q_learner = OpeningBookCalculator(0.5,1)
    for x in xrange(10000):
        # zeromq_boolRunning = True
        # contextHandle = zmq.Context()
        # socketHandle = contextHandle.socket(zmq.PAIR)
        # socketHandle.bind("tcp://*:" + str(main_intZeromq))
        if x != 0:
            chess_reset()
        jsonOut = {}
        # jsonIn = None
        jsonOut["strOut"] = main_strName
        # socketHandle.send(json.dumps(jsonOut))
        # socketHandle.send(json.dumps(jsonOut))
        jsonOut["strOut"] = chess_boardGet()
        # socketHandle.send(json.dumps(jsonOut))
        counter = 0
        while chess_winner() == "?": 
            # if counter >= 4:         
            #     jsonOut["strOut"] = chess_moveAlphabeta(3, 200000)
            # else:
            #     jsonOut["strOut"] = chess_moveRandom()
            #     counter += 1
            q_learner.computeActionFromQValues()
            # socketHandle.send(json.dumps(jsonOut))
            jsonOut["strOut"] = chess_boardGet()
            # socketHandle.send(json.dumps(jsonOut))
            # print chess_boardGet()
        move_history = []
        if "W" in chess_winner():
            q_learner.computeValueFromQValues(1) 
        if "B" in chess_winner():
            q_learner.computeValueFromQValues(-1) 
        else:
            q_learner.computeValueFromQValues(0)
        print chess_winner()
        print getHistory()
        print q_learner.q_val
        q_learner.state = ()

    
    # socketHandle.send(json.dumps(jsonOut))
        # jsonIn = None
        # jsonOut = {}
        # jsonIn = socketHandle.recv_json()
        
        # if jsonIn["strFunction"] == "ping":
        #     jsonOut["strOut"] = main_strName
            
        # elif jsonIn["strFunction"] == "chess_reset":
        #     chess_reset()
            
        # elif jsonIn["strFunction"] == "chess_boardGet":
        #     jsonOut["strOut"] = chess_boardGet()
            
        # elif jsonIn["strFunction"] == "chess_boardSet":
        #     chess_boardSet(jsonIn["strIn"])
            
        # elif jsonIn["strFunction"] == "chess_winner":
        #     jsonOut["strReturn"] = chess_winner()
            
        # elif jsonIn["strFunction"] == "chess_isValid":
        #     jsonOut["boolReturn"] = chess_isValid(jsonIn["intX"], jsonIn["intY"])
            
        # elif jsonIn["strFunction"] == "chess_isEnemy":
        #     jsonOut["boolReturn"] = chess_isEnemy(jsonIn["strPiece"])
            
        # elif jsonIn["strFunction"] == "chess_isOwn":
        #     jsonOut["boolReturn"] = chess_isOwn(jsonIn["strPiece"])
            
        # elif jsonIn["strFunction"] == "chess_isNothing":
        #     jsonOut["boolReturn"] = chess_isNothing(jsonIn["strPiece"])
            
        # elif jsonIn["strFunction"] == "chess_eval":
        #     jsonOut["intReturn"] = chess_eval()
            
        # elif jsonIn["strFunction"] == "chess_moves":
        #     strOut = chess_moves()
            
        #     jsonOut["intOut"] = len(strOut)
        #     jsonOut["strOut"] = str.join('', strOut)
            
        # elif jsonIn["strFunction"] == "chess_movesShuffled":
        #     strOut = chess_movesShuffled()
            
        #     jsonOut["intOut"] = len(strOut)
        #     jsonOut["strOut"] = str.join('', strOut)
            
        # elif jsonIn["strFunction"] == "chess_movesEvaluated":
        #     strOut = chess_movesEvaluated()
            
        #     jsonOut["intOut"] = len(strOut)
        #     jsonOut["strOut"] = str.join('', strOut)
            
        # elif jsonIn["strFunction"] == "chess_move":
        #     chess_move(jsonIn["strIn"])
            
        # elif jsonIn["strFunction"] == "chess_moveRandom":
        #     jsonOut["strOut"] = chess_moveRandom()
            
        # elif jsonIn["strFunction"] == "chess_moveGreedy":
        #     jsonOut["strOut"] = chess_moveGreedy()
            
        # elif jsonIn["strFunction"] == "chess_moveNegamax":
        #     jsonOut["strOut"] = chess_moveNegamax(jsonIn["intDepth"], jsonIn["intDuration"])
            
        # elif jsonIn["strFunction"] == "chess_moveAlphabeta":
        #     jsonOut["strOut"] = chess_moveAlphabeta(jsonIn["intDepth"], jsonIn["intDuration"])
            
        # elif jsonIn["strFunction"] == "chess_undo":
        #     chess_undo()

        # jsonOut["strOut"]  = chess_reset()
        # socketHandle.send(json.dumps(jsonOut))
        # time.sleep(10)
        # while chess_winner() == "?" and zeromq_boolRunning == True:
        #     jsonOut["strOut"] = chess_moveAlphabeta(4, 200000)
        #     socketHandle.send(json.dumps(jsonOut))

        
        # socketHandle.send(json.dumps(jsonOut))
        
        # jsonIn = None
        # jsonOut = None

	    
    # socketHandle.close()
    # contextHandle.destroy()


def zeromq_stop():
    global zeromq_boolRunning

    zeromq_boolRunning = false