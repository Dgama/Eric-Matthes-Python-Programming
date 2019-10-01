import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename='death_valley_2014.csv'

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    # #使得更容易阅读
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

    #获取最高温度,遍历各行，每次reader都会从当前行往下读一行
    dates,highs,lows=[],[],[]
    for row in reader:
        try:#避免缺失数据情况
            current_date=datetime.strptime(row[0],'%Y-%m-%d')#格式化日期
            high=int(row[1])#转化为整数类型
            low=int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)



#绘制图像,
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates,highs,lows,facecolor='blue',alpha='0.1')#填充颜色，alpha为透明度，0为完全透明
plt.title("daily high and low temperature-2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#避免字符重叠
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()