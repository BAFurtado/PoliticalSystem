""" Keeps results
"""


class Projects:
    def __init__(self, i, ideology):
        self.id = i
        self.ideology = ideology
        self.category = 'proposed'
        self.vote = 0

    def cast_vote(self):
        self.vote += 1

    def define_category(self, status):
        self.category = status

    def __str__(self):
        return 'Id: {}, ideology: {:.4f}, votes: {}, status: {}'.format(self.id, self.ideology,
                                                                        self.vote, self.category)


if __name__ == '__main__':
    p = Projects(0, .5)
    print(p)
