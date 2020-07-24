# -*- coding: UTF-8 -*-
"""
Flask tests cases - check get methods
Version 1.0
Author Joanna Dmochowska
"""

import unittest
from validator import app


class FlaskTestCases(unittest.TestCase):

    def setUp(self) -> None:
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_nip_correct(self):

        nip_list = ["4178292374", "3384712922"]

        for nip in nip_list:
            # get url
            result_variable = self.app.get('/check/nip/' + nip)
            # convert result_variable.data to string from byte
            result_variable_str = str(result_variable.data, "utf-8")
            # assertion
            self.assertEqual(result_variable_str, '<b style="color:green">'
                                                  'NIP number ' + nip +
                             ' is correct</b>')

    def test_regon_correct(self):

        regon_list = ["413498285", "711508900"]

        for regon in regon_list:
            result_variable = self.app.get('/check/regon/' + regon)
            result_variable_str = str(result_variable.data, "utf-8")
            self.assertEqual(result_variable_str, '<b style="color:green">'
                                                  'Regon number ' + regon +
                             ' is correct</b>')

    def test_pesel_correct(self):
        pesel_list = ["13301593751", "12040309502"]

        for pesel in pesel_list:
            result_variable = self.app.get('/check/pesel/' + pesel)
            result_variable_str = str(result_variable.data, "utf-8")
            self.assertEqual(result_variable_str, '<b style="color:green">'
                                                  'Pesel number ' + pesel +
                             ' is correct</b>')

    def test_nip_incorrect(self):

        nip_list = ["111233", "111abc"]

        for nip in nip_list:
            result_variable = self.app.get('/check/nip/' + nip)
            result_variable_str = str(result_variable.data, "utf-8")
            self.assertEqual(result_variable_str, '<b style="color:red">'
                                                  'NIP number ' + nip +
                             ' is incorrect</b>')

    def test_regon_incorrect(self):

        regon_list = ["4732314", "4732abc"]

        for regon in regon_list:
            result_variable = self.app.get('/check/regon/' + regon)
            result_variable_str = str(result_variable.data, "utf-8")
            self.assertEqual(result_variable_str, '<b style="color:red">'
                                                  'Regon number ' + regon +
                             ' is incorrect</b>')

    def test_pesel_incorrect(self):

        pesel_list = ["5005051", "5005abc"]

        for pesel in pesel_list:
            result_variable = self.app.get('/check/pesel/' + pesel)
            result_variable_str = str(result_variable.data, "utf-8")
            self.assertEqual(result_variable_str, '<b style="color:red">'
                                                  'Pesel number ' + pesel +
                             ' is incorrect</b>')
