""" Keeps results
"""


class Projects:
    def __init__(self, i, ideology):
        self.id = i
        self.ideology = ideology
        self.category = None

    def __str__(self):
        return 'Id: {}, ideology: {:.4f}'.format(self.id, self.ideology)


if __name__ == '__main__':
    p = Projects(0, .5)
    print(p)
