""" The government
"""


from representatives import Representative


class Government(Representative):
    def __init__(self, i, id, tol):
        super().__init__(i, id, tol)


if __name__ == '__main__':
    g = Government(0, .5, .1)
