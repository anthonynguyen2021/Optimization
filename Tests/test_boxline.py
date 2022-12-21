from scipy.io import loadmat
import numpy as np
import unittest
import sys

sys.path.append('Python/')
from boxline import boxline

class Test_boxline(unittest.TestCase):

    # Line 139 pounders.m from callpounders.m
    def test_callPounders1(self):

        # variable generation
        dictionaryData = loadmat('boxlineCallpounders.mat')
        X = dictionaryData['X']
        Modeld = dictionaryData['Modeld']
        Low = dictionaryData['Low']
        Upp = dictionaryData['Upp']
        delta = dictionaryData['delta']
        # theta = dictionaryData['theta']
        T = dictionaryData['T']

        # tests check for correctness
        for i in range(np.shape(T)[1]):
            self.assertTrue(T[0, i] == boxline(delta * Modeld[i, :], X, Low, Upp))
            self.assertTrue(T[1, i] == boxline(-delta * Modeld[i, :], X, Low, Upp))

    # Line 194 pounders.m from callpounders.m
    def test_callPounders2(self):

        # variable generation
        dictionaryData = loadmat('boxlineCallpounders2.mat')
        X = dictionaryData['X']
        Modeld = dictionaryData['Modeld']
        Low = dictionaryData['Low']
        Upp = dictionaryData['Upp']
        delta = dictionaryData['delta']
        # theta = dictionaryData['theta']
        T = dictionaryData['T']

        # tests check for correctness
        for i in range(np.shape(T)[1]):
            self.assertTrue(T[0, i] == boxline(delta * Modeld[i, :], X, Low, Upp))
            self.assertTrue(T[1, i] == boxline(-delta * Modeld[i, :], X, Low, Upp))


if __name__ == '__main__':
    unittest.main()
