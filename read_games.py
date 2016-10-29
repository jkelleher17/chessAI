import chess.pgn

pgn = open('data/KingBase2016-03-A00-A39.pgn')
first_game = chess.pgn.read_game(pgn)
print first_game
pgn.close()