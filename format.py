import os
from qdata.baidu_index import PROVINCE_CODE,CITY_CODE

def get_txt(file_path):
    data=open(file_path,encoding='utf-8')
    data=data.read()
    return data

if __name__ == '__main__':
    file_name=r"D:\pywork\baidunumbers\百度指数数据\area_number.txt"
    #data=get_txt(file_name)
    number=[]
    place=[]
    data=CITY_CODE
    print(data.get(95))
    tem='2011-01-01'
    two_start=11
    tem=tem[:2]+str(two_start+1)+tem[4:]
    
    print(tem)
    
    #print(int(tem[1]))
    # for i in data:
    #     tem_data=data.split(':')
    #     if (tem_data[0]=='合肥')
    #for i in range(0,len(data)):
        
        
    Y_gt = [1, 1, 1, 0, 0, 0], # 用户1
           [1, 1, 1, 0, 1, 0], # 用户2
           [1, 1, 1, 0, 0, 1], # 用户3
           [0, 0, 0, 1, 1, 0], # 用户4
           [0, 0, 0, 1, 1, 1], # 用户5
           [1, 0, 1, 0, 0, 1], # 用户6
