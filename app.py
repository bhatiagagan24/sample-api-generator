# main api file

from flask import Flask
from flask.globals import request
import pymongo

app = Flask(__name__)

routeList = ['posts', 'comments', 'albums', 'photos', 'todos', 'users']


@app.route('/')
def homePage():
    return "This is the home page"

@app.route('/<value>')
def returnValue(value):
    num = 1
    if value in routeList:
        try:
            num = request.args.get("count")
        except:
            num = 1
        return "Value found"
    else:
        return "Value not found"


if __name__ == '__main__':
    app.run(debug=True)