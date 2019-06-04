from django.shortcuts import render
from datetime import datetime
import random
import json
import requests


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def hola(request):
    return render(request, 'pages/hola.html')

def dinner(request):
    menu = ['닭슴살','한솥','피자','백반']
    pick = random.choice(menu)
    context = {'pick':pick}
    return render(request, 'pages/dinner.html', context)


def hello(request, name):
    context = {'name':name}
    return render(request, 'pages/hello.html', context)

def introduce(request, name, age):
    context = {'name':name, 'age':age}
    return  render(request, 'pages/introduce.html', context)

def times(request, num1, num2):
    num3 = num1 * num2
    context = {'num1':num1, 'num2':num2, 'num3':num3}
    return  render(request, 'pages/times.html', context)

def area(request, r):
    area = (r**2) * 3.14
    context = {'r':r, 'area':area}
    return  render(request, 'pages/area.html', context)

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
    return render(request, 'pages/template_language.html', context)

def isbirthday(request):
    today = datetime.now()
    if today.month == 9 and today.day == 8:
        result = True
    else:
        result = False
    context = {'result':result}
    return render(request, 'pages/isbirthday.html', context)

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {'message':message, 'message2':message2}
    return render(request, 'pages/catch.html',  context)


def lotto(request):
    name = request.GET.get('name')
    lotto = sorted(random.sample(range(1,45),6))
    context = {"lotto": lotto,"name": name}
    return render(request, "pages/lotto.html", context)

def name(request):
    return render(request, "pages/name.html")

def lotto2(request):
    return render(request, 'pages/lotto2.html')

def picklotto(request):
    name = request.GET.get('name')

    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=861')
    lotto = json.loads(res.text)

    winner = []
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    picked = sorted(random.sample(range(1, 46),6))
    matched = len(set(winner) & set(picked))

    if matched == 6:
        result = '1등입니다.퇴사'
    elif matched == 5:
        result = '3등입니다.휴다'
    elif matched == 4:
        result = '4등입니다.술'
    elif matched == 3:
        result = '5등입나다.로또사자'
    else:
        result = '꽝입니다.충성'

    context = {'name':name, 'result':result}

    return render(request, 'pages/picklotto.html', context)

def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form 태그로 날린 데이터를 받는다.
    word = request.GET.get('word')

    #2. artii API를 통해 보낸 응답 결과를 text로 fonts에 저장한다
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. fonts(str)를 font 리스트의 형태로 저장한다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소중 하나를 선택해서 font에저장한다.
    font = random.choice(fonts)

    #5. 위에서 사용자에게 받은 word와 랜덤하게 뽑은 font 를가지고 다시요청을 보낸다
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {'result':result}
    return render(request, 'pages/result.html', context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name':name, 'pwd':pwd}
    return  render(request, 'pages/user_create.html', context)

def static_example(request):
    return render(request, 'pages/static_example.html')

def photo(request):
    return render(request, 'pages/photo.html')