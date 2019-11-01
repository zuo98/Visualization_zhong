$(function () {
    echart_1();
    echart_2();

    echart_3();
    echart_4();

    echart_map();
    echart_5();

    //echart_1湖南货物收入
    function echart_1() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_1'));
        
    }

    //echart_2湖南省地图
    function echart_2() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_2'));

    }

    // echart_map中国地图
    function echart_map() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_map'));

        myMapOption = {
            baseOption: {
                timeline: {
                    autoPlay: true,
                    playInterval: 1000,
                    data: [],
                    width: 1000,
                    left: 'center',
                    label: {
                        show: false,
                        color: '#F2F2F2',
                        formatter: function (s) {
                            return (new Date(s)).getFullYear();
                        }
                    },
                    show: false, //hide the timeline label,but the function still exists.
                    lineStyle: {
                        color: '#F2F2F2'
                    },
                    itemStyle: {
                        color: '#F2F2F2'
                    },
                    controlStyle: {
                        color: '#F2F2F2',
                        borderColor: '#F2F2F2'
                    }
                },
                // backgroundColor: '#404a59',//div背景颜色
                title: [{
                        text: yearList[0].toString(),
                        textAlign: 'center',
                        left: '85%',
                        top: '50%',
                        textStyle: {
                            fontSize: 60,
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    },{
                        text: '2014-2016年部分地区月平均气温（℃）',
                        left: 'center',
                        top: '3%',
                        textStyle: {
                            color: '#fff',
                            fontWeight: 'lighter',
                            fontSize: 28,
                        }
                    }
                ],
                tooltip: {},
                legend: {
                    bottom: 10,
                    right: 10,
                    textStyle: {
                        color: '#fff'
                    }
                },
                visualMap: {
                    left: 10,
                    bottom: 10,
                    pieces: [{
                            min: 35,
                            label: '>35（℃）'
                        },
                        {
                            min: 30,
                            max: 35,
                            label: '30~35（℃）'
                        },
                        {
                            min: 25,
                            max: 30,
                            label: '25~30（℃）'
                        },
                        {
                            min: 20,
                            max: 25,
                            label: '20~25（℃）'
                        },
                        {
                            min: 15,
                            max: 20,
                            label: '15~20（℃）'
                        },
                        {
                            min: 10,
                            max: 15,
                            label: '10~15（℃）'
                        },
                        {
                            min: 5,
                            max: 10,
                            label: '5~10（℃）'
                        },
                        {
                            min: 0,
                            max: 5,
                            label: '0~5（℃）'
                        },
                        {
                            min: -5,
                            max: 0,
                            label: '-5~0（℃）'
                        },
                        {
                            min: -10,
                            max: -5,
                            label: '-10~-5（℃）'
                        },
                        {
                            min: -15,
                            max: -10,
                            label: '-15~-10（℃）'
                        },
                        {
                            max: -15,
                            label: '<-15（℃）'
                        },
                        {
                            max: -999,
                            label: '数据缺失'
                        }
                    ],
                    color: ['#d94e5d', '#eac736', '#50a3ba'],
                    textStyle: {
                        color: '#fff'
                    }
                },
                geo: {
                    map: 'china',
                    label: {
                        emphasis: {
                            show: false
                        }
                    },
                    // itemStyle: {
                    //     normal: {
                    //         areaColor: '#323c48',
                    //         borderColor: 'white'
                    //     },
                    //     emphasis: {
                    //         areaColor: '#2a333d'
                    //     }
                    // }
                    roam: true,//开启地图平移和缩放
                    itemStyle: {
                        normal: {
                            borderColor: 'rgba(147, 235, 248, 1)',
                            borderWidth: 1,
                            areaColor: {
                                type: 'radial',
                                x: 0.5,
                                y: 0.5,
                                r: 0.8,
                                colorStops: [{
                                    offset: 0,
                                    color: 'rgba(175,238,238, 0)' // 0% 处的颜色
                                }, {
                                    offset: 1,
                                    color: 'rgba(47,79,79, .1)' // 100% 处的颜色
                                }],
                                globalCoord: false // 缺省为 false
                            },
                            // shadowColor: 'rgba(128, 217, 248, 1)',
                            // shadowOffsetX: -2,
                            // shadowOffsetY: 2,
                            // shadowBlur: 10
                        },
                        emphasis: {
                            areaColor: '#389BB7',
                            borderWidth: 0
                        }
                    }
                },
                series: [{
                    name: '气温',
                    type: 'scatter',
                    coordinateSystem: 'geo',
                    encode: {
                        lng: 1,
                        lat: 2,
                        tooltip: [0, 3]
                    },
                    symbolSize: 9, //地图上圆点的大小
                    label: {
                        normal: {
                            formatter: '{@[0]}:{@[3]}次',
                            position: 'right',
                            show: false,
                        },
                        emphasis: {
                            show: false
                        }
                    },
                    itemStyle: {
                        emphasis: {
                            borderColor: '#fff',
                            borderWidth: 1
                        }
                    },

                }]
            },
            options: []
        };

        for (var i = 0; i < yearList.length; i++) {
            myMapOption.baseOption.timeline.data.push(yearList[i].toString());
            myMapOption.options.push({
                title: {
                    text: yearList[i].toString(),
                },
                dataset: {
                    dimensions: ['站点ID', '经度', '纬度', '温度（℃）'],
                    source: yearMean[yearList[i].toString()],
                },
            })
        }

        myChart.setOption(myMapOption)
    }

    //echart_3货物周转量
    function echart_3() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_3'));
        
    }
    //湖南高速公路
    function echart_4() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_4'));

    }
    //湖南省飞机场
    function echart_5() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_5'));

    }
    
});