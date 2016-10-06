from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/auth', methods=['GET', 'POST'])
def hello_world():
    if request.headers.get('X-Authorization') != '1234':
        return "FAIL", 401
    else:
        return "PASS", 200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
