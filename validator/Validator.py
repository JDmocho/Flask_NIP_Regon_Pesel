# -*- coding: UTF-8 -*-
"""
Nip, Regon and Pesel Validator
Version 1.0
Author Joanna Dmochowska
"""


class Validator:

    def check_nip(self, nip: str) -> bool:
        nip = nip.replace('-', '')
        if len(nip) != 10 or not nip.isdigit():
            return False
        digits = [int(i) for i in nip]
        weights = (6, 5, 7, 2, 3, 4, 5, 6, 7)
        check_sum = sum(d * w for d, w in zip(digits, weights)) % 11
        return check_sum == digits[9]

    def check_regon(self, regon: str) -> bool:
        regon = regon.replace('-', '')
        if len(regon) != 9 or not regon.isdigit():
            return False
        digits = [int(i) for i in regon]
        weights = (8, 9, 2, 3, 4, 5, 6, 7)
        check_sum = sum(d * w for d, w in zip(digits, weights)) % 11
        return check_sum == digits[8]

    def check_pesel(self, pesel: str) -> bool:
        if pesel.isdigit():
            pesel = list(map(int, str(pesel)))
        else:
            return False

        if len(pesel) != 11:
            return False

        checksum = (9 * pesel[0] + 7 * pesel[1] + 3 * pesel[2] + pesel[3] + 9 * pesel[4] + 7 * pesel[5] + 3 * pesel[6] +
                    pesel[7] + 9 * pesel[8]
                    + 7 * pesel[9]) % 10
        if checksum == pesel[10]:
            return True
        else:
            return False
