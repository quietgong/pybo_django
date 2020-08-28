from django import forms
from academic.models import Question, Answer, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'grade', 'upload_files', ]
        labels = {
            'subject': '제목',
            'content': '내용',
            'grade' : '학년',
            'upload_files': '파일',
        }
        # widget 항목 삭제 (목적 : 디자인 영역과 서버 영역 분리)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }