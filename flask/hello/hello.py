from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/mulcam')
def mulcam():
    return 'This is Inhyuk Jeon house~!!'

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다, {name}님!'

@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return f'{result}'
# [실습] 특정 사람 수 만큼 점심 메뉴 추천하기
# <int:people>


@app.route('/junch/<int:people>')
def lunch(people):
    menu = ['20', '양자강', '김밥', '순남시래기']
    return str(random.sample(menu, people))

@app.route('/html')
def html():
    multiple_sting = """
        <h1>this is h1 tag</h1>
        <p>this is p tag</p>
    """
    return multiple_sting

@app.route('/html_file')
def html_file():
    return render_template('html_file.html')

@app.route('/hi/<string:name>')
def hi(name):
    #Template Variable
    return render_template('hi.html', your_name=name)

@app.route('/menu_list')
def menu_list():
    menu = ['20층','고갯마루', '순남', '병턴순대']
    return render_template('menu_list.html', menu_list=menu)



if __name__ == '__main__':
    app.run(debug=True)
