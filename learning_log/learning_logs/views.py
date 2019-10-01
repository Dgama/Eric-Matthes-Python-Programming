from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Topic,Entry
from .form import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
import os
# Create your views here.
def index(request):
    return render(request,'learning_logs/index.html')

@login_required
def topics(request):
    """显示所有主题"""
    topics=Topic.objects.filter(owner=request.user).order_by('date_added')#查询数据库，查询集存储于topics
    context={'topics':topics}#发送给模板的上下文，上下文是一个字典，key是模板中访问数据的名称，值是数据
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    """显示单个主题的所有条目"""
    topic=get_object_or_404(Topic,id=topic_id)
    #确认请求的属于当前用户
    if topic.owner != request.user:
        raise Http404
    entries=topic.entry_set.order_by('-date_added')#减号表示降序排列
    context={'topic':topic,'entries':entries}#主题和条目均存储在上下文中
    return render(request,'learning_logs/topic.html',context)

#网页请求主要有两种。一种是请求服务器数据的，get；一种是写入数据的post。在newtopics界面存在两种，所以需要判断
@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':#请求类不只有post,get但是，除去post以外，其他请求生成一个空表单都是没有问题的
        #未提交数据:创建新表单
        form=TopicForm()#通过上下文字字典，传送给模板，可以产生空界面
    else:
        #POST提交数据，对数据进行处理
        form=TopicForm(request.POST)
        if form.is_valid():#判断表单是否必不可少的字段都有了
            new_topic=form.save(commit=False)#将创建者与主题相互连接
            new_topic.owner=request.user
            new_topic.save()#可以写入数据库了
            #reverse方法根据指定的url模型确定URL；httpresponseredirect，这里跳转回topics主界面，让用户看到新添加的topic
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context={'form':form}
    return render(request,'learning_logs/new_topic.html',context)
@login_required
def new_entry(request,topic_id):
    """在特定主题中添加新的条目"""
    topic=Topic.objects.get(id=topic_id)

    if request.method!='POST':
        form=EntryForm()
    else:
        form=EntryForm(data=request.POST)#试了一下，指不指定data都可以，都是表示用POST的数据来填充
        # 下面的一通操作：先检测表单的内容有没有缺失（不管主题匹配）；正确后将form信息save进新的new_entry（条目对象），false表示不进入数据库；指定条目的topic属性，相关联；存储
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            #reverse有两个实参，一个是模式名称，一个是url实参，通过列表传递
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    context={'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    """编辑条目"""
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method!='POST':
        #初次请求，当前表单填充原来的信息，即没修改之前的
        form=EntryForm(instance=entry)#传递原来的类型，创建一个内容相同的可编辑表单
    else:
        #修改过后，重新存储
        form=EntryForm(instance=entry,data=request.POST)#以原有的填充后，按照POST中的内容修改，因为有可能修改只修改了部分？
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))

    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)

