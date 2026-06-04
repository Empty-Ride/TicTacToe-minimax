import pygame
class Graphics:
    def __init__(self, screen , cellsize = 200, cross_marker = 1, circle_marker = 2):
        self.screen = screen
        self.cellsize = cellsize
        self.width = cellsize*3
        self.height = cellsize*3
        self.cross_marker = cross_marker
        self.circle_marker = circle_marker
        pygame.font.init()
        self.font = pygame.font.Font(None, self.cellsize//2)

        #colors
        self.BG_COLOR = (255, 255, 255)
        self.LINE_COLOR = (0,0,0)
        self.X_COLOR = (0,0,255)
        self.O_COLOR = (255,0,0)

        #initializing
        pygame.init()

    def draw_grid(self):
        self.screen.fill(self.BG_COLOR)
        #vertical lines
        pygame.draw.line(self.screen, self.LINE_COLOR,(self.cellsize,0),(self.cellsize,self.height),15)
        pygame.draw.line(self.screen, self.LINE_COLOR,(self.cellsize*2,0),(self.cellsize*2,self.height),15)
        #horizontal lines
        pygame.draw.line(self.screen, self.LINE_COLOR,(0,self.cellsize),(self.width,self.cellsize),15)
        pygame.draw.line(self.screen, self.LINE_COLOR,(0,self.cellsize*2),(self.width, self.cellsize*2),15)


    def win_line(self, board):
        check_win = board.check_win()
        if check_win[0] in [self.cross_marker, self.circle_marker]:
            win_seq = check_win[1]
            start_cell = win_seq[0]
            end_cell = win_seq[2]

            start_row = start_cell//3
            start_col = start_cell%3
            end_row = end_cell//3
            end_col = end_cell%3

            start_pos = (int(start_col*self.cellsize + self.cellsize/2), int(start_row*self.cellsize + self.cellsize/2))
            end_pos = (int(end_col*self.cellsize + self.cellsize/2), int(end_row*self.cellsize + self.cellsize/2))

            pygame.draw.line(self.screen, (0,255,0), start_pos, end_pos, 15)
            

    def draw_message(self, message):
        self.screen.fill(self.BG_COLOR)
        text = self.font.render(message, True, (0, 0, 0))
        self.screen.blit(text, (self.width // 2 - text.get_width() // 2, self.height // 2 - text.get_height() // 2))
    

            

    def draw_markers(self, board):
        for i in range(9):
            cell_val = board.get_cell_value(i)
            row = i//3
            column = i%3
            center_x  = int(column * self.cellsize + self.cellsize / 2)
            center_y = int(row * self.cellsize + self.cellsize / 2)

            if cell_val == self.cross_marker:
                offset = self.cellsize/3
                pygame.draw.line(self.screen, self.X_COLOR, (center_x-offset,center_y-offset),(center_x+offset,center_y+offset),10)
                pygame.draw.line(self.screen, self.X_COLOR, (center_x+offset,center_y-offset),(center_x-offset,center_y+offset), 10)

            if cell_val == self.circle_marker:
                pygame.draw.circle(self.screen, self.O_COLOR, (center_x,center_y), self.cellsize/3,10)
    
    def update_display(self, board):
        self.draw_grid()
        self.draw_markers(board)
        self.win_line(board)
        pygame.display.update()
        



        




    