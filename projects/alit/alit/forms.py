from django import forms
from alit.models import Question, Answer, Algoset, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용'
        }

class AlgoForm(forms.ModelForm):
    class Meta:
        model = Algoset
        fields = ['title', 'body']
        labels = {
            'title': '제목',
            'body': '내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글'  
        }