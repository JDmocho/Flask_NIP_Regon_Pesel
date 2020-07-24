# -*- coding: UTF-8 -*-
"""
Nip, Regon and Pesel Validator
Version 1.0
Author Joanna Dmochowska
"""

from validator import app
from flask import render_template
from flask import request
from validator.Validator import Validator


@app.route('/')
def show_form():
    return render_template('form.html')


@app.route('/check/nip/<nip>')
def show_results_nip(nip):
    validator = Validator()
    result_nip = validator.check_nip(nip)
    if result_nip:
        return '<b style="color:green">NIP number ' + nip + ' is correct</b>'
    else:
        return '<b style="color:red">NIP number ' + nip + ' is incorrect</b>'


@app.route('/check/regon/<regon>')
def show_results_regon(regon):
    validator = Validator()
    result_regon = validator.check_regon(regon)
    if result_regon:
        return '<b style="color:green">Regon number ' \
               + regon + ' is correct</b>'
    else:
        return '<b style="color:red">Regon number ' \
               + regon + ' is incorrect</b>'


@app.route('/check/pesel/<pesel>')
def show_results_pesel(pesel):
    validator = Validator()
    result_pesel = validator.check_pesel(pesel)
    if result_pesel:
        return '<b style="color:green">Pesel number ' \
               + pesel + ' is correct</b>'
    else:
        return '<b style="color:red">Pesel number ' \
               + pesel + ' is incorrect</b>'


@app.route('/check', methods=['POST'])
def check():
    nip = request.form.get('nip')
    regon = request.form.get('regon')
    pesel = request.form.get('pesel')

    validator = Validator()
    result_nip = validator.check_nip(nip)
    result_regon = validator.check_regon(regon)
    result_pesel = validator.check_pesel(pesel)

    return render_template('form.html', nip=nip, regon=regon,
                           pesel=pesel, result_nip=result_nip,
                           result_regon=result_regon,
                           result_pesel=result_pesel)
