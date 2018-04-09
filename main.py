import json
from datetime import date
from yidong import QueryYidong
import config
from savedata import SaveData
from sendmail import sendmail
from upload_to_qiniu import upload



if __name__ == '__main__':
    yd = QueryYidong()
    yd.saveAll()

    s = SaveData()
    s.saveSimple()
    # sendmail('报错测试')
    # upload()
