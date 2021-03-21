from app import db

books_and_authors = db.Table('books_and_authors',
                             db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
                             db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True),

                             )


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    authors = db.relationship(
        'Author',
        secondary=books_and_authors,
        lazy='subquery',
        backref=db.backref(
            'books',
            lazy=True,
        )
    )
    def __init__(self, name):
        self.name = name


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    # books = db.relationship(
    #     'Book',
    #     secondary=books_and_authors,
    #     lazy='subquery',
    #     backref=db.backref(
    #         'authors',
    #         lazy=True,
    #     )
    # )

    def __init__(self, name):
        self.name = name
