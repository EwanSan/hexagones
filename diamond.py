import numpy as np
from string import ascii_uppercase as alc
from random import randint
from numpy.lib.stride_tricks import sliding_window_view as swv

SMALL_DIAMOND = np.array(
    [
        ['', '', 'A', '', ''],
        ['', 'B', '', 'C', ''],
        ['D', '', 'E', '', 'F'],
        ['', 'G', '', 'H', ''],
        ['', '', 'I', '', '']
    ]
)

REG_DIAMOND = np.array(
    [
        ['', '', 'A', '', 'B', '', 'C', '', ''],
        ['', 'D', '', 'E', '', 'F', '', 'G', ''],
        ['H', '', 'I', '', 'J', '', 'K', '', 'L'],
        ['', 'M', '', 'N', '', 'O', '', 'P', ''],
        ['', '', 'Q', '', 'R', '', 'S', '', '']
    ]
)

class Diamond:
    def __init__(self, size='regular', minimum=1, maximum=6):
        self.size = size
        self.letter_matrix = SMALL_DIAMOND if self.size == 'small' else REG_DIAMOND
        ### Building number matrix
        nbm = np.zeros(self.letter_matrix.shape, dtype=np.uint8)
        fill_boolean = self.letter_matrix != ''
        nbm[fill_boolean] = np.random.randint(minimum, maximum, fill_boolean.sum())
        self.number_matrix = nbm
        self.goal = self.get_goal()
    
    def print_letter_matrix(self):
        print(self.letter_matrix)
    
    def print_number_matrix(self):
        print(self.number_matrix)
    
    def get_goal(self):
        windows = swv(self.number_matrix, (3,3))
        diags = np.vstack([
            np.diagonal(windows, axis1=-2, axis2=-1).reshape(-1,3),
            np.diagonal(windows[..., ::-1], axis1=-2, axis2=-1).reshape(-1,3)
        ]).tolist()
        diags = np.array([d for d in diags if not 0 in d])
        return np.random.choice(diags.sum(axis=1))
    
    def guess(self, letters):
        cumsum = 0
        for letter in letters:
            idx = np.argwhere(self.letter_matrix==letter)[0]
            cumsum += self.number_matrix[idx[0], idx[1]]
        if cumsum == self.goal:
            return 1
        else:
            return -1