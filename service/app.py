from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    return "Hello, /!" + request.headers.get('X-Authorization',"")

@app.route('/private', methods=['GET', 'POST'])
def private():
    return "Hello, Private!" + request.headers.get('X-Authorization',"")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
