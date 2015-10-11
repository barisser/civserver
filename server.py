from flask import Flask
from flask import request
from flask import make_response
import json
import time
import random
import world_queries

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def respond_to_index():
    response = make_response("Hi this is a random number " + str(random.randint(0,1000)), 200)
    response.headers['Access-Control-Allow-Origin']= '*'
    return response

@app.route('/', methods=['POST'])
def redmatter():
    response=make_response("you just sent a post request, the time is " + str(time.time()), 200)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin']= '*'
    return response

@app.route('/world')
def world():
    d = world_queries.total_pop()
    return render_response(d)

@app.route('/world/tiles/<x>/<y>', methods=['GET'])
def pops(x=None ,y=None):
    d = world_queries.tile_query(int(x), int(y))
    return render_response(d)

@app.route('/world/map/pops', methods=['GET'])
def pop_map():
    s = str(world_queries.pop_map())
    return render_response(s)

def render_response(mystring):
    response=make_response(str(mystring), 200)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin']= '*'
    return response

def serve():
    app.run(host='0.0.0.0', port=5000)
