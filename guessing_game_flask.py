from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def display_h1():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<image src='https://media1.giphy.com/media/RoBjhqlygXkCtgsWe6/giphy.webp?cid=ecf05e473mrk5q7ynl5eoasrxynj7gufnz7cn2wqp3h10mpv&rid=giphy.webp&ct=g'>"

@app.route('/<int:number>')
def number_guessed(number):
    rand_number = random.randint(0,9)
    if number == rand_number:
        return "<h1 style='color:green'>You've guessed it!</h1>" \
               "<image src='https://media1.giphy.com/media/SB5fjrUhAeLte/200w.webp?cid=ecf05e47tf36d3x50dt787il3sn2yh905rmbfywd2xkmk3i8&rid=200w.webp&ct=g'>"
    else:
        return "<h1 style:'color:red'>Sorry! Wrong!</h1>" \
               "<image src='https://media2.giphy.com/media/bSIwCqjd9kTNJ6AAhg/200w.webp?cid=ecf05e47zye2i6sr90mehcjawbp8iif23gdnn2rmv98jipaa&rid=200w.webp&ct=g'>"

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
