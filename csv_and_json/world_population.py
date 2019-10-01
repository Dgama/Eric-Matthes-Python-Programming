import json
from country_codes import get_country_code
import pygal
from pygal.style import RotateStyle as RS,LightColorizedStyle as LCS
#将数据加载进入列表

filename='population_data.json'
with open(filename) as f:
    pop_data=json.load(f)

#打印每个国家2010年的人口数量
cc_populations={}#创建包含人口数的字典
cc_pop_1,cc_pop_2,cc_pop_3={},{},{}#按照人口规模进行分类的字典
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name=pop_dict['Country Name']
        population=int(float(pop_dict['Value']))#人口有小数的时候无法直接转化成int类型
        code=get_country_code(country_name)
        if code:
            cc_populations[code]=population
#按照人口分类
for cc,pop in cc_populations.items():
    if pop<10000000 :
        cc_pop_1[cc]=pop
    elif pop<1000000000:
        cc_pop_2[cc]=pop
    else:
        cc_pop_3[cc]=pop

wm_style=RS('#336699',base_style=LCS)#33,66,99分别为红绿蓝分量，最小是00，最大是FF 用的是十六进制表达RGB颜色，返回的是一个样式,LCS模块设置基色为加亮颜色
wm=pygal.maps.world.World(style=wm_style)
wm.title='World Population in 2010, by country'
wm.add('0-10m',cc_pop_1)
wm.add('10m-1bn',cc_pop_2)
wm.add('>1bn',cc_pop_3)
wm.render_to_file('world_population.svg')