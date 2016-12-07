from collections import Counter

class QLearningAgent(object):

	def __init__(self, alpha, discount, epsilon=0.05):
		self.alpha = alpha
		self.discount = discount
		self.q_val = Counter()


	def q_value(self, state, action):
		if (state, action) in self.q_val:
			return self.q_val[(state, action)]
		
		return 0

	def computeValueFromQValues(self, state):
		pass

	def computeActionFromQValues(self, state):
		pass

	def getAction(self, state):
		pass

	def 

