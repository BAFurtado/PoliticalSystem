""" The government
"""


from representatives import Representative


class Government(Representative):
    def __init__(self, i):
        super().__init__(i)


if __name__ == '__main__':
    g = Government(0)
