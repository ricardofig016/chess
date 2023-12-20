class Piece(object):
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def getCode(self):
        nm = self.name
        if nm == "rook":
            return "r"
        if nm == "knight":
            return "n"
        if nm == "bishop":
            return "b"
        if nm == "queen":
            return "q"
        if nm == "king":
            return "k"
        if nm == "pawn":
            return "p"
        raise Exception(f"Not a valid piece name: {nm}")

    def __str__(self) -> str:
        return f"{self.color} {self.name}"
