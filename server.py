from flask import *
from flask import Flask, request

app = Flask(__name__)     #初始化app

@app.route('/test', methods=["POST"])     #建立路由
def hello():
    req = request.json
    print(req)
    return jsonify({"msg": "request accepted"})

if __name__ == '__main__':
    app.run()     #运行app
