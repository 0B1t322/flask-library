from app import app, path_resolver
from flask import render_template, flash, redirect, url_for
from app.models import Book, Author, books_and_authors


@app.route('/')
def index():
    return render_template(
        'index.html',
    )


@app.route('/books')
def books():
    books = Book.query.all()
    return render_template(
        'books.html',
        books=books,
        styles=[
            path_resolver.to_css('books.css')
        ]
    )
