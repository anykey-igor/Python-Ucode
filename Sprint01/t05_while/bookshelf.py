def add_to_bookshelf(book_to_add, bookshelf):
    if len(bookshelf) > 1:
        i = 0
        while i < len(bookshelf):
            if bookshelf[i] == '---':
                bookshelf[i] = book_to_add
                return True
            i += 1
        return False
    else:
        return False
