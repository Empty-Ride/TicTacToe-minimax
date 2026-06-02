from board import Board
from engine import Engine
from graphics import Graphics
import pygame

def main():
    engine = Engine(ai_marker=2,human_marker=1)
    board = Board()
    human_marker = 1
    ai_marker = 2
    
    screen = pygame.display.set_mode((600, 600))
    graphics = Graphics(screen)
    
    running = True
    while running:
        graphics.update_display(board)
        if (check_win := board.check_win()[0]) != 0:
            if check_win == human_marker:
                graphics.draw_message("You win!")
            elif check_win == ai_marker:
                graphics.draw_message("AI wins!")
            else:
                graphics.draw_message("It's a draw!")
            running = False
            pygame.time.wait(1000)
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                col = mouse_pos[0]//graphics.cellsize
                row = mouse_pos[1]//graphics.cellsize
                cell_no = row*3 + col
                
                if board.mark(cell_no, human_marker):
                    if board.check_win()[0] == 0:
                        board.mark(engine.get_best_move(board), ai_marker)


if __name__ == "__main__":
    main()