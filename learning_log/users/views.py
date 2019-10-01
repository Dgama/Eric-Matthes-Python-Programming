from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        #显示空的注册表单
        form = UserCreationForm()
    else:
        #处理已经写好的表单
        form=UserCreationForm(data=request.POST)

        #这个有效性检查是针对是否用户名合法以及是否密码不匹配，以及是否恶意
        if form.is_valid():
            new_user=form.save()#存储到数据库的同时创建新的用户对象

            #让用户自动登录，再重新定向到主页
            #这里authenticated_user是通过后面函数返回的一个验证了的用户对象；后面的函数第二个参数是表单里的第一个密码，由于已经验证成功了，2个密码中随便取一个就好
            authenticated_user=authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context={'form':form}
    return render(request,'users/register.html',context)