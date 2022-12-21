# Test with 'pytest test_calFun'
from scipy.io import loadmat
import numpy as np
import unittest
import sys

sys.path.append('Python/')
from calFun import calFun


class Test_calFun(unittest.TestCase):

    # From call_pounders.m
    def test_calFun1(self):

        # Input generation
        dictionaryData = loadmat('calFunCallpounders.mat')
        X0 = dictionaryData['X0']
        Y0 = dictionaryData['Y0']

        # test for correct output
        self.assertTrue(np.linalg.norm(calFun(X0) - Y0, float('inf')) < 10 ** -6)  # Check each entry is within 6 digits

    # From call_pounders_test.py
    def test_calFun2(self):

        # Input generation
        X0 = np.array([[0.5, 0.5]])
        Y0 = np.array([[0.75, 0.75]])

        # test for correct output
        self.assertTrue(np.linalg.norm(calFun(X0) - Y0, float('inf')) < 10 ** -6)  # Check each entry within 6 digits


if __name__ == '__main__':
    unittest.main()
