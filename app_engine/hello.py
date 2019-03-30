from flask import request, Flask, jsonify
import json
import requests

app = Flask(__name__)
to_bring_list = {"Sunglasses":0, "Baseball Cap":0, "Cup":0, "Mouse":0, "Pillow":0}
dictionary = {"Sunglasses":"太陽眼鏡", "Baseball Cap":"鴨舌帽", "Mouse":"滑鼠", "Cup":"杯子","MahJong":"麻將","Pillow":"涼宮春日的等身抱枕"}
change_list = []
client_url = "https://bot-api5.yoctol.com/kurator-bot/webhooks/line/1559843026"
previos_status = '0'


def text(message):
     x = {"messages": [
    {
      "type": "text",
      "text": message
    }
    ]
    }
    
     return json.dumps(x)
    
@app.route('/check', methods = ['GET', 'POST'])
def forgot():
    message = ""
    all_remember = 1
    for x in to_bring_list:
        if to_bring_list[x] == 0:
            all_remember = 0
            message = message + " " + dictionary[x]
    if all_remember == 0:
        message = "你忘了帶" + message
    elif all_remember == 1:
        message = "你全都帶齊了呦～棒棒"
    yoctol_message = {}
    yoctol_message = text(message)
    return yoctol_message

@app.route('/all', methods = ['GET', 'POST'])
def taken():
    message = ""
    all_forgot = 1
    for x in to_bring_list:
        if to_bring_list[x] == 1:
            all_forgot = 0
            message = message + " " + dictionary[x]
    if all_forgot == 0:
        message = "你的行李箱裡有" + message
    elif all_forgot == 1:
        message = "哇～你都忘了帶ㄟQQ"
    yoctol_message = {}
    yoctol_message = text(message)
    return yoctol_message

@app.route('/ITEM', methods = ['GET','POST'])
def response():
    id = request.args.get('id')
    obj_type = ""
    if id == '0':
        obj_type = "Sunglasses"
    elif id == '1':
        obj_type = "Baseball Cap"
    elif id == '2':
        obj_type = "Cup"
    elif id == '3':
        obj_type = "Mouse"
        print(obj_type)
    elif id == '4':
        obj_type = "MahJong"
    elif id == '5':
        obj_type = "Pillow"
    elif id == 'delta':
        obj_type = 'change_list'
    yoctol_message = {}
    if obj_type in to_bring_list:
        if to_bring_list[obj_type] == 1:
            yoctol_message = text("你已經把他放進行李箱喔~")
        elif to_bring_list[obj_type] == 0:
            yoctol_message = text("你還沒把他放進行李箱喔~")
    elif obj_type == 'change_list':
        message = ""
        for item in change_list:
            message = message + " " + dictionary[item]
        message = "你的行李箱增加了" + message + " 等物品"
        yoctol_message = text(message)
    else:
        yoctol_message = text("此項物品不在你的清單中喔~")
    # r = requests.post(client_url, data= yoctol_message)
    return yoctol_message

@app.route('/RPi', methods = ['GET','POST'])
def RPi_response():
    global previos_status
    global change_list
    cur_status = request.args.get('Status')
    if cur_status == '1':
        if previos_status == '0':
            change_list = []
        photo_info = request.data
        photo_dict = json.loads(photo_info)
        obj_list = []
        item = ""
        for i in range(len(photo_dict['Labels'])):
            if photo_dict['Labels'][i]['Confidence'] > 80:
                item = photo_dict['Labels'][i]['Name']
                if item in to_bring_list:
                    to_bring_list[item] = 1
                    change_list += [item]
                    message = item + " is put into the e-luggage."
                    print(message)
                obj_list += [item]
        print(obj_list)
    previos_status = cur_status
    return "ok"

@app.route('/list', methods=['GET','POST'])
def ChangeList():
    to_bring_info = request.get_json()
    new_bring_dict = json.loads(to_bring_info)
    return "ok"

@app.route('/look', methods=['GET,POST'])
def LookList():
    return json.dumps(to_bring_list)
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
