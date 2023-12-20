class Cell(object):
    def __init__(self, piece=None) -> None:
        self.piece = piece

    def clear(self):
        self.piece = None

    def fill(self, piece):
        self.piece = piece

    def __str__(self) -> str:
        if self.piece:
            return self.piece.getCode()
        return "-"
