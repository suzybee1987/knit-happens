from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = '__all__'


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'
