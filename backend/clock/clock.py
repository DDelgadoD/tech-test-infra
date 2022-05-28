from flask import Flask
import time
import os

from flask import Flask

app = Flask(__name__)
port = os.environ.get("PORT")
host = os.environ.get("HOSTNAME")


@app.route('/clock', methods = ['GET'])
def clock():
    return str(time.time())

if __name__=="__main__":
    app.run(debug=False,host=host,port=port)

