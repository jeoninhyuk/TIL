from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/send_ex')
def send():
    return render_template('send.ex.html')

@app.route('/receive_ex')
def receive():
    user = request.args.get('user')
    message = request.args.get('message')
    return render_template('receive.ex.html', user=user, message=message)

if __name__ == '__main__':
    app.run(debug=True)
