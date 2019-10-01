"""添加新的主题，填写的表单"""
from  django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):

    class Meta:#用来告诉django根据那个模型创建表单，以及包含哪些字段
        model=Topic#根据topic创建
        fields=['text']#该表只包含text字段
        labels={'text':''}#不要为text生成标签

class EntryForm(forms.ModelForm):

    class Meta:
        model=Entry
        fields=['text']
        labels={'text':''}
        #widgets小控件是HTML表单元素，如单行，多行文本框；下拉列表；设置属性，将text宽度设成了80
        widgets={'text':forms.Textarea(attrs={'cols':80})}