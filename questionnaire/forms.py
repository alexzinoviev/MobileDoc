from django import forms
from questionnaire.models import Questionnaire

# class ArticleForm(forms.ModelForm):
#
#     class Meta:
#         model = Article

class AnswersForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
#        fields = ['question1', 'question2']
        widgets = {
            'answer': forms.RadioSelect,
        }
