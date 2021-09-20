from flask import Flask, request, jsonify
import math
app = Flask(__name__)


@app.route('/calculate/<number>', methods=["GET"])
def square_root(number):
    try:
        dictToReturn = {'square_root': str(math.sqrt(int(number)))}

        return jsonify(dictToReturn)
    except:
        return jsonify({'error': 'Error calculate, try again.'})

@app.route('/', methods=["GET"])
def api():
    return jsonify({'Success': 'Welcome to api calculate square root'})

@app.route('/healthcheck', methods=["GET"])
def healthcheck():
    return jsonify({'Success': '200'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')