from chalice import Chalice
import chalicelib.pandas_test as pt

app = Chalice(app_name='helloworld')

@app.route('/pandas/add/{x}/{y}')
def add_df(x, y):
    return {'result': pt.add_df(x, y)}

@app.route('/add/{x}/{y}')
def add(x, y):
    return {'result': float(x) + float(y)}

@app.route('/subtract/{x}/{y}')
def subtract(x, y):
    return {'result': float(x) - float(y)}

@app.route('/multiply/{x}/{y}')
def multiply(x, y):
    return {'result': float(x) * float(y)}

@app.route('/divide/{x}/{y}')
def divide(x, y):
    return {'result': float(x) / float(y)}

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/users/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
# #
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
