#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from flask import jsonify, request, json
import time
from time import strftime, gmtime

app.article_list = {
    1: 'article 1',
    2: 'article 2',
    3: 'article 3',
    4: 'article 4',
}
app.article_next = 5


@app.route('/')
@app.route('/index')
def index():
    """Index; default entry point"""
    ret = {
        'status': 200,
        'time_stamp': strftime("%Y-%m-%dT%H:%M:%SZ", gmtime()),
        'request_type': request.method,
    }
    return jsonify(ret)


@app.route('/article', methods=['GET', 'POST', 'DELETE'])
@app.route('/articles', methods=['GET', 'POST', 'DELETE'])
def articles():
    ret = {
        'status': 200,
        'time_stamp': strftime("%Y-%m-%dT%H:%M:%SZ", gmtime()),
        'request_type': request.method,
    }

    if request.method == 'GET':
        ret['data'] = app.article_list

    elif request.method == 'POST':
        app.article_list[app.article_next] = json.loads(request.data)
        ret['message'] = "add article {}".format(app.article_next)
        app.article_next += 1

    elif request.method == 'DELETE':
        app.article_list.clear()
        ret['message'] = "DELETE all"

    return jsonify(ret)


@app.route('/article/<int:article_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def article(article_id):
    if article_id in app.article_list:
        ret = {
            'status': 200,
            'time_stamp': strftime("%Y-%m-%dT%H:%M:%SZ", gmtime()),
            'request_type': request.method,
        }

        if request.method == 'GET':
            ret['data'] = app.article_list[article_id]

        elif request.method == 'DELETE':
            app.article_list.pop(article_id)
            ret['message'] = "article {} removed.".format(article_id)

        return jsonify(ret)

    else:
        return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
