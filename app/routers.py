from app import app, path_resolver, db
from flask import render_template, flash, redirect, url_for, request
from app.models import Book, Author, books_and_authors
from app.forms import BookForm


@app.route('/')
def index():
    return render_template(
        'index.html',
    )


@app.route('/books')
def books():
    authors = Author.query.all()
    return render_template(
        'books.html',
        authors=authors,
        styles=[
            path_resolver.to_css('book_style.css')
        ]
    )


@app.route('/books/add', methods=['GET', 'POST'])
def books_add():
    form = BookForm()
    err = ''
    if form.validate_on_submit():
        flash('Add book')
        if check_if_exist(form.author.data, form.name.data):
            err = 'Book with this author exist'
        else:
            a = Author(f'{form.author.data}')
            a.books.append(Book(f'{form.name.data}'))
            db.session.add(a)
            db.session.commit()
        if err == '':
            return redirect(url_for('books'))
    return render_template(
        'book_form.html',
        form=form,
        err=err,
    )


def check_if_exist(author_name, book_name):
    author = Author\
            .query\
            .filter_by(
                name=author_name
            )\
            .join(Author.books) \
            .filter(
                Book.name == book_name
            ).all()
    if len(author) != 0:
        return True
    return False


@app.route('/books/update/<author_id>/<book_id>', methods=['GET', 'POST'])
def update(author_id, book_id):
    form = BookForm()
    err = ''
    prev_author = Author.query.get_or_404(author_id)
    prev_book = Book.query.get_or_404(book_id)
    if not form.validate_on_submit():
        form.author.data = prev_author.name
        form.name.data = prev_book.name
    else:
        if form.author.data == prev_author.name and form.name.data == prev_book.name:
            print(f'from: {form.name.data} prev: {prev_book.name}')
            print(f'from: {form.author.data} prev: {prev_author.name}')
            return redirect(url_for('books'))
        if check_if_exist(author_name=form.author.data, book_name=form.name.data):
            err = 'Book with this author exist'
        if err == '':
            prev_author.name = form.author.data
            prev_book.name = form.name.data
            db.session.add(prev_book)
            db.session.add(prev_author)
            db.session.commit()
            return redirect(url_for('books'))
    return render_template(
        'book_form.html',
        form=form,
        err=err,
    )