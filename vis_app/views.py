from django.shortcuts import render_to_response, render
# from django.http import HttpResponse
import pandas as pd
import numpy as np
import pickle
import json
# Create your views here.


def getLocYearSta(data):

    # 给数据添加‘year’列，合并‘province’和’location‘，
    # 添加‘lable’列，方便统计每个地方每年的高温频次
    # 除掉多余列'province', 'date', 'hightemp'
    data['year'] = data['date'].dt.year
    data['location'] = data['province']+'-'+data['location']
    data['lable'] = data['location']+'-'+data['year'].apply(str)
    data.drop(['province', 'date', 'hightemp'], axis=1, inplace=True)

    # 由‘lable’统计各地每年的高温频次，返回lable_count的DataFrame
    data_count = data['lable'].value_counts()
    lable = list(data_count.index)
    count = list(data_count)
    lable_count = pd.DataFrame({'lable': lable, 'count': count})

    data = data.drop_duplicates()  # 去掉data的重复行，这步骤必须在统计频次之后

    data = pd.merge(data, lable_count)  # 合并两个DataFrame
    # 生成location为横轴，count为纵轴的透视表
    df = pd.pivot_table(
        data, values='count',
        index=['location'],
        columns=['year'],
        aggfunc=np.mean,
        fill_value=0)

    yearList = list(df.columns)  # 获取年份列表
    # 生成key为location，value为count的字典
    change_year = dict(zip(list(df.index), df.values.tolist()))
    return change_year, yearList


def getLocSta(loc_sta):
    # 合并‘province’和’location‘，
    # 除掉多余列'province', 'date', 'hightemp'
    loc_sta['location'] = loc_sta['province']+'-'+loc_sta['location']
    loc_sta.drop(['province', 'date', 'hightemp'], axis=1, inplace=True)

    # 由‘location’统计各地每年的高温频次，返回lable_count的DataFrame
    location_count = loc_sta['location'].value_counts()
    location = list(location_count.index)
    count = list(location_count)
    location_count = pd.DataFrame({
        'location': location, 'count': count
    })

    loc_sta = loc_sta.drop_duplicates()  # 去掉data的重复行，这步骤必须在统计频次之后
    loc_sta = pd.merge(loc_sta, location_count)  # 合并两个DataFrame
    loc_sta = loc_sta.values.tolist()  # 转列表格式
    return loc_sta


def getHome(request):
    return render_to_response('layout.html')


def getHighCountMap(request):
    # # pickle保存数组
    # tempExcel = r"C:\Users\mei\Desktop\temp.xlsx"
    # data = pd.read_excel(tempExcel)
    # pkl = open('data.pickle', 'wb')
    # pickle.dump(data, pkl, protocol=2)
    # pkl.close()

    # 取出数据
    pkl = open('data.pickle', 'rb')
    data = pickle.load(pkl)
    pkl.close()
    location_count = getLocSta(data)

    pkl = open('data.pickle', 'rb')
    data2 = pickle.load(pkl)
    pkl.close()
    year_count, year_list = getLocYearSta(data2)

    return render(request, 'highMap.html', {
        'year_list': json.dumps(year_list),
        'year_count': json.dumps(year_count),
        'location_count': json.dumps(location_count)
    })
