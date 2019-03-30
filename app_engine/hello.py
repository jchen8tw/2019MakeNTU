from flask import request, Flask, jsonify
import json

app = Flask(__name__)

@app.route('/Hello', methods = ['GET','POST'])
def response():
    a = request.args.get('a')
    print(a)
    x = {"messages": [
    {
      "type": "text",
      "text": "歡迎使用最聰明的聊天機器人平台 —— YOCTOL.AI"
    },
    {
      "type": "text",
      "text": "您打算創建怎樣的機器人呢？"
    }
  ]
}
    return "<h1>hahah</h1>"

@app.route('/RPi', methods = ['GET','POST'])
def RPi_response():
    b = request.args.get('b')
    print('b = ', b)
    return "<h1>RPi<h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
