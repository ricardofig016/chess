from classes.cell import Cell
from classes.piece import Piece


class Board(object):
    def __init__(self) -> None:
        self.matrix = []
        self.populate()

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

    def validMoves(self, x, y):
        moves = []
        if self.matrix[x][y].piece:
            pass
        return moves

    def __str__(self) -> str:
        s = ""
        for row in self.matrix:
            for cell in row:
                s += str(cell) + " "
            s += "\n"
        return s
