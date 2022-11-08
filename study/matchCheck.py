
import json
import requests
import jsonpath
import datetime



if __name__ == '__main__':
    proxies = {
        "http": "pcd364235.netvigator.com:27552",
        "https": "pcd364235.netvigator.com:27552",
    }
    token = "5632802743:AAEsUXk8qFin53IzobLkJxioSTuJlQMNDVo"  # 替换成你自己的token
    chat_id = 5377967027  # 替换成你自己的chat_id
    # token = "5023925888:AAF-8TLg2ALZGrqwzWVQVvbhyusgET7-cfg"  # 替换成你自己的token
    # chat_id = -1001539672825  # 替换成你自己的chat_id
    botUrl =  'https://api.telegram.org/bot{token}/sendMessage'
    botData = json.dumps({"chat_id": chat_id, "text": "【机器人】测试消息"})
    #botResult = requests.post(url=botUrl,data=matchCheckData,headers=matchCheckHeaders)

    # 设置地址，请求参数等
    matchCheckurl = 'http://zb335.com/excuse/match/football/list'
    matchCheckData =json.dumps({"listType":'-1'})
    matchCheckHeaders =  {'content-type': 'application/json','charset':'utf-8'}
    # 比赛发送请求，获取相应
    matchResult = requests.post(url=matchCheckurl,data=matchCheckData,headers=matchCheckHeaders)
    requests.packages.urllib3.disable_warnings()
    # 机器人发请求
    #botResult = requests.post(url=botUrl, data=botData,verify=False)
   # print(botResult.json())
    # 将结果转换为json
    matchResult_json = matchResult.json()

    # 从json结果中只取 status ==2 的数据（进行中）
    result = jsonpath.jsonpath(matchResult_json, '$..[?(@.status==2)]')
    #print(result)
    # 获取当前系统时间
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    now1 = (datetime.datetime.now() + datetime.timedelta(minutes=-120)).strftime("%Y-%m-%d %H:%M:%S")

    #print("当前比赛场数",len(result))
    i = 0
    for key in range(len(result)):
        if result[key]['timeUpdate'] is not None:
            #print(result[key]['timeUpdate'])
            if result[key]['timeUpdate'] < now1:
                print("当前比赛场数", len(result))
                print("数据出现异常,比赛ID：",result[key]['matchId'])
                print("比赛主队名称：", result[key]['homeTeamShowName'])
                print("比赛客队名称：",result[key]['awayTeamShowName'])
                continue
            else:
                print("当前时间比赛都是正常的")
                continue
        else:
            i = i + 1

    print("当前时间有几场比赛是异常的",  i)
