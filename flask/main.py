from flask import Flask
import requests
import hashlib

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/url/<path:target>', methods=['GET'])
def get_content(target):
    try:
        response = requests.get(target)
        if response.status_code == 200:
            return hashlib.md5(response.content).hexdigest()
        else:
            return f'{response.status_code}, {response.reason}'
    except requests.ConnectionError:
        return 'Connection Error'
    except:
        return "sorry but failed :)"
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)