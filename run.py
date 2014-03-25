#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app

app.config['DEBUG'] = True
# app.config['JSON_SORT_KEYS'] = False
# app.config['UPLOAD_FOLDER'] = 'tmp'
app.run()
# app.run(host='0.0.0.0',port=5000)
