# -*- coding: UTF-8 -*-
"""
Flask tests cases - check get methods
Version 1.0
Author Joanna Dmochowska
"""

import unittest
from validator.Validator import Validator


class ValidatorCases(unittest.TestCase):

    def test_nip_correct(self):
        no = Validator()

        nip_list = ["4178292374", "338-471-29-22"]

        for nip in nip_list:
            result_nip = no.check_nip(nip)

            self.assertTrue(result_nip)

    def test_regon_correct(self):
        re = Validator()

        regon_list = ["413498285", "711508900"]

        for regon in regon_list:
            result_regon = re.check_regon(regon)

            self.assertTrue(result_regon)

    def test_pesel_correct(self):
        pe = Validator()

        pesel_list = ["84021034288", "74081519098"]

        for pesel in pesel_list:
            result_pesel = pe.check_pesel(pesel)

            self.assertTrue(result_pesel)

    def test_nip_incorrect(self):
        # pesel should be incorect
        no = Validator()

        nip_list = ["111233", "111abc"]

        for nip in nip_list:
            result_nip = no.check_nip(nip)

            self.assertFalse(result_nip)

    def test_regon_incorrect(self):
        re = Validator()

        regon_list = ["4732314", "4732abc"]

        for regon in regon_list:
            result_regon = re.check_regon(regon)

            self.assertFalse(result_regon)

    def test_pesel_incorrect(self):
        pe = Validator()

        pesel_list = ["5005051", "5005abc", "12345678912"]

        for pesel in pesel_list:
            result_pesel = pe.check_pesel(pesel)

            self.assertFalse(result_pesel)