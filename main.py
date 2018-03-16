import json
from datetime import date
from yidong import QueryYidong
import config



if __name__ == '__main__':
    yidong = QueryYidong()
    # for item in yidong.queryRouteStationTime():
    #     print(item)
    # yidong.saveRouteStationTime()
    # yidong.saveAll()
    with open(config.busSchedule_DIR+config.busSchedule_FILE,'r',encoding='utf-8') as f:
        busSchedule = f.read()
        busSchedule = json.loads(busSchedule)

    with open(config.routeStationList_DIR+config.routeStationList_FILE,'r',encoding='utf-8') as f:
        routeStationList = json.loads(f.read())

    with open(config.routeStationTime_DIR+config.routeStationTime_FILE,'r',encoding='utf-8') as f:
        routeStationTime = json.loads(f.read())

    common_items = ['routeName','routeSeq','createTime','updateTime','scheduleDate']
    schedule_items = ['departureTime','arrivalTime','remark1','routeCodeStr',\
                      'vehicleModelName','vehicleNo','name','driverId','type',\
                      'schedulingSeq','id','authId','vehicleModel','startStationName',\
                      'endStation']

    newBusSchedule = {k:{} for k in busSchedule.keys()}

    for k,v in busSchedule.items():

        for key in common_items:
            newBusSchedule[k][key] = v[0][key]

        newBusSchedule[k]['schedule'] = []
        for item in v:
            single = {}
            for key in schedule_items:
                single[key] = item[key]
            newBusSchedule[k]['schedule'].append(single)


    for k in newBusSchedule.keys():
        if k in routeStationList:
            newBusSchedule[k]['routeStationList'] = routeStationList[k]
        else:
            newBusSchedule[k]['routeStationList'] = {0:[],1:[]}
        # print(k,newBusSchedule[k]['routeStationList'])

    for k in newBusSchedule.keys():
        if k in routeStationTime:
            print(k)
            for item in newBusSchedule[k]['schedule']:
                if item['type'] == 0:
                    try:
                        item['routeStationTime'] = routeStationTime[k]["0"][item['routeCodeStr']]
                    except KeyError:
                        print('routeStationTime[{}]["0"][{}] not exists'.format(k,item['routeCodeStr']))
                        item['routeStationTime'] = []
                else:
                    try:
                        item['routeStationTime'] = routeStationTime[k]["1"][str(item['routeCodeStr'])]
                    except KeyError:
                        print('routeStationTime[{}]["1"][{}] not exists'.format(k, item['routeCodeStr']))
                        item['routeStationTime'] = []
        else:
            for item in newBusSchedule[k]['schedule']:
                item['routeStationTime'] = []

    if type(newBusSchedule) == list or type(newBusSchedule) == dict:
        documentJSON = json.dumps(newBusSchedule, ensure_ascii=False, indent=4)
        documentJSONBYTES = documentJSON.encode('utf-8')
    with open('testdata\\' + 'newBusSchedule' + str(date.today()) + '.json', 'wb') as f:
        f.write(documentJSONBYTES)

