#Question 1

# No code for this section all set up


#Question 2

def greeting_message():
    print("Hello World!")

greeting_message()


#Question 3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)


#Question 4

@app.route('/')
def hello():
    return "Hello World!"



#Question 5

# Have a file called index.html in a templates folder in the same directory

def hello(name=None):
    return render_template('index.html', name=name)

