from board import Board

class Engine:
    def __init__(self, ai_marker, human_marker):
        self.ai_marker = ai_marker
        self.human_marker = human_marker

    def minimaxing(self, board, depth, is_maximizing):
        check_win= board.check_win()[0]
        mt_cells = board.get_mt_cells()
        if check_win == self.ai_marker:
            return 10- depth
        if check_win == self.human_marker:
            return -10 + depth
        if check_win == 3:
            return 0
        
        
        if is_maximizing:
            best_score = -float('inf')
            for i in mt_cells:
                board.mark(i, self.ai_marker)
                score = self.minimaxing(board, depth+1, is_maximizing=False)
                board.unmark(i)
                if score>best_score:
                    best_score = score 
            return best_score
        else:
            best_score = float('inf')
            for i in mt_cells:
                board.mark(i, self.human_marker)
                score = self.minimaxing(board, depth+1, is_maximizing=True)
                board.unmark(i)
                if score<best_score:
                    best_score = score 
                
            return best_score 

    def get_best_move(self, board = None):
        mt_cells = board.get_mt_cells()
        best_score = -float('inf')
        best_move = None
        for i in mt_cells:
            board.mark(i, self.ai_marker)
            score = self.minimaxing(board, depth = 1, is_maximizing=False)
            board.unmark(i)
            if score>best_score:
                best_move = i
                best_score = score
        return best_move


