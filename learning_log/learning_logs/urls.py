"""定义learning_logs的url模式"""
#基本功能与learning_log中的url相同

from django.conf.urls import url

from .import views

app_name='learning_logs'
urlpatterns=[
    #主页,三个参数分别是网页的正则匹配模式，请求的界面，url的名称（可在别的地方调用）
    url(r'^$',views.index,name='index'),
    #主题
    url(r'^topics/$',views.topics,name='topics'),
    #?P<topic_id>将匹配的值存入topic_id中，\d+表示任意数位数字。这些都在//之间
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    #新主题
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
    #与8000/new_entry/id/的url相匹配，url与这个模式匹配成功后，会将请求与存储在topic_id中的信息传到new_entry中
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    #编辑条目
    url(r'edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
]
