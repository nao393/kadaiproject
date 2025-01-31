from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']  # 'image' を削除
        labels = {
            'name': '名前',
            'content': '本文',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名無しさん'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '書き込み内容',
                'rows': 3
            }),
        }
