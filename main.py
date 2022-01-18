from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello! I am running in a docker container'

@app.route('/start')
def start():
    return

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)
