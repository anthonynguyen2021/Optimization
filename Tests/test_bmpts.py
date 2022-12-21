from scipy.io import loadmat
import numpy as np
import unittest
import sys

sys.path.append('Python/')
from bmpts import bmpts

class Test_bmpts(unittest.TestCase):

    # Line 139 pounders.m from callpounders.m
    def test_callPounders1(self):

        # Variables generation
        dictionaryData = loadmat('bmptsCallpounders.mat')
        X = dictionaryData['X']
        Modeld = dictionaryData['Modeld']
        Low = dictionaryData['Low']
        Upp = dictionaryData['Upp']
        delta = dictionaryData['delta'][0, 0]
        mp = dictionaryData['mp'][0, 0]
        theta = dictionaryData['theta'][0, 0]
        MdirOutput = dictionaryData['MdirOutput']

        # Generate output from bmpts
        [output1, output2] = bmpts(X, Modeld, Low, Upp, delta, theta)

        # tests check for correctness
        self.assertTrue(output2 == mp)
        self.assertTrue(np.linalg.norm(output1 - MdirOutput, 'fro') < pow(10, -20))

    # Line 194 pounders.m from callpounders.m
    def test_callPounders2(self):

        # Variables generation
        dictionaryData = loadmat('bmptsCallpounders2.mat')
        X = dictionaryData['X']
        Modeld = dictionaryData['Modeld']
        Low = dictionaryData['Low']
        Upp = dictionaryData['Upp']
        delta = dictionaryData['delta'][0, 0]
        mp = dictionaryData['mp'][0, 0]
        theta = dictionaryData['theta'][0, 0]
        MdirOutput = dictionaryData['MdirOutput']

        # Generate output from bmpts
        [output1, output2] = bmpts(X, Modeld, Low, Upp, delta, theta)

        # tests check for correctness
        self.assertTrue(output2 == mp)
        self.assertTrue(np.linalg.norm(output1 - MdirOutput, 'fro') < 10 ** -20)


if __name__ == '__main__':
    unittest.main()
