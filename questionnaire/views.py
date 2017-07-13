from django.shortcuts import render
from .models import Questionnaire

# Create your views here.
def index(request):
    questions = Questionnaire.objects.all()
    return render(request, 'index.html', {'questions': questions})