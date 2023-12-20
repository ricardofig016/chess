import os, pygame, tkinter
from classes.board import Board


def get_screen_resolution():
    root = tkinter.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.destroy()

    return screen_width, screen_height


def window(width, height, assets_path):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    # pygame.display.toggle_fullscreen()
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()
    background = pygame.transform.scale(
        pygame.image.load(os.path.join(assets_path, "board.jpg")), (width, height)
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    return


def run():
    screen_width, screen_height = get_screen_resolution()
    width, height = 600, 600

    assets_path = "assets/"
    window(width, height, assets_path)
    board = Board()
    print(board)
    return


if __name__ == "__main__":
    run()
