
import datetime
import requests
import json
import pandas as pd
import numpy as np
import csv

from qdata.baidu_index import CITY_CODE

 
word_url = 'http://index.baidu.com/api/SearchApi/thumbnail?area=0&word={}'
city=CITY_CODE
#prov=PROVINCE_CODE

 
def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        
        "Host": "index.baidu.com",
        "Referer": "http://index.baidu.com/v2/main/index.html",
        "Cipher-Text": "1652425237825_1652501356206_VBpwl9UG8Dvs2fAi91KToRTSAP7sDsQU5phHL97raPDFJdYz3fHf9hBAQrGGCs+qJoP7yb44Uvf91F7vqJLVL0tKnIWE+W3jXAI30xx340rhcwUDQZ162FPAe0a1jsCluJRmMLZtiIplubGMW/QoE/0Pw+2caH39Ok8IsudE4wGLBUdYg1/bKl4MGwLrJZ7H6wbhR0vT5X0OdCX4bMJE7vcwRCSGquRjam03pWDGZ51X15fOlO0qMZ2kqa3BmxwNlfEZ81l3L9nZdrc3/Tl4+mNpaLM7vA5WNEQhTBoDVZs6GBRcJc/FSjd6e4aFGAiCp1Y8MD66chTiykjIN51s7gbJ44JfVS0NjBnsvuF55bs="
    }
    cookies = {
        'Cookie' : 'BIDUPSID=2EA97D98B1AD92ACAED21D8E03F7D255; PSTM=1660617139; BAIDUID=2EA97D98B1AD92AC62B78340E181FCB1:FG=1; BDUSS=Y4fmxDdXd0ZGZldlRHZ0Zhd0xFWXBjSklnQkZJbS1oa2NNQjFjOE9NZmJYY0ZqRVFBQUFBJCQAAAAAAAAAAAEAAAD0Ptk~WHi57cbHeFgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANvQmWPb0JljY0; MCITY=-288%3A; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1681439663; bdindexid=i82m2led946gvb3022n5q9i0e6; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04314521155s6qoVnridBHLMgum0mIjreiyUaOUN3fUbsytAn85H5it17qgDJoorBxoJyqDpSpC6ASIDeMUa8MacRXWGos0BoMCjOJ1CcjMF0%2FgFUGxaZagc5zONLkSEHHMyIZRJ%2FyPEbpxQ97KzJHW1KFLT1o7Ko35fVrTRcwax0OSY6at6yrb8xiEXqhqMt%2F5hS%2Fr0EnxyCld6qt4f%2BshXj76g9ts7aD7%2FG0il0T01SUSADweHF1FrRQUqS6aat4zbCiQObo9HNgNVrvm%2BoVXKmd5SsM5cVYgEJwD17DjJf%2BhbCD8g8w%3D48211353110455897918871577680478; __cas__rn__=431452115; __cas__st__212=6c117c20c164dc4f8a63cb7b806a3d9b6bf37947321aa51f2a79ba3cf2a7b710026463fffa85ee5ab8097fdc; __cas__id__212=47373947; CPID_212=47373947; CPTK_212=103934255; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; H_PS_PSSID=38516_36543_38470_38353_38368_38468_36803_38486_37921_38356_26350_38186; BA_HECTOR=00802k0k858405ag8k0l2k831i3htrb1m; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=2EA97D98B1AD92AC62B78340E181FCB1:FG=1; ZFY=Cf6ZMXJeXm7AjEIsAx3PXA1rCOoIaJzRfy0CM3M4kxA:C; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1681456040; ab_sr=1.0.1_N2IxZjk3NTNjNjRiMmNkY2RkMTBiZTYyZDQ2ZWQyNzhjZWM4MjdkNDhmYjY4ZTE0ODI3N2VmYTIwNmZjY2NlMjJhMWI1YjgyY2ZjMGM1ZDU4N2RhNDNlYTRhMDJlOTM5MDVlMzJmNDYwNzc2MjFhNGFmNGQ1MmI4YTM2Nzk1YTViNzhhYzA0YTE5MzVmMTkxYjVkNjM4N2E4MWNiZDEyNQ==; BDUSS_BFESS=Y4fmxDdXd0ZGZldlRHZ0Zhd0xFWXBjSklnQkZJbS1oa2NNQjFjOE9NZmJYY0ZqRVFBQUFBJCQAAAAAAAAAAAEAAAD0Ptk~WHi57cbHeFgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANvQmWPb0JljY0; RT="z=1&dm=baidu.com&si=89ef9a76-560d-4b35-8f83-8ccfa2861cf8&ss=lgg7ht05&sl=3&tt=36a&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=qlz"'
        #'Cookie': "__bid_n=18379203a6589298324207; BIDUPSID=2E02EE98DCCE13B3871E90D13B293B90; PSTM=1667567321; FEID=v10-907dcd0a5cc6fa5de7eb6ddc03204ab967433e10; BDUSS=UNWM2dOeDZhU215U09IaUVISHp1UjdsNUEzTVJHYmlRdkFVWFRwSGpRN1JjY0pqSVFBQUFBJCQAAAAAAAAAAAEAAAAEyXrqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANHkmmPR5JpjM; BAIDU_WISE_UID=wapp_1671101300284_101; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%223933915396%22%2C%22scope%22%3A1%7D%7D; BAIDUID=16C58FBA50EF47EF0A64399091E5A874:FG=1; BAIDUID_BFESS=16C58FBA50EF47EF0A64399091E5A874:FG=1; __xaf_fpstarttimer__=1672804972789; __xaf_thstime__=1672804973003; FPTOKEN=Ld+1YJ0/2IOF8n5w0o9hNT9x6Dgh37ZoNq6WLF+HyHg0O78kbrB2WuS6INjPP+1FBoMs/grBXUsbMe94Tcye08EvzsRFC2lD8+it5o50bMEnjRMzvEHqSO4EXjIJxCUdY8IvYeYgOK9IQVcGLklv7nEupfxOC2ncG7YSHLLczZPlFutqxJfGbs58AFqien3endohJmslnornN5poweWkL0TgmE1al+fqpEhxenk3vhGXJBxfdnvJX7cdtVJnt+N2p+CNnKvE7PtC8jDMs/BSVA01hw/vqjNYtVdLc7J+x7A0vpx4w/ZszYgPOA+ciMXDrz+kKFb353Zmv4Eof09tccc5n9qg/bdakV3Q7G3vzPu7ABZYQB+Y+J+qQZQvrDiAwe5Y/JzFlNCb/jAWKZm07w==|+zObTsWM9XyZ2tS/c7u+nKD0/ryhdm0WbmNhXuttlXM=|10|99a32f4aa90fa36396e141f8e300f55a; __xaf_fptokentimer__=1672804973023; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1672218950,1672832223; bdindexid=taqk72m8ot9a3r7inhsu68pvj7; ZD_ENTRY=bing; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04228953144t9K20c2FoG8ggPbsWRxmrGL9e3rTAF6eV4RJpk2phsJdVN9JSOlIBDGmvpI073W%2FlQOooVmfokGXaOUpF8Pul3BX2s4CiZjN%2FS036h7uD9dHHWwAmZQJYrlk2deNccShmF3ydoajbR612EEhqFINPyny0KROmA6zCGO1tObUWfjlPZ7SqlBHS6zqsOW47Xl7G%2FcoNrunrO1HT2M6dxm3uvmmtiHAPnVPB1e0%2B5gHL2rEy4C02%2FM88MFy87n%2F7lG%2BJZjwO8ITbgTbQgM3G7hZnxEIGuhnVOu%2Buu%2BaZaMDbFQ%3D18035950298843985659026702870995; __cas__rn__=422895314; __cas__st__212=187a74c8ca54618d46bf34074a2d06fa782febc8b31a4f0e29ffc36fc72e2394448db3087327d0a15f86363e; __cas__id__212=44855536; CPID_212=44855536; CPTK_212=266828396; RT=z=1&dm=baidu.com&si=a0738dc7-5b13-4a2c-9aa4-9be92b5bdc68&ss=lcifbk18&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1672891956; BDUSS_BFESS=UNWM2dOeDZhU215U09IaUVISHp1UjdsNUEzTVJHYmlRdkFVWFRwSGpRN1JjY0pqSVFBQUFBJCQAAAAAAAAAAAEAAAAEyXrqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANHkmmPR5JpjM; ab_sr=1.0.1_OTViZTdmNjAwZjljZTQwN2Q4OWQ0NWM0ODgwNzFlNDRjMThhNjlkOGY3MjFiMDQ5ZGZjMGVmNmQ4ZDEzYWJmMjI5ZThiM2NjZDI4N2E0MDcyMTkwNDYxZTVkMjU2Mjc5YzU4MTk4ZmQ2NDhhZWYxZDdmNDY2ZDFjNjU1YzhlOGFhYjQzOTRjYTNhNGMxZTFhN2Y5MTNiMGNhNWUzMzg1Mg=="
    }
    response = requests.get(url, headers=headers, cookies=cookies)
    return response.text
 
 
def decrypt(ptbk, data):
    n = list(ptbk)
    i = list(data)
    tem = {}
    result = []
    ln = int(len(n) / 2)
    start = n[ln:]
    end = n[:ln]
    for j, k in zip(start, end):
        tem.update({k: j})
    for j in data:
        result.append(tem.get(j))
    return ''.join(result)
 
 
def get_ptbk(uniqid):
    url = 'http://index.baidu.com/Interface/ptbk?uniqid={}'
    resp = get_html(url.format(uniqid))
    return json.loads(resp)['data']
 
 
def get_data_ser(keyword, start='2011-01-01', end='2021-1-1', area='广州',time=10):
    #一共十年
    two_start=11
    two_start+=1
    end=end[:2]+str(two_start)+end[4:]
    
    
    start_s = start.split("-")
    end_s = end.split("-")
    start_tem=[int(start_s[0]), int(start_s[1]), int(start_s[2])]
    end_tem=[int(end_s[0]), int(end_s[1]), int(end_s[2])]
    
    input_all=[]
    #two_start=11
    
    for i in range(0,time):
        place=city.get(area)
        #url = ""
        
        url = "https://index.baidu.com/api/SearchApi/index?area={}&word=[[%7B%22name%22:%22{}%22,%22wordType%22:1%7D]]&startDate={}&endDate={}".format(place, keyword, start, end)
        data = get_html(url)
        data = json.loads(data)
        uniqid = data['data']['uniqid']
        data = data['data']['userIndexes'][0]['all']['data']
        ptbk = get_ptbk(uniqid)
        result = decrypt(ptbk, data)
        result = result.split(',')
        
        input_data1={}
        # a = datetime.date(start_tem[0], start_tem[1], start_tem[2])
        # b = datetime.date(end_tem[0], end_tem[1], end_tem[2])
        node = len(result)
        tem_sum=0
        date_int=start_tem[0]
        #每一年
        for i in range(node):
          #date = datetime.date.fromordinal(i)
          #print(date, result[node])
          if result[i]=='':
              tem_sum+=0
          else:
              tem_sum+=int(result[i])
          node 
        #每一年计算结果写入文件
        input_data1['date']=date_int
        input_data1['data']=tem_sum
        input_all.append(input_data1)
        header=['date','data']
        #print(input_data)
        # start_tem[0]+=1
        # end_tem[0]+=1
        
        #修改start
        start=end
        two_start+=1
        end=end[:2]+str(two_start)+end[4:]
        #print(end)
        
        start_tem=[start_tem[0]+1, start_tem[1], start_tem[2]]
        end_tem=[end_tem[0]+1, end_tem[1], end_tem[2]]
        #end_tem[0]+=1
        print(end_tem[0],start_tem[0])
        
        
    with open(r'D:\pywork\baidunumbers\百度指数数据\搜索指数\碳排放-{}-{}-{}.csv'
              .format(area,start_date,end_date),'w',newline='') as file_data:
        baiduWriter= csv.DictWriter(file_data, header)
        # 2.写表头
        baiduWriter.writeheader()
        # 3.写入数据(一次性写入多行)
        baiduWriter.writerows(input_all)
    # y=np.array(y).flatten()
    # y=pd.DataFrame(y)
    # y.to_csv(r'D:\pywork\baidunumbers\百度指数数据\搜索指数\碳排放-{}-{}-{}.csv'.format(area,start,end))

     
def get_data_ser_year(keyword, start='2011-01-01', end='2021-1-1', area='南通',time=10):
    #一共十年
    place=city.get(area)
    #url = ""
    two_start=11
    url = "https://index.baidu.com/api/SearchApi/index?area={}&word=[[%7B%22name%22:%22{}%22,%22wordType%22:1%7D]]&startDate={}&endDate={}".format(place, keyword, start, end)
    data = get_html(url)
    data = json.loads(data)
    uniqid = data['data']['uniqid']
    data = data['data']['userIndexes'][0]['all']['data']
    ptbk = get_ptbk(uniqid)
    result = decrypt(ptbk, data)
    result = result.split(',')
    start = start_date.split("-")
    end = end_date.split("-")
    # if start[0]
    input_all=[]
    start_tem=[int(start[0]), int(start[1]), int(start[2])]
    end_tem=[int(start[0]), int(start[1]), int(start[2])]
    end_tem[0]+=1
    
    for i in range(0,time):
        input_data1={}
        a = datetime.date(start_tem[0], start_tem[1], start_tem[2])
        b = datetime.date(end_tem[0], end_tem[1], end_tem[2])
        node = 0
        tem_sum=0
        date_int=start_tem[0]
        #每一年
        for j in range(a.toordinal()+(365*i), b.toordinal()+(365*i)):
          #date = datetime.date.fromordinal(i)
          #print(date, result[node])
          if result[node]=='':
              tem_sum+=0
          else:
              tem_sum+=int(result[node])
          node += 1
        #每一年计算结果写入文件
        input_data1['date']=date_int
        input_data1['data']=tem_sum
        input_all.append(input_data1)
        header=['date','data']
        #print(input_data)
        start_tem[0]+=1
        end_tem[0]+=1
        
        #start 修改
        # start_tem=[end_tem[0], end_tem[1], end_tem[2]]
        # end_tem=[end_tem[0], end_tem[1], end_tem[2]]
        # end_tem[0]+=1
        print(start_tem[0],end_tem[0])
        
        
    with open(r'D:\pywork\baidunumbers\百度指数数据\搜索指数\碳排放-{}-{}-{}.csv'
              .format(area,start_date,end_date),'w',newline='') as file_data:
        baiduWriter= csv.DictWriter(file_data, header)
        # 2.写表头
        baiduWriter.writeheader()
        # 3.写入数据(一次性写入多行)
        baiduWriter.writerows(input_all)
    # y=np.array(y).flatten()
    # y=pd.DataFrame(y)
    # y.to_csv(r'D:\pywork\baidunumbers\百度指数数据\搜索指数\碳排放-{}-{}-{}.csv'.format(area,start,end))
       
def get_data_ser_year_2(keyword, start='2011-01-01', end='2021-1-1', area='南通',time=10):
    #一共十年
    place=city.get(area)
    #url = ""
    # two_start=11
    url = "https://index.baidu.com/api/SearchApi/index?area={}&word=[[%7B%22name%22:%22{}%22,%22wordType%22:1%7D]]&startDate={}&endDate={}".format(place, keyword, start, end)
    data = get_html(url)
    data = json.loads(data)
    uniqid = data['data']['uniqid']
    data = data['data']['userIndexes'][0]['all']['data']
    ptbk = get_ptbk(uniqid)
    result = decrypt(ptbk, data)
    result = result.split(',')
    start = start_date.split("-")
    end = end_date.split("-")
    a = datetime.date(int(start[0]), int(start[1]), int(start[2]))
    b = datetime.date(int(end[0]), int(end[1]), int(end[2]))
    node = 0
    input_all=[]
    count=1
    for i in range(a.toordinal(), b.toordinal()):
      input_data1={}
      date = datetime.date.fromordinal(i)
      date_str=str(date)
      #print(date, result[node])
      # input_data[date_str]=result[node]
      input_data1['date']=date_str
      input_data1['data']=result[node]
      input_all.append(input_data1)
      node += 1
    
        
    # y=np.array(y).flatten()
    # y=pd.DataFrame(y)
    # y.to_csv(r'D:\pywork\baidunumbers\百度指数数据\咨询指数\碳排放-{}-{}-{}.csv'.format(area,start,end))
    header=['date','data']
    with open(r'D:\pywork\baidunumbers\百度指数数据\咨询指数\碳排放-{}-{}-{}.csv'
              .format(area,start_date,end_date),'w',newline='') as file_data:
        baiduWriter= csv.DictWriter(file_data, header)
        # 2.写表头
        baiduWriter.writeheader()
        # 3.写入数据(一次性写入多行)
        baiduWriter.writerows(input_all)
        
    
             
def get_data_feed(keyword, start='2011-01-01', end='2021-1-1', area='合肥'):
    place=city.get(area)
    #url = "https://index.baidu.com/api/FeedSearchApi/getFeedIndex?area=0&word=[[%7B%22name%22:%22%E7%A2%B3%E6%8E%92%E6%94%BE%22,%22wordType%22:1%7D]]&days=180"
    url = "https://index.baidu.com/api/FeedSearchApi/getFeedIndex?area={}&word=[[%7B%22name%22:%22{}22,%22wordType%22:1%7D]]&startDate={}&endDate={}".format(place, keyword, start, end)
    data = get_html(url)
    data = json.loads(data)
    uniqid = data['data']['uniqid']
    data = data['data']['userIndexes'][0]['all']['data']
    ptbk = get_ptbk(uniqid)
    result = decrypt(ptbk, data)
    result = result.split(',')
    start = start_date.split("-")
    end = end_date.split("-")
    a = datetime.date(int(start[0]), int(start[1]), int(start[2]))
    b = datetime.date(int(end[0]), int(end[1]), int(end[2]))
    node = 0
    input_all=[]
    for i in range(a.toordinal(), b.toordinal()):
      input_data1={}
      date = datetime.date.fromordinal(i)
      date_str=str(date)
      #print(date, result[node])
      # input_data[date_str]=result[node]
      input_data1['date']=date_str
      input_data1['data']=result[node]
      input_all.append(input_data1)
      node += 1
    
        
    # y=np.array(y).flatten()
    # y=pd.DataFrame(y)
    # y.to_csv(r'D:\pywork\baidunumbers\百度指数数据\咨询指数\碳排放-{}-{}-{}.csv'.format(area,start,end))
    header=['date','data']
    with open(r'D:\pywork\baidunumbers\百度指数数据\咨询指数\碳排放-{}-{}-{}.csv'
              .format(area,start_date,end_date),'w',newline='') as file_data:
        baiduWriter= csv.DictWriter(file_data, header)
        # 2.写表头
        baiduWriter.writeheader()
        # 3.写入数据(一次性写入多行)
        baiduWriter.writerows(input_all)

 
if __name__ == '__main__':
    keyword = "碳排放"
    start_date = "2011-01-01"
    end_date = "2021-1-1"
    get_data_ser(keyword, start_date, end_date)
    # get_data_feed(keyword,start_date,end_date)
    # print(data)

