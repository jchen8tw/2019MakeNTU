from flask import request, Flask, jsonify
import json
import requests

to_bring_list = {}
brougth_list = {}
app = Flask(__name__)

@app.route('/ChatBot', methods = ['GET','POST'])
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
    photo_info = request.data
    print(photo_info)
    photo_dict = json.loads(photo_info)
    obj_list = []
    for i in range(len(photo_dict['Labels'])):
      if photo_dict['Labels'][i]['Confidence'] > 80:
        obj_list += [photo_dict['Labels'][i]['Name']]
    print(obj_list.decode())
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
