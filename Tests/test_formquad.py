from scipy.io import loadmat
import numpy as np
import unittest
import sys

sys.path.append('Python/')
from formquad import formquad


class Test_formquad(unittest.TestCase):

    # Line 136 Pounders.m from callpounders.m using default X0 in callpounders.m
    def test_formquad1(self):

        # Variables generation
        dictionaryData = loadmat('formquadCallPounders.mat')
        X = dictionaryData['X']
        F = dictionaryData['F']
        delta = dictionaryData['delta']
        xkin = dictionaryData['xkin']
        mpmax = dictionaryData['mpmax']
        Pars = dictionaryData['Pars']
        vf = dictionaryData['vf']
        Mdir = dictionaryData['Mdir']
        mp = dictionaryData['mp']
        mp = mp[0, 0]
        valid = dictionaryData['valid']
        valid = True if valid else False  # if valid = 1 in matlab, set it to True
        G = dictionaryData['G']
        H = dictionaryData['H']
        Mind = dictionaryData['Mind']

        # Output generation from formquad
        [MdirOut, mpOut, validOut, GOut, HOut, MindOut] = formquad(X, F, delta, xkin, mpmax, Pars, vf)

        # tests check for correctness
        self.assertTrue(mpOut == mp)
        self.assertTrue(np.shape(GOut) == np.shape(G))
        self.assertTrue(np.shape(HOut) == np.shape(H))
        self.assertTrue(MindOut == Mind)
        self.assertTrue(validOut == valid)
        self.assertTrue(np.linalg.norm(MdirOut - Mdir, 'fro') < 10 ** -10)

    # Line 154 Pounders.m from callpounders.m using default X0 in callpounders.m
    def test_formquad2(self):

        # Variables generation
        dictionaryData = loadmat('formquadCallPounders2.mat')
        X = dictionaryData['X']
        F = dictionaryData['F']
        delta = dictionaryData['delta']
        xkin = dictionaryData['xkin']
        mpmax = dictionaryData['mpmax']
        Pars = dictionaryData['Pars']
        vf = dictionaryData['vf']
        mp = dictionaryData['mp']
        mp = mp[0, 0]
        valid = dictionaryData['valid']
        valid = True if valid else False  # if valid = 1 in matlab, set it to True
        Gres = dictionaryData['Gres']
        Hresdel = dictionaryData['Hresdel']
        Mind = dictionaryData['Mind']

        # Output generation from formquad
        [_, mpOut, validOut, GOut, HOut, MindOut] = formquad(X, F, delta, xkin, mpmax, Pars, vf)

        # tests check for correctness
        self.assertTrue(mpOut == mp)
        self.assertTrue(np.linalg.norm(Gres - GOut) < 10 ** -10)
        self.assertTrue(np.linalg.norm(Hresdel - HOut) < 10 ** -10)
        self.assertTrue(sum(MindOut - Mind) == 0)  # Check indices are the same
        self.assertTrue(validOut == valid)

    # Line 192 Pounders.m from callpounders.m using default X0 in callpounders.m
    def test_formquad3(self):

        # Variables generation
        dictionaryData = loadmat('formquadCallPounders3.mat')
        X = dictionaryData['X']
        F = dictionaryData['F']
        delta = dictionaryData['delta']
        xkin = dictionaryData['xkin']
        mpmax = dictionaryData['mpmax']
        Pars = dictionaryData['Pars']
        vf = dictionaryData['vf']
        mp = dictionaryData['mp']
        mp = mp[0, 0]
        valid = dictionaryData['valid']
        valid = True if valid else False  # if valid = 1 in matlab, set it to True
        G = dictionaryData['G']
        H = dictionaryData['H']
        Mind = dictionaryData['Mind']
        Mdir = dictionaryData['Mdir']

        # Output generation from formquad
        [MdirOut, mpOut, validOut, GOut, HOut, MindOut] = formquad(X, F, delta, xkin, mpmax, Pars, vf)

        # tests check for correctness
        self.assertTrue(mpOut == mp)
        self.assertTrue(np.linalg.norm(G - GOut) < 10 ** -10)
        self.assertTrue(np.linalg.norm(H - HOut) < 10 ** -10)
        self.assertTrue(sum(abs(MindOut - Mind)) == 0)
        self.assertTrue(validOut == valid)
        self.assertTrue(np.linalg.norm(Mdir - MdirOut, 'fro') < 10 ** -10)

    # Line 205 Pounders.m from callpounders.m using default X0 in callpounders.m
    def test_formquad4(self):

        # Variables generation
        dictionaryData = loadmat('formquadCallPounders4.mat')
        X = dictionaryData['X']
        F = dictionaryData['F']
        delta = dictionaryData['delta']
        xkin = dictionaryData['xkin']
        mpmax = dictionaryData['mpmax']
        Pars = dictionaryData['Pars']
        vf = dictionaryData['vf']
        mp = dictionaryData['mp']
        mp = mp[0, 0]
        valid = dictionaryData['valid']
        valid = True if valid else False  # if valid = 1 in matlab, set it to True
        G = dictionaryData['G']
        H = dictionaryData['H']
        Mind = dictionaryData['Mind']
        Mdir = dictionaryData['Mdir']

        # Output generation from formquad
        [MdirOut, mpOut, validOut, GOut, HOut, MindOut] = formquad(X, F, delta, xkin, mpmax, Pars, vf)

        # tests check for correctness
        self.assertTrue(mpOut == mp - 1)
        self.assertTrue(np.linalg.norm(G - GOut) < 10 ** -10)
        self.assertTrue(np.linalg.norm(H - HOut) < 10 ** -10)
        self.assertTrue(sum(abs(MindOut - (Mind-1))) == 0)
        self.assertTrue(validOut == valid)
        self.assertTrue(np.linalg.norm(Mdir - MdirOut, 'fro') < 10 ** -10)


if __name__ == '__main__':
    unittest.main()
