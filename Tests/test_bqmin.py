from scipy.io import loadmat
import numpy as np
import unittest
import sys

sys.path.append('Python/')
from bqmin import bqmin


class Test_bqmin(unittest.TestCase):

    # Line 226 in pounders.m from callpounders.m
    def test_callpounders(self):

        # variable generation
        dictionaryData = loadmat('bqminCallpounders.mat')
        G = dictionaryData['G']
        H = dictionaryData['H']
        Lows = dictionaryData['Lows']
        Upps = dictionaryData['Upps']
        Xsp = dictionaryData['Xsp']
        mdec = dictionaryData['mdec']
        mdec = mdec[0, 0]

        # Generate output from bqmin
        [X, f] = bqmin(H, G, Lows, Upps)

        # tests output for correctness
        self.assertTrue((f - mdec) < 10 ** -10)
        self.assertTrue(np.linalg.norm(X - Xsp, float('inf')) < 10 ** -22)


if __name__ == '__main__':
    unittest.main()
