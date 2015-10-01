import json
import bottle

from bottle import route, run, request, abort
from pymongo import MongoClient

db = MongoClient().bottle_test


@route('/documents', method='PUT')
def put_document():
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    if '_id' not in entity:
        abort(400, 'No _id specified')
    try:
        db['documents'].save(entity)
    except:
        abort(400)


@route('/documents/:id_', method='GET')
def get_document(id_):
    entity = db['documents'].find_one({'_id': id_})
    if not entity:
        abort(404, 'No document with id %s' % id_)
    return entity

run(host='localhost', port=8080)
