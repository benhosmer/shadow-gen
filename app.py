#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
import crypt
from flask import Flask, render_template, flash, request, redirect
app = Flask(__name__)
app.secret_key = 'this is a secret'


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return render_template('index.html', shadow=None)

    if request.method == 'POST':
        plain_password = request.form.get('pass')
        random_chars = []
        if plain_password is not None:
            for x in range(6):
                random_chars.append(random.choice(string.ascii_letters))
                random_salt = ''.join(random_chars)
            shadow_value = crypt.crypt(plain_password, '$1$%s$' % random_salt)
            flash("Shadow Hash: " + shadow_value)
        return redirect('/')

if __name__ == '__main__':
    app.run(host='192.168.33.221', debug=True)
