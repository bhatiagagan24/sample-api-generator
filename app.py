# main api file

from flask import Flask
from flask.globals import request
import pymongo
import returnResponse

app = Flask(__name__)



routeList = ['posts', 'comments', 'users']

@app.route('/')
def homePage():
    return '''This is the home page. Predefined routelist is posts, comments,
    users. The request is of the format /posts, /comments, /users. Add a count get 
    request to get the number of responses. Otherwise it returns only one response.

    '''

@app.route('/<value>')
def returnValue(value):
    num = 1
    if value in routeList:
        try:
            num = request.args.get("count")
            num = int(num)
            print(type(num))
            print(num)
        except:
            num = 1
        resp = returnResponse.returnJson(value, num)
        print(type(resp))
        return resp
        # return "Value found"
    else:
        return "Value not found"


if __name__ == '__main__':
    app.run(debug=True)