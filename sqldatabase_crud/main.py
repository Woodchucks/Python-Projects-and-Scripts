from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////read-books-ratings.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.create_all()


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html', books=Book.query.all())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        new_book = Book(title=request.form["name"],
                        author=request.form["author"],
                        rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        new_book_rating = request.form["new_rating"]
        book_id = request.form["id"]
        book_to_change = Book.query.get(book_id)
        book_to_change.rating = new_book_rating
        db.session.commit()
        return redirect(url_for('home'))
    id = request.args.get('id')
    book = Book.query.get(id)
    return render_template('edit.html', book=book)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

