""" Class of Representatives
"""

import random


class Representative:
    def __init__(self, i, ideo=None, tol=None):
        self.id = i
        if ideo is None or tol is None:
            # Generate random ideological and tolerance values
            self.ideology = random.random()
            self.tolerance = random.random()
        else:
            # If ideology and tolerance are provided
            self.ideology = ideo
            self.tolerance = tol

    def __str__(self):
        return 'Id: {}, ideology: {:.4f}, tolerance:{:.4f}'.format(self.id, self.ideology, self.tolerance)


if __name__ == '__main__':
    a = Representative(0)
