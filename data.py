# html 창을 띄우기 위해서는 http://127.0.0.1/ 주소로 접속.
# css파일 및 js파일은 static 폴더에 넣고, html파일은 templates 폴더에 넣어야함. (왜인지는 모르는데 폴더 이름을 변경하면 오류가 뜸)
import requests 
import pandas as pd
from pandas import json_normalize

import json

# .html 파일에 파이썬에서 보낸 데이터를 사용하기 위한 기능
# index.html에 {% %} 또는 {{ }} 이렇게 되어있는게 flask 문법
# flask 문법이 오류처럼 표시가 되는데 실제로는 정상동작함
from flask import Flask, render_template 

# 그래프 색상을 랜덤으로 나오게 하기 위한 기능
import random 

url = 'https://api.odcloud.kr/api/15110988/v1/uddi:28552381-28fe-4825-874d-b892693a6207?page=1&perPage=500&serviceKey=AzCK2HO0AtHjboGEU5L%2B9IdpEjnFae5wTba2SBZiuxgDjeabFxWXNkePr%2FEDuX1w2deMKqt0X6NIHBawJKFCDw%3D%3D'

res = requests.get(url)
text = res.content.decode('utf-8')  # 한글을 디코딩합니다.
jsonData = json.loads(res.text)['data'] # 공공데이터의 실제 데이터 부분만 뽑아옴.

# .html파일에 보낼 전체 데이터 클래스
class TotalData: 
    def __init__(self, all_data, location_list, date_list, data_list):
        self.all_data = all_data
        self.location_list = location_list
        self.date_list = date_list
        self.data_list = data_list

# 각 지역별 연월, 일반공급 경쟁률, 특별공급 경쟁률, 그래프 색상(rgb)을 저장하기 위한 클래스
class Data:
    def __init__(self, name, date, value1, value2, r, g, b):
        self.name = name
        self.date = date
        self.value1 = value1
        self.value2 = value2
        self.r = r
        self.g = g
        self.b = b



# 지역 이름만 추출 (그래프 이름 표시를 위한 용도)
locationList = []
for d in jsonData:
    name = d['시도']
    locationList.append(name)
locationList = list(sorted(set(locationList)))


# 날짜만 추출 (그래프 하단 날짜 표시르 위한 용도)
dateList = []
for d in jsonData:
    date = d['연월']
    dateList.append(date)
dateList = list(sorted(set(dateList)))


# 전체 데이터에서 각 지역별 데이터를 뽑음.
data_list = []
for loc in locationList:
    dump_date_list = []
    dump_value1_list = []
    dump_value2_list = []
    tt = [item for item in jsonData if item.get('시도') == loc]
    for d in tt:
        date = d['연월']
        dump_date_list.append(date)
        if d['일반공급 공급세대수'] == 0: value = 0
        else: value = round(d['일반공급 접수건수']/d['일반공급 공급세대수'], 2)
        dump_value1_list.append(value)

        if d['특별공급 공급세대수'] == 0: value = 0
        else: value = round(d['특별공급 접수건수']/d['특별공급 공급세대수'], 2)
        dump_value2_list.append(value)
    data_list.append(Data(loc, dump_date_list, dump_value1_list, dump_value2_list, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))



app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html', data=TotalData(jsonData, locationList, dateList, data_list)) #index.html에 data 라는 이름으로 파이썬의 데이터들을 전달함.
    return html

if __name__ == '__main__':
    app.run(host="127.0.0.1", port='80', debug=True)
