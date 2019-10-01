"""'定义应用users的urls"""

from django.conf.urls import url

from  django.contrib.auth.views import LoginView

from . import views

app_name='users'
urlpatterns=[
    #登录界面，匹配的界面是loginView的模板，但是还是会有一些不一样，具体改动在参数中去找
    #LoginView 相当于帮你写好了View函数，所以这里的基本思路是一样的，但是之前的view函数还需要一个特定的html连接，所以这里相当于给定了这个参数
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    #注销
    url(r'^logout/$',views.logout_view,name='logout'),
    #注册
    url(r'^register/$',views.register,name='register')
]