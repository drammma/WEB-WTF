from flask import Flask, render_template

app = Flask(__name__)



@app.route('/<text>')
@app.route('/index/<text>')
def page(text):
    return render_template('base.html', title=text,  first_head='Миссия Колонизация Марса', fourth_head='И на Марсе будут яблони цвести!')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')