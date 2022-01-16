from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    return render(request, 'isitchristmas/index.html', context= {
        'title': 'Is it Christmas',
        'message': 'Yes' if date.today().day == 25 and date.today().month == 12 else 'No',
        'time': date.today(),
    })