# -*- coding: utf-8 -*-

from __future__ import with_statement, print_function, absolute_import

from flask import Blueprint

example = Blueprint('example', __name__,
                    static_folder="../../client/dist/static",
                    template_folder="../../client/dist")


@example.route('/hello')
def show():
    return 'Hello, World!'
