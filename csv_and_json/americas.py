import pygal.maps.world as pyWorld

wm=pyWorld.World()
wm.title='North, Cenrtal,and Sounth America'

#add为添加突出标签，字符串为标签名字，列表为该标签的国家代码,如果用字典的话可以显示数值
wm.add('North America',{'ca':3412600,'mx':113423000,'us':309349000})
wm.add('Central America',['bz','cr','gt'])

wm.render_to_file('americas.svg')