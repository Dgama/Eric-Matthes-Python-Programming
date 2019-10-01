#地图绘制需要两位国家编码

from pygal_maps_world.i18n import COUNTRIES

# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code,COUNTRIES[country_code])
def get_country_code(country_name):
    """按照国家名字返回国家编码"""
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
    return None#没有找到返回空值
