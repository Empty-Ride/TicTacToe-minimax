class Board:
    def __init__(self, _state=None):
        self._state = _state if _state is not None else [0 for _ in range(9)]
        self.winning_sequences = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]] 

    
    def mark(self, index, marker):
        if 0<=index<9 and self._state[index] == 0:
            self._state[index] = marker
            return True
        return False
    
    def get_cell_value(self, index):
        if 0<=index<9:
            return self._state[index]
        return None

    
    def check_win(self):
        for i in self.winning_sequences:
            if self._state[i[0]] == self._state[i[1]] == self._state[i[2]] != 0:
                return (self._state[i[0]], i)
        if 0 not in self._state:
            return (3,None)
        else:
            return (0,None)
    
    def unmark(self, index):
        if 0<=index<9 and self._state[index] != 0:
            self._state[index] = 0
            return True
        return False

    
    def get_mt_cells(self):
        mt_cells = []
        for i in range(9):
            if self._state[i] == 0:
                mt_cells.append(i)
        return mt_cells
            
            
