import random




def eval_function(board, piece_values = piece_values):
	if board.is_checkmate():
		return 1000

	pieces = piece_values.keys()
	white = black = 0
	for piece in pieces:
		white += len(board.pieces(piece, chess.WHITE)) * piece_values[piece]
		black += len(board.pieces(piece, chess.BLACK)) * piece_values[piece]
	return white - black 



def getSuccessors(board):
	nextBoard = []
	for move in board.legal_moves:
		new = board.copy()
		new.push(move)
		nextBoard.append((new,move))
	return nextBoard

def getAction(board):
	def max_value(board, depth):
		v = -1 * float('inf')
		for successor, _ in getSuccessors(board):
			v = max(v, value(successor, depth))
		return v

	def min_value(board, depth):
		v = float('inf')
		for successor, _ in getSuccessors(board):
			v = min(v, value(successor, depth))
		return v

	def value(board, depth):
		if board.is_checkmate() or depth == 0:
			return eval_function(board)

		if board.turn:
			return max_value(board, depth - 1)
		else:
			return min_value(board, depth - 1)

	def minimax(board):
		max_score = -1 * float('inf')
		for successor, move in getSuccessors(board):
			move_value = value(successor, depth = 1 * DEPTH)
			if move_value > max_score:
				chosen_move = move
				max_score = move_value
		return chosen_move

	return minimax(board)

