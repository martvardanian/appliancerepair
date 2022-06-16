import json

with open('/home/erida-employee/Desktop/Mart/ApplianceRepairAuto/Data/user_info.json', 'r') as user:
    data = json.load(user)
    print(data['fresno']['user']['time'] + data['fresno']['user']['am'])
