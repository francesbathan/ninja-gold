from django.shortcuts import render
from time import localtime, strftime

def index(request):
    context = {
        "date": strftime("%B %d, %Y", localtime()),    
        "time": strftime("%I:%M %p", localtime())
    }
    return render(request, 'time_dis.html', context)