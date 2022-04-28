def get_anonymous(books_list):
    books_list = [
        title_book for title_book in books_list
        if ' by ' not in title_book
    ]
    return books_list
