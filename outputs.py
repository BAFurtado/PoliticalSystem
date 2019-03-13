""" Keeps results
"""


class Projects:
    def __init__(self, i, ideology):
        self.id = i
        self.ideology = ideology
        self.category = None
        self.vote = 0

    def cast_vote(self):
        self.vote += 1

    def __str__(self):
        return 'Id: {}, ideology: {:.4f}, votes: {}'.format(self.id, self.ideology, self.vote)


if __name__ == '__main__':
    p = Projects(0, .5)
    print(p)
