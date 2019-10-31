import json

import numpy as np
import pandas as pd
from django.shortcuts import render, render_to_response

from vis_app.config import postgreSQLconnect

# Create your views here.


def getHome(request):
    return render_to_response('layout.html')


def getHighYearCountMap(request):

    year_list = [str(x) for x in list(range(1981, 2011))]
    # 连接到一个给定的数据库
    conn = postgreSQLconnect()
    # 建立游标，用来执行数据库操作
    cursor = conn.cursor()
    # 执行SQL SELECT命令
    cursor.execute("SELECT * from year_high_count")
    # 获取SELECT返回的元组
    rowstem = cursor.fetchall()
    tem = pd.DataFrame(np.array(rowstem), columns=['location'] + year_list)

    cursorloc = conn.cursor()
    cursorloc.execute("SELECT * from location")
    rowsloc = cursorloc.fetchall()
    location = pd.DataFrame(np.array(rowsloc),
                            columns=['location', 'longitude', 'latitude'])

    location_tem = location.merge(tem, left_on='location', right_on='location')

    yeardata = []
    for year in year_list:
        yeardata.append(
            location_tem[['location', 'longitude', 'latitude',
                          year]].values.tolist())
    yearData = dict(zip(year_list, yeardata))

    location = location_tem['location'].values.tolist()
    year_count = location_tem.drop(
        columns=['location', 'longitude', 'latitude']).values.tolist()
    year_count = dict(zip(location, year_count))

    # 关闭游标
    cursor.close()
    cursorloc.close()
    # 关闭数据库连接
    conn.close()

    return render(
        request, 'highMapTimeline.html', {
            'yearList': json.dumps(year_list),
            'yearData': json.dumps(yearData),
            'year_count': json.dumps(year_count),
        })


def airtemMapTimeline(request):

    date_list = []
    for y in range(2014, 2017):
        for m in range(1, 13):
            date_list.append(str(y) + '|' + str(m))

    # 连接到一个给定的数据库
    conn = postgreSQLconnect()
    # 建立游标，用来执行数据库操作
    cursor = conn.cursor()
    # 执行SQL SELECT命令
    cursor.execute("SELECT * from hightemperature")
    # 获取SELECT返回的元组
    rowstem = cursor.fetchall()

    hightem = pd.DataFrame(np.array(rowstem),
                           columns=['stationid', 'lon', 'lat'] + date_list)

    year_mean = {}
    for date in date_list:
        yeardata = hightem[['stationid', 'lon', 'lat', date]].round({date: 2})
        year_mean[date] = yeardata.values.tolist()

    return render(
        request,
        'airtemMapTimeline.html',
        {
            'yearList': json.dumps(date_list),
            'yearMean': json.dumps(year_mean),
            # 'stationData': json.dumps(stationData)
        })
