from engine import Engine
from graphics import Graphics
from board import Board
import pygame


class Game:
    def __init__(self, human_first = True):
        self.board = Board()
        self.ai_marker = 2
        self.human_marker = 1
        self.engine = Engine(self.ai_marker, self.human_marker)
        self.graphics = Graphics(pygame.display.set_mode((600, 600)))
        self.state = "PLAYING"
        
        if human_first:
            self.current_player = self.human_marker
        else:
            self.current_player = self.ai_marker
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN and self.current_player == self.human_marker:
                mouse_pos = pygame.mouse.get_pos()
                col = mouse_pos[0]//self.graphics.cellsize
                row = mouse_pos[1]//self.graphics.cellsize
                cell_no = row*3 + col
                if self.board.mark(cell_no, self.human_marker):
                    self.current_player = self.ai_marker
        return True
    
    def play_ai_turn(self):
        self.board.mark(self.engine.get_best_move(self.board), self.ai_marker)
        self.current_player = self.human_marker

    def win_message(self):
        if (check_win := self.board.check_win()[0]) != 0:
            if check_win == self.human_marker:
                self.graphics.draw_message("You win!")
            elif check_win == self.ai_marker:
                self.graphics.draw_message("AI wins!")
            else:
                self.graphics.draw_message("It's a draw!")




    def run(self):
        running = True
        while running:
            
            if self.state == "PLAYING":
                if self.current_player == self.ai_marker and self.board.check_win()[0] == 0:
                    self.play_ai_turn()
                if not self.handle_events(): 
                    running = False
                self.graphics.update_display(self.board)
                if self.board.check_win()[0] != 0:
                    self.state = "GAMEOVER"
                    pygame.time.wait(500)
                    self.win_message()
                    pygame.display.update()

            elif self.state == "GAMEOVER":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                        running = False
                        
        pygame.quit()
            






        

        