from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#创建栏目标题
class Topic(models.Model):
    """用户学习的主题"""
    text=models.CharField(max_length=200)#两个属性，内容，上限为200；时间，自动为当前时间
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)#关联到特定的人

    def __str__(self):#调用该方法来显示默认有关的主题信息
        """返回模型用字符串表示"""
        return self.text

class Entry(models.Model):
    """学到有关某个主题的知识"""
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)#和教材上不一样，这个后面的参数是现在必须要的
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='entries'#模型的额外属性，表示在特殊情况下的信息，比如多个条目时候显示entries，而不是Entrys

    def __str__(self):
        """返回模型的字符串类型表示"""
        return self.text[:50]+"..."