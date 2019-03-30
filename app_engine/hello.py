from flask import request, Flask, jsonify
import json
import requests

app = Flask(__name__)
to_bring_list = {"sunglasses":0, "baseball cap":0, "cup":0, "footwear":0, "Pillow":0}
client_url = "https://bot-api5.yoctol.com/kurator-bot/webhooks/line/1559843026"

@app.route('/ITEM', methods = ['GET'])
def response():
    id = int(request.args.get('id'))
    print(id)
    obj_type = ""
    if id == 0:
        obj_type = "Sunglasses"
    elif id == 1:
        obj_type = "Baseball cap"
    elif id == 2:
        obj_type = "Cup"
    elif id == 3:
        obj_type = "Footwear"
    elif id == 4:
        obj_type = "MahJong"
    elif id == 5:
        obj_type = "Pillow"
    if obj_type in to_bring_list:
        if to_bring_list[obj_type] == 0:
            requests.post(client_url, data = "你已經把他放進行李箱喔~")
        elif to_bring_list[obj_type] == 1:
            requests.post(client_url, data = "你還沒把他放進行李箱喔~")
    else:
        requests.post(client_url, data = "此項物品不在你的清單中喔~")
    '''
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
'''

    return "<h1>hahah</h1>"

@app.route('/RPi', methods = ['GET','POST'])
def RPi_response():
    photo_info = request.data
    photo_dict = json.loads(photo_info)
    obj_list = []
    for i in range(len(photo_dict['Labels'])):
      if photo_dict['Labels'][i]['Confidence'] > 80:
        item = photo_dict['Labels'][i]['Name']
        obj_list += [item]
    print(obj_list)
    return "ok"

@app.route('/ChangeList', methods=['GET','POST'])
def ChangeList():
    to_bring_info = request.data
    to_bring_dict = json.loads(to_bring_info)
    return "ok"

@app.route('/LookList', methods=['GET,POST'])
def LookList():
    requests.post()
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
