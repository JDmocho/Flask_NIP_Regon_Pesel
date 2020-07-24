# -*- coding: UTF-8 -*-
"""
Nip, Regon and Pesel Validator
Version 1.0
Author Joanna Dmochowska
"""

from flask import Flask

app = Flask(__name__)

import validator.views
