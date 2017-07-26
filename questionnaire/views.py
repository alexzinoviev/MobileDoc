from django.shortcuts import render
from .models import Questionnaire
from answers.models import Answers

# Create your views here.
def index(request):
    questions = Questionnaire.objects.all()
    categories = Questionnaire.category
    answers = Answers.answer
    return render(request, 'index.html', {'questions': questions}, {'categories': categories},)