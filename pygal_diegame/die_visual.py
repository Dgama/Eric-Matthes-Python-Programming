import pygal

from die import Die

#两个不同骰子
die_1=Die()
die_2=Die(10)
#存储多次结果
results=[]
for roll_num in range(50000):
    result=die_1.roll()+die_2.roll()
    results.append( result)

#统计次数
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#结果可视化
hist=pygal.Bar()

hist._title="Result of rolling a D6 and a D10 50000 times"

hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist._x_title="Result"
hist.y_labels="Frequency of Result"

hist.add('D6+D10',frequencies)
#关于SVG：https://baike.baidu.com/item/SVG/63178?fr=aladdin
hist.render_to_file('die_visual.svg')