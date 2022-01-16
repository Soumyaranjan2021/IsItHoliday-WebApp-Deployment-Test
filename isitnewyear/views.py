from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    return render(request, 'isitnewyear/index.html', context= {
        'title': 'Is it New Year',
        'message': 'Yes' if date.today().day == 1 and date.today().month == 1 else 'No',
        'time': date.today(),
    })