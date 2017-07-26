from django.db import models
from answers.models import Answers

# Create your models here.

#class Answers(models.Model):
#    question_id = models.ForeignKey(Questionnaire)
#    answer = models.TextField('Ответ', default=None, max_length=30)


class Questionnaire(models.Model):
    Cardio_1 = 'Cardiology_1'
    Cardio_2 = 'Cardiology_2'

    question = models.TextField('Вопрос')
    answer1 = models.ForeignKey(Answers, related_name='Answer_1')
    answer2 = models.ForeignKey(Answers, related_name='Answer_2')
    answer3 = models.ForeignKey(Answers, related_name='Answer_3')
    answer4 = models.ForeignKey(Answers, related_name='Answer_4')

    CORRECT_ANSWER = (
        (answer1, answer1),
        (answer2, answer2),
        (answer3, answer3),
        (answer4, answer4)

    )

    correct_answer = models.CharField(
        null=True, max_length=50,
        default=None,
        choices=CORRECT_ANSWER,
        verbose_name='Please choose correct answer'
    )

    CATEGORY = (
            (Cardio_1, 'Cardiology_1'),
            (Cardio_2, 'Cardiology_2')
        )

    category = models.CharField(
        null=True, max_length=100,
        default=None,
        choices=CATEGORY, verbose_name='Please choose category of question'
    )




# class Questionnaire(models.Model):
#     YES_S = 'Yes'
#     NO_S = 'No'
#
#     Cardio_1 = 'Cardiology_1'
#     Cardio_2 = 'Cardiology_2'
#
#     question = models.TextField('Вопрос')
#
#     ANSWER = (
#         (YES_S, 'Yes'),
#         (NO_S, 'No'),
#                )
#     answer = models.CharField(
#         null=True, max_length=100,
#         default=None,
#         choices=ANSWER, verbose_name='Do you?')
#
#     CATEGORY = (
#         (Cardio_1, 'Cardiology_1'),
#         (Cardio_2, 'Cardiology_2')
#     )
#
#     category = models.CharField(
#         null=True, max_length=100,
#         default=None,
#         choices=CATEGORY, verbose_name='Please choose category of question'
#     )