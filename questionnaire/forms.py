from django import forms
from questionnaire.models import Questionnaire

# class ArticleForm(forms.ModelForm):
#
#     class Meta:
#         model = Article

# class AnswersForm(forms.ModelForm):
#     class Meta:
#         model = Questionnaire
# #        fields = ['question1', 'question2']
#         widgets = {
#             'answer': forms.RadioSelect,
#         }

#ANSWERS = (Questionnaire.answer1, Questionnaire.answer2,
#           Questionnaire.answer3, Questionnaire.answer4)

# class AnswerForm(forms.Form):
#     question = Questionnaire.question
#     answers = forms.ChoiceField(widget=forms.RadioSelect(), choices=ANSWERS)