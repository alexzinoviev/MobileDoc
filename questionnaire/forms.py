from django import forms
#from questionnaire.models import Questionnaire

# class ArticleForm(forms.ModelForm):
#
#     class Meta:
#         model = Article

class AnswersForm(forms.Form):
    answer = forms.RadioSelect