import os
from datetime import date

BASE_DIR = os.getcwd()
busSchedule_DIR = BASE_DIR + '\\data\\busSchedule\\'
routeListSet_DIR = BASE_DIR + '\\data\\routeListSet\\'
routeStationList_DIR = BASE_DIR + '\\data\\routeStationList\\'
routeStationTime_DIR = BASE_DIR + '\\data\\routeStationTime\\'

busSchedule_FILE = 'busSchedule' + str(date.today())+'.json'
routeListSet_FILE = 'routeListSet' + str(date.today())+'.json'
routeStationList_FILE = 'routeStationList' + str(date.today())+'.json'
routeStationTime_FILE = 'routeStationTime' + str(date.today())+'.json'
