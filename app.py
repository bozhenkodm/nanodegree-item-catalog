from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/catalog/<category>/items')
def items(category):
    return 'Category: %s' % category


@app.route('/catalog/<category>/<item>')
def item(category, item):
    return 'Category: %s \n Item: %s' % (category, item)


@app.route('/catalog/<item>/edit')
def item_edit(item):
    return 'Item edit: %s' % item


@app.route('/catalog/<item>/delete')
def item_delete(item):
    return 'Item delete: %s' % item


@app.route('/catalog.json')
def items(category):
    return jsonify('json')