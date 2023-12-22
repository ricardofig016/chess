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

    def get_valid_moves_bishop(self, row, col):
        return

    def get_valid_moves_king(self, row, col):
        return

    def get_valid_moves_knight(self, row, col):
        return

    def get_valid_moves_pawn(self, row, col):  # MISSING EN PASSANT LOGIC
        piece = self.matrix[row][col].piece
        valid_moves = []
        if piece.color == "white":
            if not self.matrix[row - 1][col].piece:
                valid_moves.append([row - 1, col])
                if row == 6 and not self.matrix[row - 2][col].piece:
                    valid_moves.append([row - 2, col])
            # check diagonals for takes
            if (
                row - 1 >= 0
                and col + 1 < 8
                and self.matrix[row - 1][col + 1].piece
                and self.matrix[row - 1][col + 1].piece.color == "black"
            ):
                valid_moves.append([row - 1, col + 1])
            if (
                row - 1 >= 0
                and col - 1 >= 0
                and self.matrix[row - 1][col - 1].piece
                and self.matrix[row - 1][col - 1].piece.color == "black"
            ):
                valid_moves.append([row - 1, col - 1])
        if piece.color == "black":
            if not self.matrix[row + 1][col].piece:
                valid_moves.append([row + 1, col])
                if row == 1 and not self.matrix[row + 2][col].piece:
                    valid_moves.append([row + 2, col])
            # check diagonals for takes
            if (
                row + 1 < 8
                and col + 1 < 8
                and self.matrix[row + 1][col + 1].piece
                and self.matrix[row + 1][col + 1].piece.color == "white"
            ):
                valid_moves.append([row + 1, col + 1])
            if (
                row + 1 < 8
                and col - 1 >= 0
                and self.matrix[row + 1][col - 1].piece
                and self.matrix[row + 1][col - 1].piece.color == "white"
            ):
                valid_moves.append([row + 1, col - 1])
        return valid_moves

    def get_valid_moves_queen(self, row, col):
        return

    def get_valid_moves_rook(self, row, col):
        return

    def get_valid_moves(self, row, col):
        piece = self.matrix[row][col].piece
        if not piece:
            return []
        name = piece.name
        # moves = [[row, col] for row in range(8) for col in range(8)]
        if name == "bishop":
            return self.get_valid_moves_bishop(row, col)
        if name == "king":
            return self.get_valid_moves_king(row, col)
        if name == "knight":
            return self.get_valid_moves_knight(row, col)
        if name == "pawn":
            return self.get_valid_moves_pawn(row, col)
        if name == "queen":
            return self.get_valid_moves_queen(row, col)
        if name == "rook":
            return self.get_valid_moves_rook(row, col)
        return []

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
