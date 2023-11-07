# Chess-one-side-game
#chess (one side gaming)
import chess

def main():
    board = chess.Board()
    
    while not board.is_game_over():
        print(board)

        # Display all possible legal moves
        print("Possible moves: ", ", ".join([move.uci() for move in board.legal_moves]))

        move = input('Enter your move: ')
        if chess.Move.from_uci(move) in board.legal_moves:
            board.push(chess.Move.from_uci(move))
        else:
            print("Illegal move. Try again.")
    
    print("Game over")
    print("Result: " + board.result())

if __name__ == "__main__":
    main()

