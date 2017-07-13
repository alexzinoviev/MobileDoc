from django.db import models
from django import forms
#from django import forms
#from .forms import AnswersForm

# Create your models here.

class Questionnaire(models.Model):
    YES_S = 'Yes'
    NO_S = 'No'

    Cardio_1 = 'Cardiology_1'
    Cardio_2 = 'Cardiology_2'

    question = models.TextField('Вопрос')

    ANSWER = (
        (YES_S, 'Yes'),
        (NO_S, 'No'),
               )
    answer = models.CharField(
        null=True, max_length=100,
        default=None,
        choices=ANSWER, verbose_name='Do you?')

    CATEGORY = (
        (Cardio_1, 'Cardiology_1'),
        (Cardio_2, 'Cardiology_2')
    )

    category = models.CharField(
        null=True, max_length=100,
        default=None,
        choices=CATEGORY, verbose_name='Please choose category of question'
    )