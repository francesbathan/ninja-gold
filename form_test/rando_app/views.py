from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'random.html') 

def random_word(request): # creates the random string
    request.session['random'] = get_random_string(length=14)
    if 'attempt' in request.session: 
        request.session['attempt'] += 1 # increments the number of attempts to create a word
    else: 
        request.session['attempt'] = 0 # default number of attempts
    context = {
        'random': request.session['random'],
        'attempt': request.session['attempt']
    }
    return render(request, 'random.html', context)

def reset(request): # when reset button is clicked, it resets the number of attempts and also generates a new word
    request.session.clear()
    return redirect('/random/random_word') # always have the url from the project with a forward slash before it then slash the destination