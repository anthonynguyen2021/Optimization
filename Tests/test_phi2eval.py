from scipy.io import loadmat
import numpy as np
import unittest
import sys

sys.path.append('Python/')
from phi2eval import phi2eval


# Tests cases: Line 96-99 in formquad.m
class Test_phi2eval(unittest.TestCase):

    # Line 136 in pounders.m from callpounders.m
    def test_phi2eval(self):

        # variables generation
        dictionaryData = loadmat('phi2evalCallpounders.mat')
        D = dictionaryData['D']
        Mind = dictionaryData['Mind']
        Mind = Mind - 1  # Shift Matlab indices to Python
        N = dictionaryData['N']

        # test to see output matches expected output
        for i in range(0, np.shape(N)[1]):
            self.assertTrue(np.linalg.norm(N[:, i:i+1] - phi2eval(D[Mind[i:i+1, 0], :]).T, np.inf) < 10 ** -20)

    # Line 153 in pounders.m from callpounders.m
    def test_phi2eval2(self):

        # variables generation
        dictionaryData = loadmat('phi2evalCallpounders2.mat')
        D = dictionaryData['D']
        Mind = dictionaryData['Mind']
        Mind = Mind - 1  # Shift Matlab indices to Python
        N = dictionaryData['N']

        # test to see output matches expected output
        for i in range(0, np.shape(N)[1]):
            self.assertTrue(np.linalg.norm(N[:, i:i+1] - phi2eval(D[Mind[i:i+1, 0], :]).T, np.inf) < 10 ** -20)

    # Line 191 in pounders.m from callpounders.m
    def test_phi2eval3(self):

        # variables generation
        dictionaryData = loadmat('phi2evalCallpounders3.mat')
        D = dictionaryData['D']
        Mind = dictionaryData['Mind']
        Mind = Mind - 1  # Shift Matlab indices to Python
        N = dictionaryData['N']

        # test to see output matches expected output
        for i in range(0, np.shape(N)[1]):
            self.assertTrue(np.linalg.norm(N[:, i:i+1] - phi2eval(D[Mind[i:i+1, 0], :]).T, np.inf) < 10 ** -20)

    # Line 205 in pounders.m from callpounders.m
    def test_phi2eval4(self):

        # variables generation
        dictionaryData = loadmat('phi2evalCallpounders4.mat')
        D = dictionaryData['D']
        Mind = dictionaryData['Mind']
        Mind = Mind - 1  # Shift Matlab indices to Python
        N = dictionaryData['N']

        # test to see output matches expected output
        for i in range(0, np.shape(N)[1]):
            self.assertTrue(np.linalg.norm(N[:, i:i+1] - phi2eval(D[Mind[i:i+1, 0], :]).T, np.inf) < 10 ** -20)


if __name__ == '__main__':
    unittest.main()
