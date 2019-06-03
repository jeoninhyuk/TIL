from django.shortcuts import render
from datetime import datetime
import random


# Create your views here.
def index(request):
    return render(request, 'index.html')

def hola(request):
    return render(request, 'hola.html')

def dinner(request):
    menu = ['닭슴살','한솥','피자','백반']
    pick = random.choice(menu)
    context = {'pick':pick}
    return render(request, 'dinner.html', context)


def hello(request, name):
    context = {'name':name}
    return render(request, 'hello.html', context)

def introduce(request, name, age):
    context = {'name':name, 'age':age}
    return  render(request, 'introduce.html', context)

def times(request, num1, num2):
    num3 = num1 * num2
    context = {'num1':num1, 'num2':num2, 'num3':num3}
    return  render(request, 'times.html', context)

def area(request, r):
    area = (r**2) * 3.14
    context = {'r':r, 'area':area}
    return  render(request, 'area.html', context)

def template_language(request):
    menus = ['자장면', '짬뽕', '탕수육']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = ['jeoninhyuk']
    datetimenow = datetime.now()
    context = {
        'menus':menus,
        'my_sentence':my_sentence,
        'messages': messages,
        'empty_list':empty_list,
        'datetimenow':datetimenow,
    }
    return render(request, 'template_language.html', context)

def isbirthday(request):
    today = datetime.now()
    if today.month == 9 and today.day == 8:
        result = True
    else:
        result = False
    context = {'result':result}
    return render(request, 'isbirthday.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {'message':message, 'message2':message2}
    return render(request, 'catch.html',  context)


def lotto(request):
    name = request.GET.get('name')
    lotto = sorted(random.sample(range(1,45),6))
    context = {"lotto": lotto,"name": name}
    return render(request, "lotto.html", context)

def name(request):
    return render(request, "name.html")