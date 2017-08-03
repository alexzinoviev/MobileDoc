from django.shortcuts import render
from .models import Questionnaire
from answers.models import Answers
#from questionnaire.forms import AnswerForm
from django.http import HttpResponseRedirect

#Create your views here.
def index(request):
    questions = Questionnaire.objects.all()
    categories = Questionnaire.category
    answers = Answers.answer
    return render(request, 'index.html', {'questions': questions}, {'categories': categories},)

def ttt(request):
    return render(request, 'ttt.html')

# def index(request):
#     form = AnswerForm()
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             pass
#     return render(request, 'index.html', {'form': form}, )