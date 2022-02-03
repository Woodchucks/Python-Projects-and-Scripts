from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_posts = response.json()

@app.route('/blog')
def home():
    return render_template("index.html", posts=blog_posts)

@app.route('/post/<int:id>')
def post(id):
    return render_template("post.html", id=id, posts=blog_posts)

if __name__ == "__main__":
    app.run(debug=True)
