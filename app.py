from flask import Flask

app = Flask(__name__)

#Question 4 Code Below
# @app.route('/')
# def hello():
#     return "Hello World!"

#Question 5 Code Below
from flask import render_template
@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)