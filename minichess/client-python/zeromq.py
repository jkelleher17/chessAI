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
    # q_learner = OpeningBookCalculator(0.5,1)
    q_learner = OpeningBookExploiter()
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
        # move_history = []
        # if "W" in chess_winner():
        #     q_learner.computeValueFromQValues(1) 
        # if "B" in chess_winner():
        #     q_learner.computeValueFromQValues(-1) 
        # else:
        #     q_learner.computeValueFromQValues(0)
        print chess_winner()
        print getHistory()
        # print q_learner.q_val
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

class OpeningBookExploiter():
    def __init__(self):
        self.state = ()
        self.book = Counter({((), 'a2-a3'): 0.17700547277915657,
         ((), 'b1-a3'): 0.03341035090862332,
         ((), 'b1-c3'): -0.03435592913400343,
         ((), 'b2-b3'): -0.291070459590854,
         ((), 'c2-c3'): -0.2220864281030892,
         ((), 'd2-d3'): -0.14517054344810287,
         ((), 'e2-e3'): -0.3920165526541741,
         (('a2-a3',), 'a5-a4'): -0.4284303091341912,
         (('a2-a3',), 'b5-b4'): -0.6640348432449739,
         (('a2-a3',), 'c5-c4'): -0.22729773658194496,
         (('a2-a3',), 'd5-d4'): -0.3632855353895143,
         (('a2-a3',), 'd6-c4'): -0.4079409463678188,
         (('a2-a3',), 'd6-e4'): -0.29223163988493545,
         (('a2-a3',), 'e5-e4'): 0.4469952710055555,
         (('a2-a3', 'a5-a4'), 'a1-a2'): -0.21741414070129395,
         (('a2-a3', 'a5-a4'), 'b1-c3'): -0.012472353116100732,
         (('a2-a3', 'a5-a4'), 'b2-b3'): 0.20540660329225796,
         (('a2-a3', 'a5-a4'), 'c2-c3'): -0.32909083366394043,
         (('a2-a3', 'a5-a4'), 'd2-d3'): -0.25957464881412307,
         (('a2-a3', 'a5-a4'), 'e2-e3'): 0.3590246080951962,
         (('a2-a3', 'b5-b4'), 'a1-a2'): -0.25,
         (('a2-a3', 'b5-b4'), 'a3-a4'): -0.109375,
         (('a2-a3', 'b5-b4'), 'a3-b4'): 0.5487823792148412,
         (('a2-a3', 'b5-b4'), 'b1-c3'): 0.040771484375,
         (('a2-a3', 'b5-b4'), 'b2-b3'): -0.08758544921875,
         (('a2-a3', 'b5-b4'), 'c2-c3'): -0.14496111869812012,
         (('a2-a3', 'b5-b4'), 'd2-d3'): 0.6672664210054791,
         (('a2-a3', 'b5-b4'), 'e2-e3'): -0.0625,
         (('a2-a3', 'c5-c4'), 'a1-a2'): 0.013255363977092793,
         (('a2-a3', 'c5-c4'), 'a3-a4'): 0.0021614796130008385,
         (('a2-a3', 'c5-c4'), 'b1-c3'): 0.26349627961334715,
         (('a2-a3', 'c5-c4'), 'b2-b3'): -0.14377093315124512,
         (('a2-a3', 'c5-c4'), 'c2-c3'): -0.21807858056879725,
         (('a2-a3', 'c5-c4'), 'd2-d3'): -0.11111503563552969,
         (('a2-a3', 'c5-c4'), 'e2-e3'): -0.04193881708219842,
         (('a2-a3', 'd5-d4'), 'a1-a2'): 0.21416022139012977,
         (('a2-a3', 'd5-d4'), 'a3-a4'): -0.24575182259564976,
         (('a2-a3', 'd5-d4'), 'b1-c3'): -0.4556968697659961,
         (('a2-a3', 'd5-d4'), 'b2-b3'): -0.17321645747870207,
         (('a2-a3', 'd5-d4'), 'c2-c3'): 0.05523824541708122,
         (('a2-a3', 'd5-d4'), 'd2-d3'): 0.30235049634619615,
         (('a2-a3', 'd5-d4'), 'e2-e3'): 0.34141295118539505,
         (('a2-a3', 'd6-c4'), 'a1-a2'): -0.21886354312300682,
         (('a2-a3', 'd6-c4'), 'a3-a4'): -0.20809436772100298,
         (('a2-a3', 'd6-c4'), 'b1-c3'): 0.24463794007897377,
         (('a2-a3', 'd6-c4'), 'b2-b3'): -0.47265625,
         (('a2-a3', 'd6-c4'), 'c2-c3'): -0.24432373046875,
         (('a2-a3', 'd6-c4'), 'd2-d3'): -0.25,
         (('a2-a3', 'd6-c4'), 'e2-e3'): 0.07218897719940287,
         (('a2-a3', 'd6-e4'), 'a1-a2'): -0.3315026309751437,
         (('a2-a3', 'd6-e4'), 'a3-a4'): -0.20699362115341297,
         (('a2-a3', 'd6-e4'), 'b1-c3'): -0.04501760081600699,
         (('a2-a3', 'd6-e4'), 'b2-b3'): 0.22232917101854333,
         (('a2-a3', 'd6-e4'), 'c2-c3'): 0.6413462273853082,
         (('a2-a3', 'd6-e4'), 'd2-d3'): -0.25196896775367583,
         (('a2-a3', 'd6-e4'), 'e2-e3'): -0.2393974799991011,
         (('a2-a3', 'e5-e4'), 'a1-a2'): -0.3659988087842268,
         (('a2-a3', 'e5-e4'), 'a3-a4'): -0.25968199190572117,
         (('a2-a3', 'e5-e4'), 'b1-c3'): -0.09211462056988334,
         (('a2-a3', 'e5-e4'), 'b2-b3'): -0.08890605718988809,
         (('a2-a3', 'e5-e4'), 'c2-c3'): -0.029932366280467637,
         (('a2-a3', 'e5-e4'), 'd2-d3'): -0.5733184588425502,
         (('a2-a3', 'e5-e4'), 'e2-e3'): 0.4126235572110092,
         (('b1-a3',), 'a5-a4'): -0.2513065521440736,
         (('b1-a3',), 'b5-b4'): -0.4116139679641211,
         (('b1-a3',), 'c5-c4'): 0.11023491064994922,
         (('b1-a3',), 'd5-d4'): -0.524975179079525,
         (('b1-a3',), 'd6-c4'): 0.22415163020021195,
         (('b1-a3',), 'd6-e4'): -0.37459026387352085,
         (('b1-a3',), 'e5-e4'): -0.17895776859682752,
         (('b1-a3', 'a5-a4'), 'a1-b1'): -0.25,
         (('b1-a3', 'a5-a4'), 'a3-b1'): -0.109375,
         (('b1-a3', 'a5-a4'), 'a3-b5'): 0.3358039232022354,
         (('b1-a3', 'a5-a4'), 'a3-c4'): -0.25,
         (('b1-a3', 'a5-a4'), 'b2-b3'): -0.296875,
         (('b1-a3', 'a5-a4'), 'c1-b1'): -0.3232421875,
         (('b1-a3', 'a5-a4'), 'c2-c3'): -0.23122882843017578,
         (('b1-a3', 'a5-a4'), 'd2-d3'): -0.25,
         (('b1-a3', 'a5-a4'), 'e2-e3'): -0.25,
         (('b1-a3', 'b5-b4'), 'a1-b1'): -0.12157058715820312,
         (('b1-a3', 'b5-b4'), 'a3-b1'): 0.05141197084681731,
         (('b1-a3', 'b5-b4'), 'a3-b5'): 0.040393829345703125,
         (('b1-a3', 'b5-b4'), 'a3-c4'): -0.25,
         (('b1-a3', 'b5-b4'), 'b2-b3'): 0.09219646453857422,
         (('b1-a3', 'b5-b4'), 'c1-b1'): -0.5126953125,
         (('b1-a3', 'b5-b4'), 'c2-c3'): 0.7761919656186365,
         (('b1-a3', 'b5-b4'), 'd2-d3'): 0.026404380798339844,
         (('b1-a3', 'b5-b4'), 'e2-e3'): -0.2756117330516519,
         (('b1-a3', 'c5-c4'), 'a1-b1'): -0.17657470703125,
         (('b1-a3', 'c5-c4'), 'a3-b1'): -0.296875,
         (('b1-a3', 'c5-c4'), 'a3-b5'): -0.0756107906610059,
         (('b1-a3', 'c5-c4'), 'a3-c4'): -0.16089420624595632,
         (('b1-a3', 'c5-c4'), 'b2-b3'): -0.25,
         (('b1-a3', 'c5-c4'), 'c1-b1'): -0.296875,
         (('b1-a3', 'c5-c4'), 'c2-c3'): -0.25,
         (('b1-a3', 'c5-c4'), 'd2-d3'): -0.25,
         (('b1-a3', 'c5-c4'), 'e2-e3'): -0.2981109619140625,
         (('b1-a3', 'd5-d4'), 'a1-b1'): -0.25,
         (('b1-a3', 'd5-d4'), 'a3-b1'): 0.1220703125,
         (('b1-a3', 'd5-d4'), 'a3-b5'): 0.3495893291675831,
         (('b1-a3', 'd5-d4'), 'a3-c4'): -0.25,
         (('b1-a3', 'd5-d4'), 'b2-b3'): 0.008613195270299911,
         (('b1-a3', 'd5-d4'), 'c1-b1'): -0.14453125,
         (('b1-a3', 'd5-d4'), 'c2-c3'): -0.25,
         (('b1-a3', 'd5-d4'), 'd2-d3'): 0.2382659912109375,
         (('b1-a3', 'd5-d4'), 'e2-e3'): -0.25,
         (('b1-a3', 'd6-c4'), 'a1-b1'): 0.13194656372070312,
         (('b1-a3', 'd6-c4'), 'a3-b1'): 0.078125,
         (('b1-a3', 'd6-c4'), 'a3-b5'): 0.078125,
         (('b1-a3', 'd6-c4'), 'a3-c4'): -0.3433107507755153,
         (('b1-a3', 'd6-c4'), 'b2-b3'): -0.109375,
         (('b1-a3', 'd6-c4'), 'c1-b1'): -0.109375,
         (('b1-a3', 'd6-c4'), 'c2-c3'): -0.25,
         (('b1-a3', 'd6-c4'), 'd2-d3'): -0.25,
         (('b1-a3', 'd6-c4'), 'e2-e3'): 0.0,
         (('b1-a3', 'd6-e4'), 'a1-b1'): -0.25,
         (('b1-a3', 'd6-e4'), 'a3-b1'): -0.25,
         (('b1-a3', 'd6-e4'), 'a3-b5'): 0.3714462023889533,
         (('b1-a3', 'd6-e4'), 'a3-c4'): -0.25,
         (('b1-a3', 'd6-e4'), 'b2-b3'): -0.25,
         (('b1-a3', 'd6-e4'), 'c1-b1'): -0.1708984375,
         (('b1-a3', 'd6-e4'), 'c2-c3'): -0.07632635523623321,
         (('b1-a3', 'd6-e4'), 'd2-d3'): 0.3599249250610228,
         (('b1-a3', 'd6-e4'), 'e2-e3'): -0.06488037109375,
         (('b1-a3', 'e5-e4'), 'a1-b1'): 0.18359375,
         (('b1-a3', 'e5-e4'), 'a3-b1'): -0.25,
         (('b1-a3', 'e5-e4'), 'a3-b5'): -0.027347302449018063,
         (('b1-a3', 'e5-e4'), 'a3-c4'): -0.0302734375,
         (('b1-a3', 'e5-e4'), 'b2-b3'): -0.25,
         (('b1-a3', 'e5-e4'), 'c1-b1'): -0.0625,
         (('b1-a3', 'e5-e4'), 'c2-c3'): 0.03839111328125,
         (('b1-a3', 'e5-e4'), 'd2-d3'): -0.25,
         (('b1-a3', 'e5-e4'), 'e2-e3'): 0.1875,
         (('b1-c3',), 'a5-a4'): 0.1961603817567984,
         (('b1-c3',), 'b5-b4'): 0.31331231429596684,
         (('b1-c3',), 'c5-c4'): -0.28754023687626806,
         (('b1-c3',), 'd5-d4'): -0.23967193364746536,
         (('b1-c3',), 'd6-c4'): -0.531747868983075,
         (('b1-c3',), 'd6-e4'): -0.22680084742103768,
         (('b1-c3',), 'e5-e4'): -0.41196763042114587,
         (('b1-c3', 'a5-a4'), 'a1-b1'): -0.109375,
         (('b1-c3', 'a5-a4'), 'a2-a3'): -0.25,
         (('b1-c3', 'a5-a4'), 'b2-b3'): -0.25,
         (('b1-c3', 'a5-a4'), 'c1-b1'): -0.3115234375,
         (('b1-c3', 'a5-a4'), 'c3-a4'): -0.5279441652295942,
         (('b1-c3', 'a5-a4'), 'c3-b1'): -0.25,
         (('b1-c3', 'a5-a4'), 'c3-b5'): -0.3887481689453125,
         (('b1-c3', 'a5-a4'), 'c3-d5'): -0.13466267824184275,
         (('b1-c3', 'a5-a4'), 'c3-e4'): -0.17159366607666016,
         (('b1-c3', 'a5-a4'), 'd2-d3'): -0.25,
         (('b1-c3', 'a5-a4'), 'e2-e3'): -0.25,
         (('b1-c3', 'b5-b4'), 'a1-b1'): -0.25,
         (('b1-c3', 'b5-b4'), 'a2-a3'): -0.25,
         (('b1-c3', 'b5-b4'), 'b2-b3'): 0.040771484375,
         (('b1-c3', 'b5-b4'), 'c1-b1'): -0.25,
         (('b1-c3', 'b5-b4'), 'c3-a4'): -0.0625,
         (('b1-c3', 'b5-b4'), 'c3-b1'): -0.0625,
         (('b1-c3', 'b5-b4'), 'c3-b5'): -0.25,
         (('b1-c3', 'b5-b4'), 'c3-d5'): -0.31461832835958514,
         (('b1-c3', 'b5-b4'), 'c3-e4'): -0.2060546875,
         (('b1-c3', 'b5-b4'), 'd2-d3'): 0.058349609375,
         (('b1-c3', 'b5-b4'), 'e2-e3'): -0.25,
         (('b1-c3', 'c5-c4'), 'a1-b1'): 0.078125,
         (('b1-c3', 'c5-c4'), 'a2-a3'): -0.1708984375,
         (('b1-c3', 'c5-c4'), 'b2-b3'): 0.2191024087369442,
         (('b1-c3', 'c5-c4'), 'c1-b1'): -0.0625,
         (('b1-c3', 'c5-c4'), 'c3-a4'): -0.25,
         (('b1-c3', 'c5-c4'), 'c3-b1'): -0.00390625,
         (('b1-c3', 'c5-c4'), 'c3-b5'): -0.33203125,
         (('b1-c3', 'c5-c4'), 'c3-d5'): 0.31176031632496176,
         (('b1-c3', 'c5-c4'), 'c3-e4'): -0.25,
         (('b1-c3', 'c5-c4'), 'd2-d3'): -0.25,
         (('b1-c3', 'c5-c4'), 'e2-e3'): -0.14453125,
         (('b1-c3', 'd5-d4'), 'a1-b1'): -0.109375,
         (('b1-c3', 'd5-d4'), 'a2-a3'): 0.04296875,
         (('b1-c3', 'd5-d4'), 'b2-b3'): -0.25,
         (('b1-c3', 'd5-d4'), 'c1-b1'): -0.25,
         (('b1-c3', 'd5-d4'), 'c3-a4'): -0.00390625,
         (('b1-c3', 'd5-d4'), 'c3-b1'): 0.28741455078125,
         (('b1-c3', 'd5-d4'), 'c3-b5'): 0.5001879059509117,
         (('b1-c3', 'd5-d4'), 'c3-d5'): -0.0625,
         (('b1-c3', 'd5-d4'), 'c3-e4'): -0.25,
         (('b1-c3', 'd5-d4'), 'd2-d3'): 0.078125,
         (('b1-c3', 'd5-d4'), 'e2-e3'): -0.25,
         (('b1-c3', 'd6-c4'), 'c3-b5'): 0.578125,
         (('b1-c3', 'd6-c4'), 'c3-d5'): 0.020315825939178467,
         (('b1-c3', 'd6-e4'), 'a1-b1'): -0.4111328125,
         (('b1-c3', 'd6-e4'), 'a2-a3'): -0.296875,
         (('b1-c3', 'd6-e4'), 'b2-b3'): -0.4375,
         (('b1-c3', 'd6-e4'), 'c1-b1'): -0.28515625,
         (('b1-c3', 'd6-e4'), 'c3-a4'): -0.296875,
         (('b1-c3', 'd6-e4'), 'c3-b1'): 0.23591017723083496,
         (('b1-c3', 'd6-e4'), 'c3-b5'): -0.02308368682861328,
         (('b1-c3', 'd6-e4'), 'c3-d5'): -0.3139737213496119,
         (('b1-c3', 'd6-e4'), 'c3-e4'): -0.03121419297395167,
         (('b1-c3', 'd6-e4'), 'd2-d3'): -0.296875,
         (('b1-c3', 'd6-e4'), 'e2-e3'): -0.26702880859375,
         (('b1-c3', 'e5-e4'), 'a1-b1'): 0.12509959936141968,
         (('b1-c3', 'e5-e4'), 'a2-a3'): -0.009996309818234295,
         (('b1-c3', 'e5-e4'), 'b2-b3'): -0.25,
         (('b1-c3', 'e5-e4'), 'c1-b1'): -0.296875,
         (('b1-c3', 'e5-e4'), 'c3-a4'): -0.25,
         (('b1-c3', 'e5-e4'), 'c3-b1'): -0.296875,
         (('b1-c3', 'e5-e4'), 'c3-b5'): -0.1123046875,
         (('b1-c3', 'e5-e4'), 'c3-d5'): -0.25,
         (('b1-c3', 'e5-e4'), 'c3-e4'): 0.4553059227686388,
         (('b1-c3', 'e5-e4'), 'd2-d3'): -0.25,
         (('b1-c3', 'e5-e4'), 'e2-e3'): -0.09547042846679688,
         (('b2-b3',), 'a5-a4'): -0.3251355003618992,
         (('b2-b3',), 'b5-b4'): 0.2925694018682007,
         (('b2-b3',), 'c5-c4'): -0.19168559854142828,
         (('b2-b3',), 'd5-d4'): -0.5109015743756162,
         (('b2-b3',), 'd6-c4'): -0.5857515931129456,
         (('b2-b3',), 'd6-e4'): -0.06424868132714473,
         (('b2-b3',), 'e5-e4'): -0.3042643227578994,
         (('b2-b3', 'a5-a4'), 'b3-a4'): 0.4789094179868698,
         (('b2-b3', 'a5-a4'), 'b3-b4'): -0.25,
         (('b2-b3', 'a5-a4'), 'e2-e3'): 0.2702648639678955,
         (('b2-b3', 'b5-b4'), 'a2-a3'): -0.14919114112854004,
         (('b2-b3', 'b5-b4'), 'b1-a3'): 0.134521484375,
         (('b2-b3', 'b5-b4'), 'b1-c3'): -0.578125,
         (('b2-b3', 'b5-b4'), 'c1-a3'): -0.164306640625,
         (('b2-b3', 'b5-b4'), 'c1-b2'): -0.0439453125,
         (('b2-b3', 'b5-b4'), 'd2-d3'): 0.0,
         (('b2-b3', 'b5-b4'), 'e2-e3'): 0.0751953125,
         (('b2-b3', 'c5-c4'), 'a2-a3'): -0.00390625,
         (('b2-b3', 'c5-c4'), 'b1-c3'): -0.25,
         (('b2-b3', 'c5-c4'), 'b3-b4'): -0.00390625,
         (('b2-b3', 'c5-c4'), 'b3-c4'): -0.26677376700627065,
         (('b2-b3', 'c5-c4'), 'c1-a3'): -0.0625,
         (('b2-b3', 'c5-c4'), 'c1-b2'): 0.1572265625,
         (('b2-b3', 'c5-c4'), 'c2-c3'): 0.25,
         (('b2-b3', 'c5-c4'), 'd2-d3'): 0.0,
         (('b2-b3', 'c5-c4'), 'e2-e3'): 0.0,
         (('b2-b3', 'd5-d4'), 'a2-a3'): 0.25,
         (('b2-b3', 'd5-d4'), 'b1-a3'): 0.0625,
         (('b2-b3', 'd5-d4'), 'b1-c3'): -0.1875,
         (('b2-b3', 'd5-d4'), 'b3-b4'): 0.3533445633947849,
         (('b2-b3', 'd5-d4'), 'c1-a3'): 0.075927734375,
         (('b2-b3', 'd5-d4'), 'c1-b2'): -0.29296875,
         (('b2-b3', 'd5-d4'), 'c2-c3'): -0.0625,
         (('b2-b3', 'd5-d4'), 'd2-d3'): -0.25,
         (('b2-b3', 'd6-c4'), 'b3-c4'): 0.5857515931129456,
         (('b2-b3', 'd6-e4'), 'a2-a3'): -0.0302734375,
         (('b2-b3', 'd6-e4'), 'b1-a3'): -0.1875,
         (('b2-b3', 'd6-e4'), 'b1-c3'): 0.00054931640625,
         (('b2-b3', 'd6-e4'), 'b3-b4'): 0.09007494481881384,
         (('b2-b3', 'd6-e4'), 'c1-a3'): -0.17882919311523438,
         (('b2-b3', 'd6-e4'), 'c1-b2'): 0.124267578125,
         (('b2-b3', 'd6-e4'), 'c2-c3'): -0.0625,
         (('b2-b3', 'd6-e4'), 'd2-d3'): 0.0,
         (('b2-b3', 'd6-e4'), 'e2-e3'): -0.203125,
         (('b2-b3', 'e5-e4'), 'b1-a3'): -0.25,
         (('b2-b3', 'e5-e4'), 'b1-c3'): 0.40234375,
         (('b2-b3', 'e5-e4'), 'b3-b4'): 0.056396484375,
         (('b2-b3', 'e5-e4'), 'c1-a3'): 0.140625,
         (('b2-b3', 'e5-e4'), 'c1-b2'): -0.00390625,
         (('b2-b3', 'e5-e4'), 'c2-c3'): 0.0166015625,
         (('b2-b3', 'e5-e4'), 'd2-d3'): 0.0,
         (('b2-b3', 'e5-e4'), 'e2-e3'): 0.25,
         (('c2-c3',), 'a5-a4'): 0.03370881067417958,
         (('c2-c3',), 'b5-b4'): -0.28536654997812316,
         (('c2-c3',), 'c5-c4'): -0.3285873554975706,
         (('c2-c3',), 'd5-d4'): -0.3984755542897619,
         (('c2-c3',), 'd6-c4'): -0.34856171092266575,
         (('c2-c3',), 'd6-e4'): -0.27187361951440336,
         (('c2-c3',), 'e5-e4'): -0.07289657408929351,
         (('c2-c3', 'a5-a4'), 'b1-a3'): -0.04071044921875,
         (('c2-c3', 'a5-a4'), 'c1-c2'): 0.0,
         (('c2-c3', 'a5-a4'), 'c3-c4'): -0.25,
         (('c2-c3', 'a5-a4'), 'd1-a4'): -0.44332725058194966,
         (('c2-c3', 'a5-a4'), 'd1-b3'): -0.25,
         (('c2-c3', 'a5-a4'), 'd1-c2'): -0.00390625,
         (('c2-c3', 'a5-a4'), 'd2-d3'): 0.492919921875,
         (('c2-c3', 'a5-a4'), 'e2-e3'): 0.0,
         (('c2-c3', 'b5-b4'), 'a2-a3'): 0.4375,
         (('c2-c3', 'b5-b4'), 'c1-c2'): 0.0,
         (('c2-c3', 'b5-b4'), 'c3-b4'): 0.05525920053683162,
         (('c2-c3', 'b5-b4'), 'c3-c4'): -0.25,
         (('c2-c3', 'b5-b4'), 'd1-a4'): -0.25,
         (('c2-c3', 'b5-b4'), 'd1-b3'): -0.109375,
         (('c2-c3', 'b5-b4'), 'd1-c2'): -0.25,
         (('c2-c3', 'b5-b4'), 'e2-e3'): 0.13359451293945312,
         (('c2-c3', 'c5-c4'), 'a2-a3'): 0.21873122691727076,
         (('c2-c3', 'c5-c4'), 'b1-a3'): -0.3759765625,
         (('c2-c3', 'c5-c4'), 'b2-b3'): -0.25,
         (('c2-c3', 'c5-c4'), 'c1-c2'): 0.21466064453125,
         (('c2-c3', 'c5-c4'), 'd1-a4'): -0.77752685546875,
         (('c2-c3', 'c5-c4'), 'd1-b3'): 0.20820999145507812,
         (('c2-c3', 'c5-c4'), 'd1-c2'): -0.02083955076523125,
         (('c2-c3', 'c5-c4'), 'd2-d3'): -0.06390380859375,
         (('c2-c3', 'c5-c4'), 'e2-e3'): -0.2490234375,
         (('c2-c3', 'd5-d4'), 'a2-a3'): -0.1157379150390625,
         (('c2-c3', 'd5-d4'), 'b1-a3'): -0.0937652587890625,
         (('c2-c3', 'd5-d4'), 'b2-b3'): -0.25,
         (('c2-c3', 'd5-d4'), 'c1-c2'): -0.25,
         (('c2-c3', 'd5-d4'), 'c3-c4'): 0.0625,
         (('c2-c3', 'd5-d4'), 'c3-d4'): 0.22395382836306432,
         (('c2-c3', 'd5-d4'), 'd1-a4'): -0.25,
         (('c2-c3', 'd5-d4'), 'd1-b3'): -0.25,
         (('c2-c3', 'd5-d4'), 'd1-c2'): -0.25,
         (('c2-c3', 'd5-d4'), 'd2-d3'): -0.25,
         (('c2-c3', 'd5-d4'), 'e2-e3'): -0.296875,
         (('c2-c3', 'd6-c4'), 'a2-a3'): 0.49444580078125,
         (('c2-c3', 'd6-c4'), 'c1-c2'): -0.25,
         (('c2-c3', 'd6-c4'), 'd1-a4'): -0.4375,
         (('c2-c3', 'd6-c4'), 'd1-b3'): 0.0,
         (('c2-c3', 'd6-c4'), 'd1-c2'): 0.0,
         (('c2-c3', 'd6-c4'), 'e2-e3'): -0.12115097045898438,
         (('c2-c3', 'd6-e4'), 'a2-a3'): -0.006103515625,
         (('c2-c3', 'd6-e4'), 'b1-a3'): 0.0034607164561748505,
         (('c2-c3', 'd6-e4'), 'b2-b3'): -0.0625,
         (('c2-c3', 'd6-e4'), 'c1-c2'): -0.3785514831542969,
         (('c2-c3', 'd6-e4'), 'c3-c4'): 0.7160729968537969,
         (('c2-c3', 'd6-e4'), 'd1-a4'): -0.681396484375,
         (('c2-c3', 'd6-e4'), 'd1-b3'): -0.4169921875,
         (('c2-c3', 'd6-e4'), 'd1-c2'): 0.05879278481006622,
         (('c2-c3', 'd6-e4'), 'd2-d3'): 0.014941215515136719,
         (('c2-c3', 'd6-e4'), 'e2-e3'): -0.1447192169725895,
         (('c2-c3', 'e5-e4'), 'a2-a3'): -0.25,
         (('c2-c3', 'e5-e4'), 'b1-a3'): -0.26480266731232405,
         (('c2-c3', 'e5-e4'), 'b2-b3'): -0.25,
         (('c2-c3', 'e5-e4'), 'c1-c2'): -0.1875,
         (('c2-c3', 'e5-e4'), 'c3-c4'): -0.47919545477907377,
         (('c2-c3', 'e5-e4'), 'd1-a4'): -0.9866365389898419,
         (('c2-c3', 'e5-e4'), 'd1-b3'): -0.11730575561523438,
         (('c2-c3', 'e5-e4'), 'd1-c2'): -0.09433680772781372,
         (('c2-c3', 'e5-e4'), 'd2-d3'): -0.25,
         (('c2-c3', 'e5-e4'), 'e2-e3'): 0.05684576993482256,
         (('d2-d3',), 'a5-a4'): 0.22203559457476502,
         (('d2-d3',), 'b5-b4'): 0.5106858229041051,
         (('d2-d3',), 'c5-c4'): -0.08214295965016549,
         (('d2-d3',), 'd5-d4'): -0.39419383786868734,
         (('d2-d3',), 'd6-c4'): -0.1614321507513523,
         (('d2-d3',), 'd6-e4'): -0.4578916668198383,
         (('d2-d3',), 'e5-e4'): 0.366760348644088,
         (('d2-d3', 'a5-a4'), 'b1-a3'): -0.29296875,
         (('d2-d3', 'a5-a4'), 'b1-c3'): -0.25,
         (('d2-d3', 'a5-a4'), 'b1-d2'): -0.53363037109375,
         (('d2-d3', 'a5-a4'), 'c1-d2'): 0.15009373426437378,
         (('d2-d3', 'a5-a4'), 'c1-e3'): -0.050382617861032486,
         (('d2-d3', 'a5-a4'), 'c2-c3'): 0.22519588470458984,
         (('d2-d3', 'a5-a4'), 'd1-d2'): -0.1875,
         (('d2-d3', 'a5-a4'), 'd3-d4'): -0.5583839847300816,
         (('d2-d3', 'a5-a4'), 'e1-d2'): -0.25,
         (('d2-d3', 'b5-b4'), 'a2-a3'): 0.24609375,
         (('d2-d3', 'b5-b4'), 'b1-a3'): -0.19140625,
         (('d2-d3', 'b5-b4'), 'b1-c3'): -0.21484375,
         (('d2-d3', 'b5-b4'), 'b1-d2'): 0.10154342651367188,
         (('d2-d3', 'b5-b4'), 'c1-d2'): -0.003883468824482317,
         (('d2-d3', 'b5-b4'), 'c1-e3'): -0.47265625,
         (('d2-d3', 'b5-b4'), 'c2-c3'): 0.0,
         (('d2-d3', 'b5-b4'), 'd1-d2'): -0.015338897705078125,
         (('d2-d3', 'b5-b4'), 'd3-d4'): -0.6172926304779467,
         (('d2-d3', 'b5-b4'), 'e1-d2'): -0.611083984375,
         (('d2-d3', 'b5-b4'), 'e2-e3'): -0.4375,
         (('d2-d3', 'c5-c4'), 'a2-a3'): -0.08758544921875,
         (('d2-d3', 'c5-c4'), 'b1-a3'): -0.296875,
         (('d2-d3', 'c5-c4'), 'b1-c3'): -0.25,
         (('d2-d3', 'c5-c4'), 'b1-d2'): -0.25,
         (('d2-d3', 'c5-c4'), 'b2-b3'): -0.25,
         (('d2-d3', 'c5-c4'), 'c1-d2'): -0.109375,
         (('d2-d3', 'c5-c4'), 'c1-e3'): -0.28515625,
         (('d2-d3', 'c5-c4'), 'c2-c3'): -0.25,
         (('d2-d3', 'c5-c4'), 'd1-d2'): -0.25,
         (('d2-d3', 'c5-c4'), 'd3-c4'): 0.08219432902714544,
         (('d2-d3', 'c5-c4'), 'd3-d4'): -0.25,
         (('d2-d3', 'c5-c4'), 'e1-d2'): -0.25,
         (('d2-d3', 'c5-c4'), 'e2-e3'): -0.25,
         (('d2-d3', 'd5-d4'), 'a2-a3'): 0.22248482816011717,
         (('d2-d3', 'd5-d4'), 'b1-a3'): -0.04071044921875,
         (('d2-d3', 'd5-d4'), 'b1-c3'): -0.078125,
         (('d2-d3', 'd5-d4'), 'b1-d2'): -0.01580810546875,
         (('d2-d3', 'd5-d4'), 'b2-b3'): -0.25,
         (('d2-d3', 'd5-d4'), 'c1-d2'): -0.03603321313858032,
         (('d2-d3', 'd5-d4'), 'c1-e3'): -0.078125,
         (('d2-d3', 'd5-d4'), 'c2-c3'): -0.25,
         (('d2-d3', 'd5-d4'), 'd1-d2'): -0.04169940948486328,
         (('d2-d3', 'd5-d4'), 'e1-d2'): 0.10097622871398926,
         (('d2-d3', 'd5-d4'), 'e2-e3'): -0.25,
         (('d2-d3', 'd6-c4'), 'c1-e3'): -0.25,
         (('d2-d3', 'd6-c4'), 'c2-c3'): 0.0,
         (('d2-d3', 'd6-c4'), 'd3-c4'): -0.0016052722930908203,
         (('d2-d3', 'd6-c4'), 'd3-d4'): 0.25,
         (('d2-d3', 'd6-e4'), 'a2-a3'): -0.25,
         (('d2-d3', 'd6-e4'), 'b1-a3'): -0.25,
         (('d2-d3', 'd6-e4'), 'b1-c3'): -0.13490891456604004,
         (('d2-d3', 'd6-e4'), 'b1-d2'): -0.3232421875,
         (('d2-d3', 'd6-e4'), 'b2-b3'): -0.4375,
         (('d2-d3', 'd6-e4'), 'c1-d2'): -0.25,
         (('d2-d3', 'd6-e4'), 'c1-e3'): -0.25,
         (('d2-d3', 'd6-e4'), 'c2-c3'): -0.25,
         (('d2-d3', 'd6-e4'), 'd1-d2'): -0.25,
         (('d2-d3', 'd6-e4'), 'd3-d4'): -0.3583984375,
         (('d2-d3', 'd6-e4'), 'd3-e4'): 0.4561171126081489,
         (('d2-d3', 'd6-e4'), 'e1-d2'): -0.4375,
         (('d2-d3', 'd6-e4'), 'e2-e3'): -0.25,
         (('d2-d3', 'e5-e4'), 'a2-a3'): -0.25,
         (('d2-d3', 'e5-e4'), 'b1-a3'): -0.225830078125,
         (('d2-d3', 'e5-e4'), 'b1-c3'): -0.4375,
         (('d2-d3', 'e5-e4'), 'b1-d2'): -0.28515625,
         (('d2-d3', 'e5-e4'), 'b2-b3'): -0.25,
         (('d2-d3', 'e5-e4'), 'c1-d2'): -0.2529296875,
         (('d2-d3', 'e5-e4'), 'c1-e3'): -0.18558192253112793,
         (('d2-d3', 'e5-e4'), 'c2-c3'): -0.25,
         (('d2-d3', 'e5-e4'), 'd1-d2'): -0.382568359375,
         (('d2-d3', 'e5-e4'), 'd3-d4'): -0.296875,
         (('d2-d3', 'e5-e4'), 'd3-e4'): -0.6582973913639846,
         (('d2-d3', 'e5-e4'), 'e1-d2'): -0.296875,
         (('d2-d3', 'e5-e4'), 'e2-e3'): 0.0625,
         (('e2-e3',), 'a5-a4'): -0.297879417567186,
         (('e2-e3',), 'b5-b4'): -0.7312683772871503,
         (('e2-e3',), 'c5-c4'): -0.4245940779666365,
         (('e2-e3',), 'd5-d4'): 0.4486602101902096,
         (('e2-e3',), 'd6-c4'): -0.7182870507240295,
         (('e2-e3',), 'd6-e4'): -0.0048810434943935554,
         (('e2-e3',), 'e5-e4'): -0.3942612908408352,
         (('e2-e3', 'a5-a4'), 'b1-a3'): 0.0,
         (('e2-e3', 'a5-a4'), 'b1-c3'): -0.356201171875,
         (('e2-e3', 'a5-a4'), 'b2-b3'): -0.25,
         (('e2-e3', 'a5-a4'), 'c2-c3'): 0.05859375,
         (('e2-e3', 'a5-a4'), 'd1-e2'): 0.2794647216796875,
         (('e2-e3', 'a5-a4'), 'd2-d3'): 0.17596817016601562,
         (('e2-e3', 'a5-a4'), 'e1-e2'): 0.138427734375,
         (('e2-e3', 'a5-a4'), 'e3-e4'): 0.12763834005454555,
         (('e2-e3', 'b5-b4'), 'a2-a3'): -0.12221499646472012,
         (('e2-e3', 'b5-b4'), 'b1-a3'): 0.5236904621124268,
         (('e2-e3', 'b5-b4'), 'b1-c3'): 0.051896095275878906,
         (('e2-e3', 'b5-b4'), 'b2-b3'): 0.0,
         (('e2-e3', 'b5-b4'), 'c2-c3'): -0.055767059326171875,
         (('e2-e3', 'b5-b4'), 'd1-e2'): -0.04499440354993567,
         (('e2-e3', 'b5-b4'), 'd2-d3'): 0.16412849511103705,
         (('e2-e3', 'b5-b4'), 'e1-e2'): 0.10496218502521515,
         (('e2-e3', 'b5-b4'), 'e3-e4'): 0.27420174847449497,
         (('e2-e3', 'c5-c4'), 'a2-a3'): 0.04449462890625,
         (('e2-e3', 'c5-c4'), 'b1-a3'): -0.1956993853673339,
         (('e2-e3', 'c5-c4'), 'b1-c3'): -0.16820740699768066,
         (('e2-e3', 'c5-c4'), 'b2-b3'): 0.18735885620117188,
         (('e2-e3', 'c5-c4'), 'c2-c3'): -0.13495010789483786,
         (('e2-e3', 'c5-c4'), 'd1-e2'): -0.2552916407585144,
         (('e2-e3', 'c5-c4'), 'd2-d3'): -0.2822837829589844,
         (('e2-e3', 'c5-c4'), 'e1-e2'): 0.37872314453125,
         (('e2-e3', 'c5-c4'), 'e3-e4'): -0.5220980953650993,
         (('e2-e3', 'd5-d4'), 'a2-a3'): 0.03377750143408775,
         (('e2-e3', 'd5-d4'), 'b1-a3'): -0.37652587890625,
         (('e2-e3', 'd5-d4'), 'b1-c3'): -0.33203125,
         (('e2-e3', 'd5-d4'), 'b2-b3'): -0.3540682070152209,
         (('e2-e3', 'd5-d4'), 'c2-c3'): 0.296875,
         (('e2-e3', 'd5-d4'), 'd1-e2'): -0.25,
         (('e2-e3', 'd5-d4'), 'd2-d3'): -0.27874755859375,
         (('e2-e3', 'd5-d4'), 'e1-e2'): -0.4375,
         (('e2-e3', 'd5-d4'), 'e3-d4'): -0.7286628024922603,
         (('e2-e3', 'd5-d4'), 'e3-e4'): -0.1133575439453125,
         (('e2-e3', 'd6-c4'), 'b1-a3'): 0.578125,
         (('e2-e3', 'd6-c4'), 'b2-b3'): -0.25,
         (('e2-e3', 'd6-c4'), 'd1-e2'): 0.43359375,
         (('e2-e3', 'd6-c4'), 'd2-d3'): 0.140625,
         (('e2-e3', 'd6-c4'), 'e1-e2'): 0.0,
         (('e2-e3', 'd6-e4'), 'a2-a3'): 0.09377597397175463,
         (('e2-e3', 'd6-e4'), 'b1-a3'): -0.3291728706282126,
         (('e2-e3', 'd6-e4'), 'b1-c3'): -0.13625660809559073,
         (('e2-e3', 'd6-e4'), 'b2-b3'): 0.24752392086543296,
         (('e2-e3', 'd6-e4'), 'c2-c3'): 0.15297495227787294,
         (('e2-e3', 'd6-e4'), 'd1-e2'): -0.1858368114115853,
         (('e2-e3', 'd6-e4'), 'd2-d3'): -0.9110029479952004,
         (('e2-e3', 'd6-e4'), 'e1-e2'): -0.10636577293551597,
         (('e2-e3', 'e5-e4'), 'a2-a3'): -0.5656281884900867,
         (('e2-e3', 'e5-e4'), 'b1-a3'): 0.4115447998046875,
         (('e2-e3', 'e5-e4'), 'b1-c3'): 0.009608336724340916,
         (('e2-e3', 'e5-e4'), 'b2-b3'): -0.25,
         (('e2-e3', 'e5-e4'), 'c2-c3'): -0.0625,
         (('e2-e3', 'e5-e4'), 'd1-e2'): -0.01572122797369957,
         (('e2-e3', 'e5-e4'), 'd2-d3'): -0.12401718366891146,
         (('e2-e3', 'e5-e4'), 'e1-e2'): -0.046875})
  
    def q_value(self, state, action):
        # print (self.state, action.strip('\n'))
        if (state, action.strip('\n')) in self.book:
            return self.book[(state, action.strip('\n'))]
        return 0


    def computeActionFromQValues(self):
        move = None
        # if len(self.state) == 0 or len(self.state) == 2:
        #     # print self.state, len(self.state)
        #     max_score = -float("inf")
        #     max_move = None
        #     x = 0
        #     if len(self.state) == 2:
        #         temp_state = tuple(list(self.state))
        #         for move in chess_movesEvaluated():
        #             if self.q_value(temp_state,move) > max_score:
        #                 max_score = self.q_value(temp_state,move)
        #                 max_move  = move
        #         chess_move(max_move)
        #         move = max_move
        #     elif len(self.state) == 0:
        #         chess_move('b2-b3\n')
        #         move = 'b2-b3\n'
        if len(self.state) == 1:
            # print self.state, len(self.state)
            max_score = float("inf")
            max_move = None
            x = 0
            temp_state = tuple(list(self.state))
            for move in chess_movesEvaluated():
                if self.q_value(temp_state,move) < max_score:
                    max_score = self.q_value(temp_state,move)
                    max_move  = move
            chess_move(max_move)
            move = max_move
            # elif len(self.state) == 0:
            #     chess_move('a2-b3\n')
            #     move = 'b2-b3\n'
        else:
            move =  chess_moveAlphabeta(3,200000)
        self.state = tuple(list(self.state) + [move.strip('\n')])
        return move


        