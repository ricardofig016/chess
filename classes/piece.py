class Piece(object):
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def get_code(self):
        nm = self.name
        if nm == "rook":
            return "R"
        if nm == "knight":
            return "N"
        if nm == "bishop":
            return "B"
        if nm == "queen":
            return "Q"
        if nm == "king":
            return "K"
        if nm == "pawn":
            return ""
        raise Exception(f"Not a valid piece name: {nm}")

    def __str__(self) -> str:
        return f"{self.color} {self.name}"
