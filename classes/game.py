from classes.cell import Cell
from classes.piece import Piece


class Game(object):
    def __init__(self) -> None:
        self.matrix = []
        self.populate()
        self.turn = "white"

    def populate(self):
        w = "white"
        b = "black"

        # append black pieces
        self.matrix.append(
            [
                Cell(Piece("rook", b)),
                Cell(Piece("knight", b)),
                Cell(Piece("bishop", b)),
                Cell(Piece("queen", b)),
                Cell(Piece("king", b)),
                Cell(Piece("bishop", b)),
                Cell(Piece("knight", b)),
                Cell(Piece("rook", b)),
            ]
        )
        self.matrix.append([Cell(Piece("pawn", b)) for _ in range(8)])

        # append empty rows
        for _ in range(4):
            self.matrix.append([Cell() for _ in range(8)])

        # append white pieces
        self.matrix.append([Cell(Piece("pawn", w)) for i in range(8)])
        self.matrix.append(
            [
                Cell(Piece("rook", w)),
                Cell(Piece("knight", w)),
                Cell(Piece("bishop", w)),
                Cell(Piece("queen", w)),
                Cell(Piece("king", w)),
                Cell(Piece("bishop", w)),
                Cell(Piece("knight", w)),
                Cell(Piece("rook", w)),
            ]
        )

    def validMoves(self, row, col):
        piece = self.matrix[row][col].piece
        if not piece:
            return []
        name = piece.name
        color = piece.color
        moves = [[row, col] for row in range(8) for col in range(8)]
        valid_moves = []
        if name == "bishop":
            for move in moves:
                if abs(move[0] - row) == abs(move[1] - col):
                    valid_moves.append(move)
        elif name == "king":
            pass
        elif name == "knight":
            pass
        elif name == "pawn":
            pass
        elif name == "queen":
            pass
        elif name == "rook":
            pass
        return valid_moves

    def move(self, s_row, s_col, f_row, f_col):
        piece = self.matrix[s_row][s_col].piece
        self.matrix[s_row][s_col].clear()
        self.matrix[f_row][f_col].fill(piece)
        self.flip_turn()
        print(f"game: moved {piece} from [{s_row},{s_col}] to [{f_row},{f_col}]")
        return

    def flip_turn(self):
        self.turn = "black" if self.turn == "white" else "white"
        return

    def __str__(self) -> str:
        s = ""
        for row in self.matrix:
            for cell in row:
                s += str(cell) + " "
            s += "\n"
        return s
