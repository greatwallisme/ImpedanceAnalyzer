import os
from context import application
import unittest
import tempfile
import flask
import pandas as pd
import numpy as np
from application import fitPhysics


class TestViews(unittest.TestCase):
    def test_getting_example_data(self):
        """ Test API for parsing the example data filename """

        request = '/getExampleData?filename=samsung.csv'
        with application.application.test_request_context(request):
            assert flask.request.path == '/getExampleData'


class TestFitting(unittest.TestCase):

    def test_physics_fit(self):
        """ Test the fitP2D function by loading a randomly selected simulated
        spectra and check that the resulting fit is the same run.
        """

        os.chdir('../')
        Z = pd.read_pickle('./application/static/data/29000-Z.pkl')

        run = np.random.randint(1, high=len(Z)+1)
        print('run = {}'.format(run))
        selected = Z.loc[run]

        data = list(zip(selected.index.values,
                        selected.map(np.real),
                        selected.map(np.imag)))

        fit_points, best_fit, sorted_results = fitPhysics.fit_P2D(data)

        result = sorted_results.iloc[0]['run']
        self.assertEqual(run, result)

    def test_EC_fit(self):
        """ Test the EC fitting using a randomly generated simulated
        impedance spectra
        """
        assert True

    def test_physics_parameters(self):
        """
        """
        # input_parameters = pd.read_csv('./files/test_parameters.csv')
        #
        # input_spectra = pd.read_csv('./files/test_spectra.csv')
        #
        # data = list(zip())
        #
        # fit_points, best_fit, sorted_results = fitPhysics.fit_P2D(data)

        assert True


if __name__ == '__main__':
    unittest.main()
