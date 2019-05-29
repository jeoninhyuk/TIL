from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route('/send')
def send():
    return render_template('send.html')


@app.route('/receive')
def receive():
    user = request.args.get('user')
    message = request.args.get('message')
    return render_template('receive.html', user=user, message=message)


@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')




@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    #response.text #=> string
    lotto = response.json() #=> dict

    # winner = [] # list()
    # for n in range(1, 7):
    #     winner.append(lotto[f'drwtNo{n}'])

    # list comprehension
    a = [lotto[f'drwtNo{n}'] for n in range(1, 7)] #=> [1,2,3,4,5,6]
    b = lotto['bnusNo']

    winner = f'{a} + {b}'

    # my_numbers 가져오기 map()
    my_numbers = [int(n) for n in request.args.get('my_numbers').split()] #=> ['1','2','3','4','5','6']

    # 같은 숫자 갯수
    matched = len(set(a) & set(my_numbers))  # 1
    # set(a) #=> [4,8,18,25,27,32]
    # set(my_numbers) #=> [1.2.3.4.5.6]
    # set() #{1,2,3,4}

    #같은 숫자의 갯수애 따른 등수
    if matched == 6:
        result = '1등입니다'
    elif matched == 5:
        # [2,4,6,8,10,12] +3
        # [2,3,6,8,10,12]

        if lotto['bnusNo'] in my_numbers:
            result = '3등입니다'
        elif matched == 4:
            result = '4등입니다'
    elif matched == 3:
        result = '5등입니다'
    elif:
        result = '꽝입니다....'

    return render_template('lotto_result.html', lotto=winner, lotto_round=lotto_round, my_numbers=my_numbers, result=result)


if __name__ == '__main__':
    app.run(debug=True)
