import unittest
from game.main import Spielfeld, GUI, Spielregeln, Spielmodus, DasSpiel


class ViergewinntTests(unittest.TestCase):
    def __init__(self):
        self.spielmodus = None

    def spielmodus(self):
        self.spielmodus = Spielmodus(1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
