from flask import request, Flask, jsonify
import json
import requests

app = Flask(__name__)
to_bring_list = {"Sunglasses":1, "Baseball cap":1, "Cup":1, "Footwear":1, "Pillow":0}
client_url = "https://bot-api5.yoctol.com/kurator-bot/webhooks/line/1559843026"


def text(message):
     x = {"messages": [
    {
      "type": "text",
      "text": message
    }
    ]
    }
    
     return json.dumps(x)
    


@app.route('/ITEM', methods = ['GET','POST'])
def response():
    id = request.args.get('id')
    obj_type = ""
    if id == '0':
        obj_type = "Sunglasses"
    elif id == '1':
        obj_type = "Baseball cap"
    elif id == '2':
        obj_type = "Cup"
    elif id == '3':
        obj_type = "Footwear"
        print(obj_type)
    elif id == '4':
        obj_type = "MahJong"
    elif id == '5':
        obj_type = "Pillow"
    yoctol_message = {}
    if obj_type in to_bring_list:
        if to_bring_list[obj_type] == 0:
            yoctol_message = text("你已經把他放進行李箱喔~")
        elif to_bring_list[obj_type] == 1:
            yoctol_message = text("你還沒把他放進行李箱喔~")
    else:
        yoctol_message = text("此項物品不在你的清單中喔~")
    # r = requests.post(client_url, data= yoctol_message)
    return yoctol_message

@app.route('/RPi', methods = ['GET','POST'])
def RPi_response():
    photo_info = request.data
    photo_dict = json.loads(photo_info)
    obj_list = []
    for i in range(len(photo_dict['Labels'])):
      if photo_dict['Labels'][i]['Confidence'] > 80:
        item = photo_dict['Labels'][i]['Name']
        if item in to_bring_list:
          to_bring_list[item] = 1
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
    return "ok"
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
