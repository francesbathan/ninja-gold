from django.shortcuts import render, redirect
from time import localtime, strftime
import random

def index(request):
    return render(request,'index.html')

def process_money(request):
    if 'gold_counter' not in request.session:
        request.session['gold_counter'] = 0

    if 'activities' not in request.session:
        request.session['activities'] = []

    date = strftime("%x", localtime())   
    time = strftime("%I:%M %p", localtime())
    
    current_list = request.session['activities']
    # print(current_list)

    if request.POST['location'] == 'farm': 
        gold = random.randint(10,20) # randomizes number between 10 and 20
        request.session['gold_counter'] += gold
        newmsg = f"Earned {gold} gold from the farm! ({date} {time})"
                # when location (farm, cave, house, or casino) find gold button is clicked, it posts on the activities area how much they earned

    elif request.POST['location'] == 'cave':
        gold = random.randint(5,10)
        request.session['gold_counter'] += gold
        newmsg = f"Earned {gold} gold from the cave! ({date} {time})"
        

    elif request.POST['location'] == 'house':
        gold = random.randint(2,5)
        request.session['gold_counter'] += gold
        newmsg = f"Earned {gold} gold from the house! ({date} {time})"

    elif request.POST['location'] == 'casino':  
        gold = random.randint(-50,50)
        if gold < 0:
            request.session['gold_counter'] += gold
            newmsg = f"<p class='red'>Entered casino and lost {-gold} gold from the casino. Ouch. ({date} {time})</p>"
        else:
            request.session['gold_counter'] += gold
            newmsg = f"Earned {gold} gold from the casino! ({date} {time})"
        

    current_list.append(newmsg) # adds the new message into the current list (activities area)
    request.session['activities'] = current_list

    return redirect('/')

def reset(request):
    if request.method == 'POST':
        request.session['gold_counter'] = 0
        request.session['activities'] = []
    return redirect("/")



