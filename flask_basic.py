from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api')
def my_microservice():
    print('CM:: request', request)
    print('CM:: request.environ', request.environ)
    response = jsonify({'Hello': 'World!'})
    print('CM:: response', response)
    print('CM:: response.data', response.data)
    return response

@app.route('/api/person/<person_id>')
def person(person_id):
    response = jsonify({'Hello': person_id})
    return response

if __name__ == '__main__':
    print('CM:: app.url_map', app.url_map)
    app.run(host='0.0.0.0')
