from flask import Flask, jsonify, request
from werkzeug.routing import BaseConverter, ValidationError

_USERS = {'1': 'Tarek', '2': 'Freya'}
_IDS = {val: id for id, val in _USERS.items()}

class RegisteredUser(BaseConverter):
    def to_python(self, value):
        if value in _USERS:
            return _USERS[value]
        raise ValidationError()
    def to_url(self, value):
        return _IDS[value]

app = Flask(__name__)
app.url_map.converters['registered'] = RegisteredUser

@app.route('/api')
def my_microservice():
    print('CM:: request', request)
    print('CM:: request.environ', request.environ)
    response = jsonify({'Hello': 'World!'})
    print('CM:: response', response)
    print('CM:: response.data', response.data)
    return response

# @app.route('/api/person/<person_id>')
# def person(person_id):
#     response = jsonify({'Hello': person_id})
#     return response

@app.route('/api/person/<registered:name>')
def person(name):
    response = jsonify({'Hello hey': name})
    return response

if __name__ == '__main__':
    print('CM:: app.url_map', app.url_map)
    app.run(host='0.0.0.0')
