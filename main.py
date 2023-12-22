import os, pygame, tkinter
from classes.game import Game

WIDTH = 1000  # default is 1500
HEIGHT = int(WIDTH * 0.5625)

ASSETS_PATH = "assets/"

WHITE = (213, 222, 229)
BLUE = (117, 153, 174)
LIGHT_BLUE = (153, 218, 234)
BLACK = (0, 0, 0)

PIECES = {
    "black bishop": pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "black-bishop.png")),
        (HEIGHT * 0.125, HEIGHT * 0.125),
    ),
    "black king": pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "black-king.png")),
        (HEIGHT * 0.125, HEIGHT * 0.125),
    ),
    "black knight": pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "black-knight.png")),
        (HEIGHT * 0.125, HEIGHT * 0.125),
    ),
    "black pawn": pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "black-pawn.png")),
        (HEIGHT * 0.125, HEIGHT * 0.125),
    ),
    "black queen": pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "black-queen.png")),
        (HEIGHT * 0.125, HEIGHT * 0.125),
    ),
    "black rook": pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "black-rook.png")),
        (HEIGHT * 0.125, HEIGHT * 0.125),
    ),
    "white bishop": pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "white-bishop.png")),
        (HEIGHT * 0.125, HEIGHT * 0.125),
    ),
    "white king": pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "white-king.png")),
        (HEIGHT * 0.125, HEIGHT * 0.125),
    ),
    "white knight": pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "white-knight.png")),
        (HEIGHT * 0.125, HEIGHT * 0.125),
    ),
    "white pawn": pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "white-pawn.png")),
        (HEIGHT * 0.125, HEIGHT * 0.125),
    ),
    "white queen": pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "white-queen.png")),
        (HEIGHT * 0.125, HEIGHT * 0.125),
    ),
    "white rook": pygame.transform.scale(
        pygame.image.load(os.path.join(ASSETS_PATH, "white-rook.png")),
        (HEIGHT * 0.125, HEIGHT * 0.125),
    ),
}


def draw_board(screen):
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLUE
            pygame.draw.rect(
                screen,
                color,
                (
                    col * HEIGHT * 0.125,
                    row * HEIGHT * 0.125,
                    HEIGHT * 0.125,
                    HEIGHT * 0.125,
                ),
            )
    return


def blit_pieces(screen, game):
    for row in range(8):
        for col in range(8):
            piece = game.matrix[row][col].piece
            if piece:
                img = PIECES[piece.color + " " + piece.name]
                screen.blit(img, (HEIGHT * 0.125 * col, HEIGHT * 0.125 * row))
    return


def select_cell(screen, pos):
    pygame.draw.rect(
        screen,
        LIGHT_BLUE,
        (
            pos[1] * HEIGHT * 0.125,
            pos[0] * HEIGHT * 0.125,
            HEIGHT * 0.125,
            HEIGHT * 0.125,
        ),
    )


def highlight_valid_moves(screen, valid_moves):
    for move in valid_moves:
        pygame.draw.circle(
            screen,
            LIGHT_BLUE,
            (
                move[1] * HEIGHT * 0.125 + HEIGHT * 0.0625,
                move[0] * HEIGHT * 0.125 + HEIGHT * 0.0625,
            ),
            int(HEIGHT / 75),
        )
    return


def window():
    game = Game()
    phase = "select"  # select or move
    selected_cell = None
    valid_moves = None

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # pygame.display.toggle_fullscreen()
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(WHITE)
        draw_board(screen)
        if selected_cell:
            select_cell(screen, selected_cell)
        blit_pieces(screen, game)
        if valid_moves:
            highlight_valid_moves(screen, valid_moves)
        # separator line
        pygame.draw.line(screen, BLACK, (HEIGHT, 0), (HEIGHT, HEIGHT), 2)

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                # the click is on the board
                if mouse_pos[0] < HEIGHT:
                    cell_pos = [
                        int(mouse_pos[1] // (HEIGHT * 0.125)),
                        int(mouse_pos[0] // (HEIGHT * 0.125)),
                    ]
                    cell = game.matrix[cell_pos[0]][cell_pos[1]]
                    if phase == "move":
                        if cell_pos in valid_moves:
                            game.move(
                                selected_cell[0],
                                selected_cell[1],
                                cell_pos[0],
                                cell_pos[1],
                            )
                        selected_cell = None
                        valid_moves = None
                        phase = "select"
                    if phase == "select":
                        if cell.piece and game.turn == cell.piece.color:
                            selected_cell = cell_pos
                            valid_moves = game.get_valid_moves(
                                selected_cell[0], selected_cell[1]
                            )
                            phase = "move"
                        else:
                            selected_cell = None
                            phase = "select"
                # the click is outside of the board
                else:
                    pass  # IMPLEMENT BUTTONS

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    return


def run():
    # print(width, HEIGHT)
    window()
    return


if __name__ == "__main__":
    run()
