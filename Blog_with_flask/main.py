from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get("https://api.npoint.io/42e3519dde93dbe96c91")
posts = response.json()

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id):
    return render_template('post.html', post=posts[id-1])

if __name__ == '__main__':
    app.run(debug=True)