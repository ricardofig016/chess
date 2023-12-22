import os, pygame, tkinter
from classes.board import Board

white = (213, 222, 229)
blue = (117, 153, 174)
black = (0, 0, 0)


def get_screen_resolution():
    root = tkinter.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.destroy()

    return screen_width, screen_height


def draw_board(screen, height):
    for row in range(8):
        for col in range(8):
            color = white if (row + col) % 2 == 0 else blue
            pygame.draw.rect(
                screen,
                color,
                (
                    col * height * 0.125,
                    row * height * 0.125,
                    height * 0.125,
                    height * 0.125,
                ),
            )
    return


def get_piece_img(piece, assets_path, size):
    name = piece.name
    color = piece.color
    file_name = color + "-" + name + ".png"
    return pygame.transform.scale(
        pygame.image.load(os.path.join(assets_path, file_name)), (size, size)
    )


def blit_pieces(screen, board, assets_path, height):
    for row in range(8):
        for col in range(8):
            piece = board.matrix[row][col].piece
            if piece:
                img = get_piece_img(piece, assets_path, height * 0.125)
                screen.blit(img, (height * 0.125 * col, height * 0.125 * row))
    return


def window(width, height, assets_path):
    board = Board()

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    # pygame.display.toggle_fullscreen()
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)
        draw_board(screen, height)
        blit_pieces(screen, board, assets_path, height)
        pygame.draw.line(screen, black, (height, 0), (height, height), 2)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    return


def run():
    screen_width, screen_height = get_screen_resolution()
    width = int(screen_width * 0.8)
    height = int(width * 0.5625)
    # print(width, height)
    assets_path = "assets/"
    window(width, height, assets_path)
    return


if __name__ == "__main__":
    run()
