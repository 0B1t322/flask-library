from app import app, db
from app.models import Book, Author, BooksAndAuthors

# Для работы с объектами бд не импортируя их
@app.shell_context_processors
def make_shell_context():
    return {'db': db, 'Book': Book, 'Author': Author, 'BooksAndAuthors': BooksAndAuthors}
